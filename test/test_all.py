import unittest

from test import char_basic_test, char_skill_test, char_stat_test, char_trait_test, char_world_test, human_test, lifepath_test, req_test, skill_test, trait_test, world_test

suite = unittest.TestLoader().loadTestsFromModule(char_basic_test)
suite.addTests(unittest.TestLoader().loadTestsFromModule(char_skill_test))
suite.addTests(unittest.TestLoader().loadTestsFromModule(char_stat_test))
suite.addTests(unittest.TestLoader().loadTestsFromModule(char_trait_test))
suite.addTests(unittest.TestLoader().loadTestsFromModule(char_world_test))
suite.addTests(unittest.TestLoader().loadTestsFromModule(human_test))
suite.addTests(unittest.TestLoader().loadTestsFromModule(lifepath_test))
suite.addTests(unittest.TestLoader().loadTestsFromModule(req_test))
suite.addTests(unittest.TestLoader().loadTestsFromModule(skill_test))
suite.addTests(unittest.TestLoader().loadTestsFromModule(trait_test))
suite.addTests(unittest.TestLoader().loadTestsFromModule(world_test))

unittest.TextTestRunner().run(suite)
