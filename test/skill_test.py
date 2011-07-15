import unittest
from character import skill
import character
import character.human

class SkillTests(unittest.TestCase):
    def testDefaults(self):
        self.assertEquals(skill.Skill().name, 'Default Skill')
        self.assertEquals(skill.Skill().roots(), [])
        self.assertEquals(skill.Skill().points, 0)
    def testName(self):
        self.assertEquals(skill.Skill(name='New').name, 'New')
    def testPerceptionRoot(self):
        self.assertEquals(skill.PerceptionRoot().roots(), ['Perception'])
    def testWillRoot(self):
        self.assertEquals(skill.WillRoot().roots(), ['Will'])
    def testAgilityRoot(self):
        self.assertEquals(skill.AgilityRoot().roots(), ['Agility'])
    def testForteRoot(self):
        self.assertEquals(skill.ForteRoot().roots(), ['Forte'])
    def testPowerRoot(self):
        self.assertEquals(skill.PowerRoot().roots(), ['Power'])
    def testSpeedRoot(self):
        self.assertEquals(skill.SpeedRoot().roots(), ['Speed'])
    def testPerAgi(self):
        class PerAgi(skill.PerceptionRoot, skill.AgilityRoot):
            pass
        self.assertEquals(PerAgi().roots(), ['Perception', 'Agility'])
    def testWilAgi(self):
        class WilAgi(skill.WillRoot, skill.AgilityRoot):
            pass
        self.assertEquals(WilAgi().roots(), ['Will', 'Agility'])
    def testWilPer(self):
        class WilPer(skill.WillRoot, skill.PerceptionRoot):
            pass
        self.assertEquals(WilPer().roots(), ['Will', 'Perception'])
    def testPerSpd(self):
        class PerSpd(skill.PerceptionRoot, skill.SpeedRoot):
            pass
        self.assertEquals(PerSpd().roots(), ['Perception', 'Speed'])
    def testPowSpd(self):
        class PowSpd(skill.PowerRoot, skill.SpeedRoot):
            pass
        self.assertEquals(PowSpd().roots(), ['Power', 'Speed'])
    def testWilFor(self):
        class WilFor(skill.WillRoot, skill.ForteRoot):
            pass
        self.assertEquals(WilFor().roots(), ['Will', 'Forte'])
    def testWise(self):
        test_wise = skill.Wise('Testing')
        self.assertEquals(test_wise.name, 'Testing-wise')
        self.assertEquals(test_wise.roots(), ['Perception'])
        python_wise = skill.Wise('Python')
        test_again = skill.Wise('Testing')
        self.assertEquals(test_wise, test_again)
        self.assertNotEquals(test_wise, python_wise)
                
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(SkillTests))
