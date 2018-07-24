#include "N76E003.h"
#include "SFR_Macro.h"
#include "Function_define.h"
#include "Common.h"
#include "Delay.h"
 
//interrupt function

      /************************************************************************************************************
      *    WDT interrupt sub-routine
      ************************************************************************************************************/
      void WDT_ISR (void) interrupt 10
      {
      clr_WDTF; //clear WDT interrupt flag
      set_WDCLR;
      //USER CODE....
      }
    
 
//Function define
 
//main code
void main(void)
{

      ////***** LIRC enable part*****
      ////** Since LIRC is always enable, switch to LIRC directly
      set_OSC1; //step3: switching system clock source if needed
      clr_OSC0;
      while((CKEN)==1);  //step4: check system clock switching OK or NG
      clr_HIRCEN;
    

      set_CLOEN;  //System Clock Output Enable
    

      //WDT init
      //--------------------------------------------------------
      //Warning:
      //Pleaes always check CONFIG WDT disable first
      //only when WDT reset disable, WDT use as pure timer
      //--------------------------------------------------------
      TA=0xAA;
      TA=0x55;
      WDCON=vWDCON; //Setting WDT prescale
      set_WDTR;  //WDT run
      set_WDCLR;  //Clear WDT timer
      set_EWDT;
      //set_WIDPD;  //WDT run in POWER DOWM mode setting if needed
    
while(1);
}