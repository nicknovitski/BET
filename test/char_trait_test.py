import unittest

from character.char import Character
from character import human
from character import trait
from character.exceptions import NotAllowed
from character.lifepath import Lifepath

class CharacterTraitsTests(unittest.TestCase):
    def setUp(self):
        self.char = Character()
    def testGainsRequiredTrait(self):
        self.assertFalse(self.char.has_trait('Required Trait'))
        self.char.add_path(Lifepath(born=True, traits=[trait.Trait(name='Required Trait'), trait.Trait(name='Optional Trait')]))
        self.assertTrue(self.char.has_trait(trait.Trait(name='Required Trait')))
        self.assertFalse(self.char.has_trait(trait.Trait(name='Optional Trait')))
    def testGainsRequiredTraitsAfterMultiplePaths(self):
        self.char.add_path(Lifepath(born=True, traits=[trait.Trait(name='First Trait'), trait.Trait(name='Second Trait')]))
        self.assertTrue(self.char.has_trait(trait.Trait(name='First Trait')))
        self.assertFalse(self.char.has_trait(trait.Trait(name='Second Trait')))
        self.char.add_path(Lifepath(traits=[trait.Trait(name='First Trait'), trait.Trait(name='Second Trait')]))
        self.assertTrue(self.char.has_trait(trait.Trait(name='Second Trait')))
    def testCountTraitPoints(self):
        """Most paths give trait points.  However, they also might give access to traits.
        Every time a a path is taken:
            the first trait in the list that the character does not have is bought for one trait point
        The second time and later times a path is taken:
            If there is no such trait, then the path awards one less trait point

        I assume this is the case even with paths that never award traits

        plan:
        add path with no points or traits (0)
        add path with 1 point and first trait (0)
        add path with 2 points and second trait (1)
        add path with 2 points and first trait (2)
        add path with 1 point and second trait (2)
        add path with 1 point and no traits (3)
        add same path with 1 point and no traits (3)
        """
        self.char.add_path(human.BornNobility())
        self.assertEquals(self.char.trait_points(), 0)
        self.char.add_path(human.NobleCoeptir())
        self.assertEquals(self.char.trait_points(), 1)
        self.char.add_path(human.NobleArmiger())
        self.assertEquals(self.char.trait_points(), 1)
        self.char.add_path(human.NobleLPAnvil())
        self.assertEquals(self.char.trait_points(), 2)
        self.char.add_path(human.NobleLPAnvil())
        self.assertEquals(self.char.trait_points(), 3)
        self.char.add_path(human.NobleLPAnvil())
        self.assertEquals(self.char.trait_points(), 3)
        self.char.remove_path(5)
        self.assertEquals(self.char.trait_points(), 0)
        self.char.add_path(human.Companion())
        self.assertEquals(self.char.trait_points(), 2)
        self.char.add_path(human.Lady())
        self.assertEquals(self.char.trait_points(), 3)
        self.char.add_path(human.Lady())
        self.assertEquals(self.char.trait_points(), 3)
    def testTraitList(self):
        char = Character([human.BornNobility(), human.NobleCoeptir(), human.NobleArmiger()])
        self.assertEquals(char.traits(), [trait.MarkOfPrivilege(), trait.AnvilTrained()])
        char.add_path(human.NobleLPAnvil())
        self.assertEquals(char.traits(), [trait.MarkOfPrivilege(), trait.AnvilTrained(), trait.CorvusAndCrucis()])
        char.add_path(human.NobleLPAnvil())
        self.assertEquals(char.traits(), [trait.MarkOfPrivilege(), trait.AnvilTrained(), trait.CorvusAndCrucis(), trait.IronTrained()])
    def testLifepathTraits(self):
        """All traits on all the paths the character has taken are listed.
        """
        char = Character()
        char.add_path(human.BornNobility())
        self.assertEquals(char.lifepath_traits(), [trait.MarkOfPrivilege(), trait.YourLordship(), trait.YourEminence(), trait.YourGrace(), trait.YourMajesty()])
    def testAllowedTraits(self):
        """all traits the character has not bought and can currently afford
        """
        char = human.Human()
        self.assertEquals(char.allowed_traits(), [])
        char.add_path(human.BornNobility())
        self.assertEquals(char.allowed_traits(), [])
        char.add_path(human.NobleCoeptir())
        self.assertTrue(trait.Amorous() in char.allowed_traits())
        self.assertTrue(trait.YourLordship() in char.allowed_traits())
        self.assertTrue(trait.YourEminence() in char.allowed_traits())
        self.assertTrue(trait.YourGrace() in char.allowed_traits())
        self.assertTrue(trait.YourMajesty() in char.allowed_traits())
    def testBuyTraits(self):
        char = Character([human.BornNobility(), human.NobleCoeptir(), human.NobleArmiger()])
        char.buy_trait(trait.CharacterTrait())
        self.assertEquals(char.traits(), [trait.MarkOfPrivilege(), trait.AnvilTrained(), trait.CharacterTrait()])
        self.assertEquals(self.char.trait_points(),0)
    def testCantAffordTraits(self):
        char = Character([human.BornNobility(), human.NobleCoeptir(), human.NobleArmiger()])
        self.assertEquals(char.trait_points(), 1)
        self.assertRaises(NotAllowed, char.buy_trait, trait.CalmDemeanor())
        self.assertEquals(char.trait_points(), 1)
        char.add_path(human.NobleLPAnvil())
        self.assertEquals(char.trait_points(),2)
        char.buy_trait(trait.CalmDemeanor())
        self.assertEquals(char.traits(), [trait.MarkOfPrivilege(), trait.AnvilTrained(), trait.CorvusAndCrucis(), trait.CalmDemeanor()])
        self.assertEquals(char.trait_points(),0)
    def testRemoveTraits(self):
        char = Character([human.BornNobility(), human.NobleCoeptir(), human.NobleArmiger(), human.NobleLPAnvil()])
        char.buy_trait(trait.CharacterTrait('Trait 1'))
        char.buy_trait(trait.IronTrained())
        self.assertEquals(char.trait_points(), 0)
        char.remove_trait(trait.IronTrained())
        self.assertEquals(char.trait_points(), 1)
        self.assertRaises(Exception, char.remove_trait, trait.CharacterTrait('Trait 2'))
        char.remove_trait(trait.CharacterTrait('Trait 1'))
        self.assertEquals(char.trait_points(), 2)
        
    def testCheaperTraits(self):
        """All traits on the available list cost only one point
        """
        char = Character([human.BornNobility(), human.NobleCoeptir(), human.NobleArmiger()])
        char.buy_trait(trait.Tough())
        self.assertEquals(char.traits(), [trait.MarkOfPrivilege(), trait.AnvilTrained(), trait.Tough()])
        self.assertEquals(char.trait_points(), 0)
    def testTraitsGetCheaper(self):
        """A trait can be bought, after which a lifepath is added that puts that trait on the available list.

        The difference in cost should be refunded
        """
        char = Character([human.BornNobility(), human.Bastard(), human.TheocracyStudent(), human.Soldier(), human.Sergeant()])
        self.assertEquals(char.trait_points(), 3)
        char.buy_trait(trait.Tough())
        self.assertEquals(char.trait_points(), 0)
        char.add_path(human.NobleArmiger())
        self.assertEquals(char.trait_points(), 2)
        self.assertTrue(char.has_trait(trait.Tough()))
    def testLoseBoughtTraits(self):
        """A trait can be bought, then a lifepath removed, causing either:
        1. The loss of the points used to buy the trait
        2. The trait becomes more expensive than the character can afford

        In these cases, traits should be removed, starting with the most recently addded, until balance is restored
        """
        char = Character([human.BornNobility(), human.Bastard(), human.Soldier(), human.Sergeant()])
        self.assertEquals(char.trait_points(), 2)
        char.add_path(human.NobleArmiger())
        char.buy_trait(trait.Tough())
        self.assertEquals(char.trait_points(), 1)
        char.remove_path()
        self.assertEquals(char.trait_points(), 2)
        self.assertFalse(char.has_trait(trait.Tough()))

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(CharacterTraitsTests))
