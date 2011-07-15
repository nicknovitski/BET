import unittest
from world import world
from character.char import Character

class CharacterWorldTests(unittest.TestCase):
    
    def testAddWorld(self):

        c = Character()
        self.assertRaises(Exception, c.set_world, world.World())
        w = world.World(name='TestLand',
                        empire=world.COMORAN,
                        location=world.INT,
                        atmosphere=world.HLS,
                        topography=world.BROAD,
                        index=world.LOW,
                        government=world.NOBLE,
                        military=world.LORDSPILOT,
                        attitude=world.PARANOID,
                        export=world.INDUSTRIAL,
                        quarantine=world.NONE,
                        regulation=world.LOOSE,
                        hydrology=world.LAND)
        c.set_world(w)
        self.assertEquals(c.get_world().get_name(), 'TestLand')

    def testAttitudeTrait(self):
        """Only characters who take a born lifepath in a native setting get the planetary attitude as a character trait
        """
        pass
    def testSettingsAge(self):
        """going to a non-native setting adds two years to the character's age
        """
        pass
    def testBlockadeBlocksSpacefarer(self):
        """
        """
        pass

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(CharacterWorldTests))
