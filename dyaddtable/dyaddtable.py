from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import csv
import os
import copy
from ppp import Ui_Form
from lxml import etree
import zipfile

def Achive_Folder_To_ZIP(sFilePath):
    """
    input : Folder path and name
    output: using zipfile to ZIP folder
    """
    zf = zipfile.ZipFile(sFilePath + '.ZIP', mode='w')
    os.chdir(sFilePath)
    #print sFilePath
    for root, folders, files in os.walk(".\\"):
        for sfile in files:
            aFile = os.path.join(root, sfile)
            #print aFile
            zf.write(aFile)
    zf.close()
 

info={
      'MCU':"N76E003",
      "CLK_SOURCE":"HIRC_16M",     
      "P05":"_Input_Mode",
      "P06":"_Input_Mode",
      "P07":"_Input_Mode",
      "P20":"_Input_Mode",
      "P30":"_Input_Mode",
      "P17":"_Input_Mode",
      "GND":"",
      "P16":"_Input_Mode",
      "VDD":"",
      "P15":"_Input_Mode",
      "P14":"_Input_Mode",
      "P13":"_Input_Mode",
      "P12":"_Input_Mode",
      "P11":"_Input_Mode",
      "P10":"_Input_Mode",
      "P00":"_Input_Mode",
      "P01":"_Input_Mode",
      "P02":"_Input_Mode",
      "P03":"_Input_Mode",
      "P04":"_Input_Mode",      

      "P05_MFP":"",
      "P06_MFP":"",
      "P07_MFP":"",
      "P20_MFP":"",
      "P30_MFP":"",
      "P17_MFP":"",
      "GND_MFP":"",
      "P16_MFP":"",
      "VDD_MFP":"",
      "P15_MFP":"",
      "P14_MFP":"",
      "P13_MFP":"",
      "P12_MFP":"",
      "P11_MFP":"",
      "P10_MFP":"",
      "P00_MFP":"",
      "P01_MFP":"",
      "P02_MFP":"",
      "P03_MFP":"",
      "P04_MFP":"", 

      "vWKCON":0,       
      "vRWK":0,         
      "WAKEUP_ENABLE":1,
      "WAKEUP_MODE":"INTERRUPT",      
      "WAKEUP_INTERRUPT":"INTERRUPT",
      "WAKEUP_INIT":"INTERRUPT_INIT",

      "vWDCON":0,        
      "WDT_ENABLE":1,   
      "WDT_MODE":"INTERRUPT",      
      "WAKEUP_INTERRUPT":"INTERRUPT",
      "WAKEUP_INIT":"INTERRUPT_INIT",
      "WDT_POLL":"POLL",

      "INT0_ENABLE":1,   
      "INT0_MODE":"INTERRUPT",
      "INT0_INTERRUPT":"INTERRUPT",
      "INT0_INIT":"INTERRUPT_INIT",
      "INT0_PIN_SELECT":"LEVEL",

      "INT1_ENABLE":1,  
      "INT1_MODE":"INTERRUPT",
      "INT1_INTERRUPT":"INTERRUPT",
      "INT1_INIT":"INTERRUPT_INIT",
      "INT1_PIN_SELECT":"LEVEL",

      "PIN_ENABLE":1,  
      "PIN_MODE":"INTERRUPT",
      "PIN_INTERRUPT":"INTERRUPT",
      "PIN_INIT":"INTERRUPT_INIT",
      "PIN_INT_PORT":"Enable_INT_Port0",
      "PIN0":"Enable_BIT0_LowLevel_Trig",
      "PIN1":"Enable_BIT1_LowLevel_Trig",
      "PIN2":"Enable_BIT2_LowLevel_Trig",
      "PIN3":"Enable_BIT3_LowLevel_Trig",
      "PIN4":"Enable_BIT4_LowLevel_Trig",
      "PIN5":"Enable_BIT5_LowLevel_Trig",
      "PIN6":"Enable_BIT6_LowLevel_Trig",
      "PIN7":"Enable_BIT7_LowLevel_Trig",

      "CLK_OUT_ENABLE":1,   
      "CLK_OUT_MODE":"POLL",
      "CLK_OUT_POLL":"POLL",

      "TIMER0_ENABLE":1,
      "TIMER0_MODE":"POLL", 
      "TIMER0_MODE_SEL":"TIMER0_MODE0", 

      "vTH0_INIT":0X55,
      "vTL0_INIT":0X55,
      "TIMER0_MODE0_INTERRUPT":"INTERRUPT",
      "TIMER0_MODE0_INIT":"INIT",
      "TIMER0_MODE0_INTERRUPT_INIT":"INTERRUPT_INIT",
      "TIMER0_MODE0_POLL":"POLL",     

       "u8TH0":0x0,
       "u8TL0":0x0,
      "TIMER0_MODE1_INTERRUPT":"INTERRUPT",
      "TIMER0_MODE1_INIT":"INIT",
      "TIMER0_MODE1_INTERRUPT_INIT":"INTERRUPT_INIT",

      "uTIMER0":0x0,
      "TIMER0_MODE2_INTERRUPT":"INTERRUPT",
      "TIMER0_MODE2_INIT":"INIT",
      "TIMER0_MODE2_INTERRUPT_INIT":"INTERRUPT_INIT",

      "uTH0":0,
      "uTL0":0,
      "TIMER01_MODE3_INTERRUPT":"INTERRUPT",
      "TIMER01_MODE3_INIT":"INIT",
      "TIMER01_MODE3_INTERRUPT_INIT":"INTERRUPT_INIT",
      
      "TIMER1_ENABLE":1,
      "TIMER1_MODE":"POLL", 
      "TIMER1_MODE_SEL":"TIMER1_MODE0", 

      "vTH1_INIT":0X55, 
      "vTL1_INIT":0X55, 
      "TIMER1_MODE0_INTERRUPT":"INTERRUPT",
      "TIMER1_MODE0_INIT":"INIT",
      "TIMER1_MODE0_INTERRUPT_INIT":"INTERRUPT_INIT",
      "TIMER1_MODE0_POLL":"POLL",     

      "u8TH1":0x0,
      "u8TL1":0x0,
      "TIMER1_MODE1_INTERRUPT":"INTERRUPT",
      "TIMER1_MODE1_INIT":"INIT",
      "TIMER1_MODE1_INTERRUPT_INIT":"INTERRUPT_INIT",

      "uTIMER1":0x0,
      "TIMER1_MODE2_INTERRUPT":"INTERRUPT",
      "TIMER1_MODE2_INIT":"INIT",
      "TIMER1_MODE2_INTERRUPT_INIT":"INTERRUPT_INIT",

      "uRELOAD_VALUE_H":0x0,
      "uRELOAD_VALUE_H":0x0,
      "TIMER3_INTERRUPT":"INTERRUPT",
      "TIMER3_INIT":"INIT",
      "TIMER3_INTERRUPT_INIT":"INTERRUPT_INIT",
      "TIMER3_POLL":"POLL",


      "uBaudrate":115200,
      "UART0_ENABLE":1,   
      "UART0_MODE":"POLL", 
      "UART0_TIMER":"UART_TIMER0_INIT",
      "UART0_INTTRERUPT":"INTERRUPT",
      "UART0_INIT":"INTERRUPT_INIT",
      "UART0_POLL":"POLL",

      "uBaudrate1":115200,      
      "UART1_ENABLE":1,  
      "UART1_MODE":"INTERRUPT", 
      "UART1_TIMER":"UART1_TIMER3_INIT",
      "UART1_INTTRERUPT":"INTERRUPT",
      "UART1_INIT":"INTERRUPT_INIT",
      "UART1_POLL":"POLL",
         
      "ADC_ENABLE":1,  
      "ADC_MODE":"POLL", 
      "ADC_CH":"PIN0",
      "ADC_INTTRERUPT":"INTERRUPT",
      "ADC_INIT":"INTERRUPT_INIT",
      "ADC_POLL":"POLL",

      "uPWMPH":0x0,
      "uPWMPL":0x0,
      "uPWM0H":0x0,
      "uPWM0L":0x0,
      "uPWM1H":0x0,
      "uPWM1L":0x0,
      "uPWM2H":0x0,
      "uPWM2L":0x0,
      "uPWM3H":0x0,
      "uPWM3L":0x0,
      "uPWM4H":0x0,
      "uPWM4L":0x0,
      "uPWM5H":0x0,
      "uPWM5L":0x0,
      "PWM_ENABLE":1,   
      "PWM_MODE":"INTERRUPT", 
      "PWM_CH0":"PWM1_P12_OUTPUT_ENABLE",
      "PWM_CH1":"PWM1_P11_OUTPUT_ENABLE",
      "PWM_CH2":"PWM2_P10_OUTPUT_ENABLE",
      "PWM_CH3":"PWM3_P04_OUTPUT_ENABLE",
      "PWM_CH4":"PWM4_P01_OUTPUT_ENABLE",
      "PWM_CH5":"PWM5_P03_OUTPUT_ENABLE",
      "PWM_CLK_DIV":"PWM_CLOCK_DIV_2",
      "INIT_CLK":"INIT_PMW_CLK",      
      "PWM_SET_MODE":"PWM_IMDEPENDENT_MODE",
      "PWM_INTTERUPT_MODE":"PWM_FALLING_INT",
      "PWM_INTTRERUPT":"INTERRUPT",
      "PWM_INIT":"INTERRUPT_INIT",
      "PWM_POLL":"INIT",

      "SPI_ENABLE":1, 
      "MODE_SELECT":"Master", 
      "SS_SELECT":"GPIO",
      "LSB_SELECT":"ENABLE",
      "CPOL_SELECT":"IDLE_HIGH",
      "CPHA_SELECT":"First_Edge",
      "CLK_DIV":"SPICLK_DIV4",
      "SPI_POLL":"POLLMASTER",
      "SPI_INIT":"INTERRUPT_INIT",
      "SPI_INTERRUPUT":"INTERRUPUT",
      
      "IAP_DEFINE":"IAP_DEFINE",
      "IAP_TRIGGER":"IAP_TRIGGER",
      "IAP_ERASE":"IAP_ERASE",
      "IAP_Program":"IAP_Program",
      "IAP_Read":"IAP_Program",
      "p_SYSTEM_CLK":0,
      "p_GPIO_INIT":0, 
      "p_WAKEUP":0,                
      "p_WDT":0,
      "p_INT0":0,
      "p_INT1":0,
      "p_PIN_INT":0,
      "p_UART0":0,
      "p_UART1":0,
      "p_CLKOUT":0,
      "p_TIMER0":0,
      "p_TIMER1":0,
      "p_TIMER2":0,
      "p_TIMER3":0,
      "p_ADC":0,
      "p_PWM":0,
      "p_SPI":0,
      "p_I2C":0,
      }

file = open('N76E003_PIN.csv', 'r')

csvCursor_temp = csv.reader(file)
csvlist = []
pinlist = []
for row in csvCursor_temp:
    csvlist.append(row)
    pinlist.append(row[0])
 
probit = ["VDD","GND"]
lst0 = [""]
lst1 = ["SCL", "SDA"]
lst2 = ["/SS", "MOSI","MISO","SPCLK"]
lst3 = ["TXD_0", "RXD_0"]
lst4 = ["TXD_1", "RXD_1"]
GPIO_MODE = ["_Input_Mode", "_Quasi_Mode","_PushPull_Mode","_OpenDrain_Mode"]
from collections import OrderedDict
Q_System= OrderedDict()
Q_POLL= OrderedDict()
Q_INTERRUPT_HANDLER= OrderedDict()
Q_INTERRUPT_INIT= OrderedDict()
Q_FUNCTION=OrderedDict()
class MyMainWindow(QMainWindow, Ui_Form):
    #load menu item
    def Menu(self,item,xml_str):
        items = self.TREE.find(xml_str)
        for i in range(0,len(items)):  
                 item.addItem(items[i].tag)
        item.setEnabled(False)  
    #check enable button
    def b_Check(self,B_item,C_item):
        if(B_item.isChecked() == True):
            C_item.setEnabled(True)
        if(B_item.isChecked() == False):
            C_item.setEnabled(False)   

    def be_Check(self,B_item,E_item):
        if(B_item.isChecked() == True):
            E_item.setEnabled(True)
        if(B_item.isChecked() == False):
            E_item.setEnabled(False)   


    def BS_initial(self,b_item,c_item,xml_tag,call_back):
        self.Menu(c_item,xml_tag)
        b_item.stateChanged.connect(call_back)
        #c_item.setEnabled(False)  

    def __init__(self, parent=None):    
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.form.setFixedSize(500,500)
        self.Gen_Code.clicked.connect(self.GEN)
        parser = etree.XMLParser(recover=True)
        self.TREE = etree.parse("TEST.XML",parser)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)  #only keep close button
        
        #c_clk_change
        self.BS_initial(self.b_CLK,self.c_CLK,"./CLK_SOURCE",self.b_CLK_Change)
        
        #c_WAKUP_change
        self.BS_initial(self.b_WAKEUP,self.c_WAKEUP,"./WAKEUP/MODE",self.b_WAKEUP_Change)
        '''
        self.e_CLK.setEnabled(False)
        self.e_CLK.setText("100")
        self.e_PWM_F.setText("8000000")
        pIntValidator=QIntValidator(self)
        self.e_CLK.setValidator(pIntValidator)
        self.e_CLK.installEventFilter(self)
        ''' 
        #c_CLKOUT_change
        self.BS_initial(self.b_CLKOUT,self.c_CLKOUT,"./CLKOUT/MODE",self.b_CLKOUT_Change)

        #c_WDT_change
        self.BS_initial(self.b_WDT,self.c_WDT,"./WDT/MODE",self.b_WDT_Change)
        #self.BS_initial(self.b_WDT,self.c_WDT,"./WDT/MODE",self.b_WDT_Change)
        self.Menu(self.c_WDT_TIMEOUT,"./WDT/TIMEOUT")

         #c_INT0_change
        self.BS_initial(self.b_INT0,self.c_INT0,"./INT0/MODE",self.b_INT0_Change)
        self.Menu(self.c_INT0_PINSELECT,"./INT0/INT_SELECT")

        #c_TIMER0_change
        self.BS_initial(self.b_Timer0,self.c_Timer0,"./TIMER0_MODE0/MODE",self.b_Timer0_Change)
        self.Menu(self.c_Timer0_Mode,"./TIMER0")

        #c_TIMER1_change
        self.BS_initial(self.b_Timer1,self.c_Timer1,"./TIMER1_MODE0/MODE",self.b_Timer1_Change)
        self.Menu(self.c_Timer1_Mode,"./TIMER1")

        #c_TIMER3_change
        self.BS_initial(self.b_Timer3,self.c_Timer3,"./TIMER3/MODE",self.b_Timer3_Change)


         #c_INT1_change
        self.BS_initial(self.b_INT1,self.c_INT1,"./INT1/MODE",self.b_INT1_Change)
        self.Menu(self.c_INT1_PINSELECT,"./INT1/INT_SELECT")

         #c_PIN_change
        self.BS_initial(self.b_PININT,self.c_PIN_INT_PORT,"./PIN_INT/PIN_INT_PORT",self.b_PIN_Change)
        self.Menu(self.c_PIN0,"./PIN_INT/PIN0")
        self.Menu(self.c_PIN1,"./PIN_INT/PIN1")
        self.Menu(self.c_PIN2,"./PIN_INT/PIN2")
        self.Menu(self.c_PIN3,"./PIN_INT/PIN3")
        self.Menu(self.c_PIN4,"./PIN_INT/PIN4")
        self.Menu(self.c_PIN5,"./PIN_INT/PIN5")
        self.Menu(self.c_PIN6,"./PIN_INT/PIN6")
        self.Menu(self.c_PIN7,"./PIN_INT/PIN7")

        self.BS_initial(self.b_UART0,self.c_UART0,"./UART0/MODE",self.b_UART0_Change)
        self.Menu(self.c_UART0_Timer,"./UART0/UART0_TIMER")
        self.Menu(self.c_UART0_BaudRate,"./UART0/BAUDRATE")
   
        self.BS_initial(self.b_UART1,self.c_UART1,"./UART1/MODE",self.b_UART1_Change)
        self.Menu(self.c_UART1_Timer,"./UART1/UART1_TIMER")
        self.Menu(self.c_UART1_BaudRate,"./UART1/BAUDRATE")

         #c_ADC
        self.BS_initial(self.b_ADC,self.c_ADC,"./ADC/MODE",self.b_ADC_Change)
        self.Menu(self.c_ADC_CH,"./ADC/ADC_CH")


        #gpio table initial
        self.t_GPIO.setColumnCount(3)      
        #self.setCentralWidget(self.t_GPIO)
        self.t_GPIO.setRowCount(len(pinlist))
        self.combox_list_gpio_mode = []
        self.combox_list_mfp = []

        for ind in range(len(pinlist)):
            self.comboBox = QComboBox()            
            self.comboBox.setObjectName("comboBox_gpio_mode_" + str(ind))
            self.combox_list_gpio_mode.append(self.comboBox)
        for ind in range(len(pinlist)):
            self.comboBox = QComboBox()            
            self.comboBox.setObjectName("combox_list_mfp_" + str(ind))
            self.combox_list_mfp.append(self.comboBox)
        self.function_table = []
    
        self.function_table.append(self.s1)
        self.function_table.append(self.s2)
        self.function_table.append(self.s3)
        self.function_table.append(self.s4)
        self.function_table.append(self.s5)
        self.function_table.append(self.s6)
        self.function_table.append(self.s7)
        self.function_table.append(self.s8)
        self.function_table.append(self.s9)
        self.function_table.append(self.s10)
        self.function_table.append(self.s11)
        self.function_table.append(self.s12)
        self.function_table.append(self.s13)
        self.function_table.append(self.s14)
        self.function_table.append(self.s15)
        self.function_table.append(self.s16)
        self.function_table.append(self.s17)
        self.function_table.append(self.s18)
        self.function_table.append(self.s19)
        self.function_table.append(self.s20)
        for index in range(len(pinlist)):
            item1 = QTableWidgetItem(pinlist[index])
            self.t_GPIO.setItem(index,0,item1)
            local_temp = 0
            for l in probit:
                if str(l) in str(pinlist[index]):
                    local_temp = 1
            if local_temp == 1:         
               continue
                       
            for t in GPIO_MODE:                
                self.combox_list_gpio_mode[index].addItem(t)
            self.t_GPIO.setCellWidget(index,1,self.combox_list_gpio_mode[index])
                        
            
            self.combox_list_mfp[index].addItem("-")
            row = csvlist[index]            
            for l in range(1,len(row)):
                self.combox_list_mfp[index].addItem(row[l])
            self.t_GPIO.setCellWidget(index,2,self.combox_list_mfp[index])
        
        for index in range(len(pinlist)):        
            self.combox_list_mfp[index].currentIndexChanged.connect(self.function_table[index])   

        self.t_GPIO.setEnabled(False) 
        self.b_GPIO.stateChanged.connect(self.b_GPIO_change)
        info["p_GPIO_INIT"]=0

        #c_PWM
        self.BS_initial(self.b_PWM,self.c_PWM,"./PWM/MODE",self.b_PWM_Change)
        self.Menu(self.c_PWM_CH,"./PWM/PWM_PIN")
        info["p_PWM"]=0


        #SET TABLE CURRENT INDEX
        self.tabWidget.setCurrentIndex(0)
    def Pin_Coflict(self,index):          
          for i in range(len(pinlist)):
              if index == i:
                  continue
              if self.combox_list_mfp[index].currentText() == self.combox_list_mfp[i].currentText():
                  self.combox_list_mfp[i].setCurrentIndex(0)

    def Pin_GROUP(self,index):
        select = self.combox_list_mfp[index].currentText()
        lst = lst0
        if select in str(lst1):         
           lst = lst1        
        if select in str(lst2):         
           lst = lst2
        if select in str(lst3):         
           lst = lst3
        if select in str(lst4):         
           lst = lst4

        if lst == lst0:
           return

        temp_count = 0
        for row in csvlist:   
            for l in lst:
                if str(l) in str(row):
                    self.combox_list_mfp[temp_count].setCurrentIndex(row.index(str(l)))         
            temp_count = temp_count + 1

                 
    def s1(self,i):   
        self.Pin_GROUP(0)                           
        self.Pin_Coflict(0) 
              

    def s2(self,i): 
        self.Pin_GROUP(1)                 
        self.Pin_Coflict(1)
             

    def s3(self,i):  
        self.Pin_GROUP(2)                
        self.Pin_Coflict(2)
             

    def s4(self,i):
        self.Pin_GROUP(3)                 
        self.Pin_Coflict(3)
               

    def s5(self,i):                            
        self.Pin_GROUP(4)    
        self.Pin_Coflict(4)

    def s6(self,i):                
        self.Pin_GROUP(5)    
        self.Pin_Coflict(5)
            

    def s7(self,i):                
        self.Pin_GROUP(6)    
        self.Pin_Coflict(6)
        
    def s8(self,i):                
        self.Pin_GROUP(7)    
        self.Pin_Coflict(7)
            
    def s9(self,i):                
        self.Pin_GROUP(8)    
        self.Pin_Coflict(8)
            
    def s10(self,i):                
        self.Pin_GROUP(9)    
        self.Pin_Coflict(9)
            
    def s11(self,i):                
        self.Pin_GROUP(10)    
        self.Pin_Coflict(10)
        
    def s12(self,i):                
        self.Pin_GROUP(11)    
        self.Pin_Coflict(11)
             
                        
    def s13(self,i):                
        self.Pin_GROUP(12)    
        self.Pin_Coflict(12)
             

    def s14(self,i):                
        self.Pin_GROUP(13)    
        self.Pin_Coflict(13)
        
    def s15(self,i):                
        self.Pin_GROUP(14)    
        self.Pin_Coflict(14)
        

    def s16(self,i):                
        self.Pin_GROUP(15)    
        self.Pin_Coflict(15)
             

    def s17(self,i):                
        self.Pin_GROUP(16)    
        self.Pin_Coflict(16)
        

    def s18(self,i):                
        self.Pin_GROUP(17)    
        self.Pin_Coflict(17)
             

    def s19(self,i):                
        self.Pin_GROUP(18)    
        self.Pin_Coflict(18)
        

    def s20(self,i):             
        self.Pin_GROUP(19)               
        self.Pin_Coflict(19)
        
                    
    def b_CLK_Change(self):
        self.b_Check(self.b_CLK,self.c_CLK)
        if self.b_CLK.isChecked() == True:
            info["p_SYSTEM_CLK"]=1
        else:
            info["p_SYSTEM_CLK"]=0

    def b_WAKEUP_Change(self):
        self.b_Check(self.b_WAKEUP,self.c_WAKEUP)
        #self.be_Check(self.b_WAKEUP,self.e_CLK)
        if self.b_WAKEUP.isChecked() == True:
            info["p_WAKEUP"]=2
        else:
            info["p_WAKEUP"]=0



    def b_CLKOUT_Change(self):
        self.b_Check(self.b_CLKOUT,self.c_CLKOUT)
        if self.b_CLKOUT.isChecked() == True:
            info["p_CLKOUT"]=3
        else:
            info["p_CLKOUT"]=0

    def b_WDT_Change(self):
        self.b_Check(self.b_WDT,self.c_WDT)
        self.b_Check(self.b_WDT,self.c_WDT_TIMEOUT)
        if self.b_WDT.isChecked() == True:
            info["p_WDT"]=4
        else:
            info["p_WDT"]=0

    def b_GPIO_change(self):
         if self.b_GPIO.isChecked()==True:
            info["p_GPIO_INIT"]=2
            self.t_GPIO.setEnabled(True) 
         else:
            info["p_GPIO_INIT"]=0
            self.t_GPIO.setEnabled(False) 

    def b_INT0_Change(self):
         self.b_Check(self.b_INT0,self.c_INT0)
         self.b_Check(self.b_INT0,self.c_INT0_PINSELECT)
         if self.b_INT0.isChecked() == True:
            info["p_INT0"]=6
         else:
            info["p_INT0"]=0
    def b_INT1_Change(self):
         self.b_Check(self.b_INT1,self.c_INT1)
         self.b_Check(self.b_INT1,self.c_INT1_PINSELECT)
         if self.b_INT1.isChecked() == True:
            info["p_INT1"]=7
         else:
            info["p_INT1"]=0        

    def b_PIN_Change(self):
         self.b_Check(self.b_PININT,self.c_PIN_INT_PORT)
         self.b_Check(self.b_PININT,self.c_PIN0)
         self.b_Check(self.b_PININT,self.c_PIN1)
         self.b_Check(self.b_PININT,self.c_PIN2)
         self.b_Check(self.b_PININT,self.c_PIN3)
         self.b_Check(self.b_PININT,self.c_PIN4)
         self.b_Check(self.b_PININT,self.c_PIN5)
         self.b_Check(self.b_PININT,self.c_PIN6)
         self.b_Check(self.b_PININT,self.c_PIN7) 
         if self.b_PININT.isChecked() == True:
            info["p_PIN_INT"]=8
         else:
            info["p_PIN_INT"]=0

    def b_UART0_Change(self):  
        self.b_Check(self.b_UART0,self.c_UART0)          
        self.b_Check(self.b_UART0,self.c_UART0_Timer)         
        self.b_Check(self.b_UART0,self.c_UART0_BaudRate) 
        if self.b_UART0.isChecked() == True:
            info["p_UART0"]=9
        else:
            info["p_UART0"]=0
    def b_UART1_Change(self):  
        self.b_Check(self.b_UART1,self.c_UART1)          
        self.b_Check(self.b_UART1,self.c_UART1_Timer)         
        self.b_Check(self.b_UART1,self.c_UART1_BaudRate) 
        if self.b_UART1.isChecked() == True:
            info["p_UART1"]=10
        else:
            info["p_UART1"]=0

    def b_ADC_Change(self):
         self.b_Check(self.b_ADC,self.c_ADC)
         self.b_Check(self.b_ADC,self.c_ADC_CH)
         if self.b_ADC.isChecked() == True:
            info["p_ADC"]=11
         else:
            info["p_ADC"]=0

    def b_PWM_Change(self):
         self.b_Check(self.b_PWM,self.c_PWM)
         self.b_Check(self.b_PWM,self.c_PWM_CH)
         if self.b_PWM.isChecked() == True:
            info["p_PWM"]=12
         else:
            info["p_PMW"]=0

    def b_Timer0_Change(self):
        self.b_Check(self.b_Timer0,self.c_Timer0)
        self.b_Check(self.b_Timer0,self.c_Timer0_Mode)
        if self.b_Timer0.isChecked() == True:
            info["p_TIMER0"]=13
        else:
            info["p_TIMER0"]=0

    def b_Timer1_Change(self):
        self.b_Check(self.b_Timer1,self.c_Timer1)
        self.b_Check(self.b_Timer1,self.c_Timer1_Mode)
        if self.b_Timer1.isChecked() == True:
            info["p_TIMER1"]=14
        else:
            info["p_TIMER1"]=0

    def b_Timer3_Change(self):
        self.b_Check(self.b_Timer3,self.c_Timer3)
        if self.b_PWM.isChecked() == True:
            info["b_Timer3"]=15
        else:
            info["b_Timer3"]=0
    '''
    def eventFilter(self, object, event):                           
        if object==self.e_CLK:
            if event.type()==QEvent.FocusOut:
                if(int(self.e_CLK.text())<100 or int(self.e_CLK.text())>26112000):
                        self.e_CLK.setText("100")
                else:
                   pre={1,4,16,64,512,1024}
                   t_cont=[]
                   all_count=[]
                   clocksource=(1/10000)*1000000 #us
                   find=0
                   for i in range(1,256):
                        t_cont.append(i)
                   for pr in pre:
                       for t_con in t_cont:
                           if t_con*pr*clocksource == int(self.e_CLK.text()):
                               print(str(t_con))
                               print(str(pr))
                               print(str(t_con*pr*clocksource))
                               find=1
                   if find ==0:
                        for pr in pre:
                            for t_con in t_cont:
                                if t_con*pr*clocksource < (int(self.e_CLK.text())*1.005):
                                   if t_con*pr*clocksource > (int(self.e_CLK.text())*0.995):
                                        print("WAKEUP")
                                        print(str(t_con))
                                        print(str(pr))
                                        print(str(t_con*pr*clocksource))
                                        print(str(int(self.e_CLK.text())*1.005))
                                        print(str(int(self.e_CLK.text())*0.995))
        return QMainWindow.eventFilter(self,object,event) ##other event
    '''

    def GEN(self):
        Q_System.clear()        
        Q_POLL.clear()
        Q_INTERRUPT_HANDLER.clear()
        Q_FUNCTION.clear()
        Q_INTERRUPT_INIT.clear()
#clock
        if(info["p_SYSTEM_CLK"]!=0):
            info["CLK_SOURCE"]=self.c_CLK.currentText()
            CLK_SOURCE=self.TREE.find("./CLK_SOURCE/"+info["CLK_SOURCE"])
            temp=info["p_SYSTEM_CLK"]
            title="//System Clock Initial"
            Q_System[temp]=title+CLK_SOURCE.text  


#pins initial
        if(info["p_GPIO_INIT"]!=0):
            s_temp="//GPIO INIT\n\r"
            for te in range(0,20):
                if self.combox_list_gpio_mode[te].currentText()!="":
                   s_temp=s_temp+self.t_GPIO.item(te,0).text()+self.combox_list_gpio_mode[te].currentText()+";\n"            
            temp=info["p_GPIO_INIT"]
            Q_System[temp]=s_temp
        
#WAKEUP 
        info["WAKEUP_MODE"]=self.c_WAKEUP.currentText()
        if(info["p_WAKEUP"]!=0):
            if self.c_WAKEUP.currentText()=="POLL":            
                POLL=TREE.find("./WDT/POLL")       
                temp=info["p_WAKEUP"]
                title="//Wakeup Initial\n\r"
                Q_POLL[temp]=title+POLL.text

            if self.c_WAKEUP.currentText()=="INTERRUPT":
                INTERRUPT=self.TREE.find("./WAKEUP/INTERRUPT")       
                temp=info["p_WAKEUP"]
                Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text
                INTERRUPT_INIT=self.TREE.find("./WAKEUP/INTERRUPT_INIT")       
                temp=info["p_WAKEUP"]
                title="//Wakeup Initial\n\r"
                Q_INTERRUPT_INIT[temp]=title+INTERRUPT_INIT.text
#WDT

        if(info["p_WDT"]!=0):
            if self.c_WDT.currentText()=="POLL":  
                POLL=self.TREE.find("./WDT/POLL")       
                temp=info["p_WDT"]
                title="//WDT Initial\n\r"
                Q_POLL[temp]=title+POLL.text

            if self.c_WDT.currentText()=="INTERRUPT":
                INTERRUPT=self.TREE.find("./WDT/INTERRUPT")       
                temp=info["p_WDT"]
                Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text

                INTERRUPT_INIT=self.TREE.find("./WDT/INTERRUPT_INIT")       
                temp=info["p_WDT"]
                title="//WDT Initial\n\r"
                Q_INTERRUPT_INIT[temp]=title+INTERRUPT_INIT.text

#CLKOUT
        if(info["p_CLKOUT"]!=0):
            if self.c_CLKOUT.currentText()=="POLL":
                POLL=self.TREE.find("./CLKOUT/POLL")       
                temp=info["p_CLKOUT"]
                title="//CLK OUT Initial\n\r"
                Q_System[temp]=title+POLL.text

            if self.c_CLKOUT.currentText()=="INTERRUPT":
               INTERRUPT=self.TREE.find("./CLKOUT/INTERRUPT")       
               temp=info["p_CLKOUT"]
               Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text

               INTERRUPT_INIT=self.TREE.find("./CLKOUT/INTERRUPT_INIT")       
               temp=info["p_CLKOUT"]
               Q_INTERRUPT_INIT[temp]=INTERRUPT_INIT.text


#INT0
        if(info["p_INT0"]!=0):
            if self.c_INT0.currentText()=="POLL":
                 POLL=self.TREE.find("./INT0/POLL")       
                 temp=info["p_INT0"]
                 Q_POLL[temp]=POLL.text

            if self.c_INT0.currentText()=="INTERRUPT":
                INTERRUPT=self.TREE.find("./INT0/INTERRUPT")       
                temp=info["p_INT0"]
                Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text

                INTERRUPT_INIT=self.TREE.find("./INT0/INTERRUPT_INIT")                  
                INTERRUPT_PIN_SELECT=self.TREE.find("./INT0/"+ self.c_INT0_PINSELECT.currentText())
       
                temp=info["p_INT0"]
                Q_INTERRUPT_INIT[temp]=INTERRUPT_INIT.text+INTERRUPT_PIN_SELECT.text

#INT1
        if(info["p_INT1"]!=0):
            if self.c_INT1.currentText()=="POLL":
                 POLL=self.TREE.find("./INT1/POLL")       
                 temp=info["p_INT1"]
                 Q_POLL[temp]=POLL.text

            if self.c_INT1.currentText()=="INTERRUPT":
                INTERRUPT=self.TREE.find("./INT1/INTERRUPT")       
                temp=info["p_INT1"]
                Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text

                INTERRUPT_INIT=self.TREE.find("./INT1/INTERRUPT_INIT")       
                INTERRUPT_PIN_SELECT=self.TREE.find("./INT1/"+ self.c_INT1_PINSELECT.currentText())       
                temp=info["p_INT1"]
                Q_INTERRUPT_INIT[temp]=INTERRUPT_INIT.text+INTERRUPT_PIN_SELECT.text

#PIN INTERRUPT
        if (info["p_PIN_INT"]!=0):
                INTERRUPT=self.TREE.find("./PIN_INT/INTERRUPT")       
                temp=info["p_PIN_INT"]
                Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text

                INTERRUPT_INIT=self.TREE.find("./PIN_INT/INTERRUPT_INIT")       
                s_temp=self.c_PIN_INT_PORT.currentText()+";\n\r"
                if(self.c_PIN0.currentText()!="NONE"):      
                    s_temp=s_temp+self.c_PIN0.currentText()+";\n\r"
                if(self.c_PIN1.currentText()!="NONE"):      
                    s_temp=s_temp+self.c_PIN1.currentText()+";\n\r"
                if(self.c_PIN2.currentText()!="NONE"):                                      
                    s_temp=s_temp+self.c_PIN2.currentText()+";\n\r"
                if(self.c_PIN3.currentText()!="NONE"):      
                    s_temp=s_temp+self.c_PIN3.currentText()+";\n\r"
                if(self.c_PIN4.currentText()!="NONE"):      
                    s_temp=s_temp+self.c_PIN4.currentText()+";\n\r"
                if(self.c_PIN5.currentText()!="NONE"):      
                    s_temp=s_temp+self.c_PIN5.currentText()+";\n\r"
                if(self.c_PIN6.currentText()!="NONE"):      
                    s_temp=s_temp+self.c_PIN6.currentText()+";\n\r"
                if(self.c_PIN7.currentText()!="NONE"):      
                    s_temp=s_temp+self.c_PIN7.currentText()+";\n\r"

                temp=info["p_PIN_INT"]
                Q_INTERRUPT_INIT[temp]=INTERRUPT_INIT.text+s_temp


#UART0
        if (info["p_UART0"]!=0):
            if self.c_UART0.currentText()=="POLL":
                POLL=self.TREE.find("./UART0/POLL")   
                UART_CLK_SOURCE=self.TREE.find("./UART0/"+self.c_UART0_Timer.currentText())
                temp=info["p_UART0"]
                Q_POLL[temp]=UART_CLK_SOURCE.text+POLL.text


            if self.c_UART0.currentText()=="INTERRUPT":
                INTERRUPT=self.TREE.find("./UART0/INTERRUPT")       
                temp=info["p_UART0"]
                Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text

                INTERRUPT_INIT=self.TREE.find("./UART0/INTERRUPT_INIT")  
                UART_CLK_SOURCE=self.TREE.find("./UART0/"+info["UART0_TIMER"])            
                Q_INTERRUPT_INIT[temp]=UART_CLK_SOURCE.text+INTERRUPT_INIT.text

#UART1
        if (info["p_UART1"]!=0):
            if self.c_UART1.currentText()=="POLL":
                POLL=self.TREE.find("./UART1/POLL")   
                UART_CLK_SOURCE=self.TREE.find("./UART1/"+self.c_UART1_Timer.currentText())
                temp=info["p_UART1"]
                Q_POLL[temp]=UART_CLK_SOURCE.text+POLL.text


            if self.c_UART1.currentText()=="INTERRUPT":
                INTERRUPT=self.TREE.find("./UART1/INTERRUPT")       
                temp=info["p_UART1"]
                Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text

                INTERRUPT_INIT=self.TREE.find("./UART1/INTERRUPT_INIT")  
                UART_CLK_SOURCE=self.TREE.find("./UART1/"+self.c_UART1_Timer.currentText())            
                Q_INTERRUPT_INIT[temp]=UART_CLK_SOURCE.text+INTERRUPT_INIT.text

#ADC
        if (info["p_ADC"]!=0):
            if self.c_ADC.currentText()=="POLL":
                POLL=self.TREE.find("./ADC/POLL")   
                ADC_PIN_SOURCE=self.TREE.find("./ADC/ADC_CH/"+self.c_ADC_CH.currentText())
                temp=info["p_ADC"]
                Q_POLL[temp]=ADC_PIN_SOURCE.text+POLL.text


            if self.c_ADC.currentText()=="INTERRUPT":
                INTERRUPT=self.TREE.find("./ADC/INTERRUPT")       
                temp=info["p_ADC"]
                Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text

                INTERRUPT_INIT=self.TREE.find("./ADC/INTERRUPT_INIT")  
                ADC_PIN_SOURCE=self.TREE.find("./ADC/ADC_CH/"+self.c_ADC_CH.currentText())            
                Q_INTERRUPT_INIT[temp]=ADC_PIN_SOURCE.text+INTERRUPT_INIT.text


#PWM
        if (info["p_PWM"]!=0):
            if self.c_PWM.currentText()=="POLL":
                INIT=self.TREE.find("./PWM/INIT")   
                PWM_PIN_SOURCE=self.TREE.find("./PWM/PWM_PIN/"+self.c_PWM_CH.currentText())
                INIT_PMW_CLK=self.TREE.find("./PWM/INIT_PMW_CLK")
                PWM_PIN_CLK=0
                if "PWM0" in PWM_PIN_SOURCE.text:
                    PWM_PIN_CLK=self.TREE.find("./PWM/INIT_PMW0")
                if "PWM1" in PWM_PIN_SOURCE.text:
                    PWM_PIN_CLK=self.TREE.find("./PWM/INIT_PMW1")
                if "PWM2" in PWM_PIN_SOURCE.text:
                    PWM_PIN_CLK=self.TREE.find("./PWM/INIT_PMW2")
                if "PWM3" in PWM_PIN_SOURCE.text:
                    PWM_PIN_CLK=self.TREE.find("./PWM/INIT_PMW3")
                if "PWM4" in PWM_PIN_SOURCE.text:
                    PWM_PIN_CLK=self.TREE.find("./PWM/INIT_PMW4")
                if "PWM5" in PWM_PIN_SOURCE.text:
                    PWM_PIN_CLK=self.TREE.find("./PWM/INIT_PMW5")


                temp=info["p_PWM"]
                Q_POLL[temp]=PWM_PIN_SOURCE.text+INIT_PMW_CLK.text+PWM_PIN_CLK.text+INIT.text


            if self.c_PWM.currentText()=="INTERRUPT":
                INTERRUPT=self.TREE.find("./PWM/INTERRUPT")       
                temp=info["p_PWM"]
                Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text
                INIT_PMW_CLK=self.TREE.find("./PWM/INIT_PMW_CLK")
                PWM_PIN_CLK=0
                PWM_PIN_SOURCE=self.TREE.find("./PWM/PWM_PIN/"+self.c_PWM_CH.currentText())
                if "PWM0" in PWM_PIN_SOURCE.text:
                    PWM_PIN_CLK=self.TREE.find("./PWM/INIT_PMW0")
                if "PWM1" in PWM_PIN_SOURCE.text:
                    PWM_PIN_CLK=self.TREE.find("./PWM/INIT_PMW1")
                if "PWM2" in PWM_PIN_SOURCE.text:
                    PWM_PIN_CLK=self.TREE.find("./PWM/INIT_PMW2")
                if "PWM3" in PWM_PIN_SOURCE.text:
                    PWM_PIN_CLK=self.TREE.find("./PWM/INIT_PMW3")
                if "PWM4" in PWM_PIN_SOURCE.text:
                    PWM_PIN_CLK=self.TREE.find("./PWM/INIT_PMW4")
                if "PWM5" in PWM_PIN_SOURCE.text:
                    PWM_PIN_CLK=self.TREE.find("./PWM/INIT_PMW5")
                INTERRUPT_INIT=self.TREE.find("./PWM/INTERRUPT_INIT")  
                PWM_PIN_SOURCE=self.TREE.find("./PWM/PWM_PIN/"+self.c_PWM_CH.currentText())   
                INIT_PMW_CLK=self.TREE.find("./PWM/INIT_PMW_CLK")        
                Q_INTERRUPT_INIT[temp]=PWM_PIN_SOURCE.text+INIT_PMW_CLK.text+PWM_PIN_CLK.text+INTERRUPT_INIT.text

#timer3
        if (info["p_TIMER3"]!=0):
            if self.c_Timer3.currentText()=="POLL":
                INIT=self.TREE.find("./TIMER3/INIT")   
                POLL=self.TREE.find("./TIMER3/POLL") 
                temp=info["p_TIMER3"]
                Q_POLL[temp]=INIT.text+POLL.text

            if self.c_Timer3.currentText()=="INTERRUPT":
                INTERRUPT=self.TREE.find("./TIMER3/INTERRUPT")       
                temp=info["p_TIMER3"]
                Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text

                INIT=self.TREE.find("./TIMER3/INIT")   
                INTERRUPT_INIT=self.TREE.find("./TIMER3/INTERRUPT_INIT")        
                Q_INTERRUPT_INIT[temp]=INIT.text+INTERRUPT_INIT.text

#timer0
        if (info["p_TIMER0"]!=0):
            if self.c_Timer0.currentText()=="POLL":
                INIT=self.TREE.find("./"+self.c_Timer0_Mode.currentText()+"/INIT")   
                POLL=self.TREE.find("./"+self.c_Timer0_Mode.currentText()+"/POLL") 
                temp=info["p_TIMER0"]
                Q_POLL[temp]=INIT.text+POLL.text

            if self.c_Timer0.currentText()=="INTERRUPT":
                INTERRUPT=self.TREE.find("./"+self.c_Timer0_Mode.currentText()+"/INTERRUPT")       
                temp=info["p_TIMER0"]
                Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text

                INIT=self.TREE.find("./"+self.c_Timer0_Mode.currentText()+"/INIT")   
                INTERRUPT_INIT=self.TREE.find("./"+self.c_Timer0_Mode.currentText()+"/INTERRUPT_INIT")        
                Q_INTERRUPT_INIT[temp]=INIT.text+INTERRUPT_INIT.text

#timer1
        if (info["p_TIMER1"]!=0):
            if self.c_Timer1.currentText()=="POLL":
                INIT=self.TREE.find("./"+self.c_Timer1_Mode.currentText()+"/INIT")   
                POLL=self.TREE.find("./"+self.c_Timer1_Mode.currentText()+"/POLL") 
                temp=info["p_TIMER1"]
                Q_POLL[temp]=INIT.text+POLL.text

            if self.c_Timer1.currentText()=="INTERRUPT":
                INTERRUPT=self.TREE.find("./"+self.c_Timer1_Mode.currentText()+"/INTERRUPT")       
                temp=info["p_TIMER1"]
                Q_INTERRUPT_HANDLER[temp]=INTERRUPT.text

                INIT=self.TREE.find("./"+self.c_Timer1_Mode.currentText()+"/INIT")   
                INTERRUPT_INIT=self.TREE.find("./"+self.c_Timer1_Mode.currentText()+"/INTERRUPT_INIT")        
                Q_INTERRUPT_INIT[temp]=INIT.text+INTERRUPT_INIT.text


        if (self.b_IAP_Erase.isChecked()):
             IAP_DEFINE=self.TREE.find("./IAP/IAP_DEFINE")  
             IAP_TRIGGER=self.TREE.find("./IAP/IAP_TRIGGER") 
             IAP_ERASE=self.TREE.find("./IAP/IAP_ERASE") 
             Q_FUNCTION[0]=IAP_DEFINE.text
             Q_FUNCTION[1]=IAP_TRIGGER.text
             Q_FUNCTION[2]=IAP_ERASE.text

        if (self.b_IAP_Program.isChecked()):
             IAP_DEFINE=self.TREE.find("./IAP/IAP_DEFINE")  
             IAP_TRIGGER=self.TREE.find("./IAP/IAP_TRIGGER") 
             IAP_Program=self.TREE.find("./IAP/IAP_Program") 
             Q_FUNCTION[0]=IAP_DEFINE.text
             Q_FUNCTION[1]=IAP_TRIGGER.text
             Q_FUNCTION[3]=IAP_Program.text

        if (self.b_IAP_Read.isChecked()):
             IAP_DEFINE=self.TREE.find("./IAP/IAP_DEFINE")  
             IAP_TRIGGER=self.TREE.find("./IAP/IAP_TRIGGER") 
             IAP_Read=self.TREE.find("./IAP/IAP_Read") 
             Q_FUNCTION[0]=IAP_DEFINE.text
             Q_FUNCTION[1]=IAP_TRIGGER.text
             Q_FUNCTION[4]=IAP_Read.text
               
        self.e_GEN_CODE.setText("")
        self.e_GEN_CODE.append("#include \"N76E003.h\"")
        self.e_GEN_CODE.append("#include \"SFR_Macro.h\"")
        self.e_GEN_CODE.append("#include \"Function_define.h\"")
        self.e_GEN_CODE.append("#include \"Common.h\"")
        self.e_GEN_CODE.append("#include \"Delay.h\"")
        self.e_GEN_CODE.append(" ")
        self.e_GEN_CODE.append("//interrupt function")
        #out put arrary
        for k,v in Q_INTERRUPT_HANDLER.items():
            #print(v)
            self.e_GEN_CODE.append(v)
        self.e_GEN_CODE.append(" ")
        self.e_GEN_CODE.append("//Function define")
        #out put arrary
        for k,v in Q_FUNCTION.items():
            #print(v)
            self.e_GEN_CODE.append(v)
        #print("void main(void)")
        #print("{")
        self.e_GEN_CODE.append(" ")
        self.e_GEN_CODE.append("//main code")
        self.e_GEN_CODE.append("void main(void)")
        self.e_GEN_CODE.append("{")
        for k,v in Q_System.items():
            #print(v)
            self.e_GEN_CODE.append(v)

        for k,v in Q_INTERRUPT_INIT.items():
            #print(v)
            self.e_GEN_CODE.append(v)

        for k,v in Q_POLL.items():
            #print(v)
            self.e_GEN_CODE.append(v)
        self.e_GEN_CODE.append("while(1);")
        self.e_GEN_CODE.append("}")
        with open('.\\N76E003_BSP_Keil\\Sample_Code\\PROJECT\\Code\\main.c', 'w') as the_file:
                the_file.write(self.e_GEN_CODE.toPlainText())

        Achive_Folder_To_ZIP(".\\N76E003_BSP_Keil");
        #print("while(1);")
        #print("}")
        '''
        #PWM CAL
        pre={1,4,16,64,512,1024}
        t_cont=[]
        all_count=[]
        clocksource=16000000 
        find=0
        #for i in range(1,65536):
        #    t_cont.append(i)
        for pr in pre:
            for t_con in range(1,65536):
                if  (clocksource/pr)/t_con == int(self.e_PWM_F.text()):
                        print(str(t_con))
                        print(str(pr))
                        print(str( (clocksource/pr)/t_con))
                        find=1
        if find ==0:
            for pr in pre:
                for t_con in range(1,65536):
                    if (clocksource/pr)/t_con < (int(self.e_PWM_F.text())*1.005):
                            if (clocksource/pr)/t_con > (int(self.e_PWM_F.text())*0.995):
                                        print("WAKEUP")
                                        print(str(t_con))
                                        print(str(pr))
                                        print(str( (clocksource/pr)/t_con ))
                                        print(str(int(self.e_CLK.text())*1.005))
                                        print(str(int(self.e_CLK.text())*0.995)) 
        '''
if __name__ == "__main__":  
    app = QApplication(sys.argv) 
    s = QStyleFactory.create('Fusion')
    app.setStyle(s)
    myWin = MyMainWindow() 
     
    myWin.show()  
    sys.exit(app.exec_())
