class Requirement(object):
    def __init__(self, 
                 age=0,
                 paths={},
                 trait_any=[],
                 trait_none=[],
                 traits={}):
        self.age = age
        self.paths = paths
        self.traits = traits
        self.trait_any = trait_any
        self.trait_none = trait_none

    def __str__(self):
        return 'None'
    
    def allowed(self, character):
        if self.age:
            if character.age() < self.age:
                return False

        if self.paths:
            for path_list, times in self.paths.iteritems():
                if times > 0:
                    if not character.has_taken_any(path_list, times):
                        return False
                elif times == 0:
                    if not character.has_taken_all(path_list):
                        return False

        if self.traits:
            for trait_list, times in self.traits.iteritems():
                if times > 0:
                    found = False
                    for t in trait_list:
                        if character.has_trait(t):
                            found = True
                    if not found:
                        return False
                if times < 0:
                    for t in trait_list:
                        if character.has_trait(t):
                            return False

        return True
