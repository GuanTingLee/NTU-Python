from ast import And
from unicodedata import name

class Head:
    def title():
        print('<<Automatic Adjust Ventilator Setting Application>>')
        print('=========== Please enter patient data ===========')
    
class Patient:
    def __init__(self):
        self.pNo = []
        self.name = []
        self.age = []
        self.sex = []
        self.height = []
        self.weight = []
        self.ibw = []
        self.diagnosis= []
	
    def Pdata(self):
        pNo = input('Patient NO.: ')
        self.pNo.append(pNo)
        name = input('Name: ')
        self.name.append(name)
        age = eval(input('age(y/o): '))
        self.age.append(age)
        self.Sex()
        height = eval(input('Hight(cm): '))
        self.height.append(height)
        weight = eval(input('Weight(kg): '))
        self.weight.append(weight)
        self.IBW()
        diagnosis = input('diagnosis: ')
        self.diagnosis.append(diagnosis)
    
    def Sex(self):
        sex = input('sex(m:male/f:female): ')
        if sex == 'm':
            self.sex.append(sex)
            return self.sex
        elif sex == 'f':
            self.sex.append(sex)
            return self.sex
        else:
            print('Please enter m or f')
            self.Sex()
        
    def IBW(self):
        if self.sex[-1] == 'm':
            ibw  = 62+(self.height[-1]-170)*0.6
            print('Ibw: ', ibw)
            self.ibw.append(ibw)
            return self.ibw
        elif self.sex[-1] == 'f':
            ibw = 52+(self.height[-1]-158)*0.5
            print('Ibw: ', ibw)
            self.ibw.append(ibw)
            return self.ibw

class Ventilator(Patient):
    def __init__(self):
        super().__init__()#繼承Patient的能力
        self.mode = []
        self.pressure = []
        self.tide_volume = []
        self.sug_vt = []
        self.PEEP = []
        self.FiO2 = []
        self.RR = []
        self.Ti = []
        
    def Mode(self):
        mode = input('Mode(PCV / VC+ / PS): ')
        if mode == 'PCV':
            self.mode.append(mode)
            return self.mode
        elif mode == 'VC+':
            self.mode.append(mode)
            return self.mode
        elif mode == 'PS':
            self.mode.append(mode)
            return self.mode
        else:
            print('Error Mode, please enter again')
            self.Mode()
    
    def Setting(self):
        print('======== Please enter ventilator setting ========')
        self.Mode()
        if (self.mode[-1] == 'PCV'):
            self.sug_vt.append((self.ibw[-1]*8))
            print('(!!!suggest Tidal volume: %.2f ml)' % self.sug_vt[-1])
            pressure = eval(input('Pressure(cmH2O): '))
            self.pressure.append(pressure)
            PEEP = eval(input('PEEP(cmH2O): '))
            self.PEEP.append(PEEP)
            FiO2 = eval(input('FiO2(%): '))
            self.FiO2.append(FiO2)
            RR = eval(input('RR(bpm): '))
            self.RR.append(RR)
            Ti = eval(input('Ti(sec): '))
            self.Ti.append(Ti)
        
        elif (self.mode[-1] == 'VC+'):
            self.sug_vt.append((self.ibw[-1]*8))
            print('(!!!suggest Tidal volume: %.2f ml)' % self.sug_vt[-1])
            tide_volume = eval(input('Tidal volume: '))
            self.tide_volume.append(tide_volume)
            PEEP = eval(input('PEEP(cmH2O): '))
            self.PEEP.append(PEEP)
            FiO2 = eval(input('FiO2(%): '))
            self.FiO2.append(FiO2)
            RR = eval(input('RR(bpm): '))
            self.RR.append(RR)
            Ti = eval(input('Ti(sec): '))
            self.Ti.append(Ti)    
        
        elif (self.mode[-1] == 'PS'):
            self.sug_vt.append((self.ibw[-1]*4))
            print('(!!!suggest Tidal volume: %.2f ml)' % self.sug_vt[-1])
            pressure = eval(input('Pressure(cmH2O): '))
            self.pressure.append(pressure)
            PEEP = eval(input('PEEP(cmH2O): '))
            self.PEEP.append(PEEP)
            FiO2 = eval(input('FiO2(%): '))
            self.FiO2.append(FiO2)

class PatientMonitor(Ventilator):
    def __init__(self):
        super().__init__() #繼承Ventilator的能力		
        self.vt = []
        self.mv = []
        self.rr = []
        self.pip = []
        self.Map = []
        self.hr = []
        self.spo2 = []
        self.bp = [[0 for i in range(2)] for j in range(5)] #二維陣列存取收縮壓及舒張壓
        self.ekg_rr = []
              
    def Sign(self):
        print('=============== Patient Vital Sign ===============')
        vt = eval(input('Tidal Volume(cmH2O): '))
        self.vt.append(vt)
        rr = eval(input('RR(bpm): '))
        self.rr.append(rr)
        ekg_rr = eval(input('EKG RR(bpm): '))
        self.ekg_rr.append(ekg_rr)       
        mv = eval(input('Minute Volume(L/min): '))
        self.mv.append(mv)     
        pip = eval(input('Peak Pressure(cmH2O): '))
        self.pip.append(pip)       
        Map = eval(input('Mean Airway Pressure(cmH2O): '))
        self.Map.append(Map)
        hr = eval(input('Heart Rate(bpm): '))
        self.hr.append(hr)
        spo2 = eval(input('SpO2(%): '))
        self.spo2.append(spo2)
        bpS, bpD = map(int,input('Please Enter Blood Pressure: ').split())
        print('BP(mmHg): %d/%d'% (bpS,bpD))
        self.bp.append(bpS) #收縮壓及舒張壓寫入二維陣列存取
        self.bp.append(bpD) 
        # print(self.bp[-2])   二維陣列中倒數第二個值:收縮壓
        # print(self.bp[-1])   二維陣列中最後一個值:舒張壓

class ABG(PatientMonitor):
    def __init__(self):
        super().__init__()
        self.ph = []
        self.pao2 = []
        self.paco2 = []
        self.hco3 = []
        self.be = []
        self.sao2 = []
        self.type = []
    
    def Type(self, ph, paco2, hco3):
        if(ph>=7.35 and ph<=7.45 and paco2>=35 and paco2<=45):
            type = 'normal ABG'
            self.type.append(type)
        elif((ph>7.45 and paco2>45 and hco3<22) or (ph<7.35 and paco2<35 and hco3>26)):
            type = 'Error ABG'
            self.type.append(type)
        elif(paco2>45): #呼吸酸
            if(ph>=7.35 and ph<=7.45): #有代償 
                type = 'Respiratory Acidosis with metabolic compensation'
                self.type.append(type)
            elif(ph<7.35): #沒有代償
                type = 'Respiratory Acidosis without compensation'
                self.type.append(type)
        elif(paco2<35):#呼吸鹼
            if(ph>=7.35 and ph<=7.45):#有代償
                type = 'Respiratory Alkadosis with metabolic compensation'
                self.type.append(type)
            elif(ph>7.45):#沒有代償
                type = 'Respiratory Alkadosis without compensation'
                self.type.append(type)    
        elif(hco3<22):#代謝酸
            if(ph>=7.35 and ph<=7.45):#有代償
                type = 'Metabolic Acidosis with respiratory compensation'
                self.type.append(type)
            elif(ph<7.35):#沒有代償
                type = 'Metabolic Acidosis without compensation'
                self.type.append(type)
        elif(ph>=7.35 and paco2>45 and hco3>26):#代謝鹼
            if(ph>=7.35 and ph<=7.45):#有代償
                type = 'Metabolic Alkadosis with respiratory compensation'
                self.type.append(type)
            elif(ph>=7.45):#沒有代償
                type = 'Metabolic Alkadosis without compensation'
                self.type.append(type)
        
    def Blood(self):
        print('=============== Aterial Blood Gas ===============')
        ph = eval(input('PH: '))
        self.ph.append(ph)
        pao2 = eval(input('PaO2(mmHg): '))
        self.pao2.append(pao2)
        paco2 = eval(input('PaCO2(mmHg): '))
        self.paco2.append(paco2)
        hco3 = eval(input('HCO3(mmol/L): '))
        self.hco3.append(hco3)
        be = eval(input('BE: '))
        self.be.append(be)
        sao2 = eval(input('SaO2(%): '))
        self.sao2.append(sao2)
        self.Type(self.ph[-1], self.paco2[-1], self.hco3[-1]);
        print('Result:',self.type[-1])

class Analysis(ABG):
    def __init__(self):
        super().__init__()
        self.lead = 0
        self.PcVt = []
        self.lead_mark = 0#用來標記是否有異常
        self.o2_mark = 0
        self.co2_mark = 0
        self.alarm_mark = 0

    def lead_off(self):
        if((self.rr[-1] - self.ekg_rr[-1] >= 10) or (self.ekg_rr[-1] - self.rr[-1] >= 10)):
            print('Lead Off, Please Check EKG Lead!')
            self.lead = 0
            return self.lead
        elif(self.rr[-1] > 30 and self.lead != 0):
            print('Tachypnea?')
        elif(self.rr[-1] == 0 and self.lead != 0):
            print('Apnea?')
        else:
            self.lead_mark = 1 #表沒有異常
            return self.lead_mark 

    def o2(self):
        if(self.spo2[-1] < 90 and self.spo2[-1] > 80) :
            print('!!!Hypoxia' )
            newfio2 = self.FiO2[-1]+10
            self.FiO2.pop()
            self.FiO2.append(newfio2)
            print('Increased FiO2 to', self.FiO2[-1])
            return self.FiO2
        elif(self.spo2[-1] <= 80):
            print('!!!Severe Hypoxia')
            self.FiO2.pop()
            self.FiO2.append(100)
            print('Increased FiO2 to', self.FiO2[-1])
            return self.FiO2
        else:
            self.o2_mark = 1 #表沒有異常
            return self.o2_mark

    def co2(self):
        if(self.type[-1] == 'Respiratory Acidosis without compensation'):#呼吸酸沒代償
            self.adjustCo2(40)#normal paco2:40
        elif(self.type[-1] == 'Metabolic Acidosis without compensation'):#代謝酸沒代償
            self.adjustCo2(35)#target paco2:35
        else:
            self.co2_mark = 1 #表沒有異常
            return self.co2_mark    
    def adjustCo2(self, TargetCo2):
        # print('!!!CO2 retention' )
        if(self.mode[-1] == 'PCV' and self.rr[-1] == self.RR[-1] and self.RR[-1] <30 and self.RR[-1]>10): #PCV mode, adjust RR
            newRR = (self.paco2[-1] * self.mv[-1]*1000)/(TargetCo2 * self.vt[-1]) 
            self.RR.pop()
            self.RR.append(newRR)
            print('Adjust RR to %d bpm'% self.RR[-1])
        elif(self.mode[-1] == 'VC+' and self.rr[-1] == self.RR[-1] and self.RR[-1] <30 and self.RR[-1]>10): #VC+ mode, adjust RR
            newRR = (self.paco2[-1] * self.mv[-1]*1000)/(TargetCo2 * self.tide_volume[-1]) 
            self.RR.pop()
            self.RR.append(newRR)
            print('Adjust RR to %d bpm'% self.RR[-1])
        elif(self.mode[-1] == 'PCV'): #PCV mode, adjust PCV
            PcVt = (self.paco2[-1] * self.mv[-1]*1000)/(TargetCo2 * self.rr[-1])
            self.sug_vt.pop()
            self.sug_vt.append(PcVt)
            print('Adjust PCV to provide enough tidal volume: %d ml'% self.sug_vt[-1])
        elif(self.mode[-1] == 'VC+' and self.vt[-1] > self.ibw[-1]*4): #VC+ mode , adjust Vt
            newMV = (self.paco2[-1] * self.mv[-1]*1000)/TargetCo2 
            newtide_volume = newMV/self.rr[-1]
            newRR = 0
            while(newtide_volume > self.ibw[-1]*15):#最多Vt調至ibw*15，若超過則每次增加RR:2，並算出新的Vt
                newRR = newRR+2
                newtide_volume = newMV/newRR
            else:
                self.tide_volume.pop()
                self.tide_volume.append(newtide_volume)
                self.RR.pop()
                self.RR.append(newRR)
            print('Adjust Tidal volume to %d ml and RR to %d bpm'% (self.tide_volume[-1],self.RR[-1]))
                
    def alarm(self):
        if(self.mv[-1]>10 and self.rr[-1] >30):
            print('Hyperventilation?')
        elif(self.mv[-1]<3 and self.rr[-1] != 0):
            print('Hypoventilation?')   
        if(self.pip[-1]>35):
            print('PIP high?')
        elif(self.pip[-1]<10):
            print('PIP low?')
        if(self.hr[-1]>120):
            print('Tachycardia?')
        elif(self.hr[-1]<60):
            print('Bradicardia?')    
        if(self.bp[-2] >130 and self.bp[-1] >90):
            print('hypertention?')
        elif(self.bp[-2] <70 and self.bp[-1] <40):
            print('hypotention?')
            
    def monitor(self):	
        print('===================== Alarm =====================')
        self.lead_off()
        self.alarm()
        self.o2()
        self.co2()
        # print(self.co2_mark, self.lead_mark, self.o2_mark, self.co2_mark)
        if(self.co2_mark == 1 and self.lead_mark == 1 and self.o2_mark == 1 and self.co2_mark == 1):
            print('No Alarms')
    def suggest_setting(self):
        print('================ Suggest Setting ================')
        if(self.mode[-1] == 'PCV'):
            print('Mode: PCV' )
            print('Pressure(cmH2O):', self.pressure[-1])
        elif(self.mode[-1] == 'VC+'):
            print('Mode: VC+' )
            print('Tidal volume: %d ml'% self.tide_volume[-1])
        elif(self.mode[-1] == 'PS'):
            print('Mode: PS' )
            print('Pressure: %d cmH2O'% self.pressure[-1])
        print('PEEP: %d cmH2O'% self.PEEP[-1])
        print('FiO2: %d %%'% self.FiO2[-1])
        print('RR: %d bpm'% self.RR[-1])
        print('Ti: %.2f sec'% self.Ti[-1])
        
Head.title()
p1 = Analysis()
p1.Pdata()
p1.Setting()
p1.Sign()
p1.Blood()
p1.monitor()
p1.suggest_setting()