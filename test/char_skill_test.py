import unittest

from character.char import Character
from character import skill
from character.lifepath import Lifepath
from character.exceptions import CantAfford 

class CharacterSkillTests(unittest.TestCase):
    def setUp(self):
        self.c = Character(starting_paths=[Lifepath(born=True, years=1, floater_points=100)])
        self.c.buy_agility(2)
        self.c.buy_speed(2)
        self.c.buy_power(2)
        self.c.buy_forte(2)
        self.c.buy_perception(2)
        self.c.buy_will(2)
    def testBlank(self):
        self.assertEquals(self.c.skill_points(), 0)
        self.assertEquals(self.c.get_skills(), [])
        
    def testCountSkillPoints(self):
        """The first and second times a path is taken, the first untaken skill must be opened
        The third time, this is not the case, but the path only gives half points
        After this, no points are awarded.
        """
        self.assertEquals(self.c.skill_points(), 0)
        self.c.add_path(Lifepath(name = "Path A", skill_points=1))
        self.assertEquals(self.c.skill_points(), 1)
        self.c.add_path(Lifepath(name = "Path B", skill_points=2))
        self.assertEquals(self.c.skill_points(), 3)
        self.c.add_path(Lifepath(name = "Path C", skill_points=1, skills=[skill.Skill(name='Required Skill'), skill.Skill(name='Optional Skill')]))
        self.assertEquals(self.c.skill_points(), 3)
        self.c.add_path(Lifepath(name = "Path B", skill_points=2))
        self.assertEquals(self.c.skill_points(), 5)
        self.c.add_path(Lifepath(name = "Path B", skill_points=2))
        self.assertEquals(self.c.skill_points(), 6)
        self.c.add_path(Lifepath(name = "Path B", skill_points=2))
        self.assertEquals(self.c.skill_points(), 6)
    def testLifepathSkillList(self):
        self.assertEquals(self.c.lifepath_skills(), [])
        self.c.add_path(Lifepath(name = "Path A", skills = [skill.Skill(name='Lifepath Skill')], skill_points=1))
        self.assertTrue(len(self.c.lifepath_skills()), 1)
        
        self.c.add_path(Lifepath(name = "Path B", skills = [skill.Skill(name='Lifepath Skill')], skill_points=1))
        self.assertEquals(len(self.c.lifepath_skills()), 1)
        self.c.add_path(Lifepath(name = "Path C", skills = [skill.Skill(name='New Skill'), skill.Skill(name='Other Skill')], skill_points=1))
        self.assertEquals(len(self.c.lifepath_skills()), 3)
    def testRequiredLPSkills(self):
        self.c.add_path(Lifepath(name = "Path A", skills=[skill.PerceptionRoot(name='Skill on list 1'), skill.AgilityRoot(name='Skill on list 2')], skill_points=1))
        self.assertEquals(len(self.c.lifepath_skills()), 2)
        self.assertEquals([{'name':'Skill on list 1','roots':['Perception']}], self.c.required_skills())
        self.assertEquals([{'name':'Skill on list 1','roots':['Perception'],'points':1}], self.c.get_skills())
        self.assertEquals([{'name':'Skill on list 1','roots':['Perception'],'points':1}], self.c.get_skills())
        #self.assertEquals(len(self.c.get_skills()), 1)
        self.assertEquals(self.c.skill_points(), 0)
        self.c.add_path(Lifepath(name = "Path A", skills=[skill.PerceptionRoot(name='Skill on list 1'), skill.AgilityRoot(name='Skill on list 2')], skill_points=1))
        self.assertEquals(self.c.skill_points(), 0)
        self.assertEquals(len(self.c.lifepath_skills()), 2)
        self.assertTrue({'name':'Skill on list 1','roots':['Perception']} in self.c.required_skills())
        self.assertTrue({'name':'Skill on list 2','roots':['Agility']} in self.c.required_skills())
        self.assertTrue({'name':'Skill on list 1','roots':['Perception'],'points':1} in self.c.get_skills())
        self.assertTrue({'name':'Skill on list 2','roots':['Agility'],'points':1} in self.c.get_skills())
    def testBuySkillNotOnList(self):
        """General points are halved the third time a lifepath is taken, and removed the fourth time.
        """
        # like floater points, general points are always spent last and returned first
        path_g = Lifepath(name ='Path G', general_skill_points=2)
        self.assertRaises(CantAfford, self.c.buy_skill, skill.Skill(name='Skill not on lifepath list'))
        self.c.add_path(Lifepath(skill_points=1))
        self.assertRaises(CantAfford, self.c.buy_skill, skill.PerceptionRoot(name='Skill not on lifepath list'))
        self.c.add_path(path_g)
        self.assertEquals(self.c.general_skill_points(), 2)
        self.c.buy_skill(skill.PerceptionRoot(name='Skill not on lifepath list'))
        self.assertEquals(self.c.skill_points(), 1)
        self.assertEquals(self.c.general_skill_points(), 1)
        self.c.buy_skill(skill.PerceptionRoot(name='Skill not on lifepath list'))
        self.assertEquals(self.c.general_skill_points(), 0)
        self.assertEquals(self.c.skill_points(), 1)
        self.assertRaises(CantAfford, self.c.buy_skill, skill.PerceptionRoot(name='Skill not on lifepath list'))
        self.c.add_path(path_g)
        self.assertEquals(self.c.general_skill_points(), 2)
        self.c.add_path(path_g)
        self.assertEquals(self.c.general_skill_points(), 3)
        self.c.add_path(path_g)
        self.assertEquals(self.c.general_skill_points(), 3)
    def testBuySkillOnList(self):
        self.assertEquals(self.c.get_skills(), [])
        self.c.add_path(Lifepath(name = "Path A", skills=[skill.PerceptionRoot(name='Skill on list 1'), skill.AgilityRoot(name='Skill on list 2')], skill_points=1))
        self.assertEquals([{'name':'Skill on list 1','roots':['Perception'],'points':1}], self.c.get_skills())
        self.assertEquals(self.c.skill_points(), 0)
        self.assertRaises(CantAfford, self.c.buy_skill, skill.PerceptionRoot(name='Skill on list 2'))
        self.c.add_path(Lifepath(name = "Path B", skill_points=2))
        self.assertEquals(self.c.skill_points(), 2)
        self.c.buy_skill(skill.PerceptionRoot(name='Skill on list 1'))
        self.assertEquals(self.c.skill_points(), 1)
        self.assertTrue({'name':'Skill on list 1','roots':['Perception'],'points':2} in self.c.get_skills())
        self.c.buy_skill(skill.PerceptionRoot(name='Skill on list 2'))
        self.assertTrue({'name':'Skill on list 2','roots':['Perception'],'points':1} in self.c.get_skills())
        self.assertEquals(self.c.skill_points(), 0)
    def testSkillExponent(self):
        self.assertEquals(self.c.skill_totals(), [])
        self.c.bought_skills = [{'name':'Skill on list 1','roots':['Perception'],'points':1}]
        self.assertEquals(self.c.skill_totals(), [{'name':'Skill on list 1', 'exponent':1}])
        self.c.bought_skills = [{'name':'Skill on list 1','roots':['Perception'],'points':3}]
        self.assertEquals(self.c.skill_totals(), [{'name':'Skill on list 1', 'exponent':3}])
        self.c.perception += 1
        self.assertEquals(self.c.skill_totals(), [{'name':'Skill on list 1', 'exponent':3}])
        self.c.perception += 1
        self.assertEquals(self.c.skill_totals(), [{'name':'Skill on list 1', 'exponent':4}])
        self.c.bought_skills = [{'name':'Skill on list 1','roots':['Perception', 'Will'],'points':3}]
        self.assertEquals(self.c.skill_totals(), [{'name':'Skill on list 1', 'exponent':3}])
    def testRemoveSkills(self):
        skill_one = skill.PerceptionRoot(name='Skill on list 1')
        skill_two = skill.AgilityRoot(name='Skill on list 2')
        self.c.add_path(Lifepath(name = "Path A", skills=[skill_one, skill_two], skill_points=2))
        self.assertEquals([{'name':'Skill on list 1','roots':['Perception'],'points':1}], self.c.get_skills())
        
        self.assertRaises(Exception, self.c.remove_skill, skill_one)
        self.assertEquals(self.c.skill_points(), 1)
        self.c.buy_skill(skill_two)
        self.assertEquals(self.c.skill_points(), 0)
        self.assertTrue({'name':'Skill on list 2','roots':['Agility'],'points':1} in self.c.get_skills())
        self.c.remove_skill(skill_two)
        self.assertEquals([{'name':'Skill on list 1','roots':['Perception'],'points':1}], self.c.get_skills())
        self.assertEquals(self.c.skill_points(), 1)
        self.c.buy_skill(skill_two)
        self.c.add_path(Lifepath(name='Path G', general_skill_points = 1))
        self.assertEquals(self.c.general_skill_points(), 1)
        self.assertEquals(self.c.skill_points(), 0)
        self.c.buy_skill(skill_two)
        self.assertEquals(self.c.general_skill_points(), 0)
        self.assertEquals(self.c.skill_points(), 0)
        self.c.remove_skill(skill_two)
        self.assertEquals(self.c.general_skill_points(), 1)
        self.assertEquals(self.c.skill_points(), 0)
    def testRemovePath(self):
        pass
    
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(CharacterSkillTests))
