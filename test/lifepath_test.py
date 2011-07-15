import unittest

from character.lifepath import Lifepath
from character import human, trait

class BasicLifepathTests(unittest.TestCase):
    def testName(self):
        self.assertEquals(Lifepath().name, 'Default')
        self.assertEquals(Lifepath(name='New Path').name, 'New Path')
    def testYears(self):
        self.assertEquals(Lifepath().years, 0)
        self.assertEquals(Lifepath(years=1).years, 1)
    def testResources(self):
        self.assertEquals(Lifepath().resources, 0)
        self.assertEquals(Lifepath(resources=1).resources, 1)
    def testCircles(self):
        self.assertEquals(Lifepath().circles, 0)
        self.assertEquals(Lifepath(circles=1).circles, 1)
    def testSame(self):
        self.assertEquals(human.Novitiate(), human.Novitiate())
        self.assertFalse(human.Novitiate() != human.Novitiate())
    def testNotSame(self):
        self.assertFalse(human.Novitiate() == human.Speaker())
        self.assertTrue(human.Novitiate() != human.Speaker())
        self.assertFalse(human.NobleCoeptir() == human.HammerCoeptir())
        self.assertTrue(human.NobleCoeptir() != human.HammerCoeptir())
    def testTraitPoints(self):
        self.assertEquals(Lifepath(trait_points=1).trait_points, 1)
        self.assertEquals(Lifepath().trait_points, 0)
    def testTraits(self):
        self.assertEquals(len(Lifepath().traits), 0)
        self.assertEquals(len(Lifepath(traits=[trait.ABitMad(), trait.Abandoned()]).traits), 2)
    def testDifferentSettings(self):
        self.assertFalse(human.BornNobility().same_setting(human.CourtCoeptir()))
        self.assertTrue(human.BornNobility().same_setting(human.NobleArmiger()))
    def testBonusPoints(self):
        crap_path = Lifepath()
        physical_path = Lifepath(physical_points =1)
        mental_path = Lifepath(mental_points = 1)
        flexible_path = Lifepath(floater_points=1)
        awesome_path = Lifepath(mental_points=1, physical_points=1)
        self.assertEquals(crap_path.physical_points, 0)
        self.assertEquals(crap_path.mental_points, 0)
        self.assertEquals(crap_path.floater_points, 0)
        self.assertEquals(physical_path.physical_points, 1)
        self.assertEquals(mental_path.mental_points, 1)
        self.assertEquals(flexible_path.floater_points, 1)
        self.assertEquals(awesome_path.physical_points, 1)
        self.assertEquals(awesome_path.mental_points, 1)
    def testBorn(self):
        self.assertFalse(Lifepath().born)
        self.assertTrue(Lifepath(born=True).born)
    def testSkillPoints(self):
        self.assertEquals(Lifepath().skill_points, 0)
        self.assertEquals(Lifepath(skill_points=1).skill_points, 1)
    def testGeneralPoints(self):
        self.assertEquals(Lifepath().general_skill_points, 0)
        self.assertEquals(Lifepath(general_skill_points=1).general_skill_points, 1)
    def testSkills(self):
        self.assertEquals(Lifepath().skills, [])
        self.assertEquals(Lifepath(skills=['A','B','C']).skills, ['A','B','C'])

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(BasicLifepathTests))
