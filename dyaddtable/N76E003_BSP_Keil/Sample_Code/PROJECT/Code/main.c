#include "N76E003.h"
#include "SFR_Macro.h"
#include "Function_define.h"
#include "Common.h"
#include "Delay.h"
 
//interrupt function

      void WakeUp_Timer_ISR (void)  interrupt 17 //ISR for self wake-up timer
      {
      clr_WKTF; //clear wakeup interrupt flag
      //USER CODE....
      }
    

      void EXT_INT0(void) interrupt 0
      {

      }
    
 
//Function define
 
//main code
void main(void)
{
//System Clock Initial
      ////***** LIRC enable part*****
      ////** Since LIRC is always enable, switch to LIRC directly
      set_OSC1; //step3: switching system clock source if needed
      clr_OSC0;
      while((CKEN)==1);  //step4: check system clock switching OK or NG
      clr_HIRCEN;
    
//GPIO INIT

P05_Input_Mode;
P06_Input_Mode;
P07_Input_Mode;
P20_Input_Mode;
P30_Input_Mode;
P17_Input_Mode;
P16_Input_Mode;
P15_Input_Mode;
P14_Input_Mode;
P13_Input_Mode;
P12_Input_Mode;
P11_Input_Mode;
P10_Input_Mode;
P00_Input_Mode;
P01_Input_Mode;
P02_Input_Mode;
P03_Input_Mode;
P04_Input_Mode;

//Wakeup Initial

      WKCON = vWKCON; //timer base 10k, Pre-scale = 1/WKCON setting Value
      RWK = vRWK;
      set_EWKT; // enable WKT interrupt
      set_WKTR; // Wake-up timer run
    

      set_EX0;  //ENABLE INT0 interrrupt
    
      IT0 = 0; //LOW LEVEL      
    
while(1);
}