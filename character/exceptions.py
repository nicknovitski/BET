class NotAllowed(Exception):
    def __init__(self, path='Path', reason='not allowed', character = '', requirements=0):
        self.path = path
        self.reason = reason
        self.character = character
        self.requirements = requirements
    def __str__(self):
        if self.requirements:
            excep = str(self.path) + ' cannot be added to character (' + str(self.character)+ ')  Requires: '+str(self.requirements)
        else:
            excep = str(self.path) + ' cannot be added to character ' + str(self.character)+'; ' + self.reason
        return excep

class CantAfford(Exception):
    def __init__(self, reason):
        self.reason = reason
    def __str__(self):
        return self.reason

class ExceedsMaximum(Exception):
    def __init__(self, stat, maximum):
        self.stat = stat
        self.maximum = maximum
    def __str__(self):
        excep = "Character's "+self.stat+" cannot exceed "+str(self.maximum)+" in in creation"
        return excep
