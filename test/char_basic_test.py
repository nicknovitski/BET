import unittest
from character.char import Character
from character.lifepath import Lifepath
from character import human
from character.exceptions import NotAllowed 

class BasicCharacterTests(unittest.TestCase):
    def setUp(self):
        self.char = Character()
    def testPathCountBlank(self):
        self.assertEquals(self.char.path_count(), len(self.char.life_paths))
        self.assertEquals(self.char.path_count(), 0)
    def testAddPath(self):
        self.char.add_path(Lifepath(born=True))
        self.assertEquals(self.char.path_count(), 1)
        self.assertEquals(self.char.path_count(), len(self.char.life_paths))
        self.char.add_path(Lifepath())
        self.assertEquals(self.char.path_count(), 2)
        self.assertEquals(self.char.path_count(), len(self.char.life_paths))
        self.char.add_path(Lifepath()).add_path(Lifepath())
        self.assertEquals(self.char.path_count(), 4)
        self.assertEquals(self.char.path_count(), len(self.char.life_paths))
    def testCreateInBatch(self):
        char_series = Character().add_path(Lifepath(born=True)).add_path(Lifepath()).add_path(Lifepath())
        char_batch = Character([Lifepath(born=True),Lifepath(),Lifepath()])
        self.assertEquals(char_series.path_count(),char_batch.path_count())
        self.assertEquals(char_series.age(),char_batch.age())
        self.assertEquals(char_series.circles(),char_batch.circles())
        self.assertEquals(char_series.resources(),char_batch.resources())
        self.assertEquals(char_series.traits(),char_batch.traits())
        self.assertEquals(char_series.lifepath_traits(),char_batch.lifepath_traits())
        self.assertEquals(char_series.trait_points(),char_batch.trait_points())
    def testAddNotAllowed(self):
        self.char.add_path(Lifepath(born=True))
        self.assertRaises(NotAllowed, self.char.add_path, Lifepath(born=True))
    def testHasTaken(self):
        self.assertFalse(self.char.has_taken('Born Lifepath'))
        self.char.add_path(Lifepath(name = 'Born Lifepath', born=True))
        self.assertTrue(self.char.has_taken('Born Lifepath'))
        self.assertFalse(self.char.has_taken('Other Lifepath'))
    def testHasTakenError(self):
        """has_taken and all related functions expect a string and throw a type error otherwise
        """
        self.assertRaises(TypeError, self.char.has_taken, 5)
        self.assertRaises(TypeError, self.char.has_taken, ('Lifepath',))
        self.assertRaises(TypeError, self.char.has_taken, ['Lifepath'])
        
    def testHasTakenAny(self):
        self.char.add_path(Lifepath(name = 'Born Lifepath', born=True))
        self.assertTrue(self.char.has_taken_any(['Court Coeptir', 'Court Clerk', 'Born Lifepath']))
        self.assertFalse(self.char.has_taken_any(['Court Coeptir', 'Court Clerk', 'Lord-Pilot Anvil']))
        
    def testHasTakenAll(self):
        self.char.add_path(Lifepath(name = 'Born Lifepath', born=True)).add_path(Lifepath('Lifepath'))
        self.assertTrue(self.char.has_taken_all(['born lifepath']))
        self.assertTrue(self.char.has_taken_all(['born lifepath', 'lifepath']))
        self.assertFalse(self.char.has_taken_all(['born lifepath', 'lifepath', 'other lifepath']))
        self.char.add_path(Lifepath(name='Other Lifepath'))
        self.assertTrue(self.char.has_taken_all(['born lifepath', 'lifepath', 'other lifepath']))
        
    def testTimesTaken(self):
        self.char.add_path(Lifepath(name = 'Born Lifepath', born=True)).add_path(Lifepath('Lifepath')).add_path(Lifepath(name='Lifepath'))
        self.assertEquals(self.char.times_taken('Lifepath'), 2)
        self.assertEquals(self.char.times_taken('Born Lifepath'), 1)
        self.assertEquals(self.char.times_taken('Anything Else'), 0)
        
    def testHasTakenTwice(self):
        self.char.add_path(Lifepath(born=True)).add_path(Lifepath('Lifepath')).add_path(Lifepath(name='Lifepath'))
        self.assertTrue(self.char.has_taken_twice('Lifepath'))
        self.assertFalse(self.char.has_taken_twice('Default'))
        self.assertTrue(self.char.has_taken('Lifepath', 2))
        self.assertFalse(self.char.has_taken('Default', 2))
        
    def testHasTakenAny(self):
        self.char.add_path(Lifepath(name = 'Born Lifepath', born=True)).add_path(Lifepath('Lifepath'))
        self.assertTrue(self.char.has_taken_any(['Born Lifepath', 'Lifepath'], 2))
        self.assertFalse(self.char.has_taken_any(['Born Lifepath'], 2))
        self.char.add_path(Lifepath())
        self.assertTrue(self.char.has_taken_any(['Default', 'Lifepath'], 2))
        self.assertTrue(self.char.has_taken_any(['Default', 'Lifepath', 'Born Lifepath'], 3))
        
    def testHasTakenAnyRepeating(self):
        """if the list has the same name on it multiple times, that should be ignored
        """
        self.char.add_path(Lifepath(name = 'Born Lifepath', born=True))
        self.assertFalse(self.char.has_taken_any(['Born Lifepath', 'Born Lifepath'], 2))
        self.assertFalse(self.char.has_taken_any(['Born Lifepath', 'Something Else', 'Born Lifepath', 'born lifePath'], 2))
        
    def testIgnoresCase(self):
        """lifepaths are identified by non-unique names.  Upper- and lower-case letters shouldn't matter
        """
        self.char.add_path(Lifepath(name = 'Born Lifepath', born=True))
        self.assertTrue(self.char.has_taken('born lifepath'))
        self.assertTrue(self.char.has_taken('BORN LIFEPATH'))
        self.assertEquals(self.char.times_taken('born lifepath'), 1)
        self.assertEquals(self.char.times_taken('BORN lIFEPATH'), 1)
        self.char.add_path(Lifepath()).add_path(Lifepath())
        self.assertTrue(self.char.has_taken('default', 2))
        self.assertTrue(self.char.has_taken('DEFAULT', 2))
        self.assertTrue(self.char.has_taken_any(['born lifepath']))
        self.assertTrue(self.char.has_taken_any(['BORN LIFEPATH']))
        self.assertTrue(self.char.has_taken_any(['DEFAULT'], 2))
        self.assertTrue(self.char.has_taken_any(['default'], 2))
        self.assertTrue(self.char.has_taken_any(['born lifepath', 'default'], 3))
        self.assertTrue(self.char.has_taken_any(['BORN LIFEPATH', 'DEFAULT'], 3))
    def testHasTakenAnyFromSetting(self):
        """Born Lifepaths never count for the purposes of this function.
        """
        self.char.add_path(human.NobleLifepath(born=True)).add_path(human.HammerLifepath())
        self.assertTrue(self.char.has_taken_any_from(human.HammerLifepath))
        self.assertFalse(self.char.has_taken_any_from(human.TheocracyLifepath))
        self.assertFalse(self.char.has_taken_any_from(human.NobleLifepath))
    def testHasTakenAnyFromSettingTwice(self):
        """Born Lifepaths never count for the purposes of this function.
        """
        self.char.add_path(human.NobleLifepath(born=True)).add_path(human.NobleLifepath())
        self.assertFalse(self.char.has_taken_any_from(human.NobleLifepath, 2))
        self.char.add_path(human.NobleLifepath())
        self.assertTrue(self.char.has_taken_any_from(human.NobleLifepath, 2))
    def testRemove(self):
        self.char.add_path(Lifepath(born=True)).add_path(Lifepath()).add_path(Lifepath())
        self.assertEquals(self.char.traits(), [])
        self.assertEquals(self.char.trait_points(), 0)
        self.char.remove_path()
        self.assertEquals(self.char.path_count(), 2)
        self.char.remove_path(3)
        self.assertEquals(self.char.path_count(), 0)
    def testClear(self):
        self.char.add_path(Lifepath(born=True)).add_path(Lifepath()).clear()
        self.assertEquals(self.char.path_count(), 0)
    def testNoAge(self):
        self.assertEquals(self.char.age(), 0)
    def testBornAge(self):
        self.char.add_path(Lifepath(born=True, years=8))
        self.assertEquals(self.char.age(), 8)
        self.char.remove_path()
        self.assertEquals(self.char.age(), 0)
    def testSameSettingAge(self):
        character = Character([human.NobleLifepath(born=True, years=1),
                                        human.NobleLifepath(years=1),
                                        human.NobleLifepath(years=1)])
        self.assertEquals(character.age()
                          ,3)
    def testMoveSettingsAge(self):
        self.char.add_path(human.BornNobility()).add_path(human.CourtCoeptir())
        self.assertEquals(self.char.age(), 13)
        self.char.remove_path()
        self.assertEquals(self.char.age(), 8)

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(BasicCharacterTests))
