import unittest
from character.char import Character
from character.lifepath import Lifepath
from character.trait import *
from character.human import Human,CommuneLifepath, MerchantLeagueLifepath, OutcastLifepath

class TraitTests(unittest.TestCase):
    def setUp(self):
        self.char =  Character([ Lifepath(born=True, years=1,trait_points=100)])
    def testDie(self):
        dietrait = DieTrait('Mark of Privilege', 3)
        self.assertEquals(dietrait.name, 'Mark of Privilege')
        self.assertEquals(dietrait.cost, 3)
        dietrait = DieTrait('Corvus and Crucis', 4)
        self.assertEquals(dietrait.name, 'Corvus and Crucis')
        self.assertEquals(dietrait.cost, 4)
    def testCallOn(self):
        cotrait = CallOnTrait('Follow the Money', 2)
        self.assertEquals(cotrait.name, 'Follow the Money')
        self.assertEquals(cotrait.cost, 2)
        cotrait = CallOnTrait('Forked Tongue',  3)
        self.assertEquals(cotrait.name, 'Forked Tongue')
        self.assertEquals(cotrait.cost, 3)
    def testChar(self):
        ctrait = CharacterTrait('Testing Fiend')
        ctrait2 = CharacterTrait('Testing Fiend')
        self.assertEquals(ctrait.name, 'Testing Fiend')
        self.assertEquals(ctrait.cost, 1)
        self.assertEquals(ctrait, ctrait2)
    def testISolzjah(self):
        # No Kerrn requirement?  Humans and Vaylen can take it?
        pass
    def testHumanOnlyTrait(self):
        human_only = [BrightMark(), Forged(), FuurBlood(), HammerLord(), Primarch()]
        pass
    def testRequiresBrightMarkTrait(self):
        """test if Gift of Ahmilahk and The Psychologists Code require the Bright Makr
        """
        req_bright_mark = [GiftOfAhmilahk(), ThePsychologistsCode()]
        for x in req_bright_mark:
            self.assertFalse(x.allowed(self.char))
            self.assertFalse(x in self.char.allowed_traits())
            self.char.buy_trait(BrightMark())
            self.assertTrue(x.allowed(self.char))
            self.assertTrue(x in self.char.allowed_traits())
            self.char.remove_trait(BrightMark())
    def testWarriorsCode(self):
        """test requirements for Warriors Code trait
        'Bright Mark required.  Alternately, the player may use the mule trait,but he must also take a Branded Character Trait.  The circle brands him as one of their own'
        Bright mark OR (Mule AND Branded?)  Is branded free?  I will guess no
        """
        self.assertFalse(WarriorsCode().allowed(self.char))
        self.assertFalse(WarriorsCode() in self.char.allowed_traits())
        self.char.buy_trait(BrightMark())
        self.assertTrue(WarriorsCode().allowed(self.char))
        self.assertTrue(WarriorsCode() in self.char.allowed_traits())
        self.char.remove_trait(BrightMark())
        self.assertFalse(WarriorsCode().allowed(self.char))
        self.assertFalse(WarriorsCode() in self.char.allowed_traits())
        self.char.buy_trait(Mule())
        self.assertFalse(WarriorsCode().allowed(self.char))
        self.assertFalse(WarriorsCode() in self.char.allowed_traits())
        self.char.buy_trait(Branded())
        self.assertTrue(WarriorsCode().allowed(self.char))
        self.assertTrue(WarriorsCode() in self.char.allowed_traits())
    def testAnvilLord(self):
        """test requirements for Anvil Lord Trait
        'if not gained as an lp trait, the character must be born to rule or have the magnate lifepath'
        ie: requires magnate, born to rule, or anvil lord
        """
        for test_name in ['Magnate', 'Born to Rule', 'Anvil Lord']:
            self.assertFalse(AnvilLord().allowed(self.char))
            self.assertFalse(AnvilLord() in self.char.allowed_traits())
            self.char.add_path( Lifepath(test_name))
            self.assertTrue(AnvilLord().allowed(self.char))
            self.assertTrue(AnvilLord() in self.char.allowed_traits())
            self.char.remove_path()
            
    def testAnvilTrained(self):
        """test requirements for Anvil Trained trait: may not be taken by mukhadish
        i.e., only human, kern or vaylen
        """
        pass
    
    def testArbiter(self):
        """test requirements for Arbiter Trait
        Archcotare or Cult Leader LP
        """
        for test_name in ['Archcotare', 'Cult Leader']:
            self.assertFalse(Arbiter().allowed(self.char))
            self.assertFalse(Arbiter() in self.char.allowed_traits())
            self.char.add_path(Lifepath(test_name))
            self.assertTrue(Arbiter().allowed(self.char))
            self.assertTrue(Arbiter() in self.char.allowed_traits())
            self.char.remove_path()
            
    def testRequiresBornToRule(self):
        """Test requirements for Bastard and Your Eminence/Grace/Lordship/Majesty: Born to Rule Lifepath
        """
        req_born_to_rule = [Bastard(), YourEminence(), YourGrace(), YourLordship(), YourMajesty()]
        for x in req_born_to_rule:
            self.assertFalse(x.allowed(self.char))
            self.assertFalse(x in self.char.allowed_traits())
            self.char.remove_path()
            self.char.add_path( Lifepath(name='Born to Rule', born=True, trait_points=100))
            self.assertTrue(x.allowed(self.char))
            self.assertTrue(x in self.char.allowed_traits())
            self.char.remove_path()
            self.char.add_path( Lifepath(born=True, trait_points=100))
    def testBornOnTheWheel(self):
        """test requirements for Born on the Wheel trait: Born on the Wheel LP only
        """
        self.assertFalse(BornOnTheWheel().allowed(self.char))
        self.assertFalse(BornOnTheWheel() in self.char.allowed_traits())
        self.char.add_path(Lifepath(name='Born on the Wheel'))
        self.assertTrue(BornOnTheWheel().allowed(self.char))
        self.assertTrue(BornOnTheWheel() in self.char.allowed_traits())
    def testCitizenOfTheCommune(self):
        """test requirements for Citizen of the Commune trait: Born Citizen LP only
        """
        self.assertFalse(CitizenOfTheCommune().allowed(self.char))
        self.assertFalse(CitizenOfTheCommune() in self.char.allowed_traits())
        self.char.remove_path()
        self.char.add_path( Lifepath(name='Born Citizen', born=True, trait_points=100))
        self.assertTrue(CitizenOfTheCommune().allowed(self.char))
        self.assertTrue(CitizenOfTheCommune() in self.char.allowed_traits())
    def testCodebreaker(self):
        """test requirements for Codebreaker trait: Psychologist-type characters only
        """
        
        pass
    def testContender(self):
        """test requirements for Contender trait: Mark of Privilege Trait
        """
        self.assertFalse(Contender().allowed(self.char))
        self.assertFalse(Contender() in self.char.allowed_traits())
        self.char.buy_trait(MarkOfPrivilege())
        self.assertTrue(Contender().allowed(self.char))
        self.assertTrue(Contender() in self.char.allowed_traits())
    def testCorvusAndCrucis(self):
        #Characters with a human body
        #ie: humans, and vaylen in the human or infiltrator settings
        pass
    def testCotarFomas(self):
        """test requirements for Cotar Fomas trait: cotar fomas lp only
        """
        self.assertFalse(CotarFomas().allowed(self.char))
        self.assertFalse(CotarFomas() in self.char.allowed_traits())
        self.char.add_path( Lifepath(name='Cotar Fomas'))
        self.assertTrue(CotarFomas().allowed(self.char))
        self.assertTrue(CotarFomas() in self.char.allowed_traits())
    def testDevotedToFire(self):
        """test requirements for Devoted to Fire trait: Devoted to Fire LP only
        What?!  But why is it listed in the Sodalis-Brother LP?
        """
        self.assertFalse(DevotedToFire().allowed(self.char))
        self.assertFalse(DevotedToFire() in self.char.allowed_traits())
        self.char.add_path( Lifepath(name='Devoted to Fire'))
        self.assertTrue(DevotedToFire().allowed(self.char))
        self.assertTrue(DevotedToFire() in self.char.allowed_traits())
    def testDregutai(self):
        """test requirements for Dregutai trait: Dregus LP only
        """
        self.assertFalse(Dregutai().allowed(self.char))
        self.assertFalse(Dregutai() in self.char.allowed_traits())
        self.char.add_path( Lifepath(name='Dregus'))
        self.assertTrue(Dregutai().allowed(self.char))
        self.assertTrue(Dregutai() in self.char.allowed_traits())
    def testEducated(self):
        """test requirements for Educated trait: Human and Vaylen only
        #any vaylen setting?  It seems like more of a human or makara caste thing
        """
        h = Human([Lifepath(born=True, trait_points=100)])
        self.assertTrue(Educated().allowed(h))
        self.assertTrue(Educated() in h.allowed_traits())
    def testEmperorsSteward(self):
        """test requirements of Emperor's Steward Trait:Lord Steward LP
        """
        self.assertFalse(EmperorsSteward().allowed(self.char))
        self.assertFalse(EmperorsSteward() in self.char.allowed_traits())
        self.char.add_path(Lifepath(name='Lord Steward'))
        self.assertTrue(EmperorsSteward().allowed(self.char))
        self.assertTrue(EmperorsSteward() in self.char.allowed_traits())
    def testFamily(self):
        #Kerrn Diazspherah, Human, Mukhadish Underworld setting and Vaylen setting characters only
        #any human?  the human stock?
        pass
    def testGarbo(self):
        #Human or Human-bodied Vaylen only
        #Ie, human stock, or lifepath in human caste or invader settings?  any or ends in?
        pass
    def testRequiresCorvusAndCrucis(self):
        """test requirements for Iron Trained and Wigged trait: Corvus and Crucis trait
        """
        for x in [IronTrained(), Wigged()]:
            self.assertFalse(x.allowed(self.char))
            self.assertFalse(x in self.char.allowed_traits())
            self.char.buy_trait(CorvusAndCrucis())
            self.assertTrue(x.allowed(self.char))
            self.assertTrue(x in self.char.allowed_traits())
            self.char.remove_trait(CorvusAndCrucis())
    def testKeeperOfTheFire(self):
        """test requirements for Keeper of the Fire Trait: Keeper of the Fire LP only
        No such lifepath.  I assume they mean Cotar
        """
        self.assertFalse(KeeperOfTheFire().allowed(self.char))
        self.assertFalse(KeeperOfTheFire() in self.char.allowed_traits())
        self.char.add_path(Lifepath(name='Cotar'))
        self.assertTrue(KeeperOfTheFire().allowed(self.char))
        self.assertTrue(KeeperOfTheFire() in self.char.allowed_traits())
    def testKravMagahTrained(self):
        #Human, Vaylen and Mukhadish characters may only take this if there are no Kerrn player characters in their group
        # So Kerrn can take it without restriction.  Maybe a notice otherwise?
        pass
    def testMarkOfPrivilege(self):
        """test requirements for Mark of Privilege trait: Born to Rule, Vaylen Captain and Vaylen Command LPs only
        """
        self.assertFalse(MarkOfPrivilege().allowed(self.char))
        self.assertFalse(MarkOfPrivilege() in self.char.allowed_traits())
        self.char.add_path(Lifepath(name='Born to Rule'))
        self.assertTrue(MarkOfPrivilege().allowed(self.char))
        self.assertTrue(MarkOfPrivilege() in self.char.allowed_traits())
    def testMetropolitan(self):
        """test requirements for Metropolitan and Word is Law traits: Cotar Antistes LP only
        """
        self.assertFalse(Metropolitan().allowed(self.char))
        self.assertFalse(Metropolitan() in self.char.allowed_traits())
        self.assertFalse(WordIsLaw().allowed(self.char))
        self.assertFalse(WordIsLaw() in self.char.allowed_traits())
        self.char.add_path( Lifepath(name='Cotar Antistes'))
        self.assertTrue(Metropolitan().allowed(self.char))
        self.assertTrue(Metropolitan() in self.char.allowed_traits())
        self.assertTrue(WordIsLaw().allowed(self.char))
        self.assertTrue(WordIsLaw() in self.char.allowed_traits())
        
    def testOfficer(self):
        """test requirements for Officer trait: Hammer Captain and Vaylen Captain LPs only
        """
        self.assertFalse(Officer().allowed(self.char))
        self.assertFalse(Officer() in self.char.allowed_traits())
        self.char.add_path( Lifepath(name='Hammer Captain'))
        self.assertTrue(Officer().allowed(self.char))
        self.assertTrue(Officer() in self.char.allowed_traits())
        
    def testOwnerAboard(self):
        #The character must purchase a ship as part of his starting resources and must begin with Resources 7 or higher
        pass
    def testPublicServant(self):
        """test requirements for public servant:Civilian Commune or Merchant League Only
        taken once, or "ends with"?
        """
        self.assertFalse(PublicServant().allowed(self.char))
        self.assertFalse(PublicServant() in self.char.allowed_traits())
        self.char.add_path(CommuneLifepath())
        self.assertTrue(PublicServant().allowed(self.char))
        self.assertTrue(PublicServant() in self.char.allowed_traits())
        self.char.remove_path()
        self.assertFalse(PublicServant().allowed(self.char))
        self.assertFalse(PublicServant() in self.char.allowed_traits())
        self.char.add_path(MerchantLeagueLifepath())
        self.assertTrue(PublicServant().allowed(self.char))
        self.assertTrue(PublicServant() in self.char.allowed_traits())
    def testSenator(self):
        """test requirements for Senator trait: Legislative [Official] LP only
        """
        self.assertFalse(Senator().allowed(self.char))
        self.assertFalse(Senator() in self.char.allowed_traits())
        self.char.add_path(Lifepath(name='Legislative Official'))
        self.assertTrue(Senator().allowed(self.char))
        self.assertTrue(Senator() in self.char.allowed_traits())
    def testSlaggah(self):
        """test requirements for Slaggah trait: only for characters with the Artillery or Strategy skills
        Not sure if that's a real requirement
        """
        pass
    def testTough(self):
        """round up calculations for mortal wound
        """
        self.char.buy_power()
        self.char.buy_forte()
        self.assertEquals(self.char.mortal_wound(), 'H7')
        self.assertEquals(self.char.maimed_wound(), 'H5')
        self.char.buy_forte()
        self.assertEquals(self.char.mortal_wound(), 'H7')
        self.assertEquals(self.char.maimed_wound(), 'H5')
        self.char.buy_trait(Tough())
        self.assertEquals(self.char.mortal_wound(), 'H8')
        self.assertEquals(self.char.maimed_wound(), 'H6')
        self.char.buy_forte()
    def testVig(self):
        """test requirements for Vig Trait: Outcast and Criminal LPs only
        """
        self.assertFalse(Vig().allowed(self.char))
        self.assertFalse(Vig() in self.char.allowed_traits())
        self.char.add_path(OutcastLifepath())
        self.assertTrue(Vig().allowed(self.char))
        self.assertTrue(Vig() in self.char.allowed_traits())

class InhumanCharacterTraitRequirementsTests(unittest.TestCase):
    def testKerrnOnly(self):
        #Cryptic, Emperor's Armor Bearer(stock or lifepath?)
        pass
    def testVaylenOnly(self):
        #Aeumiflesh, Animal life, AnnelidaClan (not the naiven lifepath?), Lucky to be in a human body (setting or stock?)
        pass
    def testAadauClan(self):
        #Aadau Naiven LP only
        pass
    def testAmedhyen(self):
        #Amedhyen Naiven LP only
        pass
    def testChild(self):
        #Vaylen only.  Any vaylen character who has human caste lps or whose last lifepath is slave labor, cultist or sleeper may choose to begin the game with a child body for one trait point.
        # ie: this is a lifepath trait for those lifepaths
        #...in fact, that's what they say in the book.
        pass
    def testFaziaToAll(self):
        #Ghetto Sheef
        pass
    def testMakaraBody(self):
        #Yaadasahm Naiven LP only
        pass
    def testMeshenClan(self):
        #Meshhen Naiven only
        pass
    def testOffisah(self):
        #Kerrn Offisah LP only
        pass
    def testClanLeader(self):
        #Ksatriyen Vaylen only
        #the setting, or the Ksatriya lifepath?
        pass
    def testOmshiipOffisah(self):
        #Kerrn Sheef LP only
        pass
    def testOmshiipStaff(self):
        #Kerrn Omshiip LPs only
        pass
    def testOmshiipsMaster(self):
        #Emcheef LP only
        pass
    def testSelfMadeKerrn(self):
        #Kerrn who have Opvraeta lifepaths only
        pass
    def testUsurper(self):
        #Vaylen only
        #stock or setting?
        pass
    def testVibhuutenClan(self):
        #Vibhuuten Naiven only
        pass
    
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(TraitTests))
    unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(InhumanCharacterTraitRequirementsTests))
