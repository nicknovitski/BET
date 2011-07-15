import pickle

class InvalidChoice(Exception):
    def __init__(self, msg='Choice is invalid'):
        self.msg = msg
    def __str__(self):
        return self.msg

BLANK = 'None'

CASIGURAN = 'Casiguran Matriarchy'
COMORAN = 'Comoran Worlds'
DARIKAHN = 'Darikahn Empire'
DUNEDIN = 'Dunedin Worlds'
GONZAGIN = 'Gonzagin Empire'
KARSAN = 'Karsan League'
KUDUS = 'Kudus Theocracy'
URFAN = 'Urfan Worlds'
EMPIRES = [BLANK, CASIGURAN, COMORAN, DARIKAHN, DUNEDIN, GONZAGIN, KARSAN, KUDUS, URFAN]

CORE = 'Old Imperial Core World'
INT = 'Interior World'
OUT = 'Outworld'
VOID = 'Void World'
LOCATIONS = [BLANK, CORE, INT, OUT, VOID]

ALS = 'Alien-Life-Supporting'
HLS = 'Human-Life-Supporting'
NLS = 'Non-Life-Supporting'
PLS = 'Partial-Life-Supporting'
ATMOSPHERES = [BLANK, ALS, HLS, NLS, PLS]

LIQUID = 'Predominantly Liquid'
LAND = 'Predominantly Land'
HYDROLOGIES = [BLANK, LIQUID, LAND]

ARTIFICIAL = 'Artificially Created Environs'
RUGGED = 'Naturally Rugged and/or Broken Terrain'
TAME = 'Naturally Tame and/or Habitable Terrain'
BROAD = 'Broad Range of Conditions'
TOPOGRAPHIES = [BLANK, ARTIFICIAL, RUGGED, TAME, BROAD]

SUB = 'Sub Index'
ZERO = 'Zero Index'
LOW = 'Low Index'
HIGH = 'High Index'
INDICES = [BLANK, SUB, ZERO, LOW, HIGH]

COMMUNE = 'Civilian Commune'
STEWARD = 'Imperial Stewardship'
LAWLESS = 'Lawless or Anarchic'
LEAGUE = 'Merchant League'
DICTATORSHIP = 'Military Dictatorship'
NOBLE = 'Noble Fief'
THEOCRACY = 'Theocracy'
GOVERNMENTS = [BLANK, COMMUNE, STEWARD, LAWLESS, LEAGUE, DICTATORSHIP, NOBLE, THEOCRACY]

LEVY = 'Levy'
LORDSPILOT = 'Lords-Pilot'
VOLUNTEER = 'Professional Volunteer Force'
RELIGIOUS = 'Religious Orders'
MILITARIES = [BLANK, LEVY, LORDSPILOT, VOLUNTEER, RELIGIOUS]

EDUCATED = 'Educated or Informed'
FEAR = 'Hysterical Fear'
IGNORANT = 'Ignorant'
INDIFFERENT = 'Indifferent'
PARANOID = 'Paranoid'
EXPERIENCE = 'Personal Experience'
ATTITUDES = [BLANK, EDUCATED, FEAR, IGNORANT, INDIFFERENT, PARANOID, EXPERIENCE]


AGRICULTURE ='Agriculture'
INDUSTRIAL = 'Industrial Capital'
MILITARY = 'Military Capital'
MATERIALS = 'Raw Materials'
GOODS = 'Refined Goods'
SKILLED = 'Services or Skilled Labor'
UNSKILLED = 'Unskilled Labor'
EXPORTS = [BLANK, AGRICULTURE, INDUSTRIAL, MILITARY, MATERIALS, GOODS, SKILLED, UNSKILLED]

NONE = 'No Quarantine'
STANDARD = 'Standard Quarantine'
ADVANCED = 'Advanced Quarantine'
STRICT = 'Strict Quarantine'
QUARANTINES = [BLANK, NONE, STANDARD, ADVANCED, STRICT]

UNREGULATED = 'Unregulated'
LOOSE = 'Loosely Regulated'
MODERATE = 'Moderately Regulated'
TIGHT = 'Tightly Regulated'
REGULATIONS = [BLANK, UNREGULATED, LOOSE, MODERATE, TIGHT]

COMMUNES = 'Civilian Communes'
CULTS = 'Cult Churches'
COURT = 'Imperial Bureaucracy and/or Court'
ALIENS = 'Indigenous Life-Forms'
KERRN = 'Kerrn Diazspherah'
CORP = 'Merchant League/Corporate Entity'
JUNTA = 'Military Junta'
CRIME = 'Organized Crime'
FOUNDATION = 'Psychologist Foundation'
REBELS = 'Rebel Line/Royalists'
SLAVES = 'Slaves and Serfs'
CHURCHES = 'Theocratic Institutions'

FACTIONS = [COMMUNES,CULTS, COURT, ALIENS, KERRN, CORP, JUNTA, CRIME, FOUNDATION, REBELS, SLAVES, CHURCHES]

class World(object):
    name= BLANK
    military = BLANK
    attitude = BLANK
    export = BLANK
    quarantine = BLANK
    regulation = BLANK
    faction_list = []
    remove_freemen=False
    blockade = False
    quarantine_items=[]
    index = BLANK
    barred_tech = []
    allowed_tech = BLANK
    def __init__(self, name=BLANK, empire=BLANK, location=BLANK, atmosphere=BLANK,
                 hydrology=BLANK, topography=BLANK, index=BLANK, government=BLANK,
                 military=BLANK, attitude=BLANK, export=BLANK, quarantine=BLANK,
                 regulation=BLANK):
        self.faction_list=[]
        self.set_name(name)
        self.set_empire(empire)
        self.set_location(location)
        self.set_atmosphere(atmosphere)
        self.set_hydrology(hydrology)
        self.set_topography(topography)
        self.set_index(index)
        self.set_government(government)
        self.set_military(military)
        self.set_attitude(attitude)
        self.set_export(export)
        self.set_quarantine(quarantine)
        self.set_regulation(regulation)

    def save(self):
        if not self.ready():
            raise Exception
        f = file(self.get_name()+'.world', 'w')
        pickle.dump(self, f)

    def load(self, filename):
        f = file(filename+'.world', 'r')
        loaded = pickle.load(f)
        settings = [(self.set_empire,loaded.get_empire),
                    (self.set_location,loaded.get_location),
                    (self.set_atmosphere,loaded.get_atmosphere),
                    (self.set_topography,loaded.get_topography),
                    (self.set_hydrology,loaded.get_hydrology),
                    (self.set_index,loaded.get_index),
                    (self.set_government, loaded.get_government),
                    (self.set_military, loaded.get_military),
                    (self.set_export, loaded.get_export),
                    (self.set_attitude, loaded.get_attitude),
                    (self.set_quarantine, loaded.get_quarantine),
                    (self.set_regulation,loaded.get_regulation),
                    (self.set_name, loaded.get_name)]
        for change, get in settings:
            change(get())
        
    def wikicode(self):
        wiki = ""
        if self.get_location() == BLANK:
            gal_loc = self.get_empire()
        else:
            gal_loc = self.get_empire().split(' ')[0] +' ' +self.get_location()
        wiki+= "== Galactic Location: %s ==\n" % gal_loc
        wiki+="== Atmospheric Conditions: %s ==\n" % self.get_atmosphere()
        wiki+="== Hydrology: %s ==\n" % self.get_hydrology()
        wiki+="== Topography: %s ==\n" % self.get_topography()
        wiki+="== Tech Index: %s ==\n" % self.get_index()
        if self.get_allowed_tech() != BLANK:
            wiki+="#Allowed technology from higher index:\n"
            wiki+="##"+ self.get_allowed_tech()
        if self.get_barred_tech() != []:
            wiki+="#Barred technology:"
            for x in self.get_barred_tech():
                wiki+="##"+x
        wiki+="== Dominant Form of Government: %s ==\n" % self.get_government()

        if self.get_factions() or self.remove_freemen or self.blockade:
            wiki+="== Factions ==\n"
            for faction in self.get_factions():
                wiki+="=== %s ===\n" % faction # sub-name?
            if self.remove_freemen:
                wiki+="=== Special Option: Remove Freemen ===\n"
            if self.blockade:
                wiki+="=== Special Option: Blockade (Remove Spacefarer) ===\n"

        wiki+="== Predominant Military: %s ==\n" % self.get_military()
        wiki+="== Planetary Attitude toward Vaylen: %s ==\n" % self.get_attitude()
        wiki+="== Primary Export or Industry: %s ==\n" % self.get_export()
        wiki+="== Level of Quarantine: %s ==\n" % self.get_quarantine()
        wiki+="== Level of Economic Regulation: %s ==\n" % self.get_regulation()
        wiki+="""== Infection Dispositions ==
{{DispositionTotals
|vinf=%(vinf)d
|vus=%(vus)d
|vinv=%(vinv)d
|hinf=%(hinf)d
|hus=%(hus)d
|hinv=%(hinv)d
}}
""" % {'vinf':self.vaylen_infiltration(),'vus':self.vaylen_usurpation(),'vinv':self.vaylen_invasion(),'hinf':self.human_infiltration(),'hus':self.human_usurpation(),'hinv':self.human_invasion()}
        wiki += """== Figures of Note ==
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
"""
        wiki += "made with BET\n"
        wiki += "[[Category: Worlds]]"
        return wiki
    def print_wiki(self):
        print self.wikicode()

    def ready(self):
        for get in [self.get_empire, self.get_location, self.get_atmosphere,
                    self.get_topography, self.get_hydrology, self.get_index,
                    self.get_government, self.get_military, self.get_export,
                    self.get_attitude, self.get_quarantine, self.get_regulation,
                    self.get_name]:
            if get() == BLANK:
                return False
        if self.get_quarantine() in [STANDARD, ADVANCED] and len(self.get_quarantine_items()) < 2:
            return False
        elif self.get_quarantine() == STRICT and len(self.get_quarantine_items()) == 0:
            return False
        return True
    def get_name(self):
        return self.name
    def set_name(self, n):
        self.name = n
    def vaylen_infiltration(self):
        locations = {BLANK:0, CORE:2, INT:2, OUT:1, VOID:2}
        atmospheres = {BLANK:0, ALS:3, HLS:2, NLS:1, PLS:3}
        hydrologies = {BLANK:0, LIQUID:3, LAND:2}
        topographies = {BLANK:0, ARTIFICIAL:1, RUGGED:2, TAME:1, BROAD:3}
        indices = {BLANK:0, SUB:2, ZERO:2, LOW:2, HIGH:1}
        governments = {BLANK:0, COMMUNE:2, STEWARD:2, LAWLESS:3, LEAGUE:3, DICTATORSHIP:1, NOBLE:2, THEOCRACY:1}
        militaries = {BLANK:0, LEVY:3, LORDSPILOT:1, VOLUNTEER:2, RELIGIOUS:2}
        attitudes = {BLANK:0, EDUCATED:2, FEAR:4, IGNORANT:6, INDIFFERENT:5, PARANOID:3, EXPERIENCE:1}
        exports = {BLANK:0, AGRICULTURE:4, INDUSTRIAL:2, MILITARY:2, MATERIALS:1, GOODS:1, SKILLED:3, UNSKILLED:3}
        quarantines = {BLANK:0, NONE:4, STANDARD:3, ADVANCED:2, STRICT:1}
        regulations = {BLANK:0, UNREGULATED:3, LOOSE:1, MODERATE:0, TIGHT:1}
        matrix = {self.get_location():locations,
                   self.get_atmosphere():atmospheres,
                   self.get_hydrology():hydrologies,
                   self.get_topography():topographies,
                   self.get_index():indices,
                   self.get_government():governments,
                   self.get_military():militaries,
                  self.get_attitude():attitudes,
                  self.get_export():exports,
                  self.get_quarantine():quarantines,
                  self.get_regulation():regulations}
        value = 0
        for choice, dispositions in matrix.iteritems():
            value += dispositions[choice]
        if self.get_factions() != []:
            value += 4
        return value
    def vaylen_usurpation(self):
        locations = {BLANK:0, CORE:3, INT:2, OUT:1, VOID:2}
        atmospheres = {BLANK:0, ALS:1, HLS:2, NLS:2, PLS:0}
        hydrologies = {BLANK:0, LIQUID:1, LAND:2}
        topographies = {BLANK:0, ARTIFICIAL:3, RUGGED:1, TAME:4, BROAD:2}
        indices = {BLANK:0, SUB:1, ZERO:2, LOW:3, HIGH:4}
        governments = {BLANK:0, COMMUNE:2, STEWARD:3, LAWLESS:1, LEAGUE:2, DICTATORSHIP:5, NOBLE:4, THEOCRACY:4}
        militaries = {BLANK:0, LEVY:1, LORDSPILOT:3, VOLUNTEER:3, RELIGIOUS:3}
        attitudes = {BLANK:0, EDUCATED:2, FEAR:4, IGNORANT:6, INDIFFERENT:5, PARANOID:3, EXPERIENCE:1}
        exports = {BLANK:0, AGRICULTURE:1, INDUSTRIAL:2, MILITARY:3, MATERIALS:2, GOODS:3, SKILLED:3, UNSKILLED:1}
        quarantines = {BLANK:0, NONE:4, STANDARD:3, ADVANCED:2, STRICT:1}
        regulations = {BLANK:0, UNREGULATED:0, LOOSE:1, MODERATE:4, TIGHT:5}
        matrix = {self.get_location():locations,
                   self.get_atmosphere():atmospheres,
                   self.get_hydrology():hydrologies,
                   self.get_topography():topographies,
                   self.get_index():indices,
                   self.get_government():governments,
                   self.get_military():militaries,
                  self.get_attitude():attitudes,
                  self.get_export():exports,
                  self.get_quarantine():quarantines,
                  self.get_regulation():regulations}
        value = 0
        for choice, dispositions in matrix.iteritems():
            value += dispositions[choice]
        if self.get_factions() != []:
            value += 1
        if self.remove_freemen:
            value += 3
        return value
    def vaylen_invasion(self):
        locations = {BLANK:0, CORE:1, INT:2, OUT:4, VOID:8}
        atmospheres = {BLANK:0, ALS:2, HLS:2, NLS:3, PLS:3}
        hydrologies = {BLANK:0, LIQUID:2, LAND:2}
        topographies = {BLANK:0, ARTIFICIAL:2, RUGGED:3, TAME:1, BROAD:1}
        indices = {BLANK:0, SUB:3, ZERO:2, LOW:1, HIGH:1}
        governments = {BLANK:0, COMMUNE:2, STEWARD:1, LAWLESS:2, LEAGUE:1, DICTATORSHIP:0, NOBLE:0, THEOCRACY:1}
        militaries = {BLANK:0, LEVY:2, LORDSPILOT:2, VOLUNTEER:1, RELIGIOUS:1}
        attitudes = {BLANK:0, EDUCATED:2, FEAR:4, IGNORANT:6, INDIFFERENT:5, PARANOID:3, EXPERIENCE:1}
        exports = {BLANK:0, AGRICULTURE:1, INDUSTRIAL:2, MILITARY:1, MATERIALS:3, GOODS:2, SKILLED:0, UNSKILLED:2}
        quarantines = {BLANK:0, NONE:4, STANDARD:3, ADVANCED:2, STRICT:1}
        regulations = {BLANK:0, UNREGULATED:3, LOOSE:3, MODERATE:2, TIGHT:0}
        matrix = {self.get_location():locations,
                   self.get_atmosphere():atmospheres,
                   self.get_hydrology():hydrologies,
                   self.get_topography():topographies,
                   self.get_index():indices,
                   self.get_government():governments,
                   self.get_military():militaries,
                  self.get_attitude():attitudes,
                  self.get_export():exports,
                  self.get_quarantine():quarantines,
                  self.get_regulation():regulations}
        value = 0
        for choice, dispositions in matrix.iteritems():
            value += dispositions[choice]
        if self.get_factions() != []:
            value += 1
        if self.remove_freemen:
            value += 3
        return value
    def human_infiltration(self):
        locations = {BLANK:0, CORE:2, INT:1, OUT:2, VOID:3}
        atmospheres = {BLANK:0, ALS:2, HLS:1, NLS:3, PLS:2}
        hydrologies = {BLANK:0, LIQUID:0, LAND:1}
        topographies = {BLANK:0, ARTIFICIAL:3, RUGGED:1, TAME:2, BROAD:1}
        indices = {BLANK:0, SUB:3, ZERO:2, LOW:2, HIGH:2}
        governments = {BLANK:0, COMMUNE:2, STEWARD:1, LAWLESS:0, LEAGUE:1, DICTATORSHIP:2, NOBLE:2, THEOCRACY:3}
        militaries = {BLANK:0, LEVY:1, LORDSPILOT:2, VOLUNTEER:2, RELIGIOUS:1}
        attitudes = {BLANK:0, EDUCATED:5, FEAR:3, IGNORANT:0, INDIFFERENT:2, PARANOID:4, EXPERIENCE:6}
        exports = {BLANK:0, AGRICULTURE:1, INDUSTRIAL:1, MILITARY:0, MATERIALS:1, GOODS:2, SKILLED:2, UNSKILLED:1}
        quarantines = {BLANK:0, NONE:0, STANDARD:2, ADVANCED:3, STRICT:4}
        regulations = {BLANK:0, UNREGULATED:1, LOOSE:2, MODERATE:3, TIGHT:4}
        matrix = {self.get_location():locations,
                   self.get_atmosphere():atmospheres,
                   self.get_hydrology():hydrologies,
                   self.get_topography():topographies,
                   self.get_index():indices,
                   self.get_government():governments,
                   self.get_military():militaries,
                  self.get_attitude():attitudes,
                  self.get_export():exports,
                  self.get_quarantine():quarantines,
                  self.get_regulation():regulations}
        value = 0
        for choice, dispositions in matrix.iteritems():
            value += dispositions[choice]
        if self.remove_freemen:
            value += 3
        return value
    def human_usurpation(self):
        locations = {BLANK:0, CORE:2, INT:2, OUT:2, VOID:2}
        atmospheres = {BLANK:0, ALS:2, HLS:3, NLS:2, PLS:3}
        hydrologies = {BLANK:0, LIQUID:2, LAND:2}
        topographies = {BLANK:0, ARTIFICIAL:1, RUGGED:3, TAME:2, BROAD:2}
        indices = {BLANK:0, SUB:2, ZERO:3, LOW:2, HIGH:1}
        governments = {BLANK:0, COMMUNE:2, STEWARD:2, LAWLESS:6, LEAGUE:1, DICTATORSHIP:1, NOBLE:1, THEOCRACY:0}
        militaries = {BLANK:0, LEVY:3, LORDSPILOT:1, VOLUNTEER:2, RELIGIOUS:1}
        attitudes = {BLANK:0, EDUCATED:5, FEAR:3, IGNORANT:0, INDIFFERENT:2, PARANOID:4, EXPERIENCE:6}
        exports = {BLANK:0, AGRICULTURE:3, INDUSTRIAL:2, MILITARY:1, MATERIALS:3, GOODS:2, SKILLED:2, UNSKILLED:2}
        quarantines = {BLANK:0, NONE:0, STANDARD:2, ADVANCED:3, STRICT:4}
        regulations = {BLANK:0, UNREGULATED:3, LOOSE:2, MODERATE:2, TIGHT:1}
        matrix = {self.get_location():locations,
                   self.get_atmosphere():atmospheres,
                   self.get_hydrology():hydrologies,
                   self.get_topography():topographies,
                   self.get_index():indices,
                   self.get_government():governments,
                   self.get_military():militaries,
                  self.get_attitude():attitudes,
                  self.get_export():exports,
                  self.get_quarantine():quarantines,
                  self.get_regulation():regulations}
        value = 0
        for choice, dispositions in matrix.iteritems():
            value += dispositions[choice]        
        return value
    def human_invasion(self):
        locations = {BLANK:0, CORE:8, INT:3, OUT:2, VOID:1}
        atmospheres = {BLANK:0, ALS:2, HLS:2, NLS:1, PLS:1}
        hydrologies = {BLANK:0, LIQUID:4, LAND:3}
        topographies = {BLANK:0, ARTIFICIAL:2, RUGGED:2, TAME:2, BROAD:3}
        indices = {BLANK:0, SUB:1, ZERO:1, LOW:2, HIGH:3}
        governments = {BLANK:0, COMMUNE:2, STEWARD:3, LAWLESS:0, LEAGUE:4, DICTATORSHIP:3, NOBLE:3, THEOCRACY:3}
        militaries = {BLANK:0, LEVY:2, LORDSPILOT:3, VOLUNTEER:2, RELIGIOUS:4}
        attitudes = {BLANK:0, EDUCATED:5, FEAR:3, IGNORANT:0, INDIFFERENT:2, PARANOID:4, EXPERIENCE:6}
        exports = {BLANK:0, AGRICULTURE:2, INDUSTRIAL:3, MILITARY:5, MATERIALS:2, GOODS:2, SKILLED:2, UNSKILLED:3}
        quarantines = {BLANK:0, NONE:0, STANDARD:2, ADVANCED:3, STRICT:4}
        regulations = {BLANK:0, UNREGULATED:2, LOOSE:2, MODERATE:1, TIGHT:1}
        value = 0
        matrix = {self.get_location():locations,
                   self.get_atmosphere():atmospheres,
                   self.get_hydrology():hydrologies,
                   self.get_topography():topographies,
                   self.get_index():indices,
                   self.get_government():governments,
                   self.get_military():militaries,
                  self.get_attitude():attitudes,
                  self.get_export():exports,
                  self.get_quarantine():quarantines,
                  self.get_regulation():regulations}
        for choice, dispositions in matrix.iteritems():
            value += dispositions[choice]        
        return value
    def dispositions(self):
        return [self.vaylen_infiltration(), self.vaylen_usurpation(), self.vaylen_invasion(), self.human_infiltration(), self.human_usurpation(), self.human_invasion()]

    def native_settings(self):
        settings = ['Outcast and Criminal', 'Underworld', 'Vaylen']
        if not self.remove_freemen:
            settings.append('Freeman')
        if self.get_atmosphere() == HLS or ALIENS in self.get_factions():
            settings.append('Mukhadish Wild')
        if ALIENS in self.get_factions():
            settings.append('Shudren')
        if self.get_index() in [LOW, HIGH]:
            settings.append('Spacefarer')
        if self.get_government() == COMMUNE or COMMUNES in self.get_factions():
            settings.append('Commune')
        if self.get_government() == STEWARD or COURT in self.get_factions():
            settings.append('Stewardship and Court')
        if self.get_government() == LEAGUE or CORP in self.get_factions():
            settings.append('Merchant League')
        if self.get_government() == DICTATORSHIP or JUNTA in self.get_factions() or self.get_military() in [LORDSPILOT, VOLUNTEER]:
            settings.append('Anvil')
            if self.get_index() in [LOW, HIGH]:
                settings.append('Hammer')
        if self.get_government() == NOBLE or REBELS in self.get_factions() or self.get_military() == LORDSPILOT:
            settings.append('Nobility')
        if self.get_government() == THEOCRACY or CULTS in self.get_factions():
            settings.append('Theocracy')
        if SLAVES in self.get_factions():
            settings.append('Servitude and Serfdom')
        if SLAVES in self.get_factions() or ALIENS in self.get_factions():
            settings.append('Mukhadish Slave')
        if FOUNDATION in self.get_factions():
            settings.append('Psychologist Foundation')
        if KERRN in self.get_factions():
            settings.append('Kerrn Diazspherah')
        return settings

    def get_factions(self):
        return self.faction_list

    def add_faction(self, fac):
        if not fac in FACTIONS:
            raise InvalidChoice
        if fac == FOUNDATION and self.get_index() not in [LOW, HIGH]:
            raise InvalidChoice('Psychologist Foundations require Low or High Tech Index')
        if not fac in self.faction_list:
            self.faction_list.append(fac)
            if fac == COMMUNES:
                self.remove_freemen = False
            
        
    def remove_faction(self, fac):
        if not fac in FACTIONS:
            raise InvalidChoice
        if fac in self.faction_list:
            if fac == ALIENS and self.get_atmosphere() == ALS:
                raise InvalidChoice('Alien-Life-Supporting Atmosphere requires Indigenous Lifeforms faction')
            if fac == SLAVES:
                if self.get_government() == NOBLE:
                    raise InvalidChoice('Noble Fief Government requires Slaves and Serfs faction')
                elif self.get_military() == LORDSPILOT:
                    raise InvalidChoice('Lords-Piliot military requires Slaves and Serfs faction')
                elif self.remove_freemen:
                    raise InvalidChoice('Remove Freemen option requires Slaves and Serfs faction')

            self.faction_list.remove(fac)

            if self.get_military() == LORDSPILOT and self.get_government() not in [STEWARD, NOBLE] and not REBELS in self.get_factions():
                self.set_military(BLANK)
            if fac in [CHURCHES, CULTS] and self.get_military() == RELIGIOUS and self.get_government() != THEOCRACY:
                self.set_military(BLANK)
            if fac == JUNTA and self.get_government() != DICTATORSHIP:
                self.blockade = False

    def set_remove_freemen(self, removal):
        if removal:
            if self.get_government() == COMMUNE or COMMUNES in self.get_factions():
                raise InvalidChoice('Freemen cannot be removed with Commune government or faction')
            self.add_faction(SLAVES)
        self.remove_freemen = removal

    def set_blockade(self, block):
        if block:
            if self.get_government() != DICTATORSHIP and not JUNTA in self.get_factions():
                raise InvalidChoice('Blockade requires Dictatorship Government or Junta Faction')
            if self.get_regulation() != TIGHT:
                raise InvalidChoice('Blockade requires Tight Regulation')
            if not self.get_quarantine() in [STRICT, ADVANCED]:
                raise InvalidChoice('Blockade requires Advanced or Strict Quarantine')
        self.blockade = block
    
    def set_empire(self, empire):
        if empire in EMPIRES:
            self.empire = empire
        else:
            raise InvalidChoice
    def get_empire(self):
        return self.empire
    def print_empire(self):
        print self.get_empire()

    def set_location(self, location):
        if not location in LOCATIONS:
            raise InvalidChoice
        self.location = location
        if self.get_location() in [CORE, INT] and self.get_attitude() in [EDUCATED, EXPERIENCE]:
            self.set_attitude(BLANK)
    def get_location(self):
        return self.location

    def set_atmosphere(self, atmo):
        if atmo in ATMOSPHERES:
            self.atmosphere = atmo
            if self.get_atmosphere() == ALS:
                self.set_topography(ARTIFICIAL)
                self.add_faction(ALIENS)
            elif self.get_atmosphere() == NLS:
                self.set_topography(ARTIFICIAL)
        else:
            raise InvalidChoice
    def get_atmosphere(self):
        return self.atmosphere

    def set_hydrology(self, hydro):
        if hydro in HYDROLOGIES:
            self.hydrology = hydro
        else:
            raise InvalidChoice
    def get_hydrology(self):
        return self.hydrology

    def set_topography(self, topo):
        if not topo in TOPOGRAPHIES:
            raise InvalidChoice('Choice must be valid topography or "None"')
        if self.get_atmosphere() in [ALS,NLS] and topo != ARTIFICIAL:
            if topo != BLANK:
                raise InvalidChoice('Alien-Life-Supporting and Non-Life-Supporting Atmospheres require Artificial Environs')
        self.topography = topo
    def get_topography(self):
        return self.topography

    def set_index(self, i):
        if i in INDICES:
            if self.index != i:
                self.barred_tech = []
                self.allowed_tech = BLANK
            self.index = i
            if not self.get_index() in [LOW, HIGH]:
                self.remove_faction(FOUNDATION)
                if self.get_quarantine() == ADVANCED:
                    self.set_quarantine(BLANK)
                if self.get_export() == MILITARY:
                    self.set_export(BLANK)
            if self.get_index() != HIGH and self.get_quarantine() == STRICT:
                self.set_quarantine(BLANK)
        else:
            raise InvalidChoice
    def get_index(self):
        return self.index
    def add_barred_tech(self, technology):
        if self.get_index() == BLANK:
            raise InvalidChoice
        else:
            self.barred_tech.append(technology)
    def remove_barred_tech(self, technology):
        self.barred_tech.remove(technology)
    def get_barred_tech(self):
        return self.barred_tech
    def set_allowed_tech(self, technology):
        if self.get_index() in [BLANK, HIGH]:
            raise InvalidChoice
        self.allowed_tech = technology
    def get_allowed_tech(self):
        return self.allowed_tech

    def set_government(self, gov):
        if gov in GOVERNMENTS:
            self.government = gov
            if self.get_military() == LORDSPILOT and self.get_government() not in [STEWARD, NOBLE] and not REBELS in self.get_factions():
                self.set_military(BLANK)
            if self.get_government() == NOBLE and not SLAVES in self.get_factions():
                self.add_faction(SLAVES)
            if self.get_government() == LAWLESS and self.get_regulation() in [MODERATE, TIGHT]:
                self.set_regulation(BLANK)
            if self.get_government() == THEOCRACY and self.get_military() == VOLUNTEER:
                self.set_military(BLANK)
            if self.get_military() == RELIGIOUS and self.get_government() != THEOCRACY:
                self.set_military(BLANK)
            if self.get_government() == COMMUNE:
                self.remove_freemen = False
            if self.get_government() != DICTATORSHIP and not JUNTA in self.get_factions():
                self.blockade = False
        else:
            raise InvalidChoice
    def get_government(self):
        return self.government

    def set_military(self, mil):
        if not mil in MILITARIES:
            raise InvalidChoice('Choice must be valid Military or "None"')
        if mil == LORDSPILOT:
            if not self.get_government() in [STEWARD, NOBLE] and not REBELS in self.get_factions():
                raise InvalidChoice('Lords-Pilot requires either Steward or Noble Government, or Royalist/Rebel Line faction')
        if mil == VOLUNTEER:
            if self.get_government() == THEOCRACY:
                raise InvalidChoice('Professional Volunteer military not allowed with Theocracy')
        if mil == RELIGIOUS:
            if self.get_government() != THEOCRACY and CULTS not in self.get_factions() and CHURCHES not in self.get_factions():
                raise InvalidChoice('Religious Orders military requires Theocratic government, or either of the Theocratic Institutions or Cult Churches factions')
        self.military = mil
        if self.get_military() == LORDSPILOT:
            self.add_faction(SLAVES)
        
            
    def get_military(self):
        return self.military

    def set_attitude(self, att):
        if not att in ATTITUDES:
            raise InvalidChoice('Choice must be valid attitude or "None"')
        if att in [EDUCATED, EXPERIENCE] and self.get_location() not in [OUT, VOID]:
            raise InvalidChoice('Educated/Informed and Personal Experience attitudes require Outworld or Void World')
        self.attitude = att
        
    def get_attitude(self):
        return self.attitude
    
    def set_industry(self, ind):
        self.set_export(ind)
    def get_industry(self):
        return self.get_export()
    def set_export(self, exp):
        if not exp in EXPORTS:
            raise InvalidChoice(exp + ' is invalid.  Choice must be valid export or "None"')
        if exp == MILITARY and not self.get_index() in [LOW, HIGH]:
            raise InvalidChoice('Miltary Capital export requires low or high index')
        self.export = exp
    def get_export(self):
        return self.export

    def set_quarantine(self, qua):
        if not qua in QUARANTINES:
            raise InvalidChoice
        if qua == ADVANCED and not self.get_index() in [LOW, HIGH]:
            raise InvalidChoice('Advanced Quarantine only possible with low or high tech index')
        if qua == STRICT and self.get_quarantine() == ADVANCED:
            while len(self.quarantine_items) > 1:
                self.quarantine_items.pop()
        elif qua == ADVANCED and self.get_quarantine() == STRICT:
            pass
        else:
            self.quarantine_items = []
        self.quarantine = qua
        if self.get_quarantine() == STRICT:
            self.set_index(HIGH)
        if self.get_quarantine() not in [ADVANCED, STRICT]:
            self.set_blockade(False)     
            
    def get_quarantine(self):
        return self.quarantine
    def add_quarantine_item(self, good):
        if self.get_quarantine() == NONE:
            raise InvalidChoice
        elif self.get_quarantine() in [STANDARD, ADVANCED] and len(self.get_quarantine_items()) == 3:
            raise InvalidChoice
        elif self.get_quarantine() == STRICT and len(self.get_quarantine_items()) == 1:
            raise InvalidChoice
        self.quarantine_items.append(good)
    def get_quarantine_items(self):
        return self.quarantine_items
    def remove_quarantine_item(self, good):
        self.quarantine_items.remove(good)

    def set_regulation(self, reg):
        if not reg in REGULATIONS:
            raise InvalidChoice
        if self.get_government() == LAWLESS and reg in [MODERATE, TIGHT]:
            raise InvalidChoice('Moderate and Tight levels of regulation are not possible with Lawless/Anarchic government')
        self.regulation = reg
        if self.get_regulation() != TIGHT:
            self.blockade = False
        
    def get_regulation(self):
        return self.regulation
