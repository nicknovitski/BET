class Lifepath(object):
    def __init__(self, name = 'Default',
                 years = 0, resources=0, circles=0,
                 mental_points = 0, physical_points = 0, floater_points=0,
                 trait_points=0, traits=[],
                 general_skill_points=0,
                 skill_points=0,
                 skills=[],
                 requirements=[],
                 born = False,
                 once_only=False,
                 second_only=False,
                 second_or_third_only = False,
                 not_second=False,
                 not_third=False):
        self.name = name
        self.years = years
        self.resources = resources
        self.circles = circles
        self.trait_points = trait_points
        self.traits = traits
        self.physical_points = physical_points
        self.mental_points = mental_points
        self.floater_points = floater_points
        self.general_skill_points = general_skill_points
        self.skill_points=skill_points
        self.skills=skills

        self.requirements = requirements
        self.born = born
        self.once_only = once_only
        self.second_only= second_only
        self.not_second = not_second
        self.not_third = not_third
        self.second_or_third_only = second_or_third_only

    def __str__(self):
        return self.name
        
    def same_setting(self, lifepath):
        return issubclass(self.__class__, lifepath.__class__.__bases__)

    def __eq__(self, other):
        return (isinstance(self, other.__class__) and self.name == other.name)

    def __ne__(self, other):
        return (not isinstance(self, other.__class__) or not self.name == other.name)

    def __repr__(self):
        return self.__class__.__module__+'.'+self.__class__.__name__+'()'
    
    def allowed(self, character):
        if character.path_count():
            if self.born:
                return False
        elif not self.born:
            return False
        
        if self.once_only and character.has_taken(self.name):
            return False

        if self.second_only and character.path_count() != 1:
            return False

        if self.second_or_third_only and character.path_count() != 1 and character.path_count() != 2:
            return False

        if self.not_second and character.path_count() == 1:
            return False

        if self.not_third and character.path_count() == 2:
            return False

        if character.age() + self.years > 100:
            return False

        if self.requirements:
            found = True
            found_set = False
            for x in self.requirements:
                if not found_set:
                    found_set=True
                    found=False
                if x.allowed(character):
                    found = True
            if not found:
                return False
        
        return True
