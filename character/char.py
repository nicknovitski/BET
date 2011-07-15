from decimal import *
from lifepath import Lifepath
from exceptions import ExceedsMaximum, NotAllowed, CantAfford

class Character(object):
    perception = 0
    will = 0
    agility = 0
    speed = 0
    power = 0
    forte = 0
    spent_floater=0
    spent_general=0
    world = None
    def __init__(self,
                 starting_paths=[],
                 age = 0,
                 traits = []):
        self.starting_age = age
        self.starting_traits = traits
        self.life_paths = []
        self.bought_traits = []
        self.bought_skills = []
        for x in starting_paths:
            self.add_path(x)
    def __str__(self):
        paths = '(['
        for x in self.life_paths:
            paths += str(x)
            paths += '->'
        paths += '])'
        return paths
    def set_world(self, world):
        if world.ready():
            self.world = world
        else:
            raise Exception
    def get_world(self):
        return self.world
    def add_path(self, path):
        if not isinstance(path, Lifepath):
            raise TypeError
        if self.age() + path.years > 100:
            raise ExceedsMaximum('Age', 100)
        if path.allowed(character=self):
            self.life_paths.append(path)
            while self.mental_pool() < 0:
                if self.perception > self.will:
                    self.perception -= 1
                else:
                    self.will -= 1
            while self.physical_pool() < 0:
                if self.speed >= self.power and self.speed >= self.forte and self.speed >= self.agility:
                    self.speed -= 1
                elif self.power >= self.speed and self.power >= self.forte and self.power >= self.agility:
                    self.power -= 1
                elif self.forte >= self.power and self.forte >= self.speed and self.forte >= self.agility:
                    self.forte -= 1
                elif self.agility >= self.power and self.agility >= self.forte and self.agility >= self.speed:
                    self.agility -= 1
                else:
                    pass            
            return self
        else:
            raise NotAllowed(path, character=self)
    def remove_path(self, number=1):
        i = 0
        if number > self.path_count():
            number = self.path_count()
        while i < number: 
            self.life_paths.pop()
            i+=1
        while self.trait_points() < 0:
           self.bought_traits.pop()
        while self.mental_pool() < 0:
            if self.perception > self.will:
                self.perception -= 1
            else:
                self.will -= 1
        while self.physical_pool() < 0:
            if self.speed >= self.power and self.speed >= self.forte and self.speed >= self.agility:
                self.speed -= 1
            elif self.power >= self.speed and self.power >= self.forte and self.power >= self.agility:
                self.power -= 1
            elif self.forte >= self.power and self.forte >= self.speed and self.forte >= self.agility:
                self.forte -= 1
            elif self.agility >= self.power and self.agility >= self.forte and self.agility >= self.speed:
                self.agility -= 1
            else:
                pass            
        return self 
    def clear(self):
        self.life_paths = []
        return self
    def path_count(self):
        return len(self.life_paths)
    def has_taken(self, path_name, times=1):
        if self.times_taken(path_name) >= times:
            return True
        else:
            return False
    def has_taken_twice(self, path_name):
        return self.has_taken(path_name, 2)
    def has_taken_any(self, mixed_list, times = 1):
        path_list = []
        found = False
        for x in mixed_list:
            if isinstance(x, type):
                if self.has_taken_any_from(x, times):
                    found = True
            elif isinstance(x, str):
                path_list.append(x.lower())
            else:
                raise TypeError
            
        count = 0
        for x in path_list:
            if path_list.count(x) > 1:
                del path_list[path_list.index(x)]
        for x in path_list:
            count+=self.times_taken(x)
        if count >= times or found:
            return True
        else:
            return False
    def times_taken(self, path_name):
        count = 0
        if not isinstance(path_name, str):
            raise TypeError
        for x in self.life_paths:
            if x.name.lower() == path_name.lower():
                count+=1
        return count
    def has_taken_any_from(self, setting, times = 1):
        count = 0
        for x in self.life_paths:
            if isinstance(x, setting):
                if not x.born:
                    count += 1
        if count >= times:
            return True
        else:
            return False
    def has_taken_all(self, path_list):
        for x in path_list:
            if not self.has_taken(x):
                return False
        return True
    def age(self):
        total = 0
        if self.life_paths:
            previous = self.life_paths[0]
            for path in self.life_paths:
                total += path.years
                if not path.same_setting(previous):
                    total += 1
                previous = path
        return total + self.starting_age
    def mental_pool(self):
        age = self.age()
        if age == 0:
            points = 0
        elif age >=1 and age <=10:
            points =  5
        elif age >=11 and age <=16:
            points = 6
        elif age >=17 and age <=79:
            points = 7
        elif age >=80 and age <=100:
            points = 6
        else:
            #dead
            pass
        spent = self.perception + self.will
        bonus = 0
        for x in self.life_paths:
            bonus += x.mental_points
        if points-spent+bonus < 0:
            if self.spent_floater+points-spent+bonus >= 0:
                return 0
        return points - spent + bonus
    def physical_pool(self):
        age = self.age()
        if age == 0:
            points = 0
        elif age >= 1 and age <=10:
            points = 10
        elif age >=11 and age <=14:
            points = 13
        elif age >=15 and age <=25:
            points = 16
        elif age >=26 and age <=29:
            points = 15
        elif age >=30 and age <=35:
            points = 14
        elif age >=36 and age <=40:
            points = 13
        elif age >=41 and age <=55:
            points = 12
        elif age >= 56 and age <= 65:
            points =  11
        elif age >=66 and age <= 79:
            points = 10
        elif age >=80 and age <= 100:
            points = 9
        else:
            #dead
            pass
        spent = self.agility + self.speed + self.power + self.forte
        bonus = 0
        for x in self.life_paths:
            bonus += x.physical_points
        if points-spent+bonus < 0:
            if self.spent_floater+points-spent+bonus >= 0:
                return 0
        return points - spent + bonus
    def floater_pool(self):
        points = 0
        for x in self.life_paths:
            points += x.floater_points
        return points-self.spent_floater
    def buy_perception(self, points=1):
        if self.perception + points > 6:
            raise ExceedsMaximum('Perception', 6)
        if self.mental_pool() - points >= 0:
            self.perception += points
        elif self.mental_pool() - points + self.floater_pool() >=0:
            self.spent_floater += points-self.mental_pool()
            self.perception+= points
        else:
            raise CantAfford('Cannot increase Perception by '+str(points)+', only '+str(self.mental_pool()) +' points available')

    def remove_perception(self, points=1):
        if self.perception < points:
            points = self.perception
        if self.spent_floater and self.spent_floater >= points:
            self.spent_floater -= points
        elif self.spent_floater < points:
            self.spent_floater = 0
        self.perception -= points
        
    def buy_will(self, points=1):
        if self.will + points > 6:
            raise ExceedsMaximum('Will', 6)
        if self.mental_pool() -points >=0:
            self.will += points
        elif self.mental_pool() - points + self.floater_pool() >= 0:
            self.spent_floater += points - self.mental_pool()
            self.will += points
        else:
            raise CantAfford('Cannot increase Will by '+str(points)+', only '+str(self.mental_pool()) +' points available')

    def remove_will(self, points=1):
        if self.will < points:
            points = self.will
        if self.spent_floater and self.spent_floater >= points:
            self.spent_floater -= points
        elif self.spent_floater < points:
            self.spent_floater = 0
        self.will -= points

    def buy_agility(self, points=1):
        if self.agility + points > 6:
            raise ExceedsMaximum('Agility', 6)
        if self.physical_pool() - points >= 0:
            self.agility += points
        elif self.physical_pool() - points + self.floater_pool() >= 0:
            self.spent_floater += points-self.physical_pool()
            self.agility += points
        else:
            raise CantAfford('Cannot increase Agility by '+str(points)+', only '+str(self.physical_pool()) +' points available')

    def remove_agility(self, points=1):
        if self.agility < points:
            points = self.agility
        if self.spent_floater and self.spent_floater >= points:
            self.spent_floater -= points
        elif self.spent_floater < points:
            self.spent_floater = 0
        self.agility -= points

    def buy_speed(self, points=1):
        if self.speed + points > 6:
            raise ExceedsMaximum('Speed', 6)
        if self.physical_pool() - points >= 0:
            self.speed += points
        elif self.physical_pool() - points + self.floater_pool() >= 0:
            self.spent_floater += points-self.physical_pool()
            self.speed += points
        else:
            raise CantAfford('Cannot increase Speed by '+str(points)+', only '+str(self.physical_pool()) +' points available')

    def remove_speed(self, points=1):
        if self.speed < points:
            points = self.speed
        if self.spent_floater and self.spent_floater >= points:
            self.spent_floater -= points
        elif self.spent_floater < points:
            self.spent_floater = 0
        self.speed -= points
    
    def buy_power(self, points=1):
        if self.power + points > 6:
            raise ExceedsMaximum('Power', 6)
        if self.physical_pool() - points >= 0:
            self.power += points
        elif self.physical_pool() - points + self.floater_pool() >= 0:
            self.spent_floater += points-self.physical_pool()
            self.power += points
        else:
            raise CantAfford('Cannot increase Power by '+str(points)+', only '+str(self.physical_pool()) +' points available')

    def remove_power(self, points=1):
        if self.power < points:
            points = self.power
        if self.spent_floater and self.spent_floater >= points:
            self.spent_floater -= points
        elif self.spent_floater < points:
            self.spent_floater = 0
        self.power -= points
        
    def buy_forte(self, points=1):
        if self.forte + points > 6:
            raise ExceedsMaximum('Forte', 6)
        if self.physical_pool() - points > 0:
            self.forte += points
        elif self.physical_pool() - points + self.floater_pool() >= 0:
            self.spent_floater += points-self.physical_pool()
            self.forte += points
        else:
            raise CantAfford('Cannot increase Forte by '+str(points)+', only '+str(self.physical_pool()) +' points available')

    def remove_forte(self, points=1):
        if self.forte < points:
            points = self.forte
        if self.spent_floater and self.spent_floater >= points:
            self.spent_floater -= points
        elif self.spent_floater < points:
            self.spent_floater = 0
        self.forte -= points
        
    def resources(self):
        res_total = 0
        tally = []
        for x in self.life_paths:
            tally.append(x)
            count = 0
            for y in tally:
                if x == y:
                    count +=1
            if count == 1 or count == 2:
                res_total += x.resources
            else:
                res_total += x.resources / 2
        return res_total
    def circles(self):
        circ_total = 0
        tally = []
        for x in self.life_paths:
            tally.append(x)
            count = 0
            for y in tally:
                if x == y:
                    count +=1
            if count == 1 or count == 2:
                circ_total += x.circles
        return circ_total
    def get_skills(self):
        mod_skills = self.bought_skills
        for req in self.required_skills():
            found = False
            for skill in mod_skills:
                if skill['name'] == req['name']:
                    found = True
                    skill = {'name':skill['name'], 'roots':skill['roots'], 'points':skill['points']+1}
                    break
            if not found:
                skill_dict = {'name':req['name'], 'roots':req['roots'], 'points':1}
                mod_skills.append(skill_dict)
        return mod_skills
    def required_skills(self):
        """The first and second time a lifepath is taken, the first skill not yet taken is required
        """
        required_skills = []
        skill_names = []
        lp_list = []
        for x in self.life_paths:
            lp_list.append(x)
            count = lp_list.count(x)
            if count == 1 or count == 2:
                for skill in x.skills:
                     if skill not in skill_names:
                         required_skills.append({'name':skill.name, 'roots':skill.roots()})
                         skill_names.append(skill)
                         break
        return required_skills
    def buy_skill(self, skill):
        if skill not in self.lifepath_skills() or self.skill_points() <=0:
            if self.general_skill_points() <= 0:
                raise CantAfford("Skill not in taken lifepaths, or no skill points remaining")
            else:
                self.spent_general += 1
        found = False
        for x in self.bought_skills:
            if x['name'] == skill.name:
                found = True
                x['points'] += 1
                break
        if not found:
            skill_dict = {'name':skill.name, 'roots':skill.roots(), 'points':1}
            self.bought_skills.append(skill_dict)
    def remove_skill(self, skill):
        found = False
        for x in self.get_skills():
            if skill.name == x['name']:
                found = True
                if x['points'] > 1:
                    x['points'] -= 1
                elif x['points'] == 1:
                    for y in self.required_skills():
                        if y['name'] == skill.name:
                            raise Exception
                    self.bought_skills.remove(x)
        if not found:
            raise Exception
    def skill_points(self):
        """The third time a lifepath is taken, it awards half-points, and the fourth and subsequent times, no points at all.
        """
        total = 0
        lp_list = []
        for x in self.life_paths:
            points = x.skill_points
            lp_list.append(x)
            count = lp_list.count(x)
            if count == 3:
                points = points/2
            elif count >= 4:
                points = 0 
            total += points
        for skill in self.get_skills():
            total -= skill['points']
        return total+self.spent_general
    def general_skill_points(self):
        # are general points also halved or eliminated?  I assume so...
        total = 0
        lp_list = []
        for path in self.life_paths:
            points = path.general_skill_points
            lp_list.append(path)
            count = lp_list.count(path)
            if count == 3:
                points = points/2
            elif count >= 4:
                points = 0
            total += points
        return total-self.spent_general
    def lifepath_skills(self):
        skills = []
        for path in self.life_paths:
            for skill in path.skills:
                if not skill in skills:
                    skills.append(skill)
        return skills
    def has_trait(self, check_trait):
        return check_trait in self.traits()
    def traits(self):
        required_traits = []
        tally = []
        for x in self.life_paths:
             for y in x.traits:
                 if y not in required_traits:
                     required_traits.append(y)
                     break
        return required_traits+self.bought_traits+self.starting_traits
    def lifepath_traits(self):
        traits = []
        for path in self.life_paths:
            for trait in path.traits:
                traits.append(trait)
        return traits
    def trait_points(self):
        """For each Path,
        the first time it's taken, subtract a point for the first trait in the list the character doesn't have yet.
        The second time it's taken, do the same, but if there is no such trait, reduce the awarded points by 1 (min zero).
        The third and subsequent times, the path awards no points
        """
        total = 0
        lp_list = []
        trait_list = []
        for x in self.life_paths:
            points = x.trait_points
            traits = x.traits
            lp_list.append(x)
            count = lp_list.count(x)

            if count == 1:
                for trait in traits:
                    if trait not in trait_list:
                        trait_list.append(trait)
                        points -= 1
                        break
                total += points
            elif count == 2:
                for trait in traits:
                    if trait not in trait_list:
                        trait_list.append(trait)
                        points -= 1
                        break
                if not traits and points > 0:
                    points -= 1
                total += points
        for x in self.bought_traits:
            if x in self.lifepath_traits():
                total -= 1
            else:
                total -= x.cost
        if total < 0:
            pass
        return total
    def allowed_traits(self):
        allowed_list = []
        from trait import index
        for x in index:
            if not self.has_trait(x):
                if x in self.lifepath_traits():
                    cost = 1
                else:
                    cost = x.cost
                if cost <= self.trait_points() and x.allowed(self):
                    allowed_list.append(x)
                
        return allowed_list
                
    def buy_trait(self, trait):
        if trait in self.lifepath_traits():
            cost = 1
        else:
            cost = trait.cost
        if cost > self.trait_points():
            raise NotAllowed(trait, 'Costs ' + str(cost) + ' points, character only has ' + str(self.trait_points()))
        else:
            self.bought_traits.append(trait)
            return self
    def remove_trait(self, trait):
        self.bought_traits.remove(trait)
    def paths(self):
        return self.life_paths
    def artha_fate(self):
        if self.path_count() <= 6:
            return 3
        elif self.path_count() == 7:
            return 2
        elif self.path_count() <= 9:
            return 1
        else:
            return 0
    def artha_persona(self):
        if self.path_count() <= 6:
            return 2
        elif self.path_count() <= 8:
            return 1
        else:
            return 0
    def artha_deeds(self):
        if self.path_count() <= 5:
            return 1
        else:
            return 0
    def mortal_wound(self):
        from trait import Tough
        power = Decimal(self.power)
        forte = Decimal(self.forte)
        tolerance = (power+forte)/2 + 6
        if self.has_trait(Tough()):
            tolerance = tolerance.quantize(Decimal('1.'), rounding=ROUND_UP)
        else:
            tolerance = tolerance.quantize(Decimal('1.'), rounding=ROUND_DOWN)
        return 'H'+str(tolerance)
    def superficial_wound(self):
        tolerance = self.forte/2+1
        return 'H'+str(tolerance)
    def injured_wound(self):
        tolerance = 1+self.forte/2+self.forte/2
        return 'H'+str(tolerance)
    def maimed_wound(self):
        from trait import Tough
        power = Decimal(self.power)
        forte = Decimal(self.forte)
        tolerance = (power+forte)/2 + 4
        if self.has_trait(Tough()):
            tolerance = tolerance.quantize(Decimal('1.'), rounding=ROUND_UP)
        else:
            tolerance = tolerance.quantize(Decimal('1.'), rounding=ROUND_DOWN)
        return 'H'+str(tolerance)
    def skill_totals(self):
        """The first point spent on a skill 'opens' it to one half of the average of all roots
        """
        skills = []
        for x in self.get_skills():
            dividend = len(x['roots'])
            divisor = 0
            if 'Will' in x['roots']:
                divisor += self.will
            if 'Perception' in x['roots']:
                divisor += self.perception
            if 'Agility' in x['roots']:
                divisor += self.agility
            if 'Forte' in x['roots']:
                divisor += self.forte
            if 'Power' in x['roots']:
                divisor += self.power
            if 'Speed' in x['roots']:
                divisor += self.speed
            roots = divisor/dividend
            exponent = roots/2 + x['points'] - 1
            skills.append({'name':x['name'], 'exponent':exponent})
        return skills
