
from character.lifepath import Lifepath
from character.req import Requirement
from character import trait
from character import skill
from character import char

class Human(char.Character):
    def allowed_paths(self):
        path_list = [BornNobility(), NobleCoeptir(), Bastard(), Companion(),
             NobleArmiger(), NobleLPAnvil(), NobleLPHammer(), Lady(),
             CourtLord(), HammerLord(), AnvilLord(), VoidLord(),
             ForgedLord(), CourtClerk(), CourtCourier(), ManAtArms(),
             CourtCoeptir(), Herald(), Bureaucrat(), CourtArmiger(),
             Stentor(), CourtLPAnvil(), Mandarin(), Courtier(),
             Hostage(), Duenna(), Artificer(), Ravilar(), Coroner(),
             Constable(), Justiciar(), Treasurer(), Chamberlain(),
             LordSteward(),HammerYeoman(), Shipfitter(), SensorsTech(),
             HammerSignalsTech(), TurretCrew(), FireControlTech(),
             HammerCook(), HammerCoeptir(), Surgeon(), DisciplineOfficer(),
             HammerEngineer(), Physicist(), HammerMaster(),
             HammerFirstOfficer(), HammerLPHammer(), HammerNavigator(),
             HammerCaptain(), Runner(), Soldier(), Medic(), Scout(),
             AnvilSignalsTech(), Machinist(), Sergeant(), AnvilElite(),
             Stormtrooper(), AnvilPilot(),Armorer(), AnvilEngineer(),
             Lieutenant(), Propagandist(), XO(), AnvilCaptain(),
             BornTheocracy(), TheocracyStudent(), Notary(), Fireward(),
             DevotedToFire(),Mystes(), Archivist(), Interpreter(),
             Custodian(), BringerOfFire(), Sodalis(), SodalisTechnician(),
             SodalisPilot(), SodalisBrother(), SodalisCaptain(),
             Cotar(), Dregus(), CotarFomas(), Archcotare(), AdjutantInquisitor(),
             Inquisitor(), HighInquisitor(), CotarAntistes(), CotarArderes(),
             BornLeague(), LeagueStudent(), LeagueClerk(), Scrivener(),
             Accountant(), Security(), SecurityOfficer(), Agent(),Commentariat(),
             Physician(), Merchant(), Advocate(), LeagueOfficial(), Banker(),
             Magnate(), ChiefExecutive(), BornCommune(), CommuneStudent(),
             CommuneClerk(), VolunteerSoldier(), ProfessionalOfficer(),
             Philosopher(), Instructor(), LawEnforcement(), Media(),
             Lawyer(), Judge(), LocalOfficial(), MunicipalOfficial(),
             LegislativeOfficial(), Financier(), Governor(), AppointedOfficial(),
             Diplomat(), Politico(), CabinetMember(), ExecutiveOfficial(),
             Apprentice(), Novitiate(), FoundationStudent(), CircleOf10K(),
             Psychologist(), Speaker(), FirstSpeaker(), Eremite(),
             BornSpacefarer(), SpacefarerYeoman(), ShipRigger(),SpacefarerCook(),
             SenseRigger(), SigRigger(),GunRigger(), Pilot(), CargoMaster(),
             Doctor(), SpacefarerNavigator(), ShipsEngineer(), Scientist(),
             SpacefarerFirstOfficer(), ShipsCaptain(), OwnerAboard(),
             BornFreeman(), Kid(), FreemanStudent(), LazyStayabout(), Peddler(),
             FreemanCourier(), Laborer(), Pilgrim(), Functionary(),
             ServiceWorker(), Parent(), Driver(), Hosteler(), Shopkeeper(),
             Fabricator(), ApprenticeCraftsman(), Craftsman(), Trader(),
             Engineer(), Manufacturer(), Artisan(), BornSlave(), SlaveLabor(),
             SentencedCriminal(), MigrantLabor(), TenantLabor(), Prostitute(),
             SlaveJockey(), Clown(), Footman(), Servant(), CaptiveOfWar(),
             Bondsman(), Taskmaster(), BornOutcast(), AlienMutantFreak(),
             Mule(), Urchin(), Cripple(), Deranged(), FilthyWormLover(),
             MatchstickGirl(), Beggar(), Vagrant(), Pickpocket(), Mummer(),
             BeggarKing(), Acrobat(), Cultist(), RebelPriest(), HiveThug(),
             Freebooter(), DesperateKiller(), Insurrectionist(), Outlaw(),
             ConfidenceMan(), Pirate(), Duelist(), Boxer(), Kidnapper(),
             Blackmailer(), Breaker(), Smuggler(), Counterfeiter(),
             Fence(), Whoremonger(), Gunsel(), Criminal(), Thinker(), Traveler()]
        allowed_list = []
        for x in path_list:
            if x.allowed(self):
                allowed_list.append(x)
        return allowed_list

############ NOBLE SETTING ############
class NobleLifepath(Lifepath):
    pass

class BornNobility(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Born to Rule',
                          years=8,
                             resources=2,
                             circles=1,
                             trait_points=1,
                             traits=[trait.MarkOfPrivilege(),
                                     trait.YourLordship(),
                                     trait.YourEminence(),
                                     trait.YourGrace(),
                                     trait.YourMajesty()],
                          general_skill_points=5,
                          born = True)
        

class NobleCoeptir(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Coeptir',
                          years=5,
                          resources=1,
                          physical_points=1,
                          trait_points=1,
                          skill_points=4,
                          skills=[skill.CloseCombat(),
                                  skill.Etiquette(),
                                  skill.Wise('Stentor')],
                          second_only=True,
                          requirements=[Requirement(
                              traits={(trait.MarkOfPrivilege(),):1})])

class Bastard(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Bastard',
                          years=4,
                          circles=1,
                          floater_points=1,
                          trait_points=2,
                          traits=[trait.Bastard(),
                                  trait.Contender()],
                          skill_points=3,
                          skills=[skill.Wise('Family Secret'),
                                  skill.Extortion()],
                          second_only = True,
                          once_only = True)

class Companion(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Companion',
                          years=8,
                          resources=1,
                          circles=1,
                          mental_points=1,
                          trait_points=2,
                          skill_points=7,
                          skills=[skill.Etiquette(),
                                  skill.Astronomy(),
                                  skill.MusicalInstrument(),
                                  skill.Doctrine,
                                  skill.Persuasion()],
                          second_or_third_only = True,
                          once_only = True)

class NobleArmiger(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Armiger',
                             years=5,
                             resources=1,
                             physical_points=1,
                             trait_points=1,
                             traits=[trait.AnvilTrained(),
                                     trait.Tough()],
                          skill_points=4,
                          skills=[skill.AssaultWeapons,
                                  skill.Wise('Armiger'),
                                  skill.Intimidation()],
                             requirements=[Requirement(
                                 paths = {('Coeptir', 'Sergeant', 'Court Coeptir'):1})])

class NobleLPAnvil(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Lord-Pilot Anvil',
                             years=5,
                             resources=1,
                             circles=1,
                             physical_points = 1,
                             trait_points = 2,
                             traits = [trait.CorvusAndCrucis(),
                                       trait.IronTrained()],
                          skill_points=4,
                          skills=[skill.SquadSupportWeapons(),
                                  skill.Tactics(),
                                  skill.Wise('Iron')],
                             requirements = [Requirement(
                                 paths = {('Armiger','Court Armiger', 'Magnate'):1})])

class NobleLPHammer(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Lord-Pilot Hammer',
                             years=5,
                             resources=2,
                             floater_points=1,
                             trait_points=2,
                             traits=[trait.CorvusAndCrucis()],
                          skill_points=7,
                          skills=[skill.Pilot(),
                                  skill.Helm(),
                                  skill.Navigation(),
                                  skill.Tactics(),
                                  skill.VehicularWeapons(),
                                  skill.ZeroG()],
                             requirements=[Requirement(
                                 paths = {('Armiger','Court Armiger', 'Magnate'):1})])
class Lady(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Lady',
                          years=7,
                          resources=2,
                          circles=2,
                          mental_points=1,
                          trait_points=1,
                          skill_points=8,
                          skills=[skill.SoothingPlatitudes(),
                                  skill.ChildRearing(),
                                  skill.EstateManagement(),
                                  skill.Seduction,
                                  skill.Inconspicuous,
                                  skill.Wise('Court'),
                                  skill.Wise('Husband')],
                          requirements=[Requirement(
                              paths = {('Companion',):1})])
        
class CourtLord(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Court Lord',
                          years=8,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          trait_points= 2,
                          traits=[trait.Wigged(),
                                  trait.Effeminate(),
                                  trait.Scheming()],
                          skill_points=8,
                          skills=[skill.Persuasion(),
                                  skill.Falsehood(),
                                  skill.Etiquette(),
                                  skill.Conspicuous(),
                                  skill.Wise('Court'),
                                  skill.Wise('Lord'),
                                  skill.Wise('Scheme')],
                          requirements=[Requirement(
                              paths = {('Chamberlain','Treasurer', 'Constable', 'Coroner', 'Lord-Pilot Hammer', 'Lord-Pilot Anvil'):1})])

class HammerLord(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Hammer Lord',
                          years=9,
                          resources=3,
                          circles=1,
                          mental_points=1,
                          trait_points=2,
                          traits=[trait.HammerLord(),
                                  trait.REMF()],
                          skill_points=6,
                          skills=[skill.Strategy(),
                                  skill.Command(),
                                  skill.Physics(),
                                  skill.Artillery(),
                                  skill.Wise('Hammer')],
                          requirements=[Requirement(
                              paths = {('Lord-Pilot Hammer',):1})])
        
class AnvilLord(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Anvil Lord',
                          years=7,
                          resources=3,
                          circles=1,
                          floater_points=1,
                          trait_points=2,
                          traits=[trait.AnvilLord()],
                          skill_points=6,
                          skills=[skill.Command(),
                                  skill.Strategy(),
                                  skill.Oratory(),
                                  skill.Artillery(),
                                  skill.Wise('Hammer')],
                          requirements=[Requirement(
                              paths = {('Lord-Pilot Anvil',):1})])

class VoidLord(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Void Lord',
                          years=10,
                          circles=2,
                          floater_points=1,
                          trait_points=2,
                          traits=[trait.Bitter(),
                                  trait.Frustrated(),
                                  trait.Righteous()],
                          general_skill_points=1,
                          skill_points=5,
                          skills=[skill.Wise('Void'),
                                  skill.Wise('Vaylen'),
                                  skill.Bureaucracy(),
                                  skill.Wise('Lost Secrets')],
                          requirements=[Requirement(
                              paths = {('Hammer Lord', 'Anvil Lord'):1})])

class ForgedLord(NobleLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Forged Lord',
                          years=12,
                          resources=3,
                          circles=2,
                          floater_points=1,
                          trait_points=1,
                          traits=[trait.Forged()],
                          general_skill_points=2,
                          skill_points=7,
                          skills=[skill.Administration(),
                                  skill.Logistics(),
                                  skill.Wise('Noble'),
                                  skill.Wise('Hammer'),
                                  skill.Wise('Anvil'),
                                  skill.Wise('Planet')],
                          requirements=[Requirement(paths={('Hammer Lord','Anvil Lord'):0}),
                                        Requirement(traits={(trait.YourGrace(),trait.YourMajesty()):1})])

############ STEWARDSHIP & COURT SETTING ############
class CourtLifepath(Lifepath):
    pass

class CourtClerk(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Court Clerk',
                          years=4,
                          resources=1,
                          trait_points=1,
                          skill_points=4,
                          skills=[skill.Bureaucracy(),
                                  skill.Wise('Bribe'),
                                  skill.Wise('Paperwork')])

class CourtCourier(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Courier',
                          years=4,
                          physical_points=1,
                          trait_points=2,
                          traits=[trait.Late()],
                          skill_points=4,
                          skills=[skill.Streetwise(),
                                  skill.Wise('Palace'),
                                  skill.Inconspicuous()],)

class ManAtArms(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Man-at-Arms',
                          years=4,
                          physical_points=1,
                          trait_points=1,
                          traits=[trait.Muscle()],
                          skill_points=5,
                          skills=[skill.CloseCombat(),
                                  skill.Intimidation(),
                                  skill.Etiquette(),
                                  skill.Security()],
                          requirements=[Requirement(
                              paths ={('Discipline Officer', 'Anvil Elite', 'Sergeant', 'Sodalis'):1})])

class CourtCoeptir(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Court Coeptir',
                          years=4,
                          resources=1,
                          physical_points=1,
                          trait_points=1,
                          skill_points=4,
                          skills=[skill.Wise('Court'),
                                  skill.Etiquette(),
                                  skill.Wise('Stentor')],
                          second_only = True)

class Herald(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Herald',
                          years=5,
                          resources=1,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Formalist(),
                                  trait.EideticMemory()],
                          skill_points=3,
                          skills=[skill.Heraldry(),
                                  skill.Wise('Noble Family')],
                          requirements=[Requirement(
                              paths = {('Coeptir', 'Court Coeptir', 'Born to Fire'): 1})])

class Bureaucrat(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Bureaucrat',
                          years=6,
                          resources=1,
                          circles=1,
                          trait_points=2,
                          traits=[trait.AdumbrateVeil()],
                          skill_points=4,
                          skills=[skill.Bureaucracy(),
                                  skill.SoothingPlatitudes(),
                                  skill.Wise('Form')],
                          requirements=[Requirement(
                              paths = {('Courtier', 'Court Clerk', 'Coeptir', 'Court Coeptir', 'Student'):1})])

class CourtArmiger(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Court Armiger',
                          years=5,
                          resources=1,
                          physical_points=1,
                          trait_points=1,
                          traits=[trait.AnvilTrained(),
                                  trait.Pragmatic()],
                          skill_points=5,
                          skills=[skill.Etiquette(),
                                  skill.AssaultWeapons(),
                                  skill.Wise('Armiger'),
                                  skill.Intimidation()],
                          requirements=[Requirement(
                              paths = {('Novitiate','Coeptir','Court Coeptir','Sergeant','Man-at-Arms'):1})])

class Stentor(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Stentor',
                          years=6,
                          resources=1,
                          circles=1,
                          floater_points=1,
                          trait_points=1,
                          traits=[trait.AppreciativeOfGoodCraft()],
                          skill_points=4,
                          skills=[skill.Wise('Iron'),
                                  skill.Fabrication(),
                                  skill.Repair()],
                          requirements=[Requirement(
                              paths = {('Coeptir','Court Coeptir'):1},
                              traits = {(trait.YourEminence(), trait.YourGrace(), trait.YourLordship(), trait.YourMajesty()):-1})])
                                     
class CourtLPAnvil(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Lord-Pilot Anvil',
                          years=5,
                          resources=1,
                          circles=1,
                          physical_points=1,
                          skill_points=5,
                          skills=[skill.Etiquette(),
                                  skill.SquadSupportWeapons(),
                                  skill.Tactics(),
                                  skill.Wise('Iron')],
                          trait_points=2,
                          traits=[trait.CorvusAndCrucis(),
                                  trait.Groundhog(),
                                  trait.IronTrained()],
                          requirements=[Requirement(traits={(trait.MarkOfPrivilege(),):1}, paths={('Armiger','Court Armiger'):1}),
                                        Requirement(paths={('Anvil Captain','Executive Official','Magnate','Treasurer','Financier','Chamberlain'):1})])

class Mandarin(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Mandarin',
                          years=6,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          skill_points=7,
                          skills=[skill.ImperialLaw(),
                                  skill.ChurchLaw(),
                                  skill.Instruction(),
                                  skill.Wise('Province'),
                                  skill.Bureaucracy(),
                                  skill.Wise('Discipline')],
                          trait_points=2,
                          traits=[trait.Mustache(),
                                  trait.Scheming()],
                          requirements=[Requirement(
                              paths = {('Student', 'Court Clerk', 'Foundation Student', 'Courtier'):1})])

class Courtier(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Courtier',
                          years=6,
                          resources=1,
                          circles=2,
                          skill_points=8,
                          skills=[skill.UglyTruth(),
                                  skill.Persuasion(),
                                  skill.Seduction(),
                                  skill.Inconspicuous(),
                                  skill.Wise('Gossip'),
                                  skill.Wise('Noble')],
                          trait_points=2,
                          traits=[trait.Fop(),
                                  trait.RapierWit()],
                          requirements=[Requirement(
                              paths = {('Coeptir', 'Court Coeptir'):1})])

class Hostage(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Hostage',
                          years=4,
                          resources=1,
                          mental_points= 1,
                          skill_points=3,
                          skills=[skill.ForeignLanguages(),
                                  skill.ForeignHistory()],
                          trait_points=2,
                          traits=[trait.Homesick()],
                          general_skill_points=1,
                          requirements=[Requirement(
                              traits = {(trait.MarkOfPrivilege(),):1})])

class Duenna(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Duenna',
                          years=6,
                          resources=1,
                          circles=1,
                          skill_points=4,
                          skills=[skill.ChildRearing(),
                                  skill.Wise('Heir'),
                                  skill.UglyTruth(),
                                  skill.Instruction()],
                          trait_points=2,
                          traits=[trait.Dismissive(), trait.Curt()],
                          requirements=[Requirement(
                              paths = {('Companion',):1},
                              traits = {(trait.YourEminence(), trait.YourGrace(), trait.YourLordship(), trait.YourMajesty()):-1})])

class Artificer(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Artificer',
                          years=10,
                          resources=2,
                          circles=2,
                          floater_points=1,
                          skill_points=5,
                          skills=[skill.IronArtifice(),
                                  skill.Wise('Lord-Pilot'),
                                  skill.Wise('Weapon Technology')],
                          trait_points=1,
                          traits=[trait.Artisan()],
                          requirements=[Requirement(
                              paths = {('Stentor',):1})])

class Ravilar(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Ravilar',
                          years=5,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          skill_points=5,
                          skills=[skill.History(),
                                  skill.Composition(),
                                  skill.Propaganda(),
                                  skill.ObscureHistory()],
                          trait_points=1,
                          traits=[trait.EarForVoices()],
                          requirements=[Requirement(
                              paths = {('Companion','Student','Foundation Student','Courtier'):1})])

class Coroner(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Coroner',
                          years=6,
                          resources=2,
                          circles=2,
                          skill_points=5,
                          skills=[skill.HumanBiology(),
                                  skill.InvestigativeLogic(),
                                  skill.Wise('Writ'),
                                  skill.Wise('Murder')],
                          trait_points=2,
                          traits=[trait.IronStomach()],
                          requirements=[Requirement(
                              paths = {('Mandarin', 'Court Lord', 'Magnate', 'Dregus', 'Advocate'):1})])

class Constable(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Constable',
                          years=5,
                          resources=2,
                          circles=2,
                          skill_points=6,
                          skills=[skill.ImperialLaw(),
                                  skill.Wise('Outlaw'),
                                  skill.Wise('Province'),
                                  skill.Wise('Spaceport'),
                                  skill.Wise('Tax')],
                          trait_points=1,
                          traits=[trait.NoseForTrouble()],
                          requirements=[Requirement(
                              paths = {('Mandarin','Lord-Pilot Hammer','Lord-Pilot Anvil','Coroner','First Officer','X-O'):1})])

class Justiciar(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Justiciar',
                          years=6,
                          resources=2,
                          circles=2,
                          floater_points=1,
                          skill_points=5,
                          skills=[skill.Interrogation(),
                                  skill.Torture(),
                                  skill.Wise('Criminal'),
                                  skill.Amercement()],
                          trait_points=1,
                          traits=[trait.SternDemeanor()],
                          requirements=[Requirement(
                              paths = {('Mandarin','Constable','Coroner','Anvil Captain','Hammer Captain'):1})])

class Treasurer(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Treasurer',
                          years=5,
                          resources=3,
                          skill_points=6,
                          skills=[skill.Wise('Treasury'),
                                  skill.EstateManagement(),
                                  skill.Accounting(),
                                  skill.Wise('Tax'),
                                  skill.Wise('Debt')],
                          trait_points=2,
                          traits=[trait.Pecunious(),
                                  trait.LavishTaste()],
                          requirements=[Requirement(
                              paths = {('Banker','Financier','Constable','Coroner','Anvil Lord','Hammer Lord','Court Lord','Void Lord'): 1})])

class Chamberlain(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Chamberlain',
                          years=8,
                          resources=3,
                          circles=2,
                          skill_points=10,
                          skills=[skill.SoothingPlatitudes(),
                                  skill.Intimidation(),
                                  skill.UglyTruth(),
                                  skill.Wise('Bureaucracy'),
                                  skill.Wise('Power Player'),
                                  skill.Wise('Diplomat'),
                                  skill.Wise('Lord Steward')],
                          trait_points=1,
                          general_skill_points=1,
                          requirements=[Requirement(
                              paths = {('Justiciar', 'Treasurer', 'Court Lord'):1})])

class LordSteward(CourtLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Lord Steward',
                          years=5,
                          resources=3,
                          circles=2,
                          skill_points=5,
                          skills=[skill.Wise('Imperial Edict'),
                                  skill.Wise('Imperial Official'),
                                  skill.Wise('Imperial Capital')],
                          trait_points=2,
                          traits=[trait.UnderPressure(),
                                  trait.EmperorsSteward()],
                          requirements=[Requirement(
                              paths = {('Court Lord', 'Forged Lord', 'Void Lord'):1})])

############ HAMMER SETTING ############
class HammerLifepath(Lifepath):
    pass

class HammerYeoman(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Yeoman',
                          years=3,
                          physical_points=1,
                          skill_points=4,
                          skills=[skill.Crew(),
                                  skill.BackBreakingLabor(),
                                  skill.Wise('Cleaning')],
                          trait_points= 1,
                          traits=[trait.Hazed(),
                                  trait.DistortionSickness()])
        
class Shipfitter(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Shipfitter',
                          years=3,
                          physical_points=1,
                          skill_points=5,
                          skills=[skill.Repair(),
                                  skill.Wise('Damage'),
                                  skill.FireControl(),
                                  skill.Wise('Ship')],
                          trait_points=1,
                          traits=[trait.BlackFingernails()],
                          requirements=[Requirement(
                              paths = {('Yeoman',):1})])

class SensorsTech(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Sensors Tech',
                          years=3,
                          resources=1,
                          mental_points=1,
                          skill_points=4,
                          skills=[skill.Sensors(),
                                  skill.Wise('Glitch'),
                                  skill.Wise('Profile')],
                          trait_points=2,
                          traits=[trait.Twitchy()],
                          requirements=[Requirement(
                              paths = {('Yeoman',):1})])

class HammerSignalsTech(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Signals Tech',
                          years=3,
                          resources=1,
                          mental_points=1,
                          skill_points=5,
                          skills=[skill.Signals(),
                                  skill.Cryptography(),
                                  skill.Wise('Sferics'),
                                  skill.Wise('Emissions Footprint')],
                          trait_points=2,
                          traits=[trait.VacantStare(),
                                  trait.Jumpy(),
                                  trait.Paranoid()],
                          requirements=[Requirement(
                              paths = {('Yeoman',):1})])

class TurretCrew(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Turret Crew',
                          years=3,
                          resources=1,
                          skill_points=3,
                          skills=[skill.VehicularWeapons(),
                                  skill.Wise('Vehicular Weapons')],
                          trait_points=2,
                          traits=[trait.Cocky(),
                                  trait.Fatalistic(),
                                  trait.HammerFliesAnvilDies()],
                          requirements=[Requirement(
                              paths = {('Yeoman',):1})])

class FireControlTech(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Fire Control Tech',
                          years=3,
                          resources=1,
                          skill_points=4,
                          skills=[skill.Artillery(),
                                  skill.Wise('Big Guns'),
                                  skill.Wise('Attack Vector')],
                          trait_points=1,
                          traits=[trait.SeriousAsAHeartAttack()],
                          requirements=[Requirement(
                              paths = {('Yeoman',):1})])

class HammerCook(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Cook',
                          years=5,
                          resources=2,
                          skill_points=4,
                          skills=[skill.Cooking(),
                                  skill.Wise('Local Ingredients'),
                                  skill.Wise('Intestinal Disorder')],
                          trait_points=1,
                          traits=[trait.Weird(),
                                  trait.Mangled(),
                                  trait.ThousandYardStare()],
                          requirements=[Requirement(
                              paths = {('Yeoman',):1})])
        
class HammerCoeptir(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self,
                          name='Coeptir',
                          years=3,
                          circles=1,
                          skill_points=4,
                          skills=[skill.Wise('Ship'),
                                  skill.Wise('Crew'),
                                  skill.Wise('Officer')],
                          trait_points=1,
                          traits=[trait.Naive(),
                                  trait.Idealist()],#'Tailhook' seems to have been a joke
                          second_only=True,
                          requirements=[Requirement(
                              traits={(trait.MarkOfPrivilege(),):1})])

        
class Surgeon(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Surgeon',
                          years=5,
                          resources=1,
                          circles=1,
                          mental_points=1,
                          skill_points=5,
                          skills=[skill.Surgery(),
                                  skill.Pharmacology(),
                                  skill.Wise('Triage'),
                                  skill.Wise('Illness')],
                          trait_points=1,
                          traits=[trait.Grim(), trait.Practical()],
                          requirements=[Requirement(paths = {('Doctor','Physician','Coroner','Foundation Student','Court Coeptir','Coeptir','Student'):1}),
                                        Requirement(paths={(HammerLifepath,SpacefarerLifepath):2})])


class DisciplineOfficer(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Discipline Officer',
                          years=4,
                          resources=1,
                          circles=1,
                          floater_points=1,
                          skill_points=5,
                          skills=[skill.Intimidation(),
                                  skill.Interrogation(),
                                  skill.Security(),
                                  skill.Wise('Regulations')],
                          trait_points=1,
                          traits=[trait.HardHearted()],
                          requirements=[Requirement(paths={('Constable', 'Justiciar'):1}),
                                        Requirement(paths={(HammerLifepath,):2})])

class HammerEngineer(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Hammer Engineer',
                          years=5,
                          resources=1,
                          floater_points=1,
                          skill_points=6,
                          skills=[skill.Munitions(),
                                  skill.Fabrication(),
                                  skill.Engineering(),
                                  skill.Armorer(),
                                  skill.Cryonics()],
                          trait_points=2,
                          traits=[trait.IKnowThisShipLikeMyOwnHands()],
                          requirements=[Requirement(
                              paths = {('Shipfitter','Student','Foundation Student','Court Armiger','Armiger'):1})])

class Physicist(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Physicist',
                          years=5,
                          resources=1,
                          mental_points=1,
                          skill_points=6,
                          skills=[skill.Physics(),
                                  skill.Science(),
                                  skill.Wise('Technology'),
                                  skill.Wise('Phenomenon'),
                                  skill.Wise('Distortion')],
                          trait_points=1,
                          traits=[trait.SmarterThanYou(),
                                  trait.Bookworm()],
                          requirements=[Requirement(
                              paths = {('Navigator','Student','Foundation Student'):1})])

class HammerMaster(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Hammer Master',
                          years=5,
                          resources=1,
                          circles=2,
                          mental_points=1,
                          skill_points=6,
                          skills=[skill.Bargaining(),
                                  skill.Accounting(),
                                  skill.Wise('Supply'),
                                  skill.Wise('Contraband'),
                                  skill.Wise('Prostitute')],
                          trait_points=2,
                          traits=[trait.Harried(),
                                  trait.FitsOfGenerosity(),
                                  trait.WitheringStare(),
                                  trait.HardNosed()],
                          requirements=[Requirement(
                              paths = {('Discipline Officer','Companion','Hammer Engineer','Surgeon',"Ship's Captain"):1})])

class HammerFirstOfficer(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='First Officer',
                          years=5,
                          resources=1,
                          circles=1,
                          mental_points=1,
                          skill_points=5,
                          skills=[skill.ShipManagement(),
                                  skill.Tactics(),
                                  skill.Wise('Officer'),
                                  skill.Wise('Crew')],
                          trait_points=1,
                          traits=[trait.NumberOne(),
                                  trait.NoNonsense()],
                          requirements=[Requirement(
                              paths = {('Hammer Master','Discipline Office','Navigator','Physicist','Hammer Engineer','Lord-Pilot Hammer'):1})])

class HammerLPHammer(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Lord-Pilot Hammer',
                          years=5,
                          resources=1,
                          circles=1,
                          floater_points=1,
                          skill_points=7,
                          skills=[skill.Command(),
                                  skill.Pilot(),
                                  skill.Helm(),
                                  skill.Navigation(),
                                  skill.VehicularWeapons(),
                                  skill.ZeroG()],
                          trait_points=2,
                          traits=[trait.CorvusAndCrucis(),
                                  trait.DistortionSickness(),
                                  trait.DistortionMonkey(),
                                  trait.HammerFliesAnvilDies()],
                          requirements=[Requirement(paths={('Armiger', "Circle of 10,000", 'Court Armiger', 'Magnate'):1}),
                                        Requirement(paths={(HammerLifepath,):3})])

class HammerNavigator(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Navigator',
                          years=4,
                          resources=1,
                          circles=1,
                          skill_points=5,
                          skills=[skill.Navigation(),
                                  skill.Wise('Star'),
                                  skill.Wise('Trade Route')],
                          requirements=[Requirement(
                              paths = {('Lord-Pilot Hammer',):1})])

class HammerCaptain(HammerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Hammer Captain',
                          years=6,
                          resources=2,
                          circles=2,
                          floater_points=1,
                          skill_points=6,
                          skills=[skill.Strategy(),
                                  skill.Wise('Hammer'),
                                  skill.Wise('Space Station'),
                                  skill.Wise('Spaceport'),
                                  skill.Wise('Interdiction')],
                          trait_points=2,
                          traits=[trait.Officer(),
                                  trait.SternDemeanor()],
                          general_skill_points=1,
                          requirements=[Requirement(paths={('Lord-Pilot Hammer',):1}),
                                        Requirement(traits={(trait.YourMajesty(),):1})])

############ ANVIL SETTING ############
class AnvilLifepath(Lifepath):
    pass

class Runner(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Runner',
                          years=2,
                          physical_points=1,
                          skill_points=5,
                          skills=[skill.Wise('Anvil'),
                                  skill.Inconspicuous(),
                                  skill.Wise('Officer'),
                                  skill.Wise('Message')],
                          trait_points=1,
                          traits=[trait.SeenTooMuchTooYoung()])
        
class Soldier(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Soldier',
                          years=3,
                          resources=1,
                          physical_points=1,
                          skill_points=4,
                          skills=[skill.Soldiering(),
                                  skill.AssaultWeapons(),
                                  skill.CloseCombat()],
                          trait_points=1,
                          traits=[trait.FUGAZI()])
        
class Medic(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Medic',
                          years=3,
                          resources=1,
                          circles=1,
                          skill_points=3,
                          skills=[skill.FieldDressing(),
                                  skill.Wise('Triage')],
                          trait_points=1,
                          traits=[trait.Burned()],
                          requirements=[Requirement(
                              paths = {('Soldier', 'Foundation Student', 'Student'):1})])
        
class Scout(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Scout',
                          years=3,
                          resources=1,
                          floater_points=1,
                          skill_points=5,
                          skills=[skill.Recon(),
                                  skill.Observation(),
                                  skill.Infiltration(),
                                  skill.Survival()],
                          trait_points=1,
                          traits=[trait.Cold()],
                          requirements=[Requirement(
                              paths = {('Soldier',):1})])

class AnvilSignalsTech(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Signals Tech',
                          years=3,
                          resources=1,
                          mental_points=1,
                          skill_points=3,
                          skills=[skill.Signals(),
                                  skill.Cryptography()],
                          trait_points=1,
                          traits=[trait.SigGeek],
                          requirements=[Requirement(
                              paths = {('Soldier', 'Foundation Student', 'Student'):1})])

class Machinist(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Machinist',
                          years=4,
                          resources=1,
                          skill_points=6,
                          skills=[skill.Fabrication(),
                                  skill.Repair(),
                                  skill.Driving(),
                                  skill.Wise('Engine'),
                                  skill.Wise('Grav')],
                          trait_points=1,
                          traits=[trait.GreaseMonkey()],
                          requirements=[Requirement(
                              paths = {('Soldier',):1})])

class Sergeant(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Sergeant',
                          years=4,
                          resources=1,
                          circles=1,
                          mental_points=1,
                          skill_points=4,
                          skills=[skill.Tactics(),
                                  skill.Intimidation(),
                                  skill.Wise('Slacker')],
                          trait_points=2,
                          traits=[trait.OddlyLikeable(),
                                  trait.BoomingVoice()],
                          requirements=[Requirement(
                              paths = {('Soldier',):1})])

class AnvilElite(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Anvil Elite',
                          years=3,
                          resources=1,
                          physical_points=1,
                          skill_points=6,
                          skills=[skill.SquadSupportWeapons(),
                                  skill.VehicularWeapons(),
                                  skill.ZeroG()],
                          trait_points=2,
                          traits=[trait.AnvilTrained()],
                          requirements=[Requirement(paths={('Sergeant','Psychologist', 'Scout'):1})])

class Stormtrooper(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Stormtrooper',
                          years=4,
                          resources=1,
                          circles=1,
                          floater_points=1,
                          skill_points=7,
                          skills=[skill.CloseCombat(),
                                  skill.Explosives(),
                                  skill.Propaganda(),
                                  skill.ForeignLanguages(),
                                  skill.Torture(),
                                  skill.SecurityRigging()],
                          trait_points=1,
                          traits=[trait.Brutal(),
                                  trait.Unflinching()],
                          requirements=[Requirement(
                              paths = {('Lord-Pilot Anvil', 'Circle of 10,000', 'Anvil Elite','Sergeant'):1})])

class AnvilPilot(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Anvil Pilot',
                          years=5,
                          resources=1,
                          skill_points=7,
                          skills=[skill.Pilot(),
                                  skill.Driving(),
                                  skill.Navigation(),
                                  skill.Sensors(),
                                  skill.Wise('Grav Sled'),
                                  skill.Wise('Assault Shuttle')],
                          trait_points=2,
                          traits=[trait.Daredevil()],
                          requirements=[Requirement(
                              paths = {('Soldier',):1})])

class Armorer(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Armorer',
                          years=5,
                          resources=1,
                          skill_points=7,
                          skills=[skill.Armorer(),
                                  skill.Munitions(),
                                  skill.Repair(),
                                  skill.Wise('Weapons'),
                                  skill.Wise('Armor'),
                                  skill.FireControl()],
                          trait_points=1,
                          traits=[trait.NoNonsense()],
                          requirements=[Requirement(
                              paths = {('Machinist', 'Stormtrooper', 'Hammer Engineer'):1})])

class AnvilEngineer(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Anvil Engineer',
                          years=5,
                          resources=1,
                          mental_points=1,
                          skill_points=6,
                          skills=[skill.Fortifications(),
                                  skill.Munitions(),
                                  skill.Recon(),
                                  skill.Infiltration(),
                                  skill.Wise('Materiel')],
                          trait_points=2,
                          traits=[trait.SmartestGuyInTheRoom()],
                          requirements=[Requirement(
                              paths = {('Student', 'Foundation Student', 'Armorer', 'Machinist', 'Lieutenant'):1})])

class Lieutenant(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Lieutenant',
                          years=4,
                          resources=2,
                          circles=1,
                          skill_points=4,
                          skills=[skill.Command(),
                                  skill.Intimidation(),
                                  skill.Wise('Sergeant')],
                          floater_points=1,
                          trait_points=1,
                          traits=[trait.CleanCut()],
                          requirements=[Requirement(
                              paths = {('Coeptir', 'Novitiate', 'Anvil Elite'):1})])

class Propagandist(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Propagandist',
                          years=5,
                          resources=1,
                          circles=1,
                          mental_points=1,
                          skill_points=5,
                          skills=[skill.Propaganda(),
                                  skill.Wise('Media'),
                                  skill.Wise('Signals Tech'),
                                  skill.Composition()],
                          trait_points=1,
                          traits=[trait.CleverBastard()],
                          requirements=[Requirement(
                              paths = {('Circle of 10,000','Psychologist','Ravilar','Lieutenant','Court Coeptir','Coeptir','Companion'):1})])

class XO(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='X-O',
                          years=3,
                          resources=1,
                          circles=1,
                          skill_points=6,
                          skills=[skill.Administration(),
                                  skill.Persuasion(),
                                  skill.Wise('Unit'),
                                  skill.Bureaucracy(),
                                  skill.Wise('Regulations')],
                          trait_points=1,
                          traits=[trait.ScutWork(),
                                  trait.PrivilegedPosition()],
                          requirements=[Requirement(
                              paths = {('Psychologist','Circle of 10,000','Lieutenant','Court Coeptir','Coeptir','Companion'):1})])

class AnvilCaptain(AnvilLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Anvil Captain',
                          years=7,
                          resources=2,
                          circles=2,
                          floater_points=1,
                          skill_points=6,
                          skills=[skill.Strategy(),
                                  skill.Wise('Anvil'),
                                  skill.Wise('Forged Lord'),
                                  skill.Wise('Hammer'),
                                  skill.Wise('Terrain')],
                          trait_points=2,
                          traits=[trait.SeenItAll(),
                                  trait.Kilgore()],
                          requirements=[Requirement(
                              paths = {('Lieutenant', 'Lord-Pilot Anvil'):1})])

############ THEOCRACY SETTING ############
class TheocracyLifepath(Lifepath):
    pass

class BornTheocracy(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Born to Fire',
                          years=9,
                          resources=1,
                          circles=1,
                          trait_points=1,
                          traits=[trait.BornOnTheWheel()],
                          general_skill_points=3,
                          born= True)

class TheocracyStudent(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Student',
                          years=6,
                          mental_points=1,
                          skill_points=8,
                          skills=[skill.Doctrine(),
                                  skill.Research(),
                                  skill.History(),
                                  skill.Astronomy(),
                                  skill.Oratory(),
                                  skill.ChurchLaw(),
                                  skill.ImperialLaw()],
                          trait_points=2,
                          traits=[trait.WellRead(),
                                  trait.BawdyFool()])

class Notary(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Notary',
                          years=5,
                          resources=1,
                          skill_points=3,
                          skills=[skill.Bureaucracy(),
                                  skill.Accounting(),
                                  skill.Wise('Forgery'),
                                  skill.Wise('Tithe')],
                          trait_points=1,
                          requirements=[Requirement(
                              paths = {('Student',):1})])

class Fireward(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Fireward',
                          years=4,
                          skill_points=8,
                          skills=[skill.Wise('Fire'),
                                  skill.FireControl(),
                                  skill.Wise('Pyromaniac'),
                                  skill.Wise('Ritual'),
                                  skill.Wise('Temple'),
                                  skill.Wise('Cotar'),
                                  skill.Wise('Worshipper'),
                                  skill.Wise('Secret Stash-wise')],
                          trait_points=1)

class DevotedToFire(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Devoted to Fire',
                          years=3,
                          resources=1,
                          mental_points=1,
                          skill_points=3,
                          skills=[skill.Doctrine,
                                  skill.Wise('Temple')],
                          trait_points=1,
                          traits=[trait.DevotedToFire()])

class Mystes(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Mystes',
                          years=4,
                          resources=1,
                          circles=1,
                          physical_points=1,
                          skill_points=5,
                          skills=[skill.Meditation(),
                                  skill.FieldDressing(),
                                  skill.Suasion(),
                                  skill.Wise('Locals')],
                          trait_points=2,
                          traits=[trait.OrderOfTheMysticFire()],
                          requirements=[Requirement(
                              paths = {('Devoted to Fire',):1})])
                                  # or does it require the trait?

class Archivist(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Archivist',
                          years=8,
                          resources=1,
                          mental_points=1,
                          skill_points=5,
                          skills=[skill.Wise('Church Records'),
                                  skill.AncientHistory(),
                                  skill.Symbology()],
                          trait_points=1,
                          traits=[trait.Harried()],
                          requirements=[Requirement(
                              paths = {('Devoted to Fire', 'Student'):0})])
                                  # or does it require the trait?

class Interpreter(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Interpreter',
                          years=7,
                          resources=1,
                          mental_points=1,
                          skill_points=7,
                          skills=[skill.ForeignLanguages(),
                                  skill.AncientLanguages(),
                                  skill.Instruction(),
                                  skill.Wise('Foreigner'),
                                  skill.Wise('Traveler'),
                                  skill.Wise('Lecture'),
                                  skill.Wise('Monograph')],
                          trait_points=1,
                          traits=[trait.Odd(),
                                  trait.Linguist()],
                          requirements=[Requirement(
                              paths = {('Devoted to Fire', 'Student'):0})])
                                  # or does it require the trait?

class Custodian(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Custodian',
                          years=7,
                          circles=1,
                          floater_points=1,
                          skill_points=5,
                          skills=[skill.Wise('Relic'),
                                  skill.ObscureHistory(),
                                  skill.Folklore(),
                                  skill.Wise('Martyr')],
                          trait_points=2,
                          traits=[trait.NoseForTrouble()],
                          requirements=[Requirement(
                              paths = {('Devoted to Fire', 'Student'):0})])
                                  # or does it require the trait?

class BringerOfFire(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Bringer of Fire',
                          years=5,
                          circles=1,
                          floater_points=1,
                          skill_points=5,
                          skills=[skill.Suasion(),
                                  skill.Wise('Locals'),
                                  skill.Wise('Mystes'),
                                  skill.Wise('Infidel')],
                          trait_points=2,
                          traits=[trait.Zealot(),
                                  trait.Jaded()],
                          requirements=[Requirement(
                              paths = {('Devoted to Fire',):1})])
                                  # or does it require the trait?

class Sodalis(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Sodalis',
                          years=3,
                          physical_points=1,
                          skill_points=4,
                          skills=[skill.AssaultWeapons(),
                                  skill.Explosives(),
                                  skill.Driving()],
                          trait_points=1,
                          traits=[trait.AnvilTrained(),
                                  trait.Loyal(),
                                  trait.Fearless()],
                          requirements=[Requirement(
                              paths = {('Devoted to Fire',):1})])
                                  # or does it require the trait?

class SodalisTechnician(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Sodalis Technician',
                          years=3,
                          mental_points=1,
                          skill_points=4,
                          skills=[skill.Wise('Technology'),
                                  skill.Signals(),
                                  skill.Sensors()],
                          trait_points=1,
                          requirements=[Requirement(
                              paths = {('Devoted to Fire',):1})])
                                  # or does it require the trait?

class SodalisPilot(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Sodalis Pilot',
                          years=3,
                          floater_points=1,
                          skill_points=4,
                          skills=[skill.Pilot(),
                                  skill.VehicularWeapons(),
                                  skill.Repair()],
                          trait_points=1,
                          traits=[trait.Flyboy()],
                          requirements=[Requirement(
                              paths = {('Devoted to Fire',):1})])
                                  # or does it require the trait?

class SodalisBrother(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Sodalis-Brother',
                          years=2,
                          resources=1,
                          circles=1,
                          floater_points=1,
                          skill_points=4,
                          skills=[skill.Wise('Cotar Fomas'),
                                  skill.Wise('Sodalis'),
                                  skill.Wise('Church Transport')],
                          trait_points=1,
                          traits=[trait.DevotedToFire(),
                                  trait.Zealot(),
                                  trait.Tough(),
                                  trait.Resourceful()],
                          requirements=[Requirement(
                              paths = {('Lord-Pilot Anvil',):1})])

class SodalisCaptain(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Sodalis-Captain',
                          years=5,
                          resources=1,
                          circles=1,
                          floater_points=1,
                          skill_points=4,
                          skills=[skill.Tactics(),
                                  skill.Command(),
                                  skill.Wise('Sodalis')],
                          trait_points=1,
                          traits=[trait.SwornToTheFire()],
                          requirements=[Requirement(paths={('Sergeant', 'Court Armiger', 'Armiger', 'Sodalis-Brother'):1}),
                                        Requirement(paths={('Sodalis', 'Sodalis Technician', 'Sodalis Pilot'):2})])
    
class Cotar(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Cotar',
                          years=5,
                          resources=1,
                          circles=2,
                          skill_points=4,
                          skills=[skill.Divination(),
                                  skill.Oratory(),
                                  skill.Wise('Parish'),
                                  skill.Suasion()],
                          trait_points=2,
                          traits=[trait.KeeperOfTheFire()],
                          requirements=[Requirement(paths={('Devoted to Fire',):1}),
                                        Requirement(traits={(trait.YourLordship(),):1})])


class Dregus(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Dregus',
                          years=6,
                          resources=2,
                          circles=2,
                          skill_points=5,
                          skills=[skill.Bureaucracy(),
                                  skill.Wise('Tithe'),
                                  skill.Wise('Cotar'),
                                  skill.Wise('Archcotare')],
                          trait_points=1,
                          traits=[trait.Dregutai(),
                                  trait.OrderBeforeChaos(),
                                  trait.Venal(),
                                  trait.Wise(),
                                  trait.Charismatic()],
                          requirements=[Requirement(
                              paths = {('Born to Rule','Cotar'):0})])

class CotarFomas(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Cotar Fomas',
                          years=4,
                          resources=2,
                          circles=1,
                          floater_points=1,
                          skill_points=5,
                          skills=[skill.Command(),
                                  skill.Wise('Sodalis'),
                                  skill.Wise('Temple'),
                                  skill.Wise('Dregus')],
                          trait_points=2,
                          traits=[trait.CotarFomas()],
                          requirements=[Requirement(paths={('Sodalis-Captain',):1}),
                                        Requirement(paths={('Lord-Pilot Anvil', 'Devoted to Fire'):0})])


class Archcotare(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Archcotare',
                          years=10,
                          resources=3,
                          circles=2,
                          mental_points=1,
                          skill_points=4,
                          skills=[skill.ReligiousHistory(),
                                  skill.ObscureHistory(),
                                  skill.Administration()],
                          trait_points=2,
                          traits=[trait.Arbiter(),
                                  trait.Independent(),
                                  trait.Liberal(),
                                  trait.Traditionalist(),
                                  trait.Leech()],
                          general_skill_points=2,
                          requirements=[Requirement(
                              paths = {('Dregus',):1},
                              traits = {(trait.YourEminence(), trait.YourGrace()):1})])

class AdjutantInquisitor(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Adjutant Inquisitor',
                          years=4,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          skill_points=4,
                          skills=[skill.ChurchLaw(),
                                  skill.InvestigativeLogic(),
                                  skill.Wise('Mundus Humanitas')],
                          trait_points=1,
                          traits=[trait.OrderOfTheSeekingFire()],
                          requirements=[Requirement(
                              paths = {('Cotar', 'Archivist', 'Custodian', 'Interpreter'):1})])

class Inquisitor(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Inquisitor',
                          years=7,
                          resources=2,
                          circles=1,
                          floater_points=1,
                          skill_points=5,
                          skills=[skill.Interrogation(),
                                  skill.Torture(),
                                  skill.Wise('Heresy'),
                                  skill.Psychology()],
                          trait_points=1,
                          traits=[trait.Skeptical(),
                                  trait.BrightMark()],
                          requirements=[Requirement(
                              paths = {('Adjutant Inquisitor',):1})])

class HighInquisitor(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='High Inquisitor',
                          years=6,
                          resources=2,
                          circles=2,
                          skill_points=5,
                          skills=[skill.Observation(),
                                  skill.Demonology(),
                                  skill.Command(),
                                  skill.Wise('Scheme')],
                          trait_points=1,
                          traits=[trait.DomineeringPresence()],
                          requirements=[Requirement(
                              paths = {('Inquisitor'):1})])

class CotarAntistes(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Cotar Antistes',
                          years=8,
                          resources=3,
                          circles=2,
                          mental_points=1,
                          trait_points=2,
                          traits=[trait.WordIsLaw(),
                                  trait.Metropolitan()],
                          general_skill_points=2,
                          requirements=[Requirement(
                              traits = {(trait.YourGrace(), trait.YourMajesty()):1})])

class CotarArderes(TheocracyLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Cotar Arderes',
                          years=10,
                          resources=3,
                          circles=2,
                          trait_points=2,
                          traits=[trait.Primarch()],
                          general_skill_points=2,
                          requirements=[Requirement(
                              paths = {('Cotar Antistes',):1})])

############ MERCHANT LEAGUE SETTING ############
class MerchantLeagueLifepath(Lifepath):
    pass

class BornLeague(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Born to the League',
                          years=10,
                          resources=1,
                          circles=1,
                          trait_points=2,
                          traits=[trait.CapitalistAtHeart(),
                                  trait.Misanthropic(),
                                  trait.Elitist()],
                          general_skill_points=4,
                          born = True)
    
class LeagueStudent(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Student',
                          years=8,
                          resources=1,
                          skill_points=5,
                          skills=[skill.Wise('Institutional Drudgery'),
                                  skill.LeagueHistory(),
                                  skill.Wise('Sports')],
                          trait_points=1,
                          traits=[trait.Agitated,
                                  trait.Broken()])

class LeagueClerk(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Clerk',
                          years=4,
                          skill_points=4,
                          skills=[skill.Bureaucracy(),
                                  skill.Wise('Bribe'),
                                  skill.Wise('Paperwork')],
                          trait_points=1)

class Scrivener(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Scrivener',
                          years=8,
                          resources=1,
                          mental_points=1,
                          skill_points=5,
                          skills=[skill.Composition(),
                                  skill.Cartography(),
                                  skill.Research(),
                                  skill.History()],
                          trait_points=2,
                          traits=[trait.CrookedFingers()],
                          requirements=[Requirement(
                              paths = {('Student', 'Clerk'):1})])
    
class Accountant(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Accountant',
                          years=6,
                          resources=2,
                          skill_points=4,
                          skills=[skill.Accounting(),
                                  skill.Wise('Books'),
                                  skill.Wise('Embezzlement')],
                          trait_points=2,
                          traits=[trait.FollowTheMoney()],
                          requirements=[Requirement(
                              paths = {('Student', 'Clerk'):1})])

class Security(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Security',
                          years=3,
                          physical_points=1,
                          skill_points=4,
                          skills=[skill.Security(),
                                  skill.Intimidation(),
                                  skill.CloseCombat()],
                          trait_points=1,
                          traits=[trait.Bored(),
                                  trait.Thug(),
                                  trait.Professional()],
                          requirements=[Requirement(age = 18)])

class SecurityOfficer(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Security Officer',
                          years=5,
                          resources=2,
                          circles=1,
                          floater_points=1,
                          skill_points=7,
                          skills=[skill.Interrogation(),
                                  skill.Torture(),
                                  skill.Wise('Rebel'),
                                  skill.Wise('Corporate Hierarchy'),
                                  skill.Pilot(),
                                  skill.Wise('Crowd Suppression'),
                                  skill.AssaultWeapons()],
                          trait_points=2,
                          traits=[trait.Mean(),
                                  trait.Cunning()],
                          requirements=[Requirement(paths={('Discipline Officer', 'Sergeant', 'Stormtrooper'):1}),
                                        Requirement(paths={SECURITY_LIFEPATHS:2})])

class Agent(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Agent',
                          years=6,
                          resources=2,
                          circles=1,
                          floater_points=1,
                          skill_points=8,
                          skills=[skill.InvestigativeLogic(),
                                  skill.SecurityRigging(),
                                  skill.Signals(),
                                  skill.Extortion(),
                                  skill.Intimidation(),
                                  skill.Wise('Bribe'),
                                  skill.Wise('Frame'),
                                  skill.Wise('Blackmail')],
                          trait_points=1,
                          traits=[trait.ColdBlooded()],
                          requirements=[Requirement(
                              paths = {('Security Officer', 'Propagandist', 'Commentariat', 'Ravilar', 'Stormtrooper'):1})])

class Commentariat(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Commentariat',
                          years=5,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          skill_points=6,
                          skills=[skill.Propaganda(),
                                  skill.Composition(),
                                  skill.Journalism(),
                                  skill.Wise('Dissent'),
                                  skill.Wise('Screed')],
                          trait_points=1,
                          traits=[trait.Casuist()],
                          requirements=[Requirement(paths={('Student', 'Scrivener', 'Propagandist', 'Media', 'Ravilar'):1}),
                                        Requirement(paths={(FoundationLifepath,):1})])

class Physician(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Physician',
                          years=5,
                          resources=3,
                          circles=1,
                          floater_points=1,
                          skill_points=5,
                          skills=[skill.Pharmacology(),
                                  skill.Surgery(),
                                  skill.Wise('Malady'),
                                  skill.Wise('Executive')],
                          trait_points=1,
                          traits=[trait.SteadyHands(),
                                  trait.SelfSatisfied()],
                          requirements=[Requirement(
                              paths = {('Foundation Student', 'Student', 'Doctor', 'Surgeon'):1})])

class Merchant(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Merchant',
                          years=6,
                          resources=3,
                          circles=1,
                          skill_points=5,
                          skills=[skill.Bargaining(),
                                  skill.Wise('Goods'),
                                  skill.Wise('Traveler'),
                                  skill.Wise('Trade')],
                          requirements=[Requirement(
                              paths = {('Foundation Student','Student','Accountant','Companion','Traveler','Hammer Master','Cargo Master',"Ship's Captain"):1})])

class Advocate(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Advocate',
                          years=6,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          skill_points=6,
                          skills=[skill.LeagueLaw(),
                                  skill.ImperialLaw(),
                                  skill.Wise('League Court'),
                                  skill.Wise('Imperial Court')],
                          trait_points=1,
                          traits=[trait.CogInTheMachine(),
                                  trait.WellSpoken(),
                                  trait.HopelesslyCorrupt()],
                          requirements=[Requirement(
                              paths = {('Foundation Student', 'Student'):1})])

class LeagueOfficial(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='League Official',
                          years=5,
                          resources=2,
                          circles=2,
                          skill_points=5,
                          skills=[skill.Bureaucracy(),
                                  skill.Persuasion(),
                                  skill.Accounting(),
                                  skill.Wise('League')],
                          trait_points=2,
                          traits=[trait.CleanCut(),
                                  trait.Ambitious(),
                                  trait.Venal()],
                          requirements=[Requirement(
                              paths={('Chamberlain', 'Merchant', 'Commentariat', 'X-O','Security Officer', 'Lieutenant'):1}),
                                        Requirement(paths={ENGINEER_LIFEPATHS:1})])

class Banker(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Banker',
                          years=7,
                          resources=3,
                          circles=1,
                          skill_points=5,
                          skills=[skill.Wise('Finances'),
                                  skill.Wise('Market'),
                                  skill.Wise('Debt'),
                                  skill.Wise('Currency')],
                          trait_points=1,
                          traits=[trait.PennyWise()],
                          requirements=[Requirement(
                              paths = {('Financier', 'Merchant'):1})])

class Magnate(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Magnate',
                          years=8,
                          resources=3,
                          circles=2,
                          skill_points=6,
                          skills=[skill.Wise('Commodities'),
                                  skill.Wise('Services'),
                                  skill.Wise('Treaty'),
                                  skill.Wise('Tariff')],
                          trait_points=2,
                          traits=[trait.AffinityForBusiness(),
                                  trait.MerchantFleetCaptain()],
                          general_skill_points=1,
                          requirements=[Requirement(
                              paths = {('Financier', 'Merchant', 'Treasurer', 'Bureaucrat'):1})])

class ChiefExecutive(MerchantLeagueLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Chief Executive',
                          years=6,
                          resources=3,
                          circles=2,
                          floater_points=1,
                          skill_points=3,
                          skills=[skill.Wise('Magnate'),
                                  skill.Wise('Competition')],
                          trait_points=1,
                          general_skill_points=2,
                          requirements=[Requirement(
                              paths = {('Magnate'):1})])

############ SETTING ############
class CommuneLifepath(Lifepath):
    pass

class BornCommune(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Born Citizen',
                          years=12,
                          resources=1,
                          trait_points=2,
                          traits=[trait.CitizenOfTheCommune(),
                                  trait.Realistic(),
                                  trait.Cynical(),
                                  trait.Idealist()],
                          general_skill_points=3,
                          born = True)

class CommuneStudent(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Student',
                          years=5,
                          resources=1,
                          circles=1,
                          mental_points=1,
                          skill_points=5,
                          skills=[skill.History(),
                                  skill.AdvancedMathematics(),
                                  skill.Rhetoric(),
                                  skill.Wise('Cop')],
                          trait_points=1,
                          traits=[trait.Educated(),
                                  trait.Drunk(),
                                  trait.Broken()])

class CommuneClerk(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Clerk',
                          years=3,
                          resources=1,
                          skill_points=3,
                          skills=[skill.Bureaucracy(),
                                  skill.Wise('Official')],
                          trait_points=1,
                          traits=[trait.Officious(),
                                  trait.Meticulous()],
                          requirements=[Requirement(
                              paths = {('Foundation Student', 'Student'):1})])

class VolunteerSoldier(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Volunteer Soldier',
                          years=4,
                          physical_points=1,
                          skill_points=6,
                          skills=[skill.Soldiering(),
                                  skill.CloseCombat(),
                                  skill.AssaultWeapons(),
                                  skill.SquadSupportWeapons(),
                                  skill.Driving()],
                          trait_points=1,
                          traits=[trait.ProudCitizen(),
                                  trait.Resourceful()],
                          requirements=[Requirement(age = 17)])

class ProfessionalOfficer(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Professional Officer',
                          years=6,
                          resources=1,
                          circles=1,
                          floater_points=1,
                          skill_points=5,
                          skills=[skill.Command(),
                                  skill.Tactics(),
                                  skill.Wise('Soldier'),
                                  skill.Wise('Anvil')],
                          trait_points=2,
                          traits=[trait.NoNonsense(),
                                  trait.Zealot()],
                          requirements=[Requirement(
                              paths = {('Volunteer Soldier','Sodalis-Captain','Sergeant','Man-at-Arms','Lord-Pilot Anvil','Lord-Pilot Hammer'):1})])


class Philosopher(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Philosopher',
                          years=6,
                          circles=1,
                          mental_points=1,
                          skill_points=6,
                          skills=[skill.Philosophy(),
                                  skill.Doctrine(),
                                  skill.Science(),
                                  skill.Composition()],
                          trait_points=1,
                          traits=[trait.Frustrated(),
                                  trait.Humanist(),
                                  trait.ConstitutionalActivist()],
                          requirements=[Requirement(
                              paths = {('Student',):1})])

class Instructor(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Instructor',
                          years=6,
                          resources=1,
                          circles=1,
                          skill_points=4,
                          skills=[skill.Instruction(),
                                  skill.Wise('Student'),
                                  skill.Wise('Textbook')],
                          trait_points= 2,
                          traits=[trait.Patient(),
                                  trait.Idealist(),
                                  trait.Jaded(),
                                  trait.Pedantic()],
                          requirements=[Requirement(
                              paths = {('Foundation Student', 'Student'):1})])

class LawEnforcement(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Law Enforcement',
                          years=5,
                          resources=1,
                          floater_points=1,
                          skill_points=5,
                          skills=[skill.InvestigativeLogic(),
                                  skill.Security(),
                                  skill.Wise('Perp'),
                                  skill.Wise('Cover Up')],
                          trait_points=1,
                          traits=[trait.ToolOfTheState()],
                          requirements=[Requirement(
                              paths={('Student', 'Foundation Student', 'Volunteer Soldier'):1}),
                                        Requirement(paths={SECURITY_LIFEPATHS:1})])


class Media(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Media',
                          years=5,
                          resources=1,
                          circles=1,
                          skill_points=5,
                          skills=[skill.Journalism(),
                                  skill.Composition(),
                                  skill.Wise('Corruption'),
                                  skill.Wise('Skeletons')],
                          trait_points=1,
                          requirements=[Requirement(
                              paths = {('Foundation Student', 'Student'):1})])
                                
class Lawyer(CommuneLifepath):
    def __init__(self):                                
        Lifepath.__init__(self, name='Lawyer',
                          years=7,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          skill_points=5,
                          skills=[skill.CommunistLaw(), #not "Commune Law"
                                  skill.ImperialLaw(),
                                  skill.LeagueLaw(),
                                  skill.Oratory()],
                          trait_points=1,
                          traits=[trait.Calculating(),
                                  trait.LawObsessed()],
                          requirements=[Requirement(paths={('Psychologist',):1}),
                                        Requirement(paths={('Student', 'Clerk'):0})])

class Judge(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Judge',
                          years=8,
                          resources=2,
                          circles=1,
                          skill_points=4,
                          skills=[skill.Observation(),
                                  skill.UglyTruth(),
                                  skill.Amercement()],
                          trait_points=2,
                          traits=[trait.HardHearted(),
                                  trait.StrictConstructionist()],
                          general_skill_points=1,
                          requirements=[Requirement(
                              paths = {('Mandarin','Lawyer','Advocate'):1})])

class LocalOfficial(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Local Official',
                          years=6,
                          resources=1,
                          circles=1,
                          skill_points=4,
                          skills=[skill.Wise('Local Politics'),
                                  skill.Wise('Neighborhood'),
                                  skill.Wise('Problem')],
                          trait_points=1,
                          traits=[trait.PublicServant(),
                                  trait.Venal(),
                                  trait.Idealist()],
                          requirements=[Requirement(
                              paths = {('Clerk','Merchant','Mandarin','Bureaucrat','Courtier','Instructor','Law Enforcement'):1})])

class MunicipalOfficial(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Municipal Official',
                          years=6,
                          resources=1,
                          circles=1,
                          skill_points=4,
                          skills=[skill.Wise('Municipal Politics'),
                                  skill.Wise('City'),
                                  skill.Administration()],
                          trait_points=1,
                          traits=[trait.CityOfficial(),
                                  trait.GladHander()],
                          requirements=[Requirement(
                              paths = {('Lawyer', 'Local Official', 'Professional Officer'):1})])
      
class LegislativeOfficial(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Legislative Official',
                          years=4,
                          resources=2,
                          circles=2,
                          mental_points=1,
                          skill_points=5,
                          skills=[skill.Bureaucracy(),
                                  skill.Wise('Legislation'),
                                  skill.Oratory(),
                                  skill.Wise('Constituency')],
                          trait_points=1,
                          traits=[trait.Senator(),
                                  trait.Righteous(),
                                  trait.Bulldog(),
                                  trait.Mouthbreather()],
                          requirements=[Requirement(
                              paths = {('Lawyer', 'Local Official', 'Municipal Official'):1})])

class Financier(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Financier',
                          years=5,
                          resources=3,
                          circles=2,
                          skill_points=4,
                          skills=[skill.Finance(),
                                  skill.Wise('Money'),
                                  skill.Wise('Bribe')],
                          trait_points=1,
                          traits=[trait.WellHeeled(),
                                  trait.Savvy(),
                                  trait.Venal()],
                          general_skill_points=1,
                          requirements=[Requirement(
                              paths = {('Student',):1})])

class Governor(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Governor',
                          years=5,
                          resources=2,
                          circles=2,
                          skill_points=5,
                          skills=[skill.Wise('Province'),
                                  skill.Administration(),
                                  skill.Wise('Budget'),
                                  skill.Wise('Deal')],
                          trait_points=1,
                          traits=[trait.PublicFace(),
                                  trait.Gracious()],
                          general_skill_points=1,
                          requirements=[Requirement(
                              paths = {('Municipal Official', 'Legislative Official'):1})])

class AppointedOfficial(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Appointed Official',
                          years=4,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          skill_points=5,
                          skills=[skill.Bureaucracy(),
                                  skill.Logistics(),
                                  skill.Persuasion(),
                                  skill.Wise('Balance of Power')],
                          trait_points=1,
                          traits=[trait.PickedMan(),
                                  trait.Mover(),
                                  trait.LameDuck()],
                          general_skill_points=1,
                          requirements=[Requirement(
                              paths = {('Governor', 'Financier', 'Judge', 'Legislative Official'):1})])

class Diplomat(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Diplomat',
                          years=5,
                          resources=2,
                          circles=2,
                          mental_points=1,
                          skill_points=6,
                          skills=[skill.Persuasion(),
                                  skill.Bargaining,
                                  skill.Wise('Faction'),
                                  skill.Wise('Back Room Deals')],
                          trait_points=2,
                          traits=[trait.WellTravelled()],
                          requirements=[Requirement(
                              paths = {('Governor', 'Financier', 'Legislative Official'):1})])

class Politico(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Politico',
                          years=5,
                          resources=2,
                          circles=1,
                          skill_points=5,
                          general_skill_points=1,
                          skills=[skill.Wise('Contributions'),
                                  skill.Wise('Merchant League'),
                                  skill.Wise('Skeletons'),
                                  skill.Wise('Media')],
                          trait_points=1,
                          traits=[trait.Ambitious(),
                                  trait.Corrupt(),
                                  trait.Determined()],
                          requirements=[Requirement(
                              paths = {('Lawyer', 'Financier', 'Judge'):1})])

class CabinetMember(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Cabinet Member',
                          years=4,
                          resources=2,
                          circles=2,
                          skill_points=6,
                          general_skill_points=1,
                          skills=[skill.Wise('Inner Circle'),
                                  skill.Wise('Commune'),
                                  skill.Wise('Department'),
                                  skill.Wise('Budget'),
                                  skill.CommunistLaw(),
                                  skill.Wise('Diplomacy')],
                          trait_points=1,
                          requirements=[Requirement(
                              paths = {('Diplomat', 'Governor','Appointed Official'):1})])

class ExecutiveOfficial(CommuneLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Executive Official',
                          years=4,
                          resources=2,
                          circles=2,
                          skill_points=7,
                          general_skill_points=2,
                          skills=[skill.Wise('Commune'),
                                  skill.Wise('Legislature'),
                                  skill.Wise('Cabinet'),
                                  skill.Wise('Imperial'),
                                  skill.Wise('League'),
                                  skill.Wise('Media')],
                          trait_points=1,
                          traits=[trait.SkeletonsInTheCloset()],
                          requirements=[Requirement(
                              paths = {('Legislative Official', 'Governor'):1})])

############ PSYCHOLOGIST FOUNDATIONS SETTING ############
class FoundationLifepath(Lifepath):
    pass

class Apprentice(FoundationLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Apprentice',
                          years=7,
                          resources=1,
                          mental_points=1,
                          skill_points=5,
                          skills=[skill.Meditation(),
                                  skill.Wise('Eremite'),
                                  skill.Wise('Remote Location'),
                                  skill.Wise('Cold'),
                                  skill.Begging(),
                                  skill.Persuasion()],
                          trait_points=1,
                          traits=[trait.BrightMark(),
                                  trait.Unwelcome(),
                                  trait.GiftOfAhmilahk()],
                          second_only=True)

class Novitiate(FoundationLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Novitiate',
                          years=8,
                          resources=1,
                          floater_points=1,
                          skill_points=5,
                          skills=[skill.Wise("Circle of 10,000"),
                                  skill.CloseCombat(),
                                  skill.Etiquette(),
                                  skill.Oratory(),
                                  skill.Wise('Psychologist')],
                          trait_points=1,
                          traits=[trait.BrightMark(),
                                  trait.Bastard()],
                          second_only=True,
                          requirements=[Requirement(          
                              traits = {(trait.MarkOfPrivilege(),):1})])
        
class FoundationStudent(FoundationLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Foundation Student',
                          years=8,
                          resources=1,
                          circles=1,
                          mental_points=1,
                          physical_points=1,
                          skill_points=8,
                          skills=[skill.Wise('Psychologist'),
                                  skill.Research(),
                                  skill.Rhetoric(),
                                  skill.History(),
                                  skill.AdvancedMathematics()],
                          trait_points=1,
                          traits=[trait.BrightMark()],
                          second_only=True)

class CircleOf10K(FoundationLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Circle of 10,000',
                          years=8,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          physical_points=1,
                          skill_points=7,
                          skills=[skill.Psychology(),
                                  skill.Strategy(),
                                  skill.Tactics(),
                                  skill.Command(),
                                  skill.Intimidation()],
                          trait_points=2,
                          traits=[trait.WarriorsCode(),
                                  trait.CoolHeaded(),
                                  trait.Codebreaker(),
                                  trait.AnvilTrained()],
                          once_only = True,
                          requirements=[Requirement(
                              paths = {('Novitiate', 'Inquisitor'):1})])
                                
class Psychologist(FoundationLifepath):
    def __init__(self):
        Lifepath.__init__(self,name='Psychologist',
                          years=6,
                          resources=1,
                          circles=1,
                          floater_points=1,
                          skill_points=7,
                          skills=[skill.Psychohistory(),
                                  skill.Persuasion(),
                                  skill.Conspicuous(),
                                  skill.Inconspicuous(),
                                  skill.Psychology()],
                          trait_points=2,
                          traits=[trait.ThePsychologistsCode(),
                                  trait.Fearless(),
                                  trait.Imperious(),
                                  trait.Vainglorious(),
                                  trait.Pharisaical(),
                                  trait.Codebreaker()],
                          requirements=[Requirement(
                              paths = {('Foundation Student', 'Apprentice'):1})])
                                
class Speaker(FoundationLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Speaker',
                          years=6,
                          resources=2,
                          circles=2,
                          mental_points=1,
                          skill_points=6,
                          skills=[skill.Administration(),
                                  skill.UglyTruth(),
                                  skill.SoothingPlatitudes(),
                                  skill.Wise('Apprentice'),
                                  skill.Wise('Student'),
                                  skill.Wise('Foundation')],
                          trait_points=2,
                          traits=[trait.EerilyConfident()],
                          requirements=[Requirement(
                              paths = {('Psychologist',):2})])

class FirstSpeaker(FoundationLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='First Speaker',
                          years=12,
                          resources=3,
                          circles=2,
                          skill_points=4,
                          general_skill_points=4,
                          skills=[skill.Oratory(),
                                  skill.Wise('Circle of 10,000'),
                                  skill.Wise('Speaker')],
                          trait_points=2,
                          traits=[trait.WeightOfTheGalaxy()],
                          requirements=[Requirement(
                              paths={('Speaker',):2})])

class Eremite(FoundationLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Eremite',
                          years=10,
                          resources=1,
                          mental_points=1,
                          trait_points=1,
                          traits=[trait.GarlicBreath(),
                                  trait.Lonely(),
                                  trait.Genius()],
                          general_skill_points=1,
                          not_third = True,
                          requirements=[Requirement(                              
                              paths = {('First Speaker', 'Apprentice', 'Mule'):1})])


############ SPACEFARER SETTING ############
class SpacefarerLifepath(Lifepath):
    pass

class BornSpacefarer(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Son of a Gun',
                          years=12,
                          resources=1,
                          trait_points=2,
                          traits=[trait.DistortionMonkey(),
                                  trait.Cynical(),
                                  trait.ChronicDepression(),
                                  trait.Distrustful()],
                          general_skill_points=2,
                          born=True)    
                                
class SpacefarerYeoman(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Yeoman',
                          years=3,
                          physical_points=1,
                          trait_points=1,
                          traits=[trait.Hazed(),
                                  trait.DistortionSickness(),
                                  trait.Bulldog()])

class ShipRigger(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Ship Rigger',
                          years=3,
                          physical_points=1,
                          trait_points=1,
                          traits=[trait.BlackFingernails()],
                          requirements=[Requirement(
                              paths = {('Yeoman',):1})])

class SpacefarerCook(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Cook',
                          years=5,
                          resources=1,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Strange()],
                          requirements=[Requirement(
                              paths = {('Yeoman',):1})])

class SenseRigger(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Sense Rigger',
                          years=3,
                          resources=1,
                          trait_points=2,
                          traits=[trait.LightSleeper()],
                          requirements=[Requirement(
                              paths = {('Yeoman',):1})])

class SigRigger(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Sig Rigger',
                          years=3,
                          resources=1,
                          mental_points=1,
                          trait_points=2,
                          traits=[trait.GoodListener()],
                          requirements=[Requirement(
                              paths = {('Yeoman',):1})])

class GunRigger(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Gun Rigger',
                          years=2,
                          resources=1,
                          physical_points=1,
                          trait_points=2,
                          traits=[trait.Alert()],
                          requirements=[Requirement(
                              paths = {('Yeoman',):1})])

class Pilot(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Pilot',
                          years=4,
                          resources=2,
                          floater_points=1,
                          trait_points=2,
                          traits=[trait.IllegalCrucis(),
                                  trait.Flyboy()],
                          requirements=[Requirement(paths = {('Yeoman',):2}),
                                        Requirement(paths={('Sense Rigger', 'Navigator'):1})])


class CargoMaster(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Cargo Master',
                          years=5,
                          resources=2,
                          circles=1,
                          trait_points=2,
                          traits=[trait.Shrewd(),
                                  trait.SelfSatisfied(),
                                  trait.Hungry()],
                          requirements=[Requirement(paths = {('Navigator',):1}),
                                        Requirement(paths={(SpacefarerLifepath,):2})])

class Doctor(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Doctor',
                          years=5,
                          resources=2,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Grim(), trait.Practical()],
                          requirements=[Requirement(
                              paths = {('Apprentice', 'Novitiate', 'Physician', 'Student'):1})])

class SpacefarerNavigator(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Navigator',
                          years=4,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          requirements=[Requirement(
                              traits = {(trait.CorvusAndCrucis(),
                                         trait.IllegalCrucis()):1})])

class ShipsEngineer(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name="Ship's Engineer",
                          years=6,
                          resources=2,
                          circles=1,
                          floater_points=1,
                          trait_points=2,
                          traits=[trait.Practical()],
                          requirements=[Requirement(
                              paths = {('Shipfitter', 'Ship Rigger', 'Machinist'):1})])

class Scientist(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Scientist',
                          years=5,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          trait_points=1,
                          traits=[trait.Curious()],
                          requirements=[Requirement(
                              paths = {("Ship's Engineer", 'Physicist', 'Navigator'):1})])

class SpacefarerFirstOfficer(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='First Officer',
                          years=5,
                          resources=1,
                          circles=1,
                          mental_points=1,
                          trait_points=1,
                          traits=[trait.Undeterred()],
                          requirements=[Requirement(
                              paths = {('Lieutenant','Hammer Master','Discipline Officer','Navigator','Physicist','Scientist','Cargo Master',"Ship's Engineer"):1})])

class ShipsCaptain(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name="Ship's Captain",
                          years=6,
                          resources=2,
                          circles=1,
                          trait_points=2,
                          traits=[trait.Aloof(),
                                  trait.Privateer(),
                                  trait.OwnerAboard(),
                                  trait.WellKnown()],
                          general_skill_points=1,
                          requirements=[Requirement(
                              paths = {('First Officer', 'Psychologist', 'Lord-Pilot Hammer'):1})])

class OwnerAboard(SpacefarerLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Owner-Aboard',
                          years=4,
                          resources=2,
                          circles=1,
                          floater_points=1,
                          trait_points=2,
                          traits=[trait.MyShipMyRules(),
                                  trait.Uneasy(),
                                  trait.Dashing()],
                          general_skill_points=2)
    def allowed(self, character):
        return False

############ FREEMAN SETTING ############
class FreemanLifepath(Lifepath):
    pass

class BornFreeman(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Born to Freeman',
                          years=10,
                          trait_points=1,
                          traits=[trait.WorkingClass(),
                                  trait.Morose(),
                                  trait.Sullen(),
                                  trait.Troubled()],
                          general_skill_points=3,
                          born=True)
    
class Kid(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Kid',
                          years=4,
                          trait_points=2,
                          traits=[trait.GoodForNothing(), trait.BadEgg()],
                          second_only = True,
                          once_only = True)
    
class FreemanStudent(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Student',
                          years=6,
                          circles=1,
                          trait_points=2,
                          traits=[trait.BruisedEyes(), trait.Rebel()])
    
class LazyStayabout(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Lazy Stayabout',
                          years=4,
                          trait_points=1,
                          traits=[trait.Laconic(), trait.Pudgy()])


class Peddler(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Peddler',
                          years=5,
                          resources=1,
                          trait_points=2,
                          traits=[trait.Odd()])

class FreemanCourier(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Courier',
                          years=4,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Late()])

class Laborer(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Laborer',
                          years=4,
                          resources=1,
                          trait_points=2,
                          traits=[trait.Proud(),
                                  trait.Drunk(),
                                  trait.WifeBeater()])

class Pilgrim(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Pilgrim',
                          years=2,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Stinky()])

class Functionary(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Functionary',
                          years=4,
                          resources=1,
                          trait_points=1,
                          traits=[trait.CrushingBoredom()],
                          requirements=[Requirement(
                              paths = {('Student', 'Foundation Student'):1})])

class ServiceWorker(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Service Worker',
                          years=3,
                          resources=1,
                          trait_points=1,
                          traits=[trait.Abused(),
                                  trait.Hater()])

class Parent(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Parent',
                          years=8,
                          resources=1,
                          circles=1,
                          trait_points=2,
                          traits=[trait.RawNerved()],
                          not_second = True)
    
class Driver(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Driver',
                          years=4,
                          resources=1,
                          circles=1,
                          trait_points=1,
                          traits=[trait.SleepDisorder()],
                          not_second = True)

class Hosteler(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Hosteler',
                          years=6,
                          resources=2,
                          circles=1,
                          requirements=[Requirement(
                              paths = {('Parent', 'Shopkeeper', 'Cargo Master', 'Hammer Master', 'Smuggler'):1})])

class Shopkeeper(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Shopkeeper',
                          years=6,
                          resources=2,
                          circles=1,
                          trait_points=1,
                          traits=[trait.ThisIsAStoreNotALibrary(),
                                  trait.FriendlyFace(),
                                  trait.Mean()],
                          requirements=[Requirement(
                              paths = {('Smuggler', 'Criminal', 'Parent', 'Driver', 'Lazy Stayabout', 'Service Worker'):1})])

class Fabricator(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Fabricator',
                          years=5,
                          resources=2,
                          trait_points=1,
                          traits=[trait.ScarredHands(),
                                  trait.Clever()],
                          requirements=[Requirement(
                              paths = {('Student', 'Laborer'):1})])

class ApprenticeCraftsman(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Apprentice Craftsman',
                          years=6,
                          trait_points=1,
                          traits=[trait.Resigned()])

class Craftsman(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Craftsman',
                          years=7,
                          resources=2,
                          circles=1,
                          floater_points=1,
                          trait_points=1,
                          traits=[trait.ProfessionalPride()],
                          requirements=[Requirement(
                              paths = {('Apprentice Craftsman',):1})])

class Trader(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Trader',
                          years=6,
                          resources=2,
                          circles=2,
                          mental_points=1,
                          trait_points=1,
                          traits=[trait.OpenMinded(),
                                  trait.PennyWise(),
                                  trait.WellTravelled()],
                          requirements=[Requirement(
                              paths = {('Shopkeeper', 'Hosteler', 'Manufacturer', 'Craftsman', 'Traveler'):1})])

class Engineer(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Engineer',
                          years=7,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          trait_points=1,
                          traits=[trait.Practical(),
                                  trait.Erudite()],
                          requirements=[Requirement(paths={('Student','Fabricator'):0}),
                                        Requirement(paths={('Craftsman',):1})])

    
class Manufacturer(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Manufacturer',
                          years=8,
                          resources=3,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Automator(),
                                  trait.ThinkBig()],
                          requirements=[Requirement(
                              paths = {('Trader', 'Engineer', 'Craftsman'):1})])

class Artisan(FreemanLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Artisan',
                          years=10,
                          resources=3,
                          circles=1,
                          floater_points=1,
                          trait_points=2,
                          traits=[trait.SteadyHands(),
                                  trait.Genius()],
                          requirements=[Requirement(
                              paths = {('Engineer',):1})])

############ SETTING ############
class SlaveLifepath(Lifepath):
    pass

class BornSlave(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Born Slave',
                          years=8,
                          trait_points=1,
                          traits=[trait.DestinedForSlavery(),
                                  trait.Beaten(),
                                  trait.Resigned(),
                                  trait.Despondent(),
                                  trait.Bleak()],
                          general_skill_points=2,
                          born=True)

class SlaveLabor(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Slave Labor',
                          years=6,
                          trait_points=1,
                          traits=[trait.Whipped()])
        
class SentencedCriminal(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Sentenced Criminal',
                          years=5,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Bitter(),
                                  trait.Vindictive()])
        
class MigrantLabor(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Migrant Labor',
                          years=4,
                          resources=1,
                          trait_points=1,
                          traits=[trait.Exhausted(),
                                  trait.Wanderlust()])
        
class TenantLabor(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Tenant Labor',
                          years=6,
                          resources=1,
                          trait_points=1,
                          traits=[trait.Earnest()])
        
class Prostitute(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Prostitute',
                          years=4,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Tolerant(),
                                  trait.Abused(),
                                  trait.Broken()])
        
class SlaveJockey(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Slave Jockey',
                          years=3,
                          trait_points=2,
                          traits=[trait.SlightBuild(),
                                  trait.ResignedToDeath()])
        
class Clown(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Clown',
                          years=4,
                          circles=1,
                          trait_points=2,
                          traits=[trait.WreckedSelfEsteem(),
                                  trait.Ennui(),
                                  trait.Garbo()])
        
class Footman(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Footman',
                          years=5,
                          resources=1,
                          trait_points=2,
                          traits=[trait.Bored(),
                                  trait.Sickly()])
        
class Servant(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Servant',
                          years=6,
                          resources=1,
                          circles=1,
                          trait_points=2,
                          traits=[trait.Deferential(),
                                  trait.Humble(),
                                  trait.Arrogant(),
                                  trait.Murderous()],
                          requirements=[Requirement(
                              paths={(SlaveLifepath,):1})])
        
class CaptiveOfWar(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Captive of War',
                          years=3,
                          trait_points=2,
                          traits=[trait.Captured(),
                                  trait.Broken(),
                                  trait.Defiant(),
                                  trait.Bitter()],
                          requirements=[Requirement(paths={('Volunteer Soldier', 'Freebooter', 'Pirate'):1}),
                                        Requirement(paths={(AnvilLifepath,HammerLifepath,NobleLifepath):1})])

class Bondsman(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Bondsman',
                          years=6,
                          resources=1,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Lucky()],
                          requirements=[Requirement(
                              paths={(SlaveLifepath,):1})])

class Taskmaster(SlaveLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Taskmaster',
                          years=5,
                          resources=1,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Brutal(),
                                  trait.HardHearted()],
                          requirements=[Requirement(paths={SECURITY_LIFEPATHS:1}),
                                        Requirement(paths={('First Officer','Criminal','Hive Thug','Duelist','Kidnapper','Boxer'):1}),
                                        Requirement(paths={SOLDIER_LIFEPATHS:1}),
                                        Requirement(paths={(SlaveLifepath,):4})])


############ OUTCAST AND CRIMINAL SETTING ############
class OutcastLifepath(Lifepath):
    pass

class BornOutcast(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Born on the Streets',
                          years=9,
                          circles=1,
                          trait_points=2,
                          traits=[trait.Orphan(),
                                  trait.Worried(),
                                  trait.Distrustful(),
                                  trait.Dark()],
                          general_skill_points=3,
                          born=True)
    
class AlienMutantFreak(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Alien Mutant Freak',
                          years=4,
                          floater_points=1,
                          trait_points=2,
                          traits=[trait.Deformed(),
                                  trait.FuurBlood(),
                                  trait.Martyr(),
                                  trait.Prophet()],
                          second_only=True)
                                
class Mule(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Mule',
                          years=4,
                          mental_points= 1,
                          trait_points=2,
                          traits=[trait.Mule(),
                                  trait.Cunning()])


class Urchin(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Urchin',
                          years=4,
                          trait_points=2,
                          traits=[trait.Addicted()],
                          second_only=True)

class Cripple(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Cripple',
                          years=4,
                          trait_points=1,
                          traits=[trait.Mangled()])
        
class Deranged(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Deranged',
                          years=5,
                          trait_points=1,
                          traits=[trait.Sickly(),
                                  trait.Dirty()])

class FilthyWormLover(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Filthy Worm Lover',
                          years=4,
                          mental_points=1,
                          trait_points=2,
                          traits=[trait.Blacklisted(),
                                  trait.WronglyAccused()])
    def allowed(self, character):
        return False

class MatchstickGirl(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Matchstick Girl',
                          years=5,
                          trait_points=1,
                          traits=[trait.AuraOfInnocence(),
                                  trait.TheStory()])

class Beggar(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Beggar',
                          years=4,
                          trait_points=2,
                          traits=[trait.Downtrodden(),
                                  trait.Broken(),
                                  trait.Hurt(),
                                  trait.Mangled()])

class Vagrant(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Vagrant',
                          years=5,
                          trait_points=1)

class Pickpocket(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Pickpocket',
                          years=4,
                          resources=1,
                          circles=1,
                          trait_points=1,
                          traits=[trait.PlainFace(),
                                  trait.Flamboyant()],
                          requirements=[Requirement(
                              paths = {('Urchin', 'Cripple', 'Vagrant', 'Beggar'):1})])
    
class Mummer(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Mummer',
                          years=4,
                          circles=1,
                          mental_points=1,
                          trait_points=2,
                          traits=[trait.Odd()])

class BeggarKing(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Beggar King',
                          years=6,
                          resources=2,
                          circles=2,
                          floater_points=1,
                          trait_points=1,
                          requirements=[Requirement(paths={('Beggar',):0,('Mummer', 'Urchin','Pickpocket', 'Deranged', 'Cripple'):1}),
                                        Requirement(paths={('Rebel Priest',):1})
                                        ])

class Acrobat(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Acrobat',
                          years=4,
                          resources=1,
                          trait_points=1,
                          traits=[trait.Contortionist()])
        
class Cultist(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Cultist',
                          years=4,
                          circles=1,
                          trait_points=2,
                          traits=[trait.Zealot(),
                                  trait.RabbleRouser(),
                                  trait.SpeakerOfTheSecretLanguage()])

class RebelPriest(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Rebel Priest',
                          years=5,
                          resources=2,
                          circles=2,
                          mental_points=1,
                          trait_points=2,
                          traits=[trait.StrangeAirs(),
                                  trait.Cultist(),
                                  trait.Heretic(),
                                  trait.Lunatic(),
                                  trait.Fiery(),
                                  trait.GooglyEyes()],
                          general_skill_points=1,
                          requirements=[Requirement(paths={('Cotar', 'Philosopher', 'Thinker'):1}),
                                        Requirement(paths={('Cultist',):2})])

        
class HiveThug(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Hive Thug',
                          years=3,
                          resources=1,
                          circles=1,
                          physical_points=1,
                          trait_points=1,
                          traits=[trait.ColdBlooded()],
                          not_second = True)

class Freebooter(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Freebooter',
                          years=3,
                          resources=1,
                          circles=1,
                          floater_points=1,
                          trait_points=1,
                          traits=[trait.Mercenary()],
                          requirements=[Requirement(paths={('Desperate Killer', 'Pirate', 'Smuggler', 'Circle of 10,000'):1}),
                                        Requirement(paths={SOLDIER_LIFEPATHS:1})])


class DesperateKiller(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Desperate Killer',
                          years=3,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Desperate()],
                          requirements = [Requirement(paths={SOLDIER_LIFEPATHS:1})])

class Insurrectionist(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Insurrectionist',
                          years=4,
                          circles=1,
                          mental_points=1,
                          trait_points=2,
                          traits=[trait.Rebel(),
                                  trait.Royalist(),
                                  trait.Democrat(),
                                  trait.Militant(),
                                  trait.Anarchist()])

class Outlaw(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Outlaw',
                          years=4,
                          circles=1,
                          mental_points=1,
                          trait_points=2,
                          traits=[trait.Outlaw()])

class ConfidenceMan(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Confidence Man',
                          years=3,
                          resources=1,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Swindler(),
                                  trait.PathologicalLiar(),
                                  trait.Logorrhea()],
                          requirements=[Requirement(
                              paths={(OutcastLifepath,SlaveLifepath,CommuneLifepath,FreemanLifepath):1})])

class Pirate(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Pirate',
                          years=4,
                          circles=1,
                          trait_points=2,
                          traits=[trait.ScumOfTheGalaxy(),
                                  trait.Insane(),
                                  trait.FunnyAccent(),
                                  trait.ColdBlooded()],
                          requirements=[Requirement(
                              paths={(SpacefarerLifepath, HammerLifepath):1})])

class Duelist(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Duelist',
                          years=3,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Loathed(),
                                  trait.Brave(),
                                  trait.Stupid(),
                                  trait.Suicidal(),
                                  trait.Mangled()],
                          requirements=[Requirement(
                              paths = {('Desperate Killer', 'Freebooter', 'Boxer', 'Alien Mutant Freak', 'Hive Thug'):1})])

class Boxer(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Boxer',
                          years=3,
                          resources=1,
                          circles=1,
                          physical_points=1,
                          trait_points=1,
                          traits=[trait.Showboat(),
                                  trait.HatPasser()],
                          requirements=[Requirement(paths={('Born on the Streets',):1}),
                                        Requirement(paths={(AnvilLifepath,):1})])

class Kidnapper(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Kidnapper',
                          years=3,
                          resources=1,
                          circles=1,
                          trait_points=1,
                          traits=[trait.SlightlyWarped(),
                                  trait.Feckless(),
                                  trait.HardHearted()])

class Blackmailer(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Blackmailer',
                          years=4,
                          resources=1,
                          circles=1,
                          trait_points=1,
                          traits=[trait.Scheming(),
                                  trait.Bungler(),
                                  trait.Clinical(),
                                  trait.NoNonsense()])

class Breaker(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Breaker', years=5,
                          resources=2,
                          floater_points=1,
                          trait_points=2,
                          traits=[trait.HommeDur(),
                                  trait.ManOfFewWords(), trait.
                                  AffinityForLocks()],
                          requirements=[Requirement(paths={SECURITY_LIFEPATHS:1}),
                                        Requirement(paths={(OutcastLifepath,):2})])

class Smuggler(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Smuggler',
                          years=5,
                          resources=2,
                          circles=1,
                          trait_points=2,
                          traits=[trait.CoolHeaded(),
                                  trait.Alert(),
                                  trait.Unglued(),
                                  trait.Useful()],
                          requirements=[Requirement(
                              paths={(OutcastLifepath,SpacefarerLifepath,HammerLifepath,AnvilLifepath):1})])

class Counterfeiter(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Counterfeiter',
                          years=5,
                          resources=2,
                          circles=1,
                          mental_points=1,
                          trait_points=1,
                          traits=[trait.EyeForDetail(),
                                  trait.Nimble(),
                                  trait.EideticMemory()],
                          requirements=[Requirement(paths={('Banker', 'Shopkeeper', 'Functionary', 'Financier', 'Merchant'):1}),
                                        Requirement(paths={(OutcastLifepath,):2})])
    
class Fence(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Fence',
                          years=6,
                          resources=2,
                          circles=1,
                          floater_points=1,
                          trait_points=2,
                          traits=[trait.Shrewd(),
                                  trait.NoNonsense(),
                                  trait.SharpDresser()],
                          requirements=[Requirement(
                              paths = {('Smuggler', 'Counterfeiter', 'Breaker', 'Shopkeeper', 'Merchant', 'Cargo Master', 'Hammer Master'):1})])

class Whoremonger(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Whoremonger',
                          years=4,
                          resources=2,
                          circles=1,
                          trait_points=1,
                          traits=[trait.LifeUnderADifferentCode(),
                                  trait.Colorful(),
                                  trait.CasuallyViolent()],
                          requirements=[Requirement(
                              paths = {('Kidnapper', 'Cargo Master', 'Hammer Master', 'Smuggler'):1})])

class Gunsel(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Gunsel',
                          years=3,
                          resources=1,
                          circles=1,
                          floater_points=1,
                          trait_points=2,
                          traits=[trait.LoyalToTheFamily(),
                                  trait.TallDarkAndMurderous(),
                                  trait.ShutUp(),
                                  trait.WeRuleTheseStreets()],
                          requirements=[Requirement(paths={('Hive Thug',):2}),
                                        Requirement(paths={('Sergeant','Man-at-Arms','Volunteer Soldier','Desperate Killer','Boxer','Duelist','Freebooter','Taskmaster'):1})])
                                
class Criminal(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Criminal',
                          years=5,
                          resources=2,
                          circles=2,
                          floater_points=1,
                          trait_points=2,
                          traits=[trait.Family(),
                                  trait.Vig(),
                                  trait.SharpDresser()],
                          requirements=[Requirement(paths={('Gunsel', 'Advocate', 'Mandarin', 'Lawyer', 'Politico', 'League Official', 'Psychologist'):1}),
                                        Requirement(paths={('Kidnapper', 'Blackmailer', 'Whoremonger', 'Fence', 'Counterfeiter', 'Breaker', 'Smuggler'):2})])


class Thinker(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Thinker',
                          years=8,
                          mental_points=1,
                          trait_points=2,
                          traits=[trait.Bearded(),
                                  trait.Ideologue()],
                          general_skill_points=1,
                          requirements=[Requirement(age = 30)])
    
class Traveler(OutcastLifepath):
    def __init__(self):
        Lifepath.__init__(self, name='Traveler',
                          years=5,
                          resources=3,
                          circles=1,
                          trait_points=2,
                          traits=[trait.Optimist(),
                                  trait.Shrewd(),
                                  trait.AffinityForTrade(),
                                  trait.IllegalCrucis(),
                                  trait.AffinityForTechnology()],
                          general_skill_points=1,
                          requirements=[Requirement(
                              paths = {('Trader', 'Fence', 'Criminal', 'Merchant', 'Physicist', 'Scientist', 'First Officer', "Ship's Captain"):1})])

#requirements constants
SECURITY_LIFEPATHS = ('Discipline Officer', 'Stormtrooper', 'Security', 'Security Officer', 'Man-at-Arms', 'Law Enforcement', 'Breaker', 'Justiciar', 'Adjutant Inquisitor', 'Coroner', 'Constable')
ENGINEER_LIFEPATHS = ('Engineer', "Ship's Engineer", 'Hammer Engineer', 'Anvil Engineer')
SOLDIER_LIFEPATHS = ('Coeptir','Court Coeptir','Court Armiger','Man-at-Arms','Soldier','Lieutenant','Anvil Elite','Sodalis', 'Volunteer Soldier', 'Freebooter')

