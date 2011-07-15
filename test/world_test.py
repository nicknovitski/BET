import os
import unittest
from world.world import *

class WorldBurnerTests(unittest.TestCase):
    def testMake(self):
        w = World()
        self.checkDispo(w, [0,0,0,0,0,0])
    def testname(self):
        w = World()
        self.assertEquals(w.get_name(), 'None')
        w.set_name('New Name')
        self.assertEquals(w.get_name(), 'New Name')
    def testInit(self):
        w = World(name='A name')
        self.assertEquals(w.get_name(), 'A name')
        for x in EMPIRES:
            w = World(empire=x)
            self.assertEquals(w.get_empire(), x)
        for x in LOCATIONS:
            w = World(location=x)
            self.assertEquals(w.get_location(), x)
        for x in ATMOSPHERES:
            w = World(atmosphere=x)
            self.assertEquals(w.get_atmosphere(), x)
        for x in HYDROLOGIES:
            w = World(hydrology=x)
            self.assertEquals(w.get_hydrology(), x)
        for x in TOPOGRAPHIES:
            w = World(topography=x)
            self.assertEquals(w.get_topography(), x)
        for x in INDICES:
            w = World(index=x)
            self.assertEquals(w.get_index(), x)
        for x in GOVERNMENTS:
            w = World(government=x)
            self.assertEquals(w.get_government(), x)
        for mil in MILITARIES:
            if mil == LORDSPILOT:
                self.assertRaises(InvalidChoice, World, military=LORDSPILOT)
                for gov in GOVERNMENTS:
                    if gov in [NOBLE, STEWARD]:
                        w = World(government=gov, military = LORDSPILOT)
                        self.assertEquals(w.get_military(), LORDSPILOT)
                    else:
                        self.assertRaises(InvalidChoice, World, government=gov, military=LORDSPILOT)
            elif mil == RELIGIOUS:
                self.assertRaises(InvalidChoice, World, military=RELIGIOUS)
                for gov in GOVERNMENTS:
                    if gov == THEOCRACY:
                        w = World(government=THEOCRACY, military=RELIGIOUS)
                        self.assertEquals(w.get_military(), RELIGIOUS)
                    else:
                        self.assertRaises(InvalidChoice, World, government=gov, military=RELIGIOUS)
            else:
                w = World(military=mil)
                self.assertEquals(w.get_military(), mil)
        for att in ATTITUDES:
            if att in [EDUCATED, EXPERIENCE]:
                self.assertRaises(InvalidChoice, World, attitude=att)
                w = World(location=OUT, attitude=att)
                self.assertEquals(w.get_attitude(), att)
                w = World(location=VOID, attitude=att)
                self.assertEquals(w.get_attitude(), att)
            else:
                w = World(attitude=att)
                self.assertEquals(w.get_attitude(), att)
        for exp in EXPORTS:
            if exp == MILITARY:
                self.assertRaises(InvalidChoice, World, export=MILITARY)
                for idx in INDICES:
                    if idx in [LOW, HIGH]:
                        w = World(index = idx,export=MILITARY)
                        self.assertEquals(w.get_export(), MILITARY)
                    else:
                        self.assertRaises(InvalidChoice, World, index=idx, export=MILITARY)
            else:
                w = World(export=exp)
                self.assertEquals(w.get_export(), exp)
        for qua in QUARANTINES:
            if qua == ADVANCED:
                self.assertRaises(InvalidChoice, World, quarantine=ADVANCED)
                for idx in INDICES:
                    if idx in [LOW, HIGH]:
                        w = World(index = idx, quarantine=ADVANCED)
                        self.assertEquals(w.get_quarantine(), ADVANCED)
                    else:
                        self.assertRaises(InvalidChoice, World, index=idx, quarantine=ADVANCED)
            else:
                w = World(quarantine=qua)
                self.assertEquals(w.get_quarantine(), qua)
        for x in REGULATIONS:
            w = World(regulation=x)
            self.assertEquals(w.get_regulation(), x)

    def testNative(self):
        w = World()
        self.assertEquals(w.native_settings(), ['Outcast and Criminal', 'Underworld', 'Vaylen', 'Freeman'])
        
    def checkDispo(self, world, dispositions):
        self.assertEquals(world.vaylen_infiltration(), dispositions[0])
        self.assertEquals(world.vaylen_usurpation(), dispositions[1])
        self.assertEquals(world.vaylen_invasion(), dispositions[2])
        
        self.assertEquals(world.human_infiltration(), dispositions[3])
        self.assertEquals(world.human_usurpation(), dispositions[4])
        self.assertEquals(world.human_invasion(), dispositions[5])
        self.assertEquals(world.dispositions(), dispositions)
        
    def testEmpire(self):
        w = World()
        self.assertEquals(w.get_empire(), 'None')
        w.set_empire(CASIGURAN)
        self.assertEquals(w.get_empire(), 'Casiguran Matriarchy')
        w.set_empire(COMORAN)
        self.assertEquals(w.get_empire(), 'Comoran Worlds')
        w.set_empire(DARIKAHN)
        self.assertEquals(w.get_empire(), 'Darikahn Empire')
        w.set_empire(DUNEDIN)
        self.assertEquals(w.get_empire(), 'Dunedin Worlds')
        w.set_empire(GONZAGIN)
        self.assertEquals(w.get_empire(), 'Gonzagin Empire')
        w.set_empire(KARSAN)
        self.assertEquals(w.get_empire(), 'Karsan League')
        w.set_empire(KUDUS)
        self.assertEquals(w.get_empire(), 'Kudus Theocracy')
        w.set_empire(URFAN)
        self.assertEquals(w.get_empire(), 'Urfan Worlds')
        self.assertRaises(InvalidChoice, w.set_empire, 'Whatever I feel like')
        self.assertEquals(w.get_empire(), 'Urfan Worlds')
        
    def testLocation(self):
        w = World()
        self.assertEquals(w.get_location(), 'None')
        w.set_location(CORE)
        self.assertEquals(w.get_location(), 'Old Imperial Core World')
        self.checkDispo(w, [2,3,1,2,2,8])
        w.set_location(INT)
        self.assertEquals(w.get_location(), 'Interior World')
        self.checkDispo(w, [2,2,2,1,2,3])
        w.set_location(OUT)
        self.assertEquals(w.get_location(), 'Outworld')
        self.checkDispo(w, [1,1,4,2,2,2])
        w.set_location(VOID)
        self.assertEquals(w.get_location(), 'Void World')
        self.checkDispo(w, [2,2,8,3,2,1])
        self.assertRaises(InvalidChoice, w.set_location, 'Whatever I feel like')
        
        
    def testAtmosphere(self):
        w = World()
        self.assertEquals(w.get_atmosphere(), 'None')
        self.assertRaises(InvalidChoice, w.set_atmosphere, 'Whatever I feel like')
        w.set_atmosphere(PLS)
        self.assertEquals(w.get_atmosphere(), 'Partial-Life-Supporting')
        self.checkDispo(w, [3,0,3,2,3,1])
        
    def testALSAtmosphere(self):
        """test ALS atmosphere
        requires artificial environs and indigenous lifeforms
        """
        w = World()
        w.set_atmosphere(ALS) 
        self.assertEquals(w.get_atmosphere(), 'Alien-Life-Supporting')
        self.assertEquals(w.get_topography(), 'Artificially Created Environs')
        self.assertTrue(ALIENS in w.get_factions())
        self.checkDispo(w, [8,5,5,5,3,4])
        self.assertRaises(InvalidChoice, w.set_topography, BROAD)
        self.assertRaises(InvalidChoice, w.remove_faction, ALIENS)
        w.set_atmosphere(HLS)
        w.set_topography(BROAD)
        w.remove_faction(ALIENS)
        
    def testHLSAtmo(self):
        """test HLS: wild mukhadish becomes native
        """
        w = World()
        w.set_atmosphere(HLS)
        self.assertEquals(w.get_atmosphere(), 'Human-Life-Supporting')
        self.checkDispo(w, [2,2,2,1,3,2])
        self.assertTrue('Mukhadish Wild' in w.native_settings())
        
    def testNLSAtmo(self):
        """test NLS atmo
        requires Artificial environs
        """
        w = World()
        w.set_atmosphere(NLS) 
        self.assertEquals(w.get_atmosphere(), 'Non-Life-Supporting')
        self.assertEquals(w.get_topography(), 'Artificially Created Environs')
        self.checkDispo(w, [2,5,5,6,3,3])
        self.assertRaises(InvalidChoice, w.set_topography, BROAD)
        
    def testHydrology(self):
        w =World()
        self.assertEquals(w.get_hydrology(), 'None')
        w.set_hydrology(LIQUID)
        self.assertEquals(w.get_hydrology(), 'Predominantly Liquid')
        self.checkDispo(w, [3,1,2,0,2,4])
        w.set_hydrology(LAND)
        self.assertEquals(w.get_hydrology(), 'Predominantly Land')
        self.checkDispo(w, [2,2,2,1,2,3])
        self.assertRaises(InvalidChoice, w.set_hydrology, 'Whatever I feel like')
    def testTopography(self):
        w = World()
        self.assertEquals(w.get_topography(), 'None')
        w.set_topography(ARTIFICIAL) 
        self.assertEquals(w.get_topography(), 'Artificially Created Environs')
        self.checkDispo(w, [1,3,2,3,1,2])
        w.set_topography(RUGGED)
        self.assertEquals(w.get_topography(), 'Naturally Rugged and/or Broken Terrain')
        self.checkDispo(w, [2,1,3,1,3,2])
        w.set_topography(TAME)
        self.assertEquals(w.get_topography(), 'Naturally Tame and/or Habitable Terrain')
        self.checkDispo(w, [1,4,1,2,2,2])
        w.set_topography(BROAD)
        self.assertEquals(w.get_topography(), 'Broad Range of Conditions')
        self.checkDispo(w, [3,2,1,1,2,3])
        self.assertRaises(InvalidChoice, w.set_topography, 'Whatever I feel like')
    def testIndex(self):
        w = World()
        self.assertEquals(w.get_index(), 'None')
        self.assertRaises(InvalidChoice, w.set_index, 'Whatever I feel like')
        w.set_index(SUB) 
        self.assertEquals(w.get_index(), 'Sub Index')
        self.checkDispo(w, [2,1,3,3,2,1])
        w.set_index(ZERO)
        self.assertEquals(w.get_index(), 'Zero Index')
        self.checkDispo(w, [2,2,2,2,3,1])
        w.set_index(LOW)
        self.assertEquals(w.get_index(), 'Low Index')
        self.checkDispo(w, [2,3,1,2,2,2])
        self.assertTrue('Spacefarer' in w.native_settings())
        w.set_index(HIGH)
        self.assertEquals(w.get_index(), 'High Index')
        self.checkDispo(w, [1,4,1,2,1,3])
        self.assertTrue('Spacefarer' in w.native_settings())

    def testCustomizeIndex(self):
        """add any number of items to special 'barred' list, and up to one item to special 'allowed' list
        whenever the index is changed, clear the lists
        """
        w=World()
        self.assertRaises(InvalidChoice, w.add_barred_tech, 'Anything')
        self.assertRaises(InvalidChoice, w.set_allowed_tech, 'Anything')
        self.assertEquals(w.get_barred_tech(), [])
        self.assertEquals(w.get_allowed_tech(), BLANK)
        w.set_index(SUB)
        w.add_barred_tech('Steel')
        w.add_barred_tech('Fire')
        w.add_barred_tech('Language')
        w.set_allowed_tech('Magic')
        self.assertTrue('Steel' in w.get_barred_tech())
        self.assertTrue('Fire' in w.get_barred_tech())
        self.assertTrue('Language' in w.get_barred_tech())
        w.remove_barred_tech('Language')
        self.assertFalse('Language' in w.get_barred_tech())
        self.assertEquals(w.get_allowed_tech(), 'Magic')
        w.set_index(HIGH)
        self.assertEquals(w.get_barred_tech(), [])
        self.assertEquals(w.get_allowed_tech(), BLANK)
        self.assertRaises(InvalidChoice, w.set_allowed_tech, 'Anything')
        
        
    def testGovernment(self):
        w = World()
        self.assertEquals(w.get_government(), 'None')
        self.assertRaises(InvalidChoice, w.set_government, 'Whatever I feel like')
        w.set_government(COMMUNE) 
        self.assertEquals(w.get_government(), 'Civilian Commune')
        self.checkDispo(w, [2,2,2,2,2,2])
        self.assertTrue('Commune' in w.native_settings())
        w.set_government(STEWARD) 
        self.assertEquals(w.get_government(), 'Imperial Stewardship')
        self.checkDispo(w, [2,3,1,1,2,3])
        self.assertTrue('Stewardship and Court' in w.native_settings())
        w.set_government(LAWLESS)
        self.assertEquals(w.get_government(), 'Lawless or Anarchic')
        self.checkDispo(w, [3,1,2,0,6,0])
        w.set_government(LEAGUE) 
        self.assertEquals(w.get_government(), 'Merchant League')
        self.checkDispo(w, [3,2,1,1,1,4])
        self.assertTrue('Merchant League' in w.native_settings())
        w.set_government(DICTATORSHIP)
        self.assertEquals(w.get_government(), 'Military Dictatorship')
        self.checkDispo(w, [1,5,0,2,1,3])
        self.assertTrue('Anvil' in w.native_settings())
        self.assertFalse('Hammer' in w.native_settings())
        w.set_index(LOW)
        self.assertTrue('Hammer' in w.native_settings())
        w.set_index(ZERO)
        self.assertFalse('Hammer' in w.native_settings())
        w.set_index(HIGH)
        self.assertTrue('Hammer' in w.native_settings())
        w.set_index(SUB)
        self.assertFalse('Hammer' in w.native_settings())
    def testNobleGovernment(self):
        """test Noble fief government
        nobility setting is native,
        requires slaves faction
        """
        w = World()
        w.set_government(NOBLE) 
        self.assertEquals(w.get_government(), 'Noble Fief')
        self.assertTrue('Nobility' in w.native_settings())
        self.assertTrue(SLAVES in w.get_factions())
        self.checkDispo(w, [6,5,1,2,1,3])
        self.assertRaises(InvalidChoice, w.remove_faction, SLAVES)
    def testTheocracy(self):
        """test Theocracy government
        theocracy becomes native,
        volunteer army not allowed
        """
        w = World()
        w.set_government(THEOCRACY)
        self.assertEquals(w.get_government(), 'Theocracy')
        self.assertTrue('Theocracy' in w.native_settings())
        self.checkDispo(w, [1,4,1,3,0,3])
        self.assertRaises(InvalidChoice, w.set_military, VOLUNTEER)
        
    def testFactions(self):
        w = World()
        self.assertEquals(w.get_factions(), [])
        w.add_faction(COMMUNES)
        self.checkDispo(w, [4,1,1,0,0,0])
        self.assertTrue(COMMUNES in w.get_factions())
        self.assertTrue('Commune' in w.native_settings())
        w.remove_faction(COMMUNES)
        self.assertFalse(COMMUNES in w.get_factions())
        
        w.add_faction(CULTS) 
        self.assertTrue(CULTS in w.get_factions())
        self.assertTrue('Theocracy' in w.native_settings())
        
        w.add_faction(COURT)
        self.assertTrue(COURT in w.get_factions())
        self.assertTrue('Stewardship and Court' in w.native_settings())

        w.add_faction(ALIENS)
        self.assertTrue(ALIENS in w.get_factions())
        self.assertTrue('Mukhadish Slave' in w.native_settings())
        self.assertTrue('Mukhadish Wild' in w.native_settings())
        self.assertTrue('Shudren' in w.native_settings())

        w.add_faction(KERRN) 
        self.assertTrue(KERRN in w.get_factions())
        self.assertTrue('Kerrn Diazspherah' in w.native_settings())

        w.add_faction(CORP) 
        self.assertTrue(CORP in w.get_factions())
        self.assertTrue('Merchant League' in w.native_settings())

        w.add_faction(JUNTA) 
        self.assertTrue(JUNTA in w.get_factions())
        self.assertTrue('Anvil' in w.native_settings())
        self.assertFalse('Hammer' in w.native_settings())
        w.set_index(LOW)
        self.assertTrue('Hammer' in w.native_settings())
        w.set_index(ZERO)
        self.assertFalse('Hammer' in w.native_settings())
        w.set_index(HIGH)
        self.assertTrue('Hammer' in w.native_settings())
        w.set_index(SUB)
        self.assertFalse('Hammer' in w.native_settings())

        w.add_faction(CRIME)
        self.assertTrue(CRIME in w.get_factions())

        w.add_faction(REBELS)
        self.assertTrue(REBELS in w.get_factions())
        self.assertTrue('Nobility' in w.native_settings())

        w.add_faction(SLAVES) 
        self.assertTrue(SLAVES in w.get_factions())
        self.assertTrue('Servitude and Serfdom' in w.native_settings())
        self.assertTrue('Mukhadish Slave' in w.native_settings())
        
        w.add_faction(CHURCHES)
        self.assertTrue(CHURCHES in w.get_factions())
        self.assertTrue('Theocracy' in w.native_settings())

    def testFoundation(self):
        """test foundation faction: makes foundations native,
        requires low or high index
        """
        w = World()
        self.assertRaises(InvalidChoice, w.add_faction, FOUNDATION)
        w.set_index(HIGH)
        w.add_faction(FOUNDATION)
        self.assertTrue(FOUNDATION in w.get_factions())
        self.assertTrue('Psychologist Foundation' in w.native_settings())
        w.set_index(ZERO)
        self.assertFalse(FOUNDATION in w.get_factions())
        self.assertRaises(InvalidChoice, w.add_faction, FOUNDATION)
        w.set_index(LOW)
        w.add_faction(FOUNDATION)
        self.assertTrue(FOUNDATION in w.get_factions())
        w.set_index(SUB)
        self.assertFalse(FOUNDATION in w.get_factions())
        self.assertRaises(InvalidChoice, w.add_faction, FOUNDATION)
        
    def testRemoveFreeman(self):
        """test remove freeman option
        freeman becomes non native
        requires slaves and serfs
        not allowed if commune government or faction
        """
        w = World()
        w.set_remove_freemen(True)
        self.assertFalse('Freeman' in w.native_settings())
        self.assertTrue(SLAVES in w.get_factions())
        self.checkDispo(w, [4,4,4,3,0,0])
        self.assertRaises(InvalidChoice, w.remove_faction, SLAVES)
        w.set_remove_freemen(False)
        self.assertTrue('Freeman' in w.native_settings())
        w.remove_faction(SLAVES)
        self.checkDispo(w, [0,0,0,0,0,0])

        w.set_remove_freemen(True)
        w.set_government(COMMUNE)
        self.assertTrue('Freeman' in w.native_settings())
        w.remove_faction(SLAVES)
        self.checkDispo(w, [2,2,2,2,2,2])
        self.assertRaises(InvalidChoice, w.set_remove_freemen, True)

        w = World()
        w.set_remove_freemen(True)
        w.add_faction(COMMUNES)
        self.assertTrue('Freeman' in w.native_settings())
        w.remove_faction(SLAVES)
        self.checkDispo(w, [4,1,1,0,0,0])
        self.assertRaises(InvalidChoice, w.set_remove_freemen, True)
    def testRemoveSpacefarer(self):
        """test blockade: make spacefarer lifepaths completely unavailable
        requires all of:
            * dictatorship or junta,
            * tight regulation
            * advanced or strict quarantine
        """
        w = World()
        self.assertRaises(InvalidChoice, w.set_blockade, True)
        w.set_regulation(TIGHT)
        self.assertRaises(InvalidChoice, w.set_blockade, True)
        w.set_quarantine(STRICT)
        self.assertRaises(InvalidChoice, w.set_blockade, True)
        w.set_government(DICTATORSHIP)
        w.set_blockade(True)
        self.assertTrue(w.blockade)

        w.set_regulation(LOOSE)
        self.assertFalse(w.blockade)
        self.assertRaises(InvalidChoice, w.set_blockade, True)

        w.set_regulation(TIGHT)
        w.set_blockade(True)
        w.set_quarantine(ADVANCED)
        self.assertTrue(w.blockade)
        w.set_quarantine(NONE)
        self.assertFalse(w.blockade)
        self.assertRaises(InvalidChoice, w.set_blockade, True)

        w.set_quarantine(STRICT)
        w.set_blockade(True)
        w.set_government(COMMUNE)
        self.assertFalse(w.blockade)
        self.assertRaises(InvalidChoice, w.set_blockade, True)

        w.add_faction(JUNTA)
        w.set_blockade(True)
        self.assertTrue(w.blockade)
        w.remove_faction(JUNTA)
        self.assertFalse(w.blockade)
        self.assertRaises(InvalidChoice, w.set_blockade, True)
        
        w.set_government(DICTATORSHIP)
        w.set_blockade(True)
        self.assertTrue(w.blockade)
        w.add_faction(JUNTA)
        w.set_government(COMMUNE)
        self.assertTrue(w.blockade)

        
    def testMilitaryLevy(self):
        w = World()
        self.assertEquals(w.get_military(), 'None')
        self.assertRaises(InvalidChoice, w.set_military, 'Whatever I feel like')
        w.set_military(LEVY)
        self.assertEquals(w.get_military(), 'Levy')
        self.checkDispo(w, [3,1,2,1,3,2])
    def testMilitaryLP(self):
        """test lords-pilot military
        requires noble or steward government, orrebel faction
        requires slave faction
        Nobility, Hammer and Anvil become native
        """
        w = World()
        self.assertRaises(InvalidChoice, w.set_military, LORDSPILOT)
        w.set_government(STEWARD)
        w.set_military(LORDSPILOT)
        self.assertEquals(w.get_military(), 'Lords-Pilot')
        self.assertTrue('Nobility' in w.native_settings())
        self.assertTrue('Anvil' in w.native_settings())
        self.assertFalse('Hammer' in w.native_settings())
        w.set_index(LOW)
        self.assertTrue('Hammer' in w.native_settings())
        w.set_index(ZERO)
        self.assertFalse('Hammer' in w.native_settings())
        w.set_index(HIGH)
        self.assertTrue('Hammer' in w.native_settings())
        w.set_index(SUB)
        self.assertFalse('Hammer' in w.native_settings())
        self.assertTrue(SLAVES in w.get_factions())
        self.assertRaises(InvalidChoice, w.remove_faction, SLAVES)
        self.checkDispo(w, [9,8,7,6,5,7])
        w.set_government(COMMUNE)
        self.assertEquals(w.get_military(), 'None')
        self.assertRaises(InvalidChoice, w.set_military, LORDSPILOT)
        w.remove_faction(SLAVES)
        self.checkDispo(w, [4,3,5,5,4,3])
        w.add_faction(REBELS)
        self.checkDispo(w, [8,4,6,5,4,3])
        w.set_military(LORDSPILOT)
        self.assertTrue('Anvil' in w.native_settings())
        self.assertFalse('Hammer' in w.native_settings())
        w.set_index(LOW)
        self.assertTrue('Hammer' in w.native_settings())
        w.set_index(ZERO)
        self.assertFalse('Hammer' in w.native_settings())
        w.set_index(HIGH)
        self.assertTrue('Hammer' in w.native_settings())
        w.set_index(SUB)
        self.assertFalse('Hammer' in w.native_settings())
        self.assertTrue(SLAVES in w.get_factions())
        self.assertRaises(InvalidChoice, w.remove_faction, SLAVES)
        self.checkDispo(w, [9,7,8,7,5,6])
        w.remove_faction(REBELS)
        self.assertEquals(w.get_military(), 'None')
        w.remove_faction(SLAVES)
        self.checkDispo(w, [4,3,5,5,4,3])
        self.assertRaises(InvalidChoice, w.set_military, LORDSPILOT)
        w.set_government(NOBLE)
        self.checkDispo(w, [8,6,4,5,3,4])
        w.set_military(LORDSPILOT)
        self.assertTrue('Anvil' in w.native_settings())
        self.assertFalse('Hammer' in w.native_settings())
        w.set_index(LOW)
        self.assertTrue('Hammer' in w.native_settings())
        w.set_index(ZERO)
        self.assertFalse('Hammer' in w.native_settings())
        w.set_index(HIGH)
        self.assertTrue('Hammer' in w.native_settings())
        w.set_index(SUB)
        self.assertFalse('Hammer' in w.native_settings())
        self.checkDispo(w, [9,9,6,7,4,7])
        
    def testMilitaryVolunteer(self):
        """test volunteed military:
        not allowed if theocracy government,
        makes hammer and anvil native,
        complex lifepath interactions
        """
        w = World()
        w.set_military(VOLUNTEER)
        self.assertEquals(w.get_military(), 'Professional Volunteer Force')
        self.checkDispo(w, [2,3,1,2,2,2])
        self.assertTrue('Anvil' in w.native_settings())
        self.assertFalse('Hammer' in w.native_settings())
        w.set_index(LOW)
        self.assertTrue('Hammer' in w.native_settings())
        w.set_index(ZERO)
        self.assertFalse('Hammer' in w.native_settings())
        w.set_index(HIGH)
        self.assertTrue('Hammer' in w.native_settings())
        w.set_index(SUB)
        self.assertFalse('Hammer' in w.native_settings())

        w.set_government(THEOCRACY)
        self.assertEquals(w.get_military(), 'None')
        self.assertRaises(InvalidChoice, w.set_military, VOLUNTEER)
        
    def testReligiousOrders(self):
        """test religious orders military:
        requires gov: theocracy or factions: institutions or cult churches
        """
        w = World()
        self.assertRaises(InvalidChoice, w.set_military, RELIGIOUS)
        w.set_government(THEOCRACY)
        w.set_military(RELIGIOUS) 
        self.assertEquals(w.get_military(), 'Religious Orders')
        self.checkDispo(w, [3,7,2,4,1,7])
        w.set_government(COMMUNE)
        self.assertEquals(w.get_military(), 'None')
        self.assertRaises(InvalidChoice, w.set_military, RELIGIOUS)
        
        w.add_faction(CHURCHES)
        w.set_military(RELIGIOUS)
        self.checkDispo(w, [8,6,4,3,3,6])
        w.remove_faction(CHURCHES)
        self.assertEquals(w.get_military(), 'None')
        self.assertRaises(InvalidChoice, w.set_military, RELIGIOUS)

        w.add_faction(CULTS)
        w.set_military(RELIGIOUS)
        self.checkDispo(w, [8,6,4,3,3,6])
        w.remove_faction(CULTS)
        self.assertEquals(w.get_military(), 'None')
        self.assertRaises(InvalidChoice, w.set_military, RELIGIOUS)

    def testAttitude(self):
        """test planetary attitude
        attitude is free required trait for a character born in any native setting
        """
        w = World()
        self.assertEquals(w.get_attitude(), 'None')
        self.assertRaises(InvalidChoice, w.set_attitude, 'Whatever I feel like')
        
        w.set_attitude(FEAR)
        self.assertEquals(w.get_attitude(), 'Hysterical Fear')
        self.checkDispo(w, [4,4,4,3,3,3])
        w.set_attitude(IGNORANT)
        self.assertEquals(w.get_attitude(), 'Ignorant')
        self.checkDispo(w, [6,6,6,0,0,0])
        w.set_attitude(INDIFFERENT)
        self.assertEquals(w.get_attitude(), 'Indifferent')
        self.checkDispo(w, [5,5,5,2,2,2])
        w.set_attitude(PARANOID)
        self.assertEquals(w.get_attitude(), 'Paranoid')
        self.checkDispo(w, [3,3,3,4,4,4])
    def testOutVoidAttitudes(self):
        """test educated and experience attitudes
        requires void or outworld
        """
        w = World()
        self.assertRaises(InvalidChoice, w.set_attitude, EDUCATED)
        self.assertRaises(InvalidChoice, w.set_attitude, EXPERIENCE)
        w.set_location(OUT)
        w.set_attitude(EDUCATED)
        self.assertEquals(w.get_attitude(), 'Educated or Informed')
        self.checkDispo(w, [3,3,6,7,7,7])
        w.set_attitude(EXPERIENCE)
        self.assertEquals(w.get_attitude(), 'Personal Experience')
        self.checkDispo(w, [2,2,5,8,8,8])
        w.set_location(CORE)
        self.assertEquals(w.get_attitude(), 'None')
        self.assertRaises(InvalidChoice, w.set_attitude, EDUCATED)
        self.assertRaises(InvalidChoice, w.set_attitude, EXPERIENCE)
        w.set_location(VOID)
        w.set_attitude(EXPERIENCE)
        w.set_attitude(EDUCATED)
        w.set_location(INT)
        self.assertEquals(w.get_attitude(), 'None')
        self.assertRaises(InvalidChoice, w.set_attitude, EDUCATED)
        self.assertRaises(InvalidChoice, w.set_attitude, EXPERIENCE)
    def testExports(self):
        """test exports
        military capital requires llow or high index
        """
        w = World()
        self.assertEquals(w.get_export(), 'None')
        self.assertRaises(InvalidChoice, w.set_export, 'Whatever I feel like')
        w.set_export(AGRICULTURE)
        self.assertEquals(w.get_export(), 'Agriculture')
        self.checkDispo(w, [4,1,1,1,3,2])
        w.set_export(INDUSTRIAL)
        self.assertEquals(w.get_export(), 'Industrial Capital')
        self.checkDispo(w, [2,2,2,1,2,3])
        w.set_export(MATERIALS)
        self.assertEquals(w.get_export(), 'Raw Materials')
        self.checkDispo(w, [1,2,3,1,3,2])
        w.set_export(GOODS)
        self.assertEquals(w.get_export(), 'Refined Goods')
        self.checkDispo(w, [1,3,2,2,2,2])
        w.set_export(SKILLED)
        self.assertEquals(w.get_export(), 'Services or Skilled Labor')
        self.checkDispo(w, [3,3,0,2,2,2])
        w.set_export(UNSKILLED)
        self.assertEquals(w.get_export(), 'Unskilled Labor')
        self.checkDispo(w, [3,1,2,1,2,3])
        
        self.assertRaises(InvalidChoice, w.set_export, MILITARY)
        w.set_index(LOW)
        w.set_export(MILITARY)
        self.assertEquals(w.get_export(), 'Military Capital')
        self.checkDispo(w, [4,6,2,2,3,7])
        w.set_index(ZERO)
        self.assertEquals(w.get_export(), 'None')
        self.assertRaises(InvalidChoice, w.set_export, MILITARY)
        w.set_index(HIGH)
        w.set_export(MILITARY)
        self.assertEquals(w.get_export(), 'Military Capital')
        w.set_index(SUB)
        self.assertEquals(w.get_export(), 'None')
        self.assertRaises(InvalidChoice, w.set_export, MILITARY)
        
    def testQuarantine(self):
        """test quarantine behaviors
        : strict requires high, advanced requires low or high
        """
        w = World()
        self.assertEquals(w.get_quarantine(), 'None')
        w.set_quarantine(NONE)
        self.assertEquals(w.get_quarantine(), 'No Quarantine')
        self.checkDispo(w, [4,4,4,0,0,0])
        w.set_quarantine(STANDARD)
        self.assertEquals(w.get_quarantine(), 'Standard Quarantine')
        self.checkDispo(w, [3,3,3,2,2,2])

        self.assertRaises(InvalidChoice, w.set_quarantine, ADVANCED)
        w.set_index(LOW)
        w.set_quarantine(ADVANCED)
        self.assertEquals(w.get_quarantine(), 'Advanced Quarantine')
        self.checkDispo(w, [4,5,3,5,5,5])
        w.set_index(ZERO)
        self.assertEquals(w.get_quarantine(), 'None')
        self.assertRaises(InvalidChoice, w.set_quarantine, ADVANCED)
        w.set_index(HIGH)
        w.set_quarantine(ADVANCED)
        self.assertEquals(w.get_quarantine(), 'Advanced Quarantine')
        w.set_index(SUB)
        self.assertEquals(w.get_quarantine(), 'None')
        self.assertRaises(InvalidChoice, w.set_quarantine, ADVANCED)
        
        w.set_quarantine(STRICT)
        self.assertEquals(w.get_quarantine(), 'Strict Quarantine')
        self.assertEquals(w.get_index(), 'High Index')
        self.checkDispo(w, [2,5,2,6,5,7])
        w.set_index(LOW)
        self.assertEquals(w.get_quarantine(), 'None')
    def testQuarantineCustomize(self):
        """for each level, choose some items that are or are not quarantined
        Standard Quarantine: up to 3 items under quarantine
        Advanced Quarantine: up to 3 items not under quarantine
        Strict quarantine: one item not under quarantine
        Readiness: 2 items are required for standard or advanced before the world is ready
        """
        w = World(name = 'Quarantinery', empire=COMORAN, location=INT, atmosphere=HLS,
                  topography=BROAD, index=HIGH, government=NOBLE,
                  military=LORDSPILOT, attitude=PARANOID, export=INDUSTRIAL,
                  regulation=LOOSE, hydrology=LAND)
        w.set_quarantine(NONE)
        self.assertRaises(InvalidChoice, w.add_quarantine_item, 'Livestock')
        self.assertTrue(w.ready())
        self.assertEquals(w.get_quarantine_items(), [])
        w.set_quarantine(STANDARD)
        self.assertFalse(w.ready())
        self.assertEquals(w.get_quarantine_items(), [])
        w.add_quarantine_item('Livestock')
        self.assertEquals(w.get_quarantine_items(), ['Livestock'])
        self.assertFalse(w.ready())
        w.add_quarantine_item('Python Programmers')
        self.assertEquals(w.get_quarantine_items(), ['Livestock', 'Python Programmers'])
        self.assertTrue(w.ready())
        w.add_quarantine_item('Medical Machinery')
        self.assertEquals(w.get_quarantine_items(), ['Livestock', 'Python Programmers', 'Medical Machinery'])
        self.assertTrue(w.ready())
        self.assertRaises(InvalidChoice, w.add_quarantine_item, 'Pets')
        w.remove_quarantine_item('Python Programmers')
        w.add_quarantine_item('Pets')
        self.assertEquals(w.get_quarantine_items(), ['Livestock', 'Medical Machinery', 'Pets'])
        w.set_quarantine(NONE)
        self.assertEquals(w.get_quarantine_items(), [])
        w.set_quarantine(STANDARD)
        w.add_quarantine_item('Livestock')
        w.set_quarantine(ADVANCED)
        self.assertEquals(w.get_quarantine_items(), [])
        self.assertFalse(w.ready())
        w.add_quarantine_item('Livestock')
        w.add_quarantine_item('Medical Machinery')
        self.assertTrue(w.ready())
        w.add_quarantine_item('Pets')
        self.assertRaises(InvalidChoice, w.add_quarantine_item, 'Python Programmers')
        self.assertEquals(w.get_quarantine_items(), ['Livestock', 'Medical Machinery', 'Pets'])
        w.set_quarantine(STRICT)
        self.assertEquals(w.get_quarantine_items(), ['Livestock'])
        self.assertTrue(w.ready())
        w.remove_quarantine_item('Livestock')
        self.assertFalse(w.ready())
        w.add_quarantine_item('Pets')
        self.assertRaises(InvalidChoice, w.add_quarantine_item, 'Python Programmers')
        w.set_quarantine(ADVANCED)
        self.assertEquals(w.get_quarantine_items(), ['Pets'])
        w.set_quarantine(STANDARD)
        self.assertEquals(w.get_quarantine_items(), [])
    def testRegulation(self):
        w = World()
        self.assertEquals(w.get_regulation(), 'None')
        w.set_regulation(UNREGULATED)
        self.assertEquals(w.get_regulation(), 'Unregulated')
        self.checkDispo(w, [3,0,3,1,3,2])
        w.set_regulation(LOOSE)
        self.assertEquals(w.get_regulation(), 'Loosely Regulated')
        self.checkDispo(w, [1,1,3,2,2,2])
    def testModerateTightRegs(self):
        """These are not permitted with the Lawless government
        """
        w = World()
        w.set_regulation(MODERATE)
        self.assertEquals(w.get_regulation(), 'Moderately Regulated')
        self.checkDispo(w, [0,4,2,3,2,1])
        w.set_government(LAWLESS)
        self.assertEquals(w.get_regulation(), 'None')
        self.assertRaises(InvalidChoice, w.set_regulation, MODERATE)
        w.set_government(COMMUNE)
        w.set_regulation(TIGHT)
        self.assertEquals(w.get_regulation(), 'Tightly Regulated')
        self.checkDispo(w, [3,7,2,6,3,3])
        w.set_government(LAWLESS)
        self.assertEquals(w.get_regulation(), 'None')
        self.assertRaises(InvalidChoice, w.set_regulation, TIGHT)
    def testCustomizeRegulation(self):
        """depending on the level of regulation, a different number of goods must be placed on restricted lists
        Loose: pick one item that is restricted/unavailable, a few others that fall under tariffs or high taxes
        Moderate: pick one or two items that are unavailable and a handful of others that are taxed/regulated
        Tight: pick two items that are simple unavailable, everything else is regulated
        After choosing unavailable...
        Tight: choose one from code 3, 2 from code 2, three from code 1, must include primary export
        Moderate: choose one or two from code 2 and two from code 1.  if the primary export is code 1 or 2, it must be regulated
        Loose: a handful of items from the code 1 list, does not need to include primary export

        I admit to not understanding this
        """
        pass
    def testReady(self):
        w = World(name='TestLand', empire=COMORAN, location=INT, atmosphere=HLS,
                  topography=BROAD, index=LOW, government=NOBLE,
                  military=LORDSPILOT, attitude=PARANOID, export=INDUSTRIAL,
                  quarantine=NONE, regulation=LOOSE, hydrology=LAND)
        self.assertTrue(w.ready())

        w.set_empire(BLANK)
        self.assertFalse(w.ready())
        w.set_empire(COMORAN)
        self.assertTrue(w.ready())

        w.set_location(BLANK)
        self.assertFalse(w.ready())
        w.set_location(INT)
        self.assertTrue(w.ready())

        w.set_atmosphere(BLANK)
        self.assertFalse(w.ready())
        w.set_atmosphere(HLS)
        self.assertTrue(w.ready())

        w.set_topography(BLANK)
        self.assertFalse(w.ready())
        w.set_topography(BROAD)
        self.assertTrue(w.ready())

        w.set_index(BLANK)
        self.assertFalse(w.ready())
        w.set_index(LOW)
        self.assertTrue(w.ready())

        w.set_quarantine(BLANK)
        self.assertFalse(w.ready())
        w.set_quarantine(NONE)
        self.assertTrue(w.ready())

        w.set_government(BLANK)
        self.assertFalse(w.ready())
        w.set_government(NOBLE)
        self.assertFalse(w.ready())
        w.set_military(LORDSPILOT)
        self.assertTrue(w.ready())
        
        w.set_military(BLANK)
        self.assertFalse(w.ready())
        w.set_military(LORDSPILOT)
        self.assertTrue(w.ready())

        w.set_attitude(BLANK)
        self.assertFalse(w.ready())
        w.set_attitude(PARANOID)
        self.assertTrue(w.ready())

        w.set_export(BLANK)
        self.assertFalse(w.ready())
        w.set_export(INDUSTRIAL)
        self.assertTrue(w.ready())

        w.set_quarantine(BLANK)
        self.assertFalse(w.ready())
        w.set_quarantine(NONE)
        self.assertTrue(w.ready())

        w.set_regulation(BLANK)
        self.assertFalse(w.ready())
        w.set_regulation(LOOSE)
        self.assertTrue(w.ready())

        w.set_hydrology(BLANK)
        self.assertFalse(w.ready())
        w.set_hydrology(LAND)


        w = World()
        self.assertFalse(w.ready())
        w.set_empire(COMORAN)
        self.assertFalse(w.ready())
        w.set_location(INT)
        self.assertFalse(w.ready())
        w.set_atmosphere(HLS)
        self.assertFalse(w.ready())
        w.set_topography(BROAD)
        self.assertFalse(w.ready())
        w.set_index(LOW)
        self.assertFalse(w.ready())
        w.set_government(NOBLE)
        self.assertFalse(w.ready())
        w.set_military(LORDSPILOT)
        self.assertFalse(w.ready())
        w.set_attitude(PARANOID)
        self.assertFalse(w.ready())
        w.set_export(INDUSTRIAL)
        self.assertFalse(w.ready())
        w.set_quarantine(NONE)
        self.assertFalse(w.ready())
        w.set_regulation(LOOSE)
        self.assertFalse(w.ready())
        w.set_hydrology(LAND)
        self.assertFalse(w.ready())
        w.set_name('ReadyTowne')
        self.assertTrue(w.ready())
    def testWiki(self):
        w = World()
        self.assertEquals(w.wikicode(), """== Galactic Location: None ==
== Atmospheric Conditions: None ==
== Hydrology: None ==
== Topography: None ==
== Tech Index: None ==
== Dominant Form of Government: None ==
== Predominant Military: None ==
== Planetary Attitude toward Vaylen: None ==
== Primary Export or Industry: None ==
== Level of Quarantine: None ==
== Level of Economic Regulation: None ==
== Infection Dispositions ==
{| border="1"
!
!Infiltration
!Usurpation
!Invasion
|- align=center
|\'\'\'Vaylen\'\'\'
|0
|0
|0
|-align=center
|\'\'\'Human\'\'\'
|0
|0
|0
|-
|}
== Figures of Note ==
{|border="1"
!
!Infiltration
!Usurpation
!Invasion
|- align=center
|'''Vaylen'''
|N/A
|N/A
|N/A
|-align=center
|'''Human'''
|N/A
|N/A
|N/A
|-
|}
made with BET
[[Category: Worlds]]""")

    def testSaveLoad(self):
        w = World()
        self.assertFalse(w.ready())
        self.assertRaises(Exception, w.save)
        w = World(empire=COMORAN, location=INT, atmosphere=HLS,
                  topography=BROAD, index=LOW, government=NOBLE,
                  military=LORDSPILOT, attitude=PARANOID, export=INDUSTRIAL,
                  quarantine=NONE, regulation=LOOSE, hydrology=LAND)
        self.assertRaises(Exception, w.save)
        w.set_name('Halifax')
        w.save()
        halifax = World()
        halifax.load('Halifax')
        self.assertEquals(w.get_empire(), halifax.get_empire())
        self.assertEquals(w.get_location(), halifax.get_location())
        self.assertEquals(w.get_atmosphere(), halifax.get_atmosphere())
        self.assertEquals(w.get_topography(),halifax.get_topography())
        self.assertEquals(w.get_hydrology(), halifax.get_hydrology())
        self.assertEquals(w.get_index(), halifax.get_index())
        self.assertEquals(w.get_government(), halifax.get_government())
        self.assertEquals(w.get_military(), halifax.get_military())
        self.assertEquals(w.get_export(), halifax.get_export())
        self.assertEquals(w.get_attitude(), halifax.get_attitude())
        self.assertEquals(w.get_quarantine(), halifax.get_quarantine())
        self.assertEquals(w.get_regulation(), halifax.get_regulation())
        self.assertEquals(w.get_name(), halifax.get_name())
        os.remove('Halifax.world')

        
if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=1).run(unittest.TestLoader().loadTestsFromTestCase(WorldBurnerTests))
