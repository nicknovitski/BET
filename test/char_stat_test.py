import unittest

from character.char import Character
from character.exceptions import CantAfford, ExceedsMaximum
from character import human
from character.lifepath import Lifepath

class CharacterStatsTests(unittest.TestCase):
    def setUp(self):
        self.char = Character()
    def testStatPtsAge0(self):
        self.assertEquals(self.char.mental_pool(), 0)
        self.assertEquals(self.char.physical_pool(), 0)
    def testStatPtsRange(self):
        various_ages = {Character(age=1):[5,10],
                        Character(age=10):[5,10],
                        Character(age=11):[6,13],
                        Character(age=14):[6,13],
                        Character(age=15):[6,16],
                        Character(age=16):[6,16],
                        Character(age=17):[7,16],
                        Character(age=25):[7,16],
                        Character(age=26):[7,15],
                        Character(age=29):[7,15],
                        Character(age=30):[7,14],
                        Character(age=35):[7,14],
                        Character(age=36):[7,13],
                        Character(age=40):[7,13],
                        Character(age=41):[7,12],
                        Character(age=55):[7,12],
                        Character(age=56):[7,11],
                        Character(age=65):[7,11],
                        Character(age=66):[7,10],
                        Character(age=79):[7,10],
                        Character(age=80):[6,9],
                        Character(age=100):[6,9]}
        for character, points in various_ages.iteritems():
            self.assertEquals(character.mental_pool(), points[0])
            self.assertEquals(character.physical_pool(), points[1])
    def testStatsDefault(self):
        """Can characters start with any stat at 0?  Paraplegics, I guess.
        """
        self.assertEquals(self.char.perception, 0)
        self.assertEquals(self.char.will, 0)
        self.assertEquals(self.char.agility, 0)
        self.assertEquals(self.char.speed, 0)
        self.assertEquals(self.char.power, 0)
        self.assertEquals(self.char.forte, 0)
    def testBuyStats(self):
        char = Character(age=1)
        char.buy_agility()
        char.buy_speed()
        char.buy_power()
        char.buy_forte()
        char.buy_perception()
        char.buy_will()
        self.assertEquals(char.perception, 1)
        self.assertEquals(char.will, 1)
        self.assertEquals(char.agility, 1)
        self.assertEquals(char.speed, 1)
        self.assertEquals(char.power, 1)
        self.assertEquals(char.forte, 1)
        self.assertEquals(char.mental_pool(), 3)
        self.assertEquals(char.physical_pool(), 6)
    def testBuyStatsMultiple(self):
        char = Character(age=1)
        char.buy_agility(2)
        char.buy_speed(2)
        char.buy_power(2)
        char.buy_forte(2)
        char.buy_perception(2)
        char.buy_will(2)
        self.assertEquals(char.perception, 2)
        self.assertEquals(char.will, 2)
        self.assertEquals(char.agility, 2)
        self.assertEquals(char.speed, 2)
        self.assertEquals(char.power, 2)
        self.assertEquals(char.forte, 2)
        self.assertEquals(char.mental_pool(), 1)
        self.assertEquals(char.physical_pool(), 2)
    def testRemoveStats(self):
        char = Character(age=1)
        char.buy_agility(2)
        char.buy_speed(2)
        char.buy_power(2)
        char.buy_forte(2)
        char.buy_perception(2)
        char.buy_will(2)
        char.remove_agility()
        char.remove_speed()
        char.remove_power()
        char.remove_forte()
        char.remove_perception()
        char.remove_will()
        self.assertEquals(char.perception, 1)
        self.assertEquals(char.will, 1)
        self.assertEquals(char.agility, 1)
        self.assertEquals(char.speed, 1)
        self.assertEquals(char.power, 1)
        self.assertEquals(char.forte, 1)
        self.assertEquals(char.mental_pool(), 3)
        self.assertEquals(char.physical_pool(), 6)
    def testBuyStatsWithoutPoints(self):
        char = Character(age = 1)
        char.buy_will(5)
        self.assertEquals(char.will, 5)
        self.assertEquals(char.mental_pool(), 0)
        self.assertRaises(CantAfford, char.buy_will)
        self.assertRaises(CantAfford, char.buy_perception)
        char.buy_forte(3)
        char.buy_speed(3)
        char.buy_power(3)
        char.buy_agility(1)
        self.assertEquals(char.forte, 3)
        self.assertEquals(char.speed, 3)
        self.assertEquals(char.power, 3)
        self.assertEquals(char.agility,1)
        self.assertEquals(char.physical_pool(),0)
        self.assertRaises(CantAfford, char.buy_forte)
        self.assertRaises(CantAfford, char.buy_agility)
        self.assertRaises(CantAfford, char.buy_speed)
        self.assertRaises(CantAfford, char.buy_power)
    def testBuyStatsPastLimits(self):
        """for humans: will and perception 8, all others 6, with no stat can be above 6 in character creation
        """
        char = Character(age = 11)
        char.buy_perception(6)
        self.assertRaises(ExceedsMaximum, char.buy_perception)
        char.remove_perception(6)
        char.buy_will(6)
        self.assertRaises(ExceedsMaximum, char.buy_will)
        char.remove_will(6)
        char.buy_agility(6)
        self.assertRaises(ExceedsMaximum, char.buy_agility)
        char.remove_agility(6)
        char.buy_speed(6)
        self.assertRaises(ExceedsMaximum, char.buy_speed)
        char.remove_speed(6)
        char.buy_power(6)
        self.assertRaises(ExceedsMaximum, char.buy_power)
        char.remove_power(6)
        char.buy_forte(6)
        self.assertRaises(ExceedsMaximum, char.buy_forte)
        char.remove_forte(6)
    def testAgeOver100(self):
        """Character's age cannot exceed 100
        """
        char = Character(age = 100)
        self.assertRaises(ExceedsMaximum, char.add_path, Lifepath(years=1))
        self.assertFalse(Lifepath(years=1).allowed(char))
    def testLoseStatsWithDecreasingAge(self):
        """Changes in Lifepaths can lead to altering point pools.  Stats should be altered to avoid negative point pools.

        Assumption: higher stats should lose points first
        """
        char = Character([Lifepath(years=14, born=True), Lifepath(years=3)])
        self.assertEquals(char.age(), 17)
        self.assertEquals(char.mental_pool(), 7)
        self.assertEquals(char.physical_pool(), 16)
        
        char.buy_perception(4)
        char.buy_will(3)
        char.remove_path()
        self.assertEquals(char.age(), 14)
        self.assertEquals(char.mental_pool(), 0)
        self.assertEquals(char.perception, 3)
        self.assertEquals(char.will, 3)

        char.add_path(Lifepath(years=3))
        char.buy_will()
        char.remove_path()
        self.assertEquals(char.age(), 14)
        self.assertEquals(char.mental_pool(), 0)
        self.assertEquals(char.perception, 3)
        self.assertEquals(char.will, 3)

        char.add_path(Lifepath(years=3))
        self.assertEquals(char.physical_pool(), 16)
        char.buy_speed(6)
        char.buy_power(5)
        char.buy_forte(3)
        char.buy_agility(2)
        self.assertEquals(char.physical_pool(), 0)
        char.remove_path()
        self.assertEquals(char.speed, 4)
        self.assertEquals(char.power, 4)
        self.assertEquals(char.forte, 3)
        self.assertEquals(char.agility, 2)
    def testLoseStatsWithIncreasingAge(self):
        char = Character(age = 79)
        self.assertEquals(char.mental_pool(), 7)
        self.assertEquals(char.physical_pool(), 10)
        char.buy_perception(4)
        char.buy_will(3)
        char.add_path(Lifepath(born=True, years=1))
        self.assertEquals(char.mental_pool(), 0)
        self.assertEquals(char.perception, 3)
        self.assertEquals(char.will, 3)
        char.remove_path()
        char.buy_will()
        char.add_path(Lifepath(born=True, years=1))
        self.assertEquals(char.perception, 3)
        self.assertEquals(char.will, 3)
        char.remove_path()
        char.buy_speed(4)
        char.buy_power(3)
        char.buy_forte(2)
        char.buy_agility(1)
        self.assertEquals(char.physical_pool(), 0)
        char.add_path(human.BornNobility())
        self.assertEquals(char.physical_pool(), 0)
        self.assertEquals(char.speed, 3)
        self.assertEquals(char.power, 3)
        self.assertEquals(char.forte, 2)
        self.assertEquals(char.agility, 1)
    def testBonusStatPoints(self):
        char = Character([Lifepath(years=1, born=True)])
        char.add_path(Lifepath(physical_points=1))
        self.assertEquals(char.physical_pool(), 11)
        char.remove_path()
        char.add_path(Lifepath(mental_points=1))
        self.assertEquals(char.mental_pool(), 6)
    def testFloaterPoints(self):
        """Some lifepaths give a bonus point for physical or mental stats.  These points should be spent last and refunded first.
        """
        char = Character([Lifepath(born=True, years=1), Lifepath(years=1, floater_points=1)])
        self.assertEquals(char.mental_pool(), 5)
        self.assertEquals(char.physical_pool(), 10)
        self.assertEquals(char.floater_pool(), 1)

        char.buy_perception(3)
        char.buy_will(2)
        char.buy_forte(4)
        char.buy_power(2)
        char.buy_agility(2)
        char.buy_speed(2)
        self.assertEquals(char.physical_pool(), 0)
        self.assertEquals(char.mental_pool(), 0)
        self.assertEquals(char.floater_pool(), 1)

        char.buy_perception()
        self.assertEquals(char.mental_pool(), 0)
        self.assertEquals(char.floater_pool(), 0)
        self.assertEquals(char.perception, 4)
        self.assertRaises(CantAfford, char.buy_will)
        self.assertRaises(CantAfford, char.buy_forte)
        self.assertRaises(CantAfford, char.buy_speed)
        self.assertRaises(CantAfford, char.buy_agility)
        self.assertRaises(CantAfford, char.buy_power)
        char.remove_perception()
        self.assertEquals(char.mental_pool(), 0)
        self.assertEquals(char.floater_pool(), 1)

        char.buy_will()
        self.assertEquals(char.mental_pool(), 0)
        self.assertEquals(char.floater_pool(), 0)
        self.assertEquals(char.will, 3)
        self.assertRaises(CantAfford, char.buy_perception)
        self.assertRaises(CantAfford, char.buy_forte)
        self.assertRaises(CantAfford, char.buy_speed)
        self.assertRaises(CantAfford, char.buy_agility)
        self.assertRaises(CantAfford, char.buy_power)
        char.remove_will()
        self.assertEquals(char.mental_pool(), 0)
        self.assertEquals(char.floater_pool(), 1)

        char.buy_forte()
        self.assertEquals(char.physical_pool(), 0)
        self.assertEquals(char.floater_pool(), 0)
        self.assertEquals(char.forte, 5)
        self.assertRaises(CantAfford, char.buy_will)
        self.assertRaises(CantAfford, char.buy_perception)
        self.assertRaises(CantAfford, char.buy_speed)
        self.assertRaises(CantAfford, char.buy_agility)
        self.assertRaises(CantAfford, char.buy_power)
        char.remove_forte()
        self.assertEquals(char.physical_pool(), 0)
        self.assertEquals(char.floater_pool(), 1)

        char.buy_power()
        self.assertEquals(char.physical_pool(), 0)
        self.assertEquals(char.floater_pool(), 0)
        self.assertEquals(char.power, 3)
        self.assertRaises(CantAfford, char.buy_will)
        self.assertRaises(CantAfford, char.buy_perception)
        self.assertRaises(CantAfford, char.buy_forte)
        self.assertRaises(CantAfford, char.buy_speed)
        self.assertRaises(CantAfford, char.buy_agility)
        char.remove_power()
        self.assertEquals(char.physical_pool(), 0)
        self.assertEquals(char.floater_pool(), 1)

        char.buy_agility()
        self.assertEquals(char.physical_pool(), 0)
        self.assertEquals(char.floater_pool(), 0)
        self.assertEquals(char.agility, 3)
        self.assertRaises(CantAfford, char.buy_will)
        self.assertRaises(CantAfford, char.buy_perception)
        self.assertRaises(CantAfford, char.buy_forte)
        self.assertRaises(CantAfford, char.buy_speed)
        self.assertRaises(CantAfford, char.buy_power)
        char.remove_agility()
        self.assertEquals(char.physical_pool(), 0)
        self.assertEquals(char.floater_pool(), 1)

        char.buy_speed()
        self.assertEquals(char.physical_pool(), 0)
        self.assertEquals(char.floater_pool(), 0)
        self.assertEquals(char.speed, 3)
        self.assertRaises(CantAfford, char.buy_will)
        self.assertRaises(CantAfford, char.buy_perception)
        self.assertRaises(CantAfford, char.buy_forte)
        self.assertRaises(CantAfford, char.buy_power)
        self.assertRaises(CantAfford, char.buy_agility)
        char.remove_speed()
        self.assertEquals(char.physical_pool(), 0)
        self.assertEquals(char.floater_pool(), 1)

    def testMortalWoundTolerance(self):
        char = Character([Lifepath(born=True, years=1)])
        char.buy_power()
        char.buy_forte()
        self.assertEquals(char.mortal_wound(), 'H7')
        char.buy_forte()
        self.assertEquals(char.mortal_wound(), 'H7')
        char.buy_forte()
        self.assertEquals(char.mortal_wound(), 'H8')
    def testSuperficialWoundTolerance(self):
        char = Character([Lifepath(born=True, years=1)])
        char.buy_forte()
        self.assertEquals(char.superficial_wound(), 'H1')
        char.buy_forte()
        self.assertEquals(char.superficial_wound(), 'H2')
        char.buy_forte()
        self.assertEquals(char.superficial_wound(), 'H2')
    def testInjuredWoundTolerance(self):
        char = Character([Lifepath(born=True, years=1)])
        char.buy_forte()
        self.assertEquals(char.injured_wound(), 'H1')
        char.buy_forte()
        self.assertEquals(char.injured_wound(), 'H3')
        char.buy_forte()
        self.assertEquals(char.injured_wound(), 'H3')
    def testMaimedWoundTolerance(self):
        char = Character([Lifepath(born=True, years=1)])
        char.buy_power()
        char.buy_forte()
        self.assertEquals(char.maimed_wound(), 'H5')
        char.buy_forte()
        self.assertEquals(char.maimed_wound(), 'H5')
        char.buy_forte()
        self.assertEquals(char.maimed_wound(), 'H6')
    def testResources(self):
        self.assertEquals(self.char.resources(), 0)
        self.char.add_path(Lifepath(born=True, resources=1))
        self.assertEquals(self.char.resources(), 1)
        self.char.remove_path()
        self.assertEquals(self.char.resources(), 0)
    def testResourcesAfterMultiplePaths(self):
        """I assume only the exact same path counts as the same path, as opposed to any path with the same name
        """
        self.char.add_path(human.BornLeague()).add_path(human.LeagueStudent())
        self.assertEquals(self.char.resources(), 2)
        self.char.add_path(human.Accountant()).add_path(human.Accountant()).add_path(human.Accountant())
        self.assertEquals(self.char.resources(), 7)
        self.char.remove_path(3).add_path(human.Scrivener()).add_path(human.Scrivener()).add_path(human.Scrivener())
        self.assertEqual(self.char.resources(), 4)
    def testCircles(self):
        self.assertEquals(self.char.circles(), 0)
        self.char.add_path(Lifepath(born=True, circles=1))
        self.assertEquals(self.char.circles(), 1)
        self.char.remove_path()
        self.assertEquals(self.char.circles(), 0)
    def testCirclesAfterMultiplePaths(self):
        self.char.add_path(human.BornNobility()).add_path(human.NobleCoeptir()).add_path(human.NobleArmiger())
        self.assertEquals(self.char.circles(), 1)
        self.char.add_path(human.NobleLPAnvil()).add_path(human.NobleLPAnvil()).add_path(human.NobleLPAnvil())
        self.assertEquals(self.char.circles(), 3)
    def testArtha(self):
        char = Character()
        
        self.assertEquals(char.artha_fate(),3)
        self.assertEquals(char.artha_persona(),2)
        self.assertEquals(char.artha_deeds(),1)

        char.add_path(Lifepath(born=True))
        self.assertEquals(char.artha_fate(),3)
        self.assertEquals(char.artha_persona(),2)
        self.assertEquals(char.artha_deeds(),1)

        char.add_path(Lifepath())
        self.assertEquals(char.artha_fate(),3)
        self.assertEquals(char.artha_persona(),2)
        self.assertEquals(char.artha_deeds(),1)

        char.add_path(Lifepath())
        self.assertEquals(char.artha_fate(),3)
        self.assertEquals(char.artha_persona(),2)
        self.assertEquals(char.artha_deeds(),1)

        char.add_path(Lifepath())
        self.assertEquals(char.artha_fate(),3)
        self.assertEquals(char.artha_persona(),2)
        self.assertEquals(char.artha_deeds(),1)

        char.add_path(Lifepath())
        self.assertEquals(char.artha_fate(),3)
        self.assertEquals(char.artha_persona(),2)
        self.assertEquals(char.artha_deeds(),1)

        char.add_path(Lifepath())
        self.assertEquals(char.artha_fate(),3)
        self.assertEquals(char.artha_persona(),2)
        self.assertEquals(char.artha_deeds(),0)

        char.add_path(Lifepath())
        self.assertEquals(char.artha_fate(),2)
        self.assertEquals(char.artha_persona(),1)
        self.assertEquals(char.artha_deeds(),0)

        char.add_path(Lifepath())
        self.assertEquals(char.artha_fate(),1)
        self.assertEquals(char.artha_persona(),1)
        self.assertEquals(char.artha_deeds(),0)

        char.add_path(Lifepath())
        self.assertEquals(char.artha_fate(),1)
        self.assertEquals(char.artha_persona(),0)
        self.assertEquals(char.artha_deeds(),0)

        char.add_path(Lifepath())
        self.assertEquals(char.artha_fate(),0)
        self.assertEquals(char.artha_persona(),0)
        self.assertEquals(char.artha_deeds(),0)

        char.add_path(Lifepath())
        self.assertEquals(char.artha_fate(),0)
        self.assertEquals(char.artha_persona(),0)
        self.assertEquals(char.artha_deeds(),0)

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(CharacterStatsTests))
