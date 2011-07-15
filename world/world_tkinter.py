from Tkinter import *
import world

class Burner(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        frame = Frame(master)
        
        frame.grid(row=5)
        
        self.w = world.World()

        self.hi_there = Button(master, text="get wiki-code", command=self.wiki_window)
        self.hi_there.grid(row=30)

        ### Block 1: Location ###
        
        l = Label(master, text='Empire').grid(row=0)
        empire_opt = Frame(master)
        empire_opt.grid(row=0, column=1, ipady=5)

        self.empire = StringVar()
        self.empire.set(world.BLANK)
        r=0
        c = 0
        for emp in world.EMPIRES:
            if emp != world.BLANK:
                b = Radiobutton(empire_opt, indicatoron=0, text=emp, variable=self.empire,
                                value=emp, command = self.set_emp)
                b.grid(row=r, column=c, sticky=W+E)
                c+=1
                if c==3:
                    r=1
                    c=0

        
        l=Label(master, text='Galactic Location').grid(row=1)
        location_opt = Frame(master)
        location_opt.grid(row=1, column=1, ipady=5)
        
        self.location = StringVar()
        self.location.set(world.BLANK)
        c=0
        for loc in world.LOCATIONS:
            if loc != world.BLANK:
                b = Radiobutton(location_opt, indicatoron =0, text=loc, variable=self.location,
                                value=loc, command = self.set_loc)
                b.grid(row=0, column=c, sticky=W+E)
                c+=1

        ### Block 2: Atmosphere, hydrology and topography ###
        
        self.atmosphere = StringVar()
        self.atmosphere.set('None')
        l = Label(master, text='Atmospheric Conditions').grid(row=2)
        
        atmosphere_opt = Frame(master)
        atmosphere_opt.grid(row=2, column=1, ipady=5)
        c=0
        r=0
        for atm in world.ATMOSPHERES:
            if atm != world.BLANK:
                b = Radiobutton(atmosphere_opt, indicatoron=0, text = atm, variable = self.atmosphere,
                                value=atm, command=self.set_atm)
                b.grid(row=r, column=c, sticky=W+E)
                c+=1
                if c==2:
                    c=0
                    r=1
        
        self.hydrology = StringVar()
        self.hydrology.set('None')
        l = Label(master, text='Hydrology').grid(row=3)
        hydrology_opt = Frame(master)
        hydrology_opt.grid(row=3, column=1, ipady=5)
        c=0
        for hyd in world.HYDROLOGIES:
            if hyd != world.BLANK:
                b = Radiobutton(hydrology_opt, indicatoron=0, text=hyd, variable = self.hydrology,
                                value=hyd, command=self.set_hy)
                b.grid(row=0, column=c, sticky=W+E)
                c+=1

        self.topography = StringVar()
        self.topography.set('None')
        l = Label(master, text='Topography').grid(row=4)
        topography_opt = Frame(master)
        topography_opt.grid(row=4, column=1, ipady=5)
        r=0
        c=0
        for top in world.TOPOGRAPHIES:
            if top != world.BLANK:
                b = Radiobutton(topography_opt, indicatoron=0, text=top,
                                     variable=self.topography, value=top,
                                     command = self.set_top)
                b.grid(row=r, column=c, sticky=W+E)
                c+=1
                if c==2:
                    r=1
                    c=0
            
        
        ### Block 3: Government, military and attitude ###
        
        self.government = StringVar()
        self.government.set(world.BLANK)
        l = Label(master, text='Dominant Form of Government').grid(row=5)
        government_opt = Frame(master)
        government_opt.grid(row=5, column=1, ipady=5)
        c=0
        r=0
        for gov in world.GOVERNMENTS:
            if gov != world.BLANK:
                b = Radiobutton(government_opt, indicatoron=0, text=gov,
                                variable=self.government, value=gov,
                                command = self.set_gov)
                b.grid(row=r, column=c, sticky=W+E)
                c+=1
                if c==4:
                    c=0
                    r=1

        self.military = StringVar()
        self.military.set(world.BLANK)
        l = Label(master, text='Predominant Military').grid(row=6)
        military_opt = Frame(master)
        military_opt.grid(row=6, column=1, ipady=5)
        c=0
        for mil in world.MILITARIES:
            if mil != world.BLANK:
                b=Radiobutton(military_opt, indicatoron=0, text=mil, variable=self.military,
                              value=mil, command = self.set_mil)
                b.grid(row=0, column=c, sticky=W+E)
                c+=1

        self.attitude = StringVar()
        self.attitude.set(world.BLANK)
        l = Label(master, text='Planetary Attitude toward Vaylen').grid(row=7)
        attitude_opt = Frame(master)
        attitude_opt.grid(row=7, column=1, ipady=5)
        r=0
        c=0
        for att in world.ATTITUDES:
            if att != world.BLANK:
                b=Radiobutton(attitude_opt, indicatoron=0, text=att, variable=self.attitude,
                              value=att, command=self.set_att)
                b.grid(row=r, column=c, sticky=W+E)
                c+=1
                if c==3:
                    c=0
                    r=1

        ### Block 4: Index, export, quarantine and regulation

        self.index = StringVar()
        self.index.set(world.BLANK)
        l = Label(master, text='Tech Index').grid(row=8)
        index_opt = Frame(master)
        index_opt.grid(row=8, column=1, ipady=5)
        c=0
        for ind in world.INDICES:
            if ind != world.BLANK:
                b=Radiobutton(index_opt, indicatoron=0, text=ind, variable=self.index,
                              value=ind, command=self.set_ind)
                b.grid(row=0, column=c, sticky=W+E)
                c+=1

        self.export = StringVar()
        self.export.set(world.BLANK)
        l = Label(master, text='Primary Export or Industry').grid(row=9)
        export_opt = Frame(master)
        export_opt.grid(row=9, column=1, ipady=5)
        c=0
        r=0
        for exp in world.EXPORTS:
            if exp != world.BLANK:
                b=Radiobutton(export_opt, indicatoron=0, text=exp, variable=self.export,
                              value=exp, command=self.set_exp)
                b.grid(row=r, column=c, sticky=W+E)
                c+=1
                if c==4:
                    c=0
                    r=1

        self.quarantine=StringVar()
        self.quarantine.set(world.BLANK)
        l = Label(master, text='Level of Quarantine').grid(row=10)
        quarantine_opt = Frame(master)
        quarantine_opt.grid(row=10, column=1, ipady=5)
        c=0
        for qua in world.QUARANTINES:
            if qua != world.BLANK:
                b=Radiobutton(quarantine_opt, indicatoron=0, text=qua, variable=self.quarantine,
                              value=qua, command=self.set_qua)
                b.grid(row=0, column=c, sticky=W+E)
                c+=1
            
        self.regulation=StringVar()
        self.regulation.set(world.BLANK)
        l = Label(master, text='Level of Economic Regulation').grid(row=11)
        regulation_opt = Frame(master)
        regulation_opt.grid(row=11, column=1, ipady=5)
        c=0
        for reg in world.REGULATIONS:
            if reg != world.BLANK:
                b=Radiobutton(regulation_opt, indicatoron=0, text=reg, variable=self.regulation,
                              value=reg, command=self.set_reg)
                b.grid(row=0, column=c, sticky=W+E)
                c+=1

        ### Block 5: Factions ###

        l = Label(master, text='Factions').grid(row=12)
        factionslist = Frame(master)
        factionslist.grid(row=12, column=1, ipady=5)
        
        self.f_communes = IntVar()
        self.c_communes = Checkbutton(factionslist, text=world.COMMUNES, variable=self.f_communes, command=self.set_fac_com)
        self.c_communes.grid(row=0)

        self.f_cults = IntVar()
        self.c_cults = Checkbutton(factionslist, text=world.CULTS, variable=self.f_cults, command=self.set_fac_cul)
        self.c_cults.grid(row=0,column=1)

        self.f_court = IntVar()
        self.c_court = Checkbutton(factionslist, text=world.COURT, variable=self.f_court, command=self.set_fac_cou)
        self.c_court.grid(row=0,column=2)

        self.f_aliens = IntVar()
        self.c_aliens = Checkbutton(factionslist, text=world.ALIENS, variable=self.f_aliens, command=self.set_fac_ali)
        self.c_aliens.grid(row=1,column=0)

        self.f_kerrn = IntVar()
        self.c_kerrn = Checkbutton(factionslist, text=world.KERRN, variable=self.f_kerrn, command=self.set_fac_ker)
        self.c_kerrn.grid(row=1,column=1)

        self.f_corp = IntVar()
        self.c_corp = Checkbutton(factionslist, text=world.CORP, variable=self.f_corp, command=self.set_fac_cor)
        self.c_corp.grid(row=1,column=2)

        self.f_junta = IntVar()
        self.c_junta = Checkbutton(factionslist, text=world.JUNTA, variable=self.f_junta, command=self.set_fac_jun)
        self.c_junta.grid(row=2,column=0)

        self.f_crime = IntVar()
        self.c_crime = Checkbutton(factionslist, text=world.CRIME, variable=self.f_crime, command=self.set_fac_cri)
        self.c_crime.grid(row=2,column=1)

        self.f_foundation = IntVar()
        self.c_foundation = Checkbutton(factionslist, text=world.FOUNDATION, variable=self.f_foundation, command=self.set_fac_fou)
        self.c_foundation.grid(row=2,column=2)

        self.f_rebels = IntVar()
        self.c_rebels = Checkbutton(factionslist, text=world.REBELS, variable=self.f_rebels, command=self.set_fac_reb)
        self.c_rebels.grid(row=3,column=0)

        self.f_slaves = IntVar()
        self.c_slaves = Checkbutton(factionslist, text=world.SLAVES, variable=self.f_slaves, command=self.set_fac_sla)
        self.c_slaves.grid(row=3,column=1)

        self.f_churches = IntVar()
        self.c_churches = Checkbutton(factionslist, text=world.CHURCHES, variable=self.f_churches, command=self.set_fac_chu)
        self.c_churches.grid(row=3,column=2)

        ## BLock 6: native settings, dispositions, remove freemen, blockade, other controls ##
        other = Frame(master)
        other.grid(row=13)

        options=Frame(other)
        options.grid(row=0)
        self.o_freemen = IntVar()
        self.c_freemen = Checkbutton(options, text='Remove Freemen', variable=self.o_freemen, command=self.set_freemen)
        self.c_freemen.grid(row=0)
        self.o_blockade = IntVar()
        self.c_blockade = Checkbutton(options, text='Blockade: Remove Spacefarer', variable=self.o_blockade, command=self.set_blockade)
        self.c_blockade.grid(row=1)        
        dispositions = Frame(other)
        dispositions.grid(row=4)
        l = Label(dispositions, text='Infiltration').grid(row=0, column=1)
        l = Label(dispositions, text='Usurpation').grid(row=0, column=2)
        l = Label(dispositions, text='Invasion').grid(row=0, column=3)
        l = Label(dispositions, text='Vaylen').grid(row=1)
        l = Label(dispositions, text='Human').grid(row=2)
        self.vinf=StringVar()
        self.vinf.set('0')
        l = Label(dispositions, textvariable=self.vinf).grid(row=1, column=1)
        self.vus=StringVar()
        self.vus.set('0')
        l = Label(dispositions, textvariable=self.vus).grid(row=1, column=2)
        self.vinv=StringVar()
        self.vinv.set('0')
        l = Label(dispositions, textvariable=self.vinv).grid(row=1, column=3)
        self.hinf=StringVar()
        self.hinf.set('0')
        l = Label(dispositions, textvariable=self.hinf).grid(row=2, column=1)
        self.hus=StringVar()
        self.hus.set('0')
        l = Label(dispositions, textvariable=self.hus).grid(row=2, column=2)
        self.hinv=StringVar()
        self.hinv.set('0')
        l = Label(dispositions, textvariable=self.hinv).grid(row=2, column=3)
        self.dispo_poll()

    def dispo_poll(self):
        self.vinf.set(str(self.w.vaylen_infiltration()))
        self.vus.set(str(self.w.vaylen_usurpation()))
        self.vinv.set(str(self.w.vaylen_invasion()))
        self.hinf.set(str(self.w.human_infiltration()))
        self.hus.set(str(self.w.human_usurpation()))
        self.hinv.set(str(self.w.human_invasion()))
        self.after(250, self.dispo_poll)

    def set_freemen(self):
        if self.o_freemen.get():
            try:
                self.w.set_remove_freemen(True)
                self.f_slaves.set(1)
            except world.InvalidChoice, ex:
                error_window(str(ex))
                self.o_freemen.set(0)
        else:
            self.w.set_remove_freemen(False)
    def set_blockade(self):
        if self.o_blockade.get():
            try:
                self.w.set_blockade(True)
            except world.InvalidChoice, ex:
                error_window(str(ex))
                self.o_blockade.set(0)
        else:
            self.w.set_blockade(False)
    def set_fac_com(self):
        if self.f_communes.get():
            self.w.add_faction(world.COMMUNES)
            self.o_freemen.set(0)
        else:
            self.w.remove_faction(world.COMMUNES)
    def set_fac_cul(self):
        if self.f_cults.get():
            self.w.add_faction(world.CULTS)
        else:
            self.w.remove_faction(world.CULTS)
            self.military.set(self.w.get_military())
    def set_fac_cou(self):
        if self.f_court.get():
            self.w.add_faction(world.COURT)
        else:
            self.w.remove_faction(world.COURT)
    def set_fac_ali(self):
        if self.f_aliens.get():
            self.w.add_faction(world.ALIENS)
        else:
            try:
                self.w.remove_faction(world.ALIENS)
            except world.InvalidChoice, ex:
                error_window(str(ex))
                self.f_aliens.set(1)
    def set_fac_ker(self):
        if self.f_kerrn.get():
            self.w.add_faction(world.KERRN)
        else:
            self.w.remove_faction(world.KERRN)
    def set_fac_cor(self):
        if self.f_corp.get():
            self.w.add_faction(world.CORP)
        else:
            self.w.remove_faction(world.CORP)
    def set_fac_jun(self):
        if self.f_junta.get():
            self.w.add_faction(world.JUNTA)
        else:
            self.w.remove_faction(world.JUNTA)
            if not self.w.blockade:
                self.o_blockade.set(0)
    def set_fac_cri(self):
        if self.f_crime.get():
            self.w.add_faction(world.CRIME)
        else:
            self.w.remove_faction(world.CRIME)
    def set_fac_fou(self):
        if self.f_foundation.get():
            try:
                self.w.add_faction(world.FOUNDATION)
            except world.InvalidChoice, ex:
                error_window(str(ex))
                self.f_foundation.set(0)
        else:
            self.w.remove_faction(world.FOUNDATION)
    def set_fac_reb(self):
        if self.f_rebels.get():
            self.w.add_faction(world.REBELS)
        else:
            self.w.remove_faction(world.REBELS)
            self.military.set(self.w.get_military())
    def set_fac_sla(self):
        if self.f_slaves.get():
            self.w.add_faction(world.SLAVES)
        else:
            try:
                self.w.remove_faction(world.SLAVES)
            except world.InvalidChoice, ex:
                error_window(str(ex))
                self.f_slaves.set(1)
    def set_fac_chu(self):
        if self.f_churches.get():
            self.w.add_faction(world.CHURCHES)
        else:
            self.w.remove_faction(world.CHURCHES)
            self.military.set(self.w.get_military())
    
    def set_emp(self):
        self.w.set_empire(self.empire.get())
    def set_loc(self):
        self.w.set_location(self.location.get())
        self.attitude.set(self.w.get_attitude())
    def set_hy(self):
        self.w.set_hydrology(self.hydrology.get())
    def set_top(self):
        try:
            self.w.set_topography(self.topography.get())
        except world.InvalidChoice, ex:
            error_window(str(ex))
            self.topography.set(self.w.get_topography())
    def set_atm(self):
        self.w.set_atmosphere(self.atmosphere.get())
        self.topography.set(self.w.get_topography())
        if self.atmosphere.get() == world.ALS:
            self.f_aliens.set(1)
    def set_gov(self):
        self.w.set_government(self.government.get())
        self.military.set(self.w.get_military())
        self.regulation.set(self.w.get_regulation())
        if world.SLAVES in self.w.get_factions():
            self.f_slaves.set(1)
        if not self.w.remove_freemen:
            self.o_freemen.set(0)
        if not self.w.blockade:
            self.o_blockade.set(0)

    def set_mil(self):
        try:
            self.w.set_military(self.military.get())
            if self.military.get()==world.LORDSPILOT:
                self.f_slaves.set(1)
        except world.InvalidChoice, ex:
            error_window(str(ex))
            self.military.set(self.w.get_military())
    def set_att(self):
        try:
            self.w.set_attitude(self.attitude.get())
        except world.InvalidChoice, ex:
            error_window(str(ex))
            self.attitude.set(self.w.get_attitude())
    def set_ind(self):
        self.w.set_index(self.index.get())
        self.export.set(self.w.get_export())
        self.quarantine.set(self.w.get_quarantine())
    def set_exp(self):
        try:
            self.w.set_export(self.export.get())
        except world.InvalidChoice, ex:
            error_window(str(ex))
            self.export.set(self.w.get_export())
    def set_qua(self):
        try:
            self.w.set_quarantine(self.quarantine.get())
            self.index.set(self.w.get_index())
            if not self.w.blockade:
                self.o_blockade.set(0)
        except world.InvalidChoice, ex:
            error_window(str(ex))
            self.quarantine.set(self.w.get_quarantine())
    def set_reg(self):
        try:
            self.w.set_regulation(self.regulation.get())
            if not self.w.blockade:
                self.o_blockade.set(0)
        except world.InvalidChoice, ex:
            error_window(str(ex))
            self.regulation.set(self.w.get_regulation())
    def wiki_window(self):
        text_window(self.w.wikicode())
        
def error_window(msg):
    top = Toplevel()
    top.title('Invalid Choice!')
    msg = Message(top, width=300, text=msg, padx=40, pady=20)
    msg.pack()
    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()
def text_window(text, title='Text Window'):
    top = Toplevel()
    top.title(title)
    t = Text(top)
    t.insert(END, text)
    t.pack()
    
root = Tk()
root.title('Burning Empires World Burner')
thing = Burner(root)

thing.mainloop()
