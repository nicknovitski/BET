import unittest
from character.req import Requirement
from character.char import Character
from character.trait import Trait
from character.lifepath import Lifepath


class ReqTests(unittest.TestCase):
    """each req object represents a set of conditions which must _all_ be met for thhe
'allowed' function to return true.  A lifepath or trait might have multiple possible sets of conditions,
_any_ of which can be met.
"""

    def testToString(self):
        self.assertEquals(str(Requirement()), 'None')

##    def testBorn(self):
##        self.assertTrue(Requirement().allowed(Character()))
##        self.assertFalse(Requirement().allowed(Character()))

##    def testMaxAge(self):
        #self.assertFalse(Requirement().allowed(Character(age=100)))

##    def testOnceOnly(self):
##        once_only = Requirement(once_only=True)
##        char = Character()
##        self.assertTrue(once_only.allowed(char, Lifepath(born=True, name='Name of Path')))
##        char.add_path(Lifepath(born= True, name='Name of Path'))
##        self.assertFalse(once_only.allowed(char, Lifepath('Name of Path')))

##    def testSecondOnly(self):
##        second_only = Requirement(second_only=True)
##        char = Character()
##        self.assertFalse(second_only.allowed(char, Lifepath(born=True)))
##        char.add_path(Lifepath(born=True))
##        self.assertTrue(second_only.allowed(char))
##        char.add_path(Lifepath())
##        self.assertFalse(second_only.allowed(char))
##
##    def testSecondThirdOnly(self):
##        second_or_third_only = Requirement(second_or_third_only=True)
##        char = Character()
##        
##        self.assertFalse(second_or_third_only.allowed(char, Lifepath(born=True)))
##        char.add_path(Lifepath(born=True))
##        self.assertTrue(second_or_third_only.allowed(char))
##        char.add_path(Lifepath())
##        self.assertTrue(second_or_third_only.allowed(char))
##        char.add_path(Lifepath())
##        self.assertFalse(second_or_third_only.allowed(char))
##
##    def testNotSecond(self):
##        not_second = Requirement(not_second = True)
##        char = Character().add_path(Lifepath(born=True))
##        self.assertFalse(not_second.allowed(char))
##        char.add_path(Lifepath())
##        self.assertTrue(not_second.allowed(char))
##
##    def testNotThird(self):
##        not_third = Requirement(not_third=True)
##        char = Character().add_path(Lifepath(born=True))
##
##        self.assertTrue(not_third.allowed(char))
##
##        char.add_path(Lifepath())
##        self.assertFalse(not_third.allowed(char))
##
##        char.add_path(Lifepath())
##        self.assertTrue(not_third.allowed(char))

    def testAge(self):
        age_req = Requirement(age=10)
        char = Character()
        char.add_path(Lifepath(years=5, born=True))

        self.assertFalse(age_req.allowed(char))
        char.add_path(Lifepath(years=5))
        self.assertTrue(age_req.allowed(char))

    def testAnyLifepath(self):
        charA = Character([Lifepath(name='A', born=True)])
        charB = Character([Lifepath(name='B', born=True)])
        charC = Character([Lifepath(name='C', born=True)])
        
        one_path_once=Requirement(paths={('A',): 1})
        self.assertTrue(one_path_once.allowed(charA))
        self.assertFalse(one_path_once.allowed(charB))
        self.assertFalse(one_path_once.allowed(charC))

        two_paths_once=Requirement(paths={('A', 'B'): 1})
        self.assertTrue(two_paths_once.allowed(charA))
        self.assertTrue(two_paths_once.allowed(charB))
        self.assertFalse(two_paths_once.allowed(charC))
        
        one_path_once_twice=Requirement(paths={('A',):1, ('B',):1})
        self.assertFalse(one_path_once_twice.allowed(charA))
        self.assertFalse(one_path_once_twice.allowed(charB))
        self.assertFalse(one_path_once_twice.allowed(charC))
        
        one_path_twice=Requirement(paths={('A',): 2})
        self.assertFalse(one_path_twice.allowed(charA))
        self.assertFalse(one_path_twice.allowed(charB))
        self.assertFalse(one_path_twice.allowed(charC))
        charA.add_path(Lifepath('A'))
        self.assertTrue(one_path_twice.allowed(charA))
        
        two_paths_twice=Requirement(paths={('A', 'B'): 2})
        self.assertTrue(two_paths_twice.allowed(charA))
        self.assertFalse(two_paths_twice.allowed(charB))
        self.assertFalse(two_paths_twice.allowed(charC))
        charB.add_path(Lifepath('A'))
        self.assertTrue(two_paths_twice.allowed(charB))
        
    def testAllLifepaths(self):
        one_path=Requirement(paths={('A',):0})
        two_paths=Requirement(paths={('A', 'B'):0})
        one_path_twice=Requirement(paths={('A',):0,('B',):0})

        charA = Character([Lifepath(name='A', born=True)])
        charB = Character([Lifepath(name='B', born=True)])
        charAPlusB =Character([Lifepath(name='A', born=True), Lifepath('B')])
        self.assertTrue(one_path.allowed(charA))
        self.assertFalse(one_path.allowed(charB))
        self.assertTrue(two_paths.allowed(charAPlusB))
        self.assertFalse(two_paths.allowed(charA))
        self.assertFalse(two_paths.allowed(charB))
        self.assertTrue(one_path_twice.allowed(charAPlusB))
        self.assertFalse(one_path_twice.allowed(charA))
        self.assertFalse(one_path_twice.allowed(charB))

    def testAnyAndAll(self):
        pass

    def testAnyFromSetting(self):
        """born lifepaths never count towards this
        """
        from character.human import AnvilLifepath, HammerLifepath
        one_if_by_land = Requirement(paths={(AnvilLifepath,):1})
        two_if_by_space = Requirement(paths={(HammerLifepath,):2})
        combined_arms = Requirement(paths={(AnvilLifepath,HammerLifepath):1})

        soldier = Character([AnvilLifepath(born=True)])
        sailor = Character([HammerLifepath(born=True)])
        marine = Character([HammerLifepath(born=True), AnvilLifepath()])

        self.assertFalse(one_if_by_land.allowed(soldier))
        self.assertFalse(two_if_by_space.allowed(soldier))
        self.assertFalse(combined_arms.allowed(soldier))
        soldier.add_path(AnvilLifepath())
        self.assertTrue(one_if_by_land.allowed(soldier))
        self.assertFalse(two_if_by_space.allowed(soldier))
        self.assertTrue(combined_arms.allowed(soldier))

        self.assertFalse(one_if_by_land.allowed(sailor))
        self.assertFalse(two_if_by_space.allowed(sailor))
        self.assertFalse(combined_arms.allowed(sailor))
        sailor.add_path(HammerLifepath())
        self.assertFalse(one_if_by_land.allowed(sailor))
        self.assertFalse(two_if_by_space.allowed(sailor))
        self.assertTrue(combined_arms.allowed(sailor))
        sailor.add_path(HammerLifepath())
        self.assertTrue(two_if_by_space.allowed(sailor))
        
        self.assertTrue(one_if_by_land.allowed(marine))
        self.assertFalse(two_if_by_space.allowed(marine))
        self.assertTrue(combined_arms.allowed(marine))
        marine.add_path(HammerLifepath())
        self.assertFalse(two_if_by_space.allowed(marine))
        marine.add_path(HammerLifepath())
        self.assertTrue(two_if_by_space.allowed(marine))
        
    def testAnyTrait(self):
        charA = Character(traits=[Trait('A')])
        charB = Character(traits=[Trait('B')])
        charC = Character(traits=[Trait('C')])
        
        A = Requirement(traits={(Trait('A'),): 1})
        self.assertTrue(A.allowed(charA))
        self.assertFalse(A.allowed(charB))
        self.assertFalse(A.allowed(charC))
        
        B = Requirement(traits={(Trait('B'),): 1})
        self.assertFalse(B.allowed(charA))
        self.assertTrue(B.allowed(charB))
        self.assertFalse(B.allowed(charC))
        
        C = Requirement(traits={(Trait('C'),): 1})
        self.assertFalse(C.allowed(charA))
        self.assertFalse(C.allowed(charB))
        self.assertTrue(C.allowed(charC))
        
        AorB = Requirement(traits={(Trait('A'),Trait('B')): 1})
        self.assertTrue(AorB.allowed(charA))
        self.assertTrue(AorB.allowed(charB))
        self.assertFalse(AorB.allowed(charC))
        
        AorC = Requirement(traits={(Trait('A'),Trait('C')): 1})
        self.assertTrue(AorC.allowed(charA))
        self.assertFalse(AorC.allowed(charB))
        self.assertTrue(AorC.allowed(charC))
        
        BorC = Requirement(traits={(Trait('B'),Trait('C')): 1})
        self.assertFalse(BorC.allowed(charA))
        self.assertTrue(BorC.allowed(charB))
        self.assertTrue(BorC.allowed(charC))
        
        whichever = Requirement(traits={(Trait('A'),Trait('B'),Trait('C')): 1})
        self.assertTrue(whichever.allowed(charA))
        self.assertTrue(whichever.allowed(charB))
        self.assertTrue(whichever.allowed(charC))
        
    def testNoTrait(self):
        charA = Character(traits=[Trait('A')])
        charB = Character(traits=[Trait('B')])
        charC = Character(traits=[Trait('C')])

        notA = Requirement(traits={('A',): -1})
        notB = Requirement(traits={('B',): -1})
        notC = Requirement(traits={('C',): -1})
        notAnorB = Requirement(traits={('A','B'): -1})
        notAnorC = Requirement(traits={('A','C'): -1})
        notBnorC = Requirement(traits={('B','C'): -1})
        none = Requirement(traits={('A','B','C'): -1})

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(ReqTests))
