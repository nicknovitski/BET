from character import req

class Trait(object):
    def __init__(self, name='Default Trait', cost=1, requirements =[]):
        self.name = name
        self.cost = cost
        self.requirements = requirements
    def __eq__(self, other):
        if not issubclass(other.__class__, Trait):
            return False
        return self.name == other.name
    def __ne__(self, other):
        if not issubclass(other.__class__, Trait):
            return True
        return self.name != other.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__class__.__module__+'.'+self.__class__.__name__+'()'
    def allowed(self, character):
        return True
##        if not self.requirements:
##            return True
##        else:
##            for x in self.requirements:
##                if x.allowed(character):
##                    return True
##            return False
        
class CallOnTrait(Trait):
    pass

class DieTrait(Trait):
    pass

class CharacterTrait(Trait):
    pass

class AadauClan(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Aadau Clan', 5)

class Abandoned(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Abandoned')

class Abused(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Abused')

class AccustomedToTheDark(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Accustomed to the Dark', 2)

class Addicted(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Addicted', 2)

class Addled(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Addled')
        
class AdumbrateVeil(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Adumbrate Veil', 2)

class Aeumiflesh(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Aeumiflesh', 3)

class AffinityFor(DieTrait):
    def __init__(self, affinity='skill'):
        Trait.__init__(self, 'Affinity for '+affinity, 4)

class AffinityForBusiness(AffinityFor):
    def __init__(self):
        AffinityFor.__init__(self, 'Business')

class AffinityForLocks(AffinityFor):
    def __init__(self):
        AffinityFor.__init__(self, 'Locks')

class AffinityForTrade(AffinityFor):
    def __init__(self):
        AffinityFor.__init__(self, 'Trade')

class AffinityForTechnology(AffinityFor):
    def __init__(self):
        AffinityFor.__init__(self, 'Technology')
        
class Aggressive(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Aggressive')
                
class Agitated(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Agitated')
        
class Agoraphobic(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Agoraphobic', 2)
        
class Alert(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Alert', 2)

class Aloof(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Aloof')
        
class Ambitious(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Ambitious')
        
class Amedhyen(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Amedhyen', 1)
        
class Amorous(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Amorous')
        
class Anarchist(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Anarchist')

class AnimalLife(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Animal Life', 1)

class AnnelidaClan(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Annelida Clan', 3)

class AnvilLord(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Anvil Lord', 5)
    def allowed(self,character):
        if not character.has_taken_any(['Magnate', 'Born to Rule', 'Anvil Lord']):
            return False
        return True

class AnvilTrained(DieTrait):
    def __init__(self):
        Trait.__init__(self,'Anvil Trained', 3)

class AppreciativeOfGoodCraft(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Appreciative of Good Craft')

class Arbiter(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Arbiter', 6)
    def allowed(self, character):
        if not character.has_taken_any(['Archcotare', 'Cult Leader']):
            return False
        return True

class Arrogant(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Arrogant')

class Artisan(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Artisan', 2)
        
class AuraOfInnocence(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Aura of Innocence', 4)

class Automator(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Automator', 3)

class BadEgg(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Bad Egg', 3)

class Bastard(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Bastard', 3)
    def allowed(self, character):
        if not character.has_taken('Born to Rule'):
                return False
        return True

class Bathetic(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Bathetic')

class BawdyFool(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Bearded')

class Bearded(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Bearded')

class Beaten(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Beaten', 2)

class Beautiful(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Beautiful')

class Berserker(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Berserker', 5)

class ABitMad(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'A Bit Mad')

class Bitter(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Bitter')

class Bizarre(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Bizarre')

class BlackFingernails(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Black Fingernails')

class Blacklisted(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Blacklisted', 2)

class Bleak(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Bleak', 1)

class Bookworm(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Bookworm', 2)

class BoomingVoice(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Booming Voice', 2)

class Boor(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Boor', 2)

class Bored(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Bored')

class BornOnTheWheel(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Born on the Wheel', 3)
    def allowed(self, character):
        if not character.has_taken('Born on the Wheel'):
            return False
        return True

class Brave(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Brave', 2)

class Breeder(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Breeder', 1)

class BrightMark(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Bright Mark', 5)
        

class Broken(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Broken', 2)

class BruisedEyes(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Bruised Eyes')

class Brutal(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Brutal')

class Brute(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Brute', 7)

class Bulldog(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Bulldog')

class Bungler(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Bungler', 1)

class Burned(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Burned', 5)

class Calculating(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Calculating')

class CalmDemeanor(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Calm Demeanor', 2)

class Cannibal(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Cannibal')

class CapitalistAtHeart(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Capitalist at Heart')

class Captured(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Captured', 2)

class CasuallyViolent(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Casually Violent', 3)

class Casuist(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Casuist', 4)

class Chameleon(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Chameleon', 2)

class ChargingBlindly(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Charging Blindly', 3)

class Charismatic(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Charismatic', 2)

class Charming(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Charming', 2)

class Child(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Child', 7)


class Chimerical(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Chimerical')

class ChronicDepression(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Chronic Depression')

class CitizenOfTheCommune(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Citizen of the Commune', 3)
    def allowed(self, character):
        if not character.has_taken('Born Citizen'):
            return False
        return True

class CityOfficial(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'City Official', 2)
        
class ClanLeader(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Clan Leader', 12)

class Claustrophobic(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Claustrophobic', 2)

class CleanCut(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Clean Cut')

class Clever(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Clever')

class CleverBastard(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Clever Bastard', 3)

class Clinical(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Clinical')

class Cocky(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Cocky')
        
class Codebreaker(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Codebreaker', 3)

class CogInTheMachine(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Cog in the Machine', 3)

class Cold(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Cold')

class ColdBlooded(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Cold Blooded', 2)

class Colorful(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Colorful')

class CommandingAura(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Commanding Aura', 4)

class Conciliator(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Conciliator', 3)

class ConstitutionalActivist(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Constitutional Activist', 2)
        
class Contender(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Contender', 2)
    def allowed(self, character):
        if not character.has_trait(MarkOfPrivilege()):
            return False
        return True
    
class Contortionist(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Contortionist', 2)

class CoolHeaded(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Cool-Headed', 3)

class Corrupt(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Corrupt')

class CorvusAndCrucis(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Corvus and Crucis', 4)
        

class Cosmopolitan(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Cosmopolitan')

class CotarFomas(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Cotar Fomas',3)
    def allowed(self, character):
        if not character.has_taken('Cotar Fomas'):
            return False
        return True

class Coy(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Coy')

class CrookedFingers(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Crooked Fingers')

class Cruel(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Cruel')

class CrushingBoredom(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Crushing Boredom')

class Cryptic(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Cryptic', 2)

class CudChewer(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Cud Chewer')

class Cultist(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Cultist', 3)

class Cunning(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Cunning')

class Curious(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Curious')

class Curt(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Curt')

class Cynical(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Cynical')

class Daredevil(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Daredevil')

class Dark(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Dark')

class Dashing(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Dashing')

class Dedicated(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Dedicated')

class DeepThinker(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Deep Thinker')

class Defeated(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Defeated', 3)
        
class Defensive(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Defensive')

class Deferential(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Deferential')

class Defiant(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Defiant')

class Deformed(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Deformed', 1)

class Democrat(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Democrat')

class Desperate(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Desperate')

class Despondent(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Despondent')

class DestinedForSlavery(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Destined for Slavery', 3)

class Determined(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Determined', 4)

class DevotedToFire(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Devoted to Fire', 3)
    def allowed(self, character):
        if not character.has_taken('Devoted to Fire'):
            return False
        return True
    
class Diplomatic(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Diplomatic')

class Dirty(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Dirty')

class Disciplined(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Disciplined', 4)

class Dismissive(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Dismissive')

class Dispassionate(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Dispassionate')

class DistortionMonkey(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Distortion Monkey', 4)

class DistortionSickness(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Distortion Sickness', 2)

class Distrustful(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Distrustful')

class Disturbing(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Disturbing')

class DomineeringPresence(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Domineering Presence', 5)

class Downtrodden(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Downtrodden')

class Dregutai(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Dregutai',4)
    def allowed(self, character):
        if not character.has_taken('Dregus'):
            return False
        return True    

class Drunk(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Drunk', 2)

class EarForVoices(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Ear for Voices', 3)

class Earnest(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Earnest')

class Educated(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Educated', 3)
        

class EerilyConfident(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Eerily Confident', 3)

class Effeminate(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Effeminate')

class EideticMemory(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Eidetic Memory', 4)

class Elitist(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Elitist')

class Empathic(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Empathic')

class EmperorsArmorBearer(DieTrait):
    def __init__(self):
        Trait.__init__(self, "Emperor's Armor Bearer", 5)
        
        
class EmperorsSteward(DieTrait):
    def __init__(self):
        Trait.__init__(self, "Emperor's Steward", 6)
    def allowed(self, character):
        if not character.has_taken('Lord Steward'):
            return False
        return True          

class Ennui(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Ennui')

class Enraged(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Enraged')

class Erudite(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Erudite')
        
class Exhausted(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Die', 2)

class EyeForDetail(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Eye for Detail', 2)

class EyeForPlace(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Eye for Place', 3)

class Family(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Family', 4)
        
       
class Fatalistic(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Fatalistic')

class FaziaToAll(DieTrait):
    def __init__(self):
        Trait.__init__(self,'Fazia to All', 5)
        

class Fearless(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Fearless', 4)

class Feckless(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Feckless')

class Feral(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Feral')

class Fetishist(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Fetishist', 3)

class Fiery(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Fiery')

class FitsOfGenerosity(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Fits of Generosity')

class Flamboyant(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Flamboyant')

class Flexible(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Flexible')

class Flyboy(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Flyboy')

class FollowTheMoney(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'FollowTheMoney', 2)

class Fop(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Fop')

class Forged(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Human Only', 10)
        

class ForkedTongue(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Forked Tongue', 3)

class Formalist(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Formalist', 3)

class Fragger(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Fragger', 3)

class Freak(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Freak', 2)

class FriendlyFace(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Friendly Face', 4)

class FrighteninglyClinical(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Frighteningly Clinical')

class Frustrated(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Frustrated')

class FUGAZI(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'FUGAZI')

class FunnyAccent(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Funny Accent')

class FuurBlood(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Fuur Blood', 4)
        

class Gadgeteer(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Gadgeteer', 5)

class GalvanizingPresence(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Galvanizing Presence', 3)

class Garbo(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Garbo', 8)
        

class GarlicBreath(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Garlic Breath')

class Genius(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Genius', 3)

class Gentle(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Gentle')

class GentleGiant(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Gentle Giant')

class GiftOfAhmilahk(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Gift of Ahmilahk', 3)
    def allowed(self, character):
        if not character.has_trait(BrightMark()):
            return False
        return True

class GladHander(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Glad Hander')

class GoodForNothing(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Good for Nothing')

class GoodListener(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Good Listener')

class GooglyEyes(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Googly Eyes')

class Graceful(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Graceful')

class Gracious(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Gracious')

class GreaseMonkey(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Grease Monkey', 2)

class Grim(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Grim')

class Groundhog(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Groundhog', 3)

class Gruff(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Gruff')

class HammerFliesAnvilDies(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Hammer Flies, Anvil Dies', 3)
        
class HammerLord(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Hammer Lord', 5)
        
class Handsome(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Handsome')

class HardHearted(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Hard Hearted', 5)

class HardNosed(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Hard Nosed', 2)

class Harried(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Harried')

class Hater(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Hater')

class HatPasser(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Hat-Passer')

class Hazed(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Hazed')

class HealthyRespectForPower(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Healthy Respect for Power')

class Heretic(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Heretic', 4)

class HiddenVenom(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Hidden Venom')

class Homesick(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Homesick')

class HommeDur(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Homme Dur', 4)

class HopelesslyCorrupt(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Hopelessly Corrupt')

class Hotshot(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Hotshot', 2)

class Humanist(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Humanist')

class Humble(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Humble')

class Hungry(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Hungry')

class HungryForKnowledge(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Hungry for Knowledge')

class Hurt(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Hurt', 2)

class IKnowThisShipLikeMyOwnHands(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'I Know This Ship Like My Own Hands', 2)

class ISolzjah(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'I, Solzjah', 3)
        

class Idealist(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Idealist', 2)

class Ideologue(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Ideologue', 3)

class IllegalCrucis(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Illegal Crucis', 3)

class Imperious(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Imperious')

class ImperiousDemeanor(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Imperious Demeanor', 3)

class Independent(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Independent')

class Indulgent(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Indulgent')

class Innocent(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Innocent', 1)

class Insane(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Insane')

class IronStomach(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Iron Stomach')
        
class IronTrained(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Iron Trained', 5)
    def allowed(self, character):
        if not character.has_trait(CorvusAndCrucis()):
            return False
        return True

class Irradiated(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Irradiated')

class Jaded(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Jaded')

class Jumpy(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Jumpy', 1)

class JustFollowingOrders(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Just Following Orders', 5)
        
class KeeperOfTheFire(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Keeper of the Fire', 2)
    def allowed(self, character):
        if not character.has_taken('Cotar'):
            return False
        return True              

class Kilgore(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Kilgore')
        
class KravMagahTrained(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Krav Magah Trained', 3)
        
class Laconic(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Laconic')

class LameDuck(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Lame Duck', 2)

class Late(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Late', 2)

class LavishTaste(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Lavish Taste', 2)

class LawObsessed(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Law-Obsessed')

class Leech(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Leech')

class Liberal(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Liberal')

class LifeUnderADifferentCode(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Life under a Different Code', 3)

class LiftingHeavyThings(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'LiftingHeavyThings', 2)

class LightSensitive(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Light Sensitive', 2)

class LightSleeper(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Light Sleeper', 2)
        
class Linguist(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Linguist', 2)

class Loathed(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Loathed', 2)

class Logorrhea(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Logorrhea')

class Lonely(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Lonely')

class LouisWu(CallOnTrait, DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Louis Wu', 3)

class Loyal(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Loyal', 3)

class LoyalToTheFamily(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Loyal to the Family', 3)

class Lucky(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Lucky', 6)

class LuckyToBeInAHumanBody(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Lucky to Be in a Human Body')
        

class Lunatic(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Lunatic', 1)

class Macbeth(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Macbeth', 3)

class Maelcum(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Maelcum')
        
class MakaraBody(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Makara Body', 10)
        

class ManOfFewWords(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Man of Few Words')

class Mangled(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Mangled', 4)

class Manipulative(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Manipulative')
        
class MarkOfPrivilege(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Mark of Privilege', 3)
    def allowed(self, character):
        if not character.has_taken('Born to Rule'):
            return False
        return True
    
class Martyr(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Martyr', 3)

class Matronly(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Matronly')

class Mean(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Mean')

class Mercenary(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Mercenary')

class MerchantFleetCaptain(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Merchant Fleet Captain', 5)
        
class MeshhenClan(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Meshhen Clan', 6)
        

class Meticulous(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Meticulous', 2)
        
class Metropolitan(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Metropolitan', 6)
    def allowed(self, character):
        if not character.has_taken('Cotar Antistes'):
            return False
        return True        

class Militant(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Militant')

class Misanthropic(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Misanthropic')

class Morose(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Morose')

class Mouthbreather(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Mouthbreather')

class Mover(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Mover', 2)

class Mule(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Mule', 5)

class Murderous(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Murderous')

class Muscle(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Muscle')

class Mustache(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Mustache')

class MyShipMyRules(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'My Ship, My Rules', 3)

class Naive(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Naive')

class NeedForSpeed(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Need for Speed')

class Nimble(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Nimble', 2)

class NoNonsense(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'No Nonsense', 3)

class NoseForTrouble(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Nose for Trouble', 2)

class Numb(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Numb', 5)

class NumberOne(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Number One!')

class Obedient(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Obedient', 2)

class Odd(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Odd')

class OddlyLikeable(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Oddly Likeable')

class Officious(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Officious')
        
class Officer(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Officer', 5)
    def allowed(self, character):
        if not character.has_taken('Hammer Captain'):
            return False
        return True            
        
class Offisah(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Offisah', 5)
        
        
class OmshiipOfficer(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Omshiip Officer', 3)
        
        
class OmshiipStaff(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Omshiip Staff', 3)
        
        
class OmshiipsMaster(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, "Omshiip's Master", 2)
        

class OpenMinded(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Open-Minded')

class Optimist(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Optimist')

class OrderBeforeChaos(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Order Before Chaos', 3)

class OrderOfTheMysticFire(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Order of the Mystic Fire', 4)

class OrderOfTheSeekingFire(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Order of the Seeking Fire', 5)

class Organized(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Organized')

class Orphan(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Orphan', 1)

class Outcast(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Outcast', 2)

class Outlaw(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Outlaw', 4)

class OwnerAboard(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Owner-Aboard', 2)
        

class Paranoid(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Paranoid')

class PathologicalLiar(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Pathological Liar')

class Patient(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Patient')

class Peacemaker(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Peacemaker', 2)

class Pecunious(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Pecunious', 2)

class Pedantic(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Pedantic')

class PennyWise(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Penny-wise', 2)

class Permissive(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Permissive')

class Pharisaical(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Pharisaical')

class Philosophical(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Philosophical')

class PickedMan(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Picked Man', 3)

class PlainFace(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Plain Face', 2)

class Polite(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Polite', 2)

class Practical(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Practical')

class Pragmatic(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Pragmatic')
        
class Primarch(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Primarch', 9)

class Privateer(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Privateer', 3)

class PrivilegedPosition(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Privileged Position', 3)

class Professional(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Professional')

class ProfessionalPride(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Professional Pride')

class Prophet(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Prophet', 5)

class Protective(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Protective')

class Proud(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Proud')

class ProudCitizen(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Proud Citizen')

class PublicFace(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Public Face', 3)

class PublicFigure(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Public Figure', 4)
        
class PublicServant(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Public Servant', 5)
    def allowed(self, character):
        from character.human import CommuneLifepath, MerchantLeagueLifepath
        if not character.has_taken_any_from(CommuneLifepath) and not character.has_taken_any_from(MerchantLeagueLifepath):
            return False
        return True
    
class Pudgy(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Pudgy')
        
class ThePsychologistsCode(DieTrait):
    def __init__(self):
        Trait.__init__(self, "The Psychologist's Code", 2)
    def allowed(self, character):
        if not character.has_trait(BrightMark()):
            return False
        return True

class QuickWitted(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Quick-Witted', 4)

class Quiet(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Quiet', 2)

class RabbleRouser(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Rabble-Rouser', 2)

class Radiohead(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Radiohead', 3)

class RapierWit(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Rapier Wit', 4)

class RawNerved(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Raw-Nerved')

class Realistic(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Realistic')

class Rebel(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Rebel')

class REMF(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'REMF', 2)

class Remote(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Remote')

class Resigned(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Resigned')

class ResignedToDeath(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Resigned to Death', 2)

class Resourceful(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Resourceful', 5)

class Righteous(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Righteous')

class Romantic(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Romantic')

class Royalist(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Royalist')

class RuleOfThree(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Rule of Three', 3)

class Saccharine(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Saccharine')

class Sanguine(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Sanguine')

class Saturnine(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Saturnine')

class Savvy(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Savvy', 2)

class ScarredHands(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Scarred Hands')

class Scheming(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Scheming', 3)

class ScumOfTheGalaxy(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Scum of the Galaxy', 3)

class ScutWork(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Scut Work', 2)

class SeeminglyConcerned(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Seemingly Concerned', 3)

class SeenItAll(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Seen it All', 2)

class SeenTooMuchTooYoung(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Seen Too Much Too Young', 2)        

class SelfMadeKerrn(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Self-Made Kerrn', 2)
        

class SelfSatisfied(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Self-Satisfied')
        
class Senator(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Senator', 6)
    def allowed(self, character):
        if not character.has_taken('Legislative Official'):
            return False
        return True             

class Sentimental(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Sentimental')

class SeriousAsAHeartAttack(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Serious as a Heart Attack')

class SharkToothedSmile(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Shark-Toothed Smile', 2)

class SharpDresser(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Sharp Dresser')

class SharpEyed(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Sharp-Eyed', 3)

class Showboat(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Showboat', 2)

class Shrewd(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Shrewd', 4)

class ShutUp(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Shut Up')

class Sickly(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Sickly', 2)

class SigGeek(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Sig Geek', 2)

class SkeletonsInTheCloset(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Skeletons in the Closet', 4)

class Skeptical(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Skeptical')
        
class Slaggah(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Slaggah', 3)

class SleepDisorder(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Sleep Disorder')

class SlightBuild(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Slight Build')

class SlightlyWarped(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Slightly Warped')

class Slow(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Slow', 2)

class SmarterThanYou(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Smarter Than You')

class SmartestGuyInTheRoom(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Smartest Guy in the Room')

class Solipsistic(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Solipsistic')

class Solitary(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Solitary')

class SpeakerOfTheSecretLanguage(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Speaker of the Secret Language')

class Spock(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Spock')

class SteadyHands(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Steady Hands', 2)

class SternDemeanor(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Stern Demeanor', 2)

class Stinky(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Stinky')

class Stoic(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Stoic', 3)

class TheStory(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'The Story', 3)

class Strange(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Strange')

class StrangeAirs(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Strange Airs')

class Strangelove(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Strangelove')

class StrictConstructionist(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Strict Constructionist')

class Stupid(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Stupid', 2)

class Suicidal(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Suicidal')

class Sullen(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Sullen')

class Superstitious(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Superstitious')


class Surreptitious(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Surreptitious')


class Suspicious(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Suspicious')

class Swagger(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Swagger')

class Swindler(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Swindler')

class SwornToTheFire(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Sworn to the Fire', 1)

class TallDarkAndMurderous(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Tall-Dark-and-Murderous', 1)

class Tenacious(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Tenacious', 6)

class ThinkBig(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Think Big')

class ThirstyForAnswers(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Thirsty for Answers')

class ThisIsAStoreNotALibrary(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'This Is a Store Not a Library!')

class ThousandYardStare(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Thousand-Yard Stare', 4)

class Thug(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Thug')

class Tinkerer(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Tinkerer', 2)

class Tolerant(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Tolerant')

class ToolOfTheState(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Tool of the State', 2)

class Tough(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Tough', 3)


class ToughAsNails(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Tough as Nails', 5)

class Traditionalist(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Traditionalist')

class Tragic(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Tragic')

class Troubled(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Troubled')

class Tweaker(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Tweaker')

class Twitchy(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Twitchy')

class Unassuming(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Unassuming')

class UnderPressure(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Under Pressure', 3)

class Undeterred(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Undeterred', 3)

class Uneasy(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Uneasy')

class Unflinching(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Unflinching', 5)

class Unglued(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Unglued')

class Unwelcome(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Unwelcome', 2)

class Useful(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Useful', 2)
        
class Usurper(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Usurper', 5)

class VacantStare(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Vacant Stare')

class Vainglorious(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Vainglorious')

class Venal(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Venal')
        
class VibhuutenClan(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Vibhuuten Clan', 7)
        
class Vig(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Vig', 4)
    def allowed(self, character):
        from character.human import OutcastLifepath
        if not character.has_taken_any_from(OutcastLifepath):
            return False
        return True        

class Vigilant(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Vigilant')

class Vindictive(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Vindictive')

class Wanderlust(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Wanderlust')
        
class WarriorsCode(DieTrait):
    def __init__(self):
        Trait.__init__(self, "Warrior's Code", 3)
    def allowed(self, character):
        if character.has_trait(BrightMark()):
            return True
        if character.has_trait(Mule()) and character.has_trait(Branded()):
            return True
        return False
        

class Branded(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Branded')

class Watchful(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Watchful', 2)

class WeRuleTheseStreets(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'We Rule These Streets', 2)

class WeightOfTheGalaxy(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Weight of the Galaxy', 7)

class Weird(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Weird')

class WellHeeled(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Well-Heeled')

class WellKnown(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Well-Known', 4)

class WellRead(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Well-Read', 2)

class WellSpoken(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Well-Spoken', 2)

class WellTravelled(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Well-Travelled', 2)

class Whipped(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Whipped', 2)

class WifeBeater(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Wife-Beater')
        
class Wigged(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Wigged', 2)
    def allowed(self, character):
        if not character.has_trait(CorvusAndCrucis()):
            return False
        return True     

class Wise(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Wise')

class WiseAphorisms(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Wise Aphorisms', 4)

class WitheringStare(CallOnTrait):
    def __init__(self):
        Trait.__init__(self, 'Withering Stare', 2)

class Wizened(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Wizened')
        
class WordIsLaw(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Word is Law', 9)
    def allowed(self, character):
        if not character.has_taken('Cotar Antistes'):
            return False
        return True        

class WorkingClass(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Working Class')

class Worried(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Worried')

class WreckedSelfEsteem(CharacterTrait):
    def __init__(self):
        Trait.__init__(self, 'Wrecked Self-Esteem')

class WronglyAccused(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Wrongly Accused', 3)

class YesBoss(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Yes, Boss', 2)
        
class YourEminence(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Your Eminence', 5)
    def allowed(self, character):
        if not character.has_taken('Born to Rule'):
                return False
        return True    
        
class YourGrace(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Your Grace', 7)
    def allowed(self, character):
        if not character.has_taken('Born to Rule'):
                return False
        return True    
        
class YourLordship(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Your Lordship', 3)
    def allowed(self, character):
        if not character.has_taken('Born to Rule'):
                return False
        return True    
        
class YourMajesty(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Your Majesty', 9)
    def allowed(self, character):
        if not character.has_taken('Born to Rule'):
                return False
        return True

class Zealot(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Zealot', 3)

# list of purchaseable traits
index= [AadauClan(), Abandoned(), Abused(), AccustomedToTheDark(), Addicted(),
 Addled(), AdumbrateVeil(), Aeumiflesh(), AffinityFor(), AffinityForBusiness(),
 AffinityForLocks(), AffinityForTrade(), AffinityForTechnology(), Aggressive(),
 Agitated(), Agoraphobic(), Alert(), Aloof(), Ambitious(), Amedhyen(), Amorous(),
 Anarchist(), AnimalLife(), AnnelidaClan(), AnvilLord(), AnvilTrained(),
 AppreciativeOfGoodCraft(), Arbiter(), Arrogant(), Artisan(), AuraOfInnocence(),
 Automator(), BadEgg(), Bastard(), Bathetic(), BawdyFool(), Bearded(),
 Beaten(), Beautiful(), Berserker(), ABitMad(), Bitter(), Bizarre(), BlackFingernails(),
 Blacklisted(), Bleak(), Bookworm(), BoomingVoice(), Boor(), Bored(), BornOnTheWheel(),
 Brave(), Breeder(), BrightMark(), Broken(), BruisedEyes(), Brutal(), Brute(),
 Bulldog(), Bungler(), Burned(), Calculating(), CalmDemeanor(), Cannibal(),
 CapitalistAtHeart(), Captured(), CasuallyViolent(), Casuist(), Chameleon(),
 ChargingBlindly(), Charismatic(), Charming(), Child(), Chimerical(), ChronicDepression(),
 CitizenOfTheCommune(), CityOfficial(), ClanLeader(), Claustrophobic(), CleanCut(),
 Clever(), CleverBastard(), Clinical(), Cocky(), Codebreaker(), CogInTheMachine(),
 Cold(), ColdBlooded(), Colorful(), CommandingAura(), Conciliator(), ConstitutionalActivist(),
 Contender(), Contortionist(), CoolHeaded(), Corrupt(), CorvusAndCrucis(), Cosmopolitan(),
 CotarFomas(), Coy(), CrookedFingers(), Cruel(), CrushingBoredom(), Cryptic(),
 CudChewer(), Cultist(), Cunning(), Curious(), Curt(), Cynical(), Daredevil(),
 Dark(), Dashing(), Dedicated(), DeepThinker(), Defeated(), Defensive(), Deferential(),
 Defiant(), Deformed(), Democrat(), Desperate(), Despondent(), DestinedForSlavery(),
 Determined(), DevotedToFire(), Diplomatic(), Dirty(), Disciplined(), Dismissive(),
 Dispassionate(), DistortionMonkey(), DistortionSickness(), Distrustful(), Disturbing(),
 DomineeringPresence(), Downtrodden(), Dregutai(), Drunk(), EarForVoices(), Earnest(),
 Educated(), EerilyConfident(), Effeminate(), EideticMemory(), Elitist(), Empathic(),
 EmperorsArmorBearer(),  EmperorsSteward(), Ennui(), Enraged(), Erudite(), Exhausted(),
 EyeForDetail(), EyeForPlace(), Family(), Fatalistic(), FaziaToAll(), Fearless(),
 Feckless(), Feral(), Fetishist(), Fiery(), FitsOfGenerosity(), Flamboyant(),
 Flexible(), Flyboy(), FollowTheMoney(), Fop(), Forged(), ForkedTongue(), Formalist(),
 Fragger(), Freak(), FriendlyFace(), FrighteninglyClinical(), Frustrated(), FUGAZI(),
 FunnyAccent(), FuurBlood(), Gadgeteer(), GalvanizingPresence(), Garbo(), GarlicBreath(),
 Genius(), Gentle(), GentleGiant(), GiftOfAhmilahk(), GladHander(), GoodForNothing(),
 GoodListener(), GooglyEyes(), Graceful(), Gracious(), GreaseMonkey(), Grim(),
 Groundhog(), Gruff(), HammerFliesAnvilDies(), HammerLord(), Handsome(),
 HardHearted(), HardNosed(), Harried(), Hater(), HatPasser(), Hazed(), HealthyRespectForPower(),
 Heretic(), HiddenVenom(), Homesick(), HommeDur(), HopelesslyCorrupt(), Hotshot(),
 Humanist(), Humble(), Hungry(), HungryForKnowledge(), Hurt(), IKnowThisShipLikeMyOwnHands(),
 ISolzjah(), Idealist(), Ideologue(), IllegalCrucis(), Imperious(), ImperiousDemeanor(),
 Independent(), Indulgent(), Innocent(), Insane(), IronStomach(), IronTrained(),
 Irradiated(), Jaded(), Jumpy(), JustFollowingOrders(), KeeperOfTheFire(), Kilgore(),
 KravMagahTrained(), Laconic(), LameDuck(), Late(), LavishTaste(), LawObsessed(),
 Leech(), Liberal(), LifeUnderADifferentCode(), LiftingHeavyThings(), LightSensitive(),
 LightSleeper(), Linguist(), Loathed(), Logorrhea(), Lonely(), LouisWu(), Loyal(),
 LoyalToTheFamily(), Lucky(), LuckyToBeInAHumanBody(), Lunatic(), Macbeth(), Maelcum(),
 MakaraBody(), ManOfFewWords(), Mangled(), Manipulative(), MarkOfPrivilege(), Martyr(),
 Matronly(), Mean(), Mercenary(), MerchantFleetCaptain(), MeshhenClan(), Meticulous(),
 Metropolitan(), Militant(), Misanthropic(), Morose(), Mouthbreather(), Mover(),
 Mule(), Murderous(), Muscle(), Mustache(), MyShipMyRules(), Naive(), NeedForSpeed(),
 Nimble(), NoNonsense(), NoseForTrouble(), Numb(), NumberOne(), Obedient(), Odd(),
 OddlyLikeable(), Officious(), Officer(), Offisah(), OmshiipOfficer(), OmshiipStaff(),
 OmshiipsMaster(), OpenMinded(), Optimist(), OrderBeforeChaos(), OrderOfTheMysticFire(),
 OrderOfTheSeekingFire(), Organized(), Orphan(), Outcast(), Outlaw(), OwnerAboard(),
 Paranoid(), PathologicalLiar(), Patient(), Peacemaker(), Pecunious(), Pedantic(),
 PennyWise(), Permissive(), Pharisaical(), Philosophical(), PickedMan(), PlainFace(),
 Polite(), Practical(), Pragmatic(), Primarch(), Privateer(), PrivilegedPosition(),
 Professional(), ProfessionalPride(), Prophet(), Protective(), Proud(), ProudCitizen(),
 PublicFace(), PublicFigure(), PublicServant(), Pudgy(), ThePsychologistsCode(),
 QuickWitted(), Quiet(), RabbleRouser(), Radiohead(), RapierWit(), RawNerved(),
 Realistic(), Rebel(), REMF(), Remote(), Resigned(), ResignedToDeath(), Resourceful(),
 Righteous(), Romantic(), Royalist(), RuleOfThree(), Saccharine(), Sanguine(),
 Saturnine(), Savvy(), ScarredHands(), Scheming(), ScumOfTheGalaxy(), ScutWork(),
 SeeminglyConcerned(), SeenItAll(), SeenTooMuchTooYoung(), SelfMadeKerrn(),
 SelfSatisfied(), Senator(), Sentimental(), SeriousAsAHeartAttack(), SharkToothedSmile(),
 SharpDresser(), SharpEyed(), Showboat(), Shrewd(), ShutUp(), Sickly(), SigGeek(),
 SkeletonsInTheCloset(), Skeptical(), Slaggah(), SleepDisorder(), SlightBuild(),
 SlightlyWarped(), Slow(), SmarterThanYou(), SmartestGuyInTheRoom(), Solipsistic(),
 Solitary(), SpeakerOfTheSecretLanguage(), Spock(), SteadyHands(), SternDemeanor(),
 Stinky(), Stoic(), TheStory(), Strange(), StrangeAirs(), Strangelove(), StrictConstructionist(),
 Stupid(), Suicidal(), Sullen(), Superstitious(), Surreptitious(), Suspicious(),
 Swagger(), Swindler(), SwornToTheFire(), TallDarkAndMurderous(), Tenacious(),
 ThinkBig(), ThirstyForAnswers(), ThisIsAStoreNotALibrary(), ThousandYardStare(),
 Thug(), Tinkerer(), Tolerant(), ToolOfTheState(), Tough(), ToughAsNails(),
 Traditionalist(), Tragic(), Troubled(), Tweaker(), Twitchy(), Unassuming(),
 UnderPressure(), Undeterred(), Uneasy(), Unflinching(), Unglued(), Unwelcome(),
 Useful(), Usurper(), VacantStare(), Vainglorious(), Venal(), VibhuutenClan(),
 Vig(), Vigilant(), Vindictive(), Wanderlust(), WarriorsCode(), Branded(),
 Watchful(), WeRuleTheseStreets(), WeightOfTheGalaxy(), Weird(), WellHeeled(),
 WellKnown(), WellRead(), WellSpoken(), WellTravelled(), Whipped(), WifeBeater(),
 Wigged(), Wise(), WiseAphorisms(), WitheringStare(), Wizened(), WordIsLaw(),
 WorkingClass(), Worried(), WreckedSelfEsteem(), WronglyAccused(), YesBoss(),
 YourEminence(), YourGrace(), YourLordship(), YourMajesty(), Zealot()]

# race traits

class Human(DieTrait):
    def __init__(self):
        Trait.__init__(self, 'Human', 0)
