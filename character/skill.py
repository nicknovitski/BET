class Skill(object):
    points = 0
    def roots(self):
        roots = []
        if isinstance(self, WillRoot):
            roots.append('Will')
        if isinstance(self, PerceptionRoot):
            roots.append('Perception')
        if isinstance(self, ForteRoot):
            roots.append('Forte')
        if isinstance(self, AgilityRoot):
            roots.append('Agility')
        if isinstance(self, PowerRoot):
            roots.append('Power')
        if isinstance(self, SpeedRoot):
            roots.append('Speed')
        return roots
    def __init__(self, name='Default Skill'):
        self.name = name
    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False
        return self.name == other.name
##    def __ne__(self, other):
##        return self.name != other.name
    def __repr__(self):
        return "Skill(name='"+self.name+"')"

class PerceptionRoot(Skill):
    pass

class WillRoot(Skill):
    pass

class AgilityRoot(Skill):
    pass

class ForteRoot(Skill):
    pass

class PowerRoot(Skill):
    pass

class SpeedRoot(Skill):
    pass

class Wise(PerceptionRoot):
    def __init__(self, subject):
        self.name = subject+'-wise'

class Accounting(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Accounting')
        
class Administration(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Administration')

class AdvancedMathematics(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Advanced Mathematics')
        
class Almanac(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Almanac')
        
class Amercement(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Amercement')
        
class AncientLanguages(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Ancient Languages')
        
class Appraisal(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Appraisal')
        
class Architect(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Architect')
        
class Armorer(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Armorer')
        
class Artillery(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Artillery')
        
class AssaultWeapons(AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Assault Weapons')
        
class Astronomy(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Astronomy')
        
class BackBreakingLabor(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Back-Breaking Labor')
        
class Bargaining(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Bargaining')
        
class Begging(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Begging')
        
class AlienBiology(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Alien Biology')
        
class HumanBiology(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Human Biology')
        
class KerrnBiology(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Kerrn Biology')
        
class NaivenBiology(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Naiven Biology')
        
class BodyService(WillRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Body Service')
        
class Bureaucracy(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Bureaucracy')
        
class Cartography(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Cartography')
        
class ChildRearing(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Child Rearing')
        
class CloseCombat(WillRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Close Combat')
        
class Command(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Command')
        
class Composition(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Composition')
        
class Conspicuous(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Conspicuous')
        
class Cooking(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Cooking')
        
class Counterfeiting(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Counterfeiting')
        
class Craft(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Craft')
        #(woodworking blacksmithing carpentry leatherworking jewelry-making)
        
class Crew(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Crew')
        
class Cryonics(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Cryonics')
        
class Cryptography(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Cryptography')
        
class Demonology(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Demonology')
        
class Disguise(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Disguise')
        
class Divination(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Divination')
        
class Doctrine(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Doctrine')
        
class HereticalDoctrine(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Heretical Doctrine')
        
class CultDoctrine(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Cult Doctrine')
        
class Driving(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Driving')
        
class Engineering(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Engineering')
        
class EstateManagement(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Estate Management')
        
class Etiquette(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Etiquette')
        
class Eugenics(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Eugenics')
        
class Excavation(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Excavation')
        
class Explosives(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Explosives')
        
class Extortion(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Extortion')
        
class Fabrication(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Fabrication')
        
class Falsehood(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Falsehood')
        
class Farming(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Farming')
        
class FieldDressing(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Field Dressing')
        
class Finance(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Finance')
        
class FireControl(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Fire Control')
        
class Folklore(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Folklore')
        
class FoodService(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Food Service')
        
class ForeignLanguages(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Foreign Languages')
        
class Forgery(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Forgery')
        
class Fortifications(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Fortifications')
        
class FusionDynamics(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Fusion Dynamics')
        
class Helm(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Helm')
        
class Heraldry(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Heraldry')
        
class History(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='History')
        
class AncientHistory(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Ancient History')
        
class MilitaryHistory(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Military History')
        
class LeagueHistory(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='League History')
        
class ForeignHistory(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Foreign History')
        
class LocalHistory(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Local History')
        
class ObscureHistory(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Obscure History')
        
class ReligiousHistory(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Religious History')
        
class KerrnHistory(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Kerrn History')
        
class VaylenHistory(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Vaylen History')
        
class Hunting(PerceptionRoot, SpeedRoot):
    def __init__(self):
        Skill.__init__(self, name='Hunting')
        
class Husbandry(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Husbandry')
        
class Hydrology(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Hydrology')
        
class Inconspicuous(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Inconspicuous')
        
class Infiltration(SpeedRoot):
    def __init__(self):
        Skill.__init__(self, name='Infiltration')
        
class Instruction(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Instruction')
        
class Interrogation(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Interrogation')
        
class Intimidation(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Intimidation')
        
class InvestigativeLogic(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Investigative Logic')
        
class IronArtifice(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Iron Artifice')
        
class Journalism(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Journalism')
        # obstacles set by attitude, regardless of subject...so attitude isn't just about vaylen
        
class JuryRigging(WillRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Jury Rigging')
        
class ChurchLaw(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Church Law')
        
class ImperialLaw(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Imperial Law')
        
class CommunistLaw(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Communist Law')
        
class LeagueLaw(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='League Law')
        
class Logistics(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Logistics')
        
class Manufacture(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Manufacture')
        
class Meditation(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Meditation')
        
class Mending(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Mending')
        
class Mummery(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Mummery')
        
class Munitions(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Munitions')
        
class MusicalInstrument(WillRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Musical Instrument')
        
class Navigation(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Navigation')
        
class Observation(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Observation')
        
class Oratory(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Oratory')
        
class Persuasion(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Persuasion')
        
class Pharmacology(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Pharmacology')
        
class Philosophy(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Philosophy')
        
class PhysicalTraining(PowerRoot, SpeedRoot):
    def __init__(self):
        Skill.__init__(self, name='Physical Training')
        
class Physics(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Physics')
        
class Pilot(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Pilot')
        
class Propaganda(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Propaganda')
        
class Psychohistory(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Psychohistory')
        
class Psychology(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Psychology')
        
class Recon(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Recon')
        
class Repair(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Repair')
        
class Research(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Research')
        
class Rhetoric(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Rhetoric')
        
class Riding(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Riding')
        
class Scavenging(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Scavenging')
        
class Science(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Science')
        
class Security(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Security')
        
class SecurityRigging(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Security Rigging')
        
class Seduction(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Seduction')
        
class Sensors(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Sensors')
        
class ShipManagement(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Ship Management')
        
class Shipwright(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Shipwright')
        
class Signals(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Signals')
        
class SleightOfHand(AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Sleight of Hand')
        
class Smuggling(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Smuggling')
        
class Soldiering(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Soldiering')
        
class SoothingPlatitudes(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Soothing Platitudes')
        
class SquadSupportWeapons(AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Squad Support Weapons')
        
class Strategy(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Strategy')
        
class StrategyGames(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Strategy Games')
        
class Streetwise(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Streetwise')
        
class Suasion(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Suasion')
        
class Surgery(PerceptionRoot, AgilityRoot):
    def __init__(self):
        Skill.__init__(self, name='Surgery')
        
class Survival(WillRoot, ForteRoot):
    def __init__(self):
        Skill.__init__(self, name='Survival')
        
class Symbology(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Symbology')
        
class Tactics(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Tactics')
        
class Torture(WillRoot, PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Torture')
        
class UglyTruth(WillRoot):
    def __init__(self):
        Skill.__init__(self, name='Ugly Truth')
        
class VaylenPhilosophy(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Vaylen Philosophy')
        
class VehicularWeapons(PerceptionRoot):
    def __init__(self):
        Skill.__init__(self, name='Vehicular Weapons')
        
class ZeroG(SpeedRoot):
    def __init__(self):
        Skill.__init__(self, name='Zero-G')
