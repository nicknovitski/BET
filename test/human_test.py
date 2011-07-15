import unittest
from character.exceptions import NotAllowed 
from character.human import *
from character import trait 

class HumanLifePathTests(unittest.TestCase):
    def setUp(self):
        """Defines a bunch of standard characters used in multiple tests
        """
        self.young_noble = Human([BornNobility()])
        self.character_two = Human([BornNobility(), CourtCoeptir()])
        self.character_three = Human([BornNobility(), CourtCoeptir(), NobleArmiger()])

        self.hammer_cook = Human([BornSpacefarer(), HammerYeoman(), HammerCook()])
        self.armiger = Human([BornNobility(), NobleCoeptir(), NobleArmiger()])
        self.court_armiger = Human([BornNobility(), Novitiate(), CourtArmiger()])
        self.magnate = Human([BornLeague(), LeagueStudent(), Merchant(), Magnate()])
        self.sergeant = Human([BornSlave(), Soldier(), Sergeant()])
        self.circle_of_10k = Human([BornTheocracy(), DevotedToFire(), Cotar(), AdjutantInquisitor(), Inquisitor(), CircleOf10K()])
        self.student= Human([BornCommune(), CommuneStudent()])
        self.chamberlain = Human([BornCommune(), CommuneStudent(), Mandarin(), Constable(), Justiciar(), Chamberlain()])
        self.man_at_arms_sol = Human([BornSpacefarer(), HammerYeoman(), HammerCook(), DisciplineOfficer(), ManAtArms()])
        self.taskmaster = Human([BornOutcast(), Mummer(), HiveThug(), Taskmaster()])
        self.foundation_student = Human([BornLeague(), FoundationStudent()])
        self.psychologist = Human([BornSlave(), Apprentice(), Psychologist()])
        self.space_cook = Human([BornSpacefarer(), SpacefarerYeoman(), SpacefarerCook()])
        self.navigator = Human([BornLeague(), Bastard(), Companion()]).buy_trait(trait.IllegalCrucis()).add_path(SpacefarerNavigator())
        self.volunteer_soldier = Human([BornFreeman(), Acrobat(), Clown(), VolunteerSoldier()])
        self.companion = Human([BornNobility(), Companion()])
        self.court_coeptir = Human([BornNobility(), CourtCoeptir()])
        self.coeptir = Human([BornNobility(), NobleCoeptir()])
        self.soldier = Human([BornSlave(), Soldier()])
        self.lieutenant = Human([BornNobility(), Novitiate(), Lieutenant()])
        self.freebooter = Human([BornOutcast(), Mummer(), Smuggler(), Freebooter()])
        self.anvil_elite = Human([BornOutcast(), Apprentice(), Psychologist(), AnvilElite()])
        self.sodalis = Human([BornTheocracy(),DevotedToFire(), Sodalis()])
        self.pirate = Human([BornSpacefarer(), SpacefarerYeoman(), Pirate()])
        self.merchant = Human([BornLeague(), LeagueStudent(), Merchant()])
        self.financier = Human([BornCommune(), CommuneStudent(), Financier()])

        self.discipline_officer = Human([BornSpacefarer(), HammerYeoman(), HammerCook(), DisciplineOfficer()])
        self.stormtrooper = Human([BornNobility(), Novitiate(), CircleOf10K(), Stormtrooper()])
        self.security = Human(starting_paths=[BornNobility()], age = 18).add_path(Security())
        self.security_officer = Human([BornLeague(), Soldier(), Sergeant(), SecurityOfficer()])
        self.law_enforcement = Human([BornCommune(), CommuneStudent(), LawEnforcement()])
        self.man_at_arms_sec = Human([BornTheocracy(), DevotedToFire(), Sodalis(), ManAtArms()])
        self.breaker = Human([BornOutcast(), AlienMutantFreak(),Mule(), Breaker()])
        self.justiciar = Human([BornCommune(), CourtClerk(), Mandarin(), Justiciar()])
        self.adjutant_inquisitor = Human([BornNobility(), DevotedToFire(), Mystes()])
        self.adjutant_inquisitor.buy_trait(trait.YourLordship())
        self.adjutant_inquisitor.add_path(Cotar()).add_path(AdjutantInquisitor())
        self.coroner = Human([BornNobility(), CourtClerk(), Mandarin(), Coroner()])
        self.constable = Human([BornCommune(), CourtClerk(), Mandarin(), Constable()])
        #(1) all lifepaths with security in their name,
        #(2) with the security, security rigging, investigative logic or interrogation skills
        self.security_characters = [self.discipline_officer,
                                    self.stormtrooper,
                                    self.security,
                                    self.security_officer,
                                    self.man_at_arms_sec,
                                    self.law_enforcement,
                                    self.breaker,
                                    self.justiciar,
                                    self.adjutant_inquisitor,
                                    self.coroner,
                                    self.constable]
        
        self.duelist = Human([BornOutcast(), AlienMutantFreak(), Duelist()])
        self.hive_thug = Human([BornFreeman(), Urchin(), HiveThug()])
        self.kidnapper = Human([BornNobility(), Kidnapper()])
        self.boxer = Human([BornOutcast(), Boxer()])
        self.gunsel = Human([BornOutcast(), Mummer(), HiveThug(), Taskmaster(), Gunsel()])
        
        #Grunts, not commanders
        self.soldier_characters = [self.coeptir,
                                   self.court_coeptir,
                                   self.court_armiger,
                                   self.man_at_arms_sol,
                                   self.soldier,
                                   self.lieutenant,
                                   self.anvil_elite,
                                   self.sodalis,
                                   self.volunteer_soldier,
                                   self.freebooter]
    def testSoldierUniques(self):
        """test to make sure none of the testing soldier characters use more than one path
        """
        SOLDIER_LIFEPATHS = ('Coeptir','Court Coeptir','Court Armiger','Man-at-Arms','Soldier','Lieutenant','Anvil Elite','Sodalis', 'Volunteer Soldier', 'Freebooter')
        for character in self.soldier_characters:
            for path in SOLDIER_LIFEPATHS:
                character.remove_path()
                self.assertFalse(character.has_taken(path))
    def testSecurityUniques(self):
        """test to make sure none of the testing soldier characters use more than one path
        """
        SECURITY_LIFEPATHS = ('Discipline Officer', 'Stormtrooper', 'Security', 'Security Officer', 'Man-at-Arms', 'Law Enforcement', 'Breaker', 'Justiciar', 'Adjutant Inquisitor', 'Coroner', 'Constable')
        for character in self.security_characters:
            for path in SECURITY_LIFEPATHS:
                character.remove_path()
                self.assertFalse(character.has_taken(path))
    def testBorn(self):
        """A born lifepath should:
        1. Always be allowed if no other lifepaths have been taken
        2. Never be allowed if any other lifepaths have been taken
        """
        BORN = [BornNobility(), BornTheocracy(), BornLeague(),
                     BornCommune(), BornSpacefarer(), BornFreeman(),
                     BornSlave(), BornOutcast()]
        for x in BORN:
            self.assertTrue(x.allowed(Human()))
            self.assertFalse(x.allowed(self.young_noble))
            self.assertRaises(NotAllowed, self.young_noble.add_path, x)
            self.assertTrue(x in Human().allowed_paths())

    def testRequiresPath(self):
        """The most common requirement for a lifepath is that the character have taken any one of a list of lifepaths.
        For example: Lord-Pilot Anvil requires Armiger, Court Armiger or Magnate
        """
        self.assertFalse(NobleLPAnvil().allowed(self.young_noble))
        self.assertRaises(NotAllowed, self.young_noble.add_path, NobleLPAnvil())
        
        self.assertFalse(NobleLPAnvil().allowed(self.character_two))
        self.assertRaises(NotAllowed, self.character_two.add_path, NobleLPAnvil())
        
        self.assertTrue(NobleLPAnvil().allowed(self.character_three))
        self.assertTrue(NobleLPAnvil() in self.character_three.allowed_paths())
        
    def testOnlyCanTakeOnce(self):
        """These lifepaths should never be allowed if they have been taken once already.

        Bastard and Kid can only be taken second, which also precludes them from being taken twice.
        """
        ONLY_ONCE = [Bastard(), Companion(), CircleOf10K(), Kid()]
        for x in ONLY_ONCE:
            char = Human([BornNobility()])
            if x == CircleOf10K():
                char.add_path(Novitiate())
                self.assertTrue(CircleOf10K().allowed(char))
                self.assertTrue(CircleOf10K() in char.allowed_paths())
                char.add_path(CircleOf10K())
                self.assertFalse(CircleOf10K().allowed(char))
                self.assertRaises(NotAllowed, char.add_path, CircleOf10K())
                char.remove_path()
            else:
                char.add_path(x)
                self.assertFalse(x.allowed(char))
                self.assertRaises(NotAllowed, char.add_path, x)

    def testSecondLifePathOnly(self):
        """These lifepaths should never be allowed if the character has not taken exactly one lifepath.
        """
        ONLY_SECOND = [NobleCoeptir(), HammerCoeptir(), Bastard(),
                            CourtCoeptir(), Apprentice(), Novitiate(),
                            FoundationStudent(), Kid(), AlienMutantFreak(),
                            Urchin()]
        for x in ONLY_SECOND:
            self.assertFalse(x.allowed(Human()))
            self.assertRaises(NotAllowed, Human().add_path, x)
            
            self.assertFalse(x.allowed(self.character_two))
            self.assertRaises(NotAllowed, self.character_two.add_path, x)

    def testSecondOrThirdLifePathOnly(self):
        """These lifepaths should never be allowed if the character has taken less than one or more than two lifepaths

        Companion can only be taken once, which means it cannot be taken both second and third.  Otherwise, this is allowed.
        """
        SECOND_OR_THIRD = [Companion()]
        for x in SECOND_OR_THIRD:
            self.assertFalse(x.allowed(Human()))
            self.assertRaises(NotAllowed, Human().add_path, x)
            
            self.assertFalse(x.allowed(self.character_three))
            self.assertRaises(NotAllowed, self.character_three.add_path, x)
            
    def testNotSecondPath(self):
        """These lifepaths should never be allowed if that character has taken exactly one lifepath.
        """
        NOT_SECOND = [Parent(), Driver(), HiveThug()]
        for x in NOT_SECOND:
            self.assertFalse(x.allowed(self.young_noble))
            self.assertRaises(NotAllowed, self.young_noble.add_path, x)

    def testNotThirdPath(self):
        """These lifepaths should never be allowed if the character has taken exactly two lifepaths
        """
        NOT_THIRD = [Eremite()]
        for x in NOT_THIRD:
            self.assertFalse(x.allowed(Human([BornNobility(), Apprentice()])))
            self.assertRaises(NotAllowed, Human([BornNobility(), Apprentice()]).add_path, x)

    def testAgeRequirements(self):
        """These lifepaths should never be allowed if the character's age is less than the specified minimum
        """
        REQ_AGE = {Thinker():30,Security():18,VolunteerSoldier():17}
        for path, min_age in REQ_AGE.iteritems():
            starting_age = min_age - BornTheocracy().years
            self.assertTrue(path.allowed(Human([BornTheocracy()], age = starting_age)))
            too_young_to_begin_the_training = min_age-BornTheocracy().years-1
            self.assertFalse(path.allowed(Human([BornTheocracy()], age = too_young_to_begin_the_training)))
            self.assertRaises(NotAllowed, Human([BornTheocracy()], age = too_young_to_begin_the_training).add_path, path)

    def testRequiresMarkOfPrivilege(self):
        """These lifepaths should never be allowed if the character does not have the trait 'Mark of Privilege'
        """
        REQ_MOP = [NobleCoeptir(), Hostage(), HammerCoeptir(), Novitiate()]
        slave = Human([BornSlave()])
        strange_slave = Human([BornSlave()], traits=[trait.MarkOfPrivilege()])
        for x in REQ_MOP:
            self.assertTrue(x.allowed(strange_slave))
            self.assertFalse(x.allowed(slave))
            self.assertRaises(NotAllowed, slave.add_path, x)
            
    def testRequiresEminenceOrGrace(self):
        """These lifepaths should never be allowed if the character does not have either:
        1. The trait 'Your Eminence'
        2. The trait 'Your Grace'
        """
        REQ_EM_GRA = [Archcotare()]
        young_baron_or_count = Human([BornNobility()], traits = [trait.YourEminence()])
        young_baron_or_count.add_path(DevotedToFire())
        young_baron_or_count.add_path(Cotar())
        young_baron_or_count.add_path(Dregus())
        young_duke_or_prince = Human([BornNobility()], traits = [trait.YourGrace()])
        young_duke_or_prince.add_path(DevotedToFire())
        young_duke_or_prince.add_path(Cotar())
        young_duke_or_prince.add_path(Dregus())
        self.young_noble.add_path(DevotedToFire()).add_path(Cotar()).add_path(Dregus())
        for path in REQ_EM_GRA:
            self.assertTrue(path.allowed(young_baron_or_count))
            self.assertTrue(path.allowed(young_duke_or_prince))
            self.assertFalse(path.allowed(self.young_noble))
            self.assertRaises(NotAllowed, self.young_noble.add_path, path)

    def testRequiresGraceOrMajesty(self):
        """These lifepaths should never be allowed if the character does not have either:
        1. The trait 'Your Grace'
        2. The trait 'Your Majesty'
        """
        REQ_GRA_MAJ = [CotarAntistes()]
        young_duke_or_prince = Human([BornNobility()], traits = [trait.YourGrace()])
        young_emperor = Human([BornNobility()], traits = [trait.YourMajesty()])
        self.young_noble.add_path(DevotedToFire()).add_path(Cotar()).add_path(Dregus())
        for path in REQ_GRA_MAJ:
            self.assertTrue(path.allowed(young_emperor.add_path(DevotedToFire()).add_path(Cotar()).add_path(Dregus())))
            self.assertTrue(path.allowed(young_duke_or_prince.add_path(DevotedToFire()).add_path(Cotar()).add_path(Dregus())))
            self.assertFalse(path.allowed(self.young_noble))
            self.assertRaises(NotAllowed, self.young_noble.add_path, path)
            
    def testNotNoble(self):
        """These lifepaths should never be allowed if the character has any of:
        1. The trait 'Your Lordship'
        2. The trait 'Your Grace'
        3. The trait 'Your Eminence'
        4. The trait 'Your Majesty'

        I don't know if it should include 'Mark of Privilege'
        """
        BARRED_NOBLE = [Stentor(), Duenna()]
        young_duke_or_prince = Human([BornNobility()], traits = [trait.YourGrace()])
        young_emperor = Human([BornNobility()], traits = [trait.YourMajesty()])
        young_baron_or_count = Human([BornNobility()], traits = [trait.YourEminence()])
        young_lord = Human([BornNobility()], traits = [trait.YourLordship()])
        princelings = [young_duke_or_prince, young_emperor, young_baron_or_count, young_lord]

        self.young_noble.add_path(Companion())
        for x in princelings:
            x.add_path(Companion())
        self.assertTrue(Duenna().allowed(self.young_noble))
        for character in princelings:
            self.assertFalse(Duenna().allowed(character))
            self.assertRaises(NotAllowed, character.add_path, Duenna())
        self.young_noble.remove_path()
        for x in princelings:
            x.remove_path()

        self.young_noble.add_path(NobleCoeptir())
        for x in princelings:
            x.add_path(NobleCoeptir())
        self.assertTrue(Stentor().allowed(self.young_noble))
        for character in princelings:
            self.assertFalse(Stentor().allowed(character))
            self.assertRaises(NotAllowed, character.add_path, Stentor())
            
    def testRequiresCrucis(self):
        """These lifepaths should never be allowed if the character does not have either:
        1. The trait 'Corvus and Crucis'
        2. The trait 'Illegal Crucis'

        Navigator has no restrictions besides this
        """
        REQ_CRUCIS = [SpacefarerNavigator()]
        space_orphan = Human([BornSpacefarer()])
        bald_orphan = Human([BornSpacefarer()], traits=[trait.CorvusAndCrucis()])
        criminal_orphan = Human([BornSpacefarer()], traits = [trait.IllegalCrucis()])
        for path in REQ_CRUCIS:
            self.assertTrue(path.allowed(bald_orphan))
            self.assertTrue(path.allowed(criminal_orphan))
            self.assertFalse(path.allowed(space_orphan))
            self.assertRaises(NotAllowed, space_orphan.add_path, path)
            
    def testForgedLord(self):
        """Requires either:
        1. Both the Hammer Lord and Anvil Lord life paths
        2. Either of the Your Grace or Your Majesty Traits
        """
        char = Human([BornNobility(), NobleCoeptir(), NobleArmiger(), NobleLPAnvil(), NobleLPHammer(), AnvilLord()])
        self.assertFalse(ForgedLord().allowed(char))
        self.assertRaises(NotAllowed, char.add_path, ForgedLord())
        char.buy_trait(trait.YourGrace())
        self.assertTrue(ForgedLord().allowed(char))
        char.remove_trait(trait.YourGrace())
        char.buy_trait(trait.YourMajesty())
        self.assertTrue(ForgedLord().allowed(char))
        char.remove_trait(trait.YourMajesty())
        char.add_path(HammerLord())
        self.assertTrue(ForgedLord().allowed(char))
        
    def checkAllowance(self, path, prospectives):
        """A helper function that checks if each prospective is allowed to take a path, and that losing a single path makes them unable.
        """
        for character in prospectives:
            self.assertTrue(path.allowed(character))
            lastpath = character.paths()[-1]
            character.remove_path()
            if lastpath != path:
                self.assertFalse(path.allowed(character))
                self.assertRaises(NotAllowed, character.add_path, path)
            character.add_path(lastpath)
        
    def testCourtLPAnvil(self):
        """Requires either:
        1. Both the Mark of Privilege trait and one of Armiger or Court Armiger
        2. Any of Anvil Captain, Executive Official, Magnate, Treasurer, Financier or Chamberlain
        """
        anvil_captain = Human([BornNobility(),NobleCoeptir(),Lieutenant(),AnvilCaptain()])
        executive = Human([BornCommune(), CommuneStudent(), CommuneClerk(), Lawyer(), MunicipalOfficial(), Governor(), ExecutiveOfficial()])        
        treasurer = Human([BornLeague(), LeagueStudent(), Merchant(), Banker(), Treasurer()])
        self.checkAllowance(CourtLPAnvil(), [self.armiger, self.court_armiger, anvil_captain, executive, self.magnate, treasurer, self.financier, self.chamberlain])
        
    def testSurgeon(self):
        """Requires either:
        1. Any two hammer lifepaths
        2. Any two spacefarer lifepaths (and not any two of any combination of those settings)
        3. Any of Doctor, Physician, Coronor, Foundation Student, Court Coeptir, Coeptir or Student

        Note that there is no lifepath which qualifies for physician which does not also qualify for surgeon
        """
        doctor = Human([BornCommune(), Apprentice(), Doctor()])
        coroner = Human([BornNobility(), CourtClerk(), Mandarin(), Coroner()])
        self.checkAllowance(Surgeon(), [doctor, self.foundation_student, self.court_coeptir, self.coeptir, self.student, coroner, self.space_cook, self.hammer_cook])
        
    def testDisciplineOfficer(self):
        """Requires either:
        1. Any two Hammer lifepaths
        2. Either Justiciar or Constable
        """
        justiciar = Human([BornCommune(), CommuneStudent(), CourtClerk(), Mandarin(), Justiciar()])
        constable = Human([BornNobility(), NobleCoeptir(), XO(), Constable()])
        self.checkAllowance(DisciplineOfficer(), [self.hammer_cook, justiciar, constable])
        
    def testHammerLPHammer(self):
        """Requires either:
        1. Any three Hammer lifepaths
        2. Any of Armiger, Circle of 10,000, court armiger or Magnate
        """
        
        triple_hammer = Human([BornSpacefarer(), HammerYeoman(), HammerCook(), HammerSignalsTech()])
        self.checkAllowance(HammerLPHammer(), [self.armiger, self.court_armiger,self.circle_of_10k, triple_hammer, self.magnate])
        
    def testHammerCaptain(self):
        """Requires either:
        1. The Lord-Pilot Hammer lifepath
        2. The Your Majesty trait
        """
        self.assertFalse(HammerCaptain().allowed(self.armiger))
        self.assertRaises(NotAllowed, self.armiger.add_path, HammerCaptain())
        self.armiger.buy_trait(trait.YourMajesty())
        self.assertTrue(HammerCaptain().allowed(self.armiger))
        self.armiger.remove_trait(trait.YourMajesty())
        self.armiger.add_path(HammerLPHammer())
        self.assertTrue(HammerCaptain().allowed(self.armiger))
        
    def testAnvilElite(self):
        """Requires either:
        1. Both the Scout and Soldier lifepaths
        2. Either the sergeant or Psychologist lifepaths

        Note that it's impossible to get the Scout or Sergeant lifepaths without the Soldier lifepath
        So it's equivalent to "scout, sergeant or psychologist"
        """
        scout = Human([BornSlave(), Soldier(), Scout()])        
        self.checkAllowance(AnvilElite(), [self.sergeant, self.psychologist, scout])
        
    def testSodalisCaptain(self):
        """Tests the requirements for the sodalis captain lifepath.
        Requires either:
        1. Any of Sergeant, Armiger, Court Armiger, or Sodalis-Brother
        2. Any two of Sodalis, Sodalis Technician, or Sodalis Pilot ("Sodalis Lifepaths")
        """
        sodalis_brother = Human([BornLeague(), LeagueStudent(), Merchant(), Magnate(), NobleLPAnvil(), SodalisBrother()])
        pilot_and_sodalis = Human([BornLeague(), DevotedToFire(), SodalisPilot(), Sodalis()])
        tech_and_pilot = Human([BornLeague(), DevotedToFire(), SodalisTechnician(), SodalisPilot()])
        sodalis_and_tech = Human([BornLeague(), DevotedToFire(), Sodalis(), SodalisTechnician()])
        self.checkAllowance(SodalisCaptain(), [sodalis_brother, self.armiger, self.court_armiger, sodalis_and_tech, pilot_and_sodalis, tech_and_pilot])
        
    def testCotar(self):
        """'Devoted to Fire or Your Lordship'
        Trait or Lifepath?
        """
        devoted_to_fire = Human([BornLeague(), DevotedToFire()])
        self.companion.buy_trait(trait.YourLordship())
        self.checkAllowance(Cotar(), [devoted_to_fire, self.companion])
        
    def testCotarFomas(self):
        """Requires either:
        1: Devoted to Fire and Lord-Pilot Anvil
        2: Sodalis-Captain
        """
        trevor = Human([BornNobility(), NobleCoeptir(), NobleArmiger(), NobleLPAnvil(), DevotedToFire()])
        sodalis_captain = Human([BornLeague(), DevotedToFire(), SodalisPilot(), Sodalis(), SodalisCaptain()])
        self.checkAllowance(CotarFomas(), [trevor, sodalis_captain])
        
    def testSecurityOfficer(self):
        """tests requires for security officer lifepath: either (1) Discipline Officer, Sergeant or Stormtrooper, (2) two Security lifepaths
        """
        self.checkAllowance(SecurityOfficer(), [self.discipline_officer, self.stormtrooper, self.sergeant])
        double_secure = []
        
        
        self.checkAllowance(SecurityOfficer(), [self.security.add_path(Security())])
        self.checkAllowance(SecurityOfficer(), [self.man_at_arms_sec.add_path(ManAtArms())])
        self.checkAllowance(SecurityOfficer(), [self.law_enforcement.add_path(LawEnforcement())])
        self.checkAllowance(SecurityOfficer(), [self.breaker.add_path(Breaker())])
        self.checkAllowance(SecurityOfficer(), [self.justiciar.add_path(Justiciar())])
        self.checkAllowance(SecurityOfficer(), [self.adjutant_inquisitor.add_path(AdjutantInquisitor())])
        self.checkAllowance(SecurityOfficer(), [self.coroner.add_path(Coroner())])
        self.checkAllowance(SecurityOfficer(), [self.constable.add_path(Constable())])
        
    def testCommentariat(self):
        """Tests requirements for Commentariat lifepath.
        Requires either (1) any of Student, Scrivener, Propagandist, Media, Ravilar or (2) any lifepath from the Psychologist Foundation setting

        Note that it is impossible to take Psychologist, speaker or first speaker without already having taken a a path in the foundation setting
        Note that it is impossible to take Media without also taking Student or Foundation Student
        """
        eremite = Human([BornOutcast(), AlienMutantFreak(),Mule(), Eremite()])
        apprentice = Human([BornTheocracy(), Apprentice()])        
        novitiate = Human([BornNobility(), Novitiate()])
        scrivener = Human([BornLeague(), LeagueClerk(), Scrivener()])
        propagandist = Human([BornNobility(), Companion(), Propagandist()])
        ravilar = Human([BornNobility(), Companion(), Ravilar()])
        self.checkAllowance(Commentariat(), [eremite, self.circle_of_10k, apprentice, novitiate, self.student])
        
    def testLeagueOfficial(self):
        """Tests requirements for League Official lifepath.
        Requires either (1) any of Chamberlain, Merchant, Commentariat, X-O, Security Officer, Lietenant or (2) any Engineer type lifepath
        I assume that to include all lifepaths with engineer in the name:
        Engineer, Ship's Engineer, Hammer Engineer, Anvil Engineer

        There may be others...machinist?  fabricator?
        """
        
        commentariat = eremite = Human([BornOutcast(), AlienMutantFreak(),Mule(), Eremite(), Commentariat()])
        xo = Human([BornNobility(), Companion(), XO()])
        engineer = Human([BornFreeman(), FreemanStudent(), Fabricator(), Engineer()])
        ships_engineer = Human([BornFreeman(), Soldier(), Machinist(), ShipsEngineer()])
        hammer_engineer = Human([BornNobility(), HammerCoeptir(), NobleArmiger(), HammerEngineer()])
        anvil_engineer = Human([BornFreeman(), Soldier(), Machinist(), AnvilEngineer()])
        self.checkAllowance(LeagueOfficial(), [self.chamberlain, self.security_officer, self.merchant, commentariat, xo, self.lieutenant, engineer, ships_engineer, hammer_engineer, anvil_engineer])
        
    def testLawEnforcement(self):
        """test requirements for Law Enforcement Lifepath: either (1) any of Student, Foundation Student or Volunteer Soldier, or (2) any security-type lifepath
        """
        
        self.checkAllowance(LawEnforcement(), [self.student, self.foundation_student, self.volunteer_soldier])
        self.checkAllowance(LawEnforcement(), [self.discipline_officer])
        self.checkAllowance(LawEnforcement(), [self.stormtrooper])
        self.checkAllowance(LawEnforcement(), [self.security])
        self.checkAllowance(LawEnforcement(), [self.security_officer])
        self.checkAllowance(LawEnforcement(), [self.man_at_arms_sec])
        self.checkAllowance(LawEnforcement(), [self.law_enforcement])
        self.checkAllowance(LawEnforcement(), [self.breaker])
        self.checkAllowance(LawEnforcement(), [self.justiciar])
        self.checkAllowance(LawEnforcement(), [self.adjutant_inquisitor])
        self.checkAllowance(LawEnforcement(), [self.coroner])
        self.checkAllowance(LawEnforcement(), [self.constable])
        
    def testLawyer(self):
        """Requires either (1) Psychologist or (2) both student and clerk
        #Student and Clerk or Psychologist
        #I assume that's "Either Psychologist, or both Student and Clerk"
        """
        student_and_clerk = Human([BornCommune(), FoundationStudent(), CommuneStudent(), CommuneClerk()])
        clerk_and_student = Human([BornCommune(), FoundationStudent(), CommuneClerk(), CommuneStudent()])
        self.checkAllowance(Lawyer(), [self.psychologist, student_and_clerk, clerk_and_student])
        
    def testSpeaker(self):
        """The character must have taken Psychologist twice
        """
        double_psychologist = self.psychologist.add_path(Psychologist())
        self.checkAllowance(Speaker(), [double_psychologist])
        
    def testFirstSpeaker(self):
        """The character must have taken Speaker twice
        """
        double_speaker = self.psychologist.add_path(Psychologist()).add_path(Speaker()).add_path(Speaker())
        self.checkAllowance(FirstSpeaker(), [double_speaker])
        
    def testPilot(self):
        """Sense Rigger, Navigator, or two Yeoman lifepaths
        # the yeoman lifepath twice?  or some actual list of paths?
        """
        sense_rigger = Human([BornSpacefarer(), SpacefarerYeoman(), SenseRigger()])
        double_yeoman = Human([BornSpacefarer(), SpacefarerYeoman(), HammerYeoman()])
        self.checkAllowance(Pilot(), [sense_rigger, self.navigator, double_yeoman])
    
    def testCargoMaster(self):
        """Requires either (1) Navigator or (2) two spacefarer lifepaths
        """
        self.checkAllowance(CargoMaster(), [self.navigator, self.space_cook])
        
    def testOwnerAboard(self):
        """The character must purchase a ship as part of his starting resources and must begin with an exponent 7 or higher resources
        This will have to wait until I implement buying stuff
        """
        pass
    
    def testEngineer(self):
        """Tests that Engineer requires 'Student plus Fabricator or Craftsman'
        I am assuming that to mean "the Student and Fabricator lifepaths, or just the Craftsman life path"
        """
        fabricator=Human([BornFreeman(), CommuneStudent(), Fabricator()])
        craftsman=Human([BornTheocracy(), ApprenticeCraftsman(), Craftsman()])
        
        self.checkAllowance(Engineer(), [fabricator, craftsman])
        
    def testServant(self):
        """Test requirements for Servant lifepath:
        Any previous path from Slavery setting
        """
        jockey = Human([BornLeague(), SlaveJockey()])
        self.checkAllowance(Servant(), [jockey])
        
    def testCaptiveOfWar(self):
        """Test Requirements for Captive of War lifepath:
        Any lifepath from Anvil, Hammer or Nobility,
        or Volunteer Soldier, Freebooter or Pirate
        """
        
        hammer_yeoman = Human([BornSpacefarer(), HammerYeoman()])
        
        self.checkAllowance(CaptiveOfWar(), [self.volunteer_soldier, self.pirate, self.freebooter, self.companion, hammer_yeoman, self.soldier])
        
    def testBondsman(self):
        """Test requirements for Bondsman lifepath:
        Any previous path from Slavery setting
        """
        jockey = Human([BornLeague(), SlaveJockey()])
        self.checkAllowance(Servant(), [jockey])
        
    def testTaskmaster(self):
        """test requirements for Taskmaster lifepath:
        (1) Four lifepaths from the slave and serfdom setting
        (2) any thug lifepath
        (3) any soldier lifepath,
        (4) any law enforcement lifepath/ any security lifepath
        (6) any discipline lifepath
        
        """
        slave_for_life = Human([BornSlave(), SlaveLabor(), Prostitute(), Clown(), MigrantLabor()])
        self.checkAllowance(Taskmaster(), [slave_for_life])

        self.checkAllowance(Taskmaster(), [self.duelist, self.hive_thug, self.kidnapper, self.boxer])

        first_officer = Human([BornLeague(), Bastard(), Companion()]).buy_trait(trait.IllegalCrucis()).add_path(SpacefarerNavigator()).add_path(SpacefarerFirstOfficer())
        criminal = Human([BornOutcast(), Blackmailer(), Blackmailer(),Criminal()])
        self.checkAllowance(Taskmaster(), [first_officer, criminal])
        
        self.checkAllowance(Taskmaster(), [self.discipline_officer])
        self.checkAllowance(Taskmaster(), [self.stormtrooper])
        self.checkAllowance(Taskmaster(), [self.security])
        self.checkAllowance(Taskmaster(), [self.law_enforcement])
        self.checkAllowance(Taskmaster(), [self.breaker])
        self.checkAllowance(Taskmaster(), [self.justiciar])
        self.checkAllowance(Taskmaster(), [self.adjutant_inquisitor])
        self.checkAllowance(Taskmaster(), [self.coroner])
        self.checkAllowance(Taskmaster(), [self.constable])

        self.checkAllowance(Taskmaster(), [self.coeptir])
        self.checkAllowance(Taskmaster(), [self.court_coeptir])
        self.checkAllowance(Taskmaster(), [self.court_armiger])
        self.checkAllowance(Taskmaster(), [self.soldier])
        self.checkAllowance(Taskmaster(), [self.lieutenant])
        self.checkAllowance(Taskmaster(), [self.anvil_elite])
        self.checkAllowance(Taskmaster(), [self.sodalis])
        self.checkAllowance(Taskmaster(), [self.volunteer_soldier])
        self.checkAllowance(Taskmaster(), [self.freebooter])
        
    def testMule(self):
        """test requirements for Mule lifepath: Requires approval of gaming group.
        Maybe a message is printed?
        """
        pass
    def testFilthyWormLover(self):
        """test requirements for Filthy Worm Lover lifepath: One previous professional or mid-tier lifepath from any setting except outcast or servitude
        Noble: Armiger
        Court: clerk, courier, Herald, bureaucrat, Stentor, Court Armiger, Mandarin, Ravilar, Coroner
        
        Freeman:
        """
        pass
    def testBeggarKing(self):
        """test requirements for Beggar King lifepath
        (1)Beggar plus one of the following: Mummer, urchin, pickpocket, deranged or cripple.
        (2)Or just Heretic Priest (IE: Rebel Priest)
        """
        rebel_priest = Human([BornTheocracy(), Cultist(), Cultist(), RebelPriest()])
        self.checkAllowance(BeggarKing(), [rebel_priest])
        mummer_beggar = Human([BornCommune(), Mummer(), Beggar()])
        beggar_mummer = Human([BornCommune(), Beggar(), Mummer()])
        urchin_beggar = Human([BornCommune(), Urchin(), Beggar()])
        # no 'beggar_urchin, since urchin must be 2nd path
        pickpocket_beggar = Human([BornCommune(), Vagrant(), Pickpocket(), Beggar()])
        beggar_pickpocket = Human([BornCommune(), Beggar(), Pickpocket()])
        deranged_beggar = Human([BornCommune(), Deranged(), Beggar()])
        beggar_deranged = Human([BornCommune(), Beggar(), Deranged()])
        beggar_cripple = Human([BornCommune(), Beggar(), Cripple()])
        cripple_beggar = Human([BornCommune(), Cripple(), Beggar()])
        beggar_army = [mummer_beggar, beggar_mummer, urchin_beggar, pickpocket_beggar, beggar_pickpocket, deranged_beggar, beggar_deranged, cripple_beggar, beggar_cripple]
        self.checkAllowance(BeggarKing(), beggar_army)

    def testRebelPriest(self):
        """test requirements Rebel Priest
        (1) Cotar, Philosopher, Thinker
        (2) Two cultist lifepaths (cultist twice?  or an actual list of paths?)
        """
        double_cultist = Human([BornTheocracy(), Cultist(), Cultist()])
        cotar = Human([BornTheocracy(), DevotedToFire(), Cotar()])
        philosopher = Human([BornCommune(), CommuneStudent(), Philosopher()])
        thinker = Human([BornOutcast(), Thinker()], age=30)
        self.checkAllowance(RebelPriest(), [double_cultist, cotar, philosopher, thinker])
    def testFreebooter(self):
        """Test requirements for Freebooter
        (1) any of Desperate Killer, Pirate, Smuggler, Circle of 10,000
        (2)or any soldier-type lifepath
        note that no character who qualifies for Desparate Killer does not qualify for freebooter
        """
        smuggler = Human([BornNobility(), Acrobat(), Smuggler()])
        self.checkAllowance(Freebooter(), [self.pirate, self.circle_of_10k, smuggler])
        self.checkAllowance(Freebooter(), self.soldier_characters)
        
    def testDesperateKiller(self):
        """test requirements for Desperate Killer lifepath
        Any soldier-type lifepath
        """
        self.checkAllowance(DesperateKiller(), self.soldier_characters)
    def testConfidenceMan(self):
        """
        #Previous outcast, servitude, Commune or Freeman lifepath
        """
        outcast = Human([BornOutcast(), Vagrant()])
        servitude = Human([BornSlave(), SlaveLabor()])
        commune = Human([BornCommune(), CommuneStudent()])
        freeman = Human([BornFreeman(), Kid()])
        self.checkAllowance(ConfidenceMan(), [outcast, servitude, commune, freeman])
    def testPirate(self):
        """test requirements for Pirate lifepath
        (1) One previous spacefarer or hammer lifepath
        hammer meaning hammer setting?
        """
        spacefarer = Human([BornOutcast(), SpacefarerYeoman()])
        hammer = Human([BornOutcast(), HammerYeoman()])
        self.checkAllowance(Pirate(), [spacefarer, hammer])
    def testBoxer(self):
        """test requirements for Boxer Lifepath: Born on the Streets or any Anvil lifepath
        just the anvil setting, or does l-p anvil count?
        """
        anvil = Human([BornTheocracy(), Soldier()])
        self.checkAllowance(Boxer(), [anvil])
        born_street = Human([BornOutcast()])
        self.checkAllowance(Boxer(), [born_street])
        
    def testBreaker(self):
        """test requirements for Breaker lifepath: Two previous outcast lifepaths or any security-related lifepath
        """
        double_outcast = Human([BornOutcast(), Vagrant(), Vagrant()])
        self.checkAllowance(Breaker(), [double_outcast])
        self.checkAllowance(Breaker(), self.security_characters)
    def testSmuggler(self):
        """test requirements for Smuggler lifepath: one previous outcast, spacefarer, hammer or Anvil lifepath
        """
        outcast = Human([BornOutcast(), Vagrant()])
        spacefarer = Human([BornOutcast(), SpacefarerYeoman()])
        hammer = Human([BornOutcast(), HammerYeoman()])
        anvil = Human([BornTheocracy(), Soldier()])
        self.checkAllowance(Smuggler(), [outcast, spacefarer, hammer, anvil])
        
    def testCounterfeiter(self):
        """test requirements for Counterfeiter lifepath:
        (1) two previous outcast lifepaths,
        (2) banker, shopkeeper, functionary, financier or merchant
        Note that it's impossible to take banker without either financier or merchant
        """
        double_outcast = Human([BornOutcast(), Vagrant(), Vagrant()])
        shopkeeper = Human([BornNobility(), ServiceWorker(), Shopkeeper()])
        functionary = Human([BornNobility(), CommuneStudent(), Functionary()])
        self.checkAllowance(Counterfeiter(), [double_outcast, shopkeeper, self.financier, functionary, self.merchant])
    def testGunsel(self):
        """test requirements for Gunsel lifepath:
        (1) Sergeant, Man-at-Arms, Volunteer Soldier, Desperate Killer, Boxer, Duelist, Freebooter, Task Master (sic)
        (2) two Hive Thug lifepaths
        """
        desperate_killer = Human([BornSlave(), Soldier(), DesperateKiller()])
        double_thug = Human([BornNobility(), Deranged(), HiveThug(), HiveThug()])
        
        self.checkAllowance(Gunsel(), [self.sergeant, self.man_at_arms_sol, self.volunteer_soldier, self.boxer, self.duelist, self.freebooter, self.taskmaster, desperate_killer, double_thug])
    def testCriminal(self):
        """test criminal requirements
        (1)Gunsel, Advocate, Mandarin, Lawyer, Politico, League Official, Psychologist
        (2) any two of the following: Kidnapper, Blackmailer, Whoremonger, Fence, Counterfeiter, Breaker or Smuggler
        """
        advocate = Human([BornCommune(), CommuneStudent(), Advocate()])
        mandarin = Human([BornCommune(), CommuneStudent(), Mandarin()])
        lawyer = Human([BornCommune(), CommuneStudent(), CommuneClerk(), Lawyer()])
        politico = Human([BornCommune(), CommuneStudent(), Financier(), Politico()])
        league_official = Human([BornNobility(), NobleCoeptir(), XO(), LeagueOfficial()])
        self.checkAllowance(Criminal(), [self.gunsel, advocate, mandarin, lawyer, politico, league_official, self.psychologist])

        double_kidnapper = self.kidnapper.add_path(Kidnapper())
        double_blackmailer = Human([BornLeague(), Blackmailer(), Blackmailer()])
        double_whoremonger = self.space_cook.add_path(CargoMaster()).add_path(Whoremonger()).add_path(Whoremonger())
        double_fence = self.merchant.add_path(Fence()).add_path(Fence())
        double_counterfeiter = Human([BornOutcast(), Vagrant(), Vagrant(), Counterfeiter(), Counterfeiter()])
        double_breaker = self.breaker.add_path(Breaker())
        double_smuggler = Human([BornOutcast(), Vagrant(), Smuggler(), Smuggler()])
        self.checkAllowance(Criminal(), [double_kidnapper, double_blackmailer, double_whoremonger, double_fence, double_counterfeiter, double_breaker, double_smuggler])
    def testGeneralPoints(self):
        """Some lifepaths give general skill points.
        """
        general_list={BornNobility():5, VoidLord():1, ForgedLord():2, Hostage(): 1, Chamberlain():1,
                      HammerCaptain():1, BornTheocracy():3, Archcotare():2, CotarAntistes(): 2,
                      CotarArderes():2, BornLeague(): 4, Magnate():1, ChiefExecutive():2, BornCommune():3,
                      Judge():1, Financier():1, Governor():1, AppointedOfficial():1,Politico():1,
                      CabinetMember():1,ExecutiveOfficial():2,FirstSpeaker():4, Eremite():1,
                      BornSpacefarer():2,ShipsCaptain():1,OwnerAboard():2,BornFreeman():3,BornSlave():2,
                      BornOutcast():3, RebelPriest():1, Thinker():1, Traveler():1}
        for path, points in general_list.iteritems():
            self.assertEquals(path.general_skill_points, points)
        

if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(HumanLifePathTests))
