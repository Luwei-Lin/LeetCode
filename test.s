; Course: COMP2280
; Lab:    5
; Author: Huayi Chen
;
            .orig  x3000
Main
            LD     R6,STACKBASE   ;set up user stack (MUST be done)

            LEA    R0,KBHandler  
            LD     R1,KBVEC
            STR    R0,R1,#0       ;set kb interrupt vector

            LD     R0,KBEN        ;enable keyboard interrupt
            STI    R0,KBSR
Loop
            BR  Loop              ;loop forever!
            HALT

;---------------------------------------------------------------
; Keyboard interrupt handler (no need for Frame pointer)
; R0 - character from keyboard, character to output
; R1 - ascii base value for output
; R2 - counts of how many 1-bit 
; R3 - temp value to store character from keyboard(ASCII)   
KBHandler
            ADD    R6,R6,#-1      ; save R0 exception 
            STR    R0,R6,#0         
            ADD    R6,R6,#-1      ; save R1
            STR    R1,R6,#0

            AND    R2,R2,#0       ; initial count number
            
            LDI    R0,KBDR        ; 得到的是 ascii码 对应的hex值，保存到R0
            
LoopCounting        
            BRz    quitLoop       ; if character not equal to 0
            ADD    R2,R2,#1       ; count number +1， 
            
            AND    R3,R3,#0       ; 又重新初始化R3值为0
            ADD    R3,R3,R0       ; ， R0 + 0 = R3  重新得到 递减后的 char 的asciiz码 （保存在R0里）
            ADD    R3,R3,#-1      ; 每次都减1， 直到下一步R0为空''跳出循环，这个offset的值（保存在R2已经）
            
            AND    R0,R0,R3       ; #比如 64 & 65 = 64 把减1后的R3值赋给R0， R0来判断是否跳出循环
                                    #如果输入是65 ‘A' 65 & 64 = 64
                                    #               
                                    #               64 & 63 = 0    跳出循环 R2 为2， 输出为‘2’
                                    #
                                    #如果输入 70 ‘F'。70 & 69 = 68
                                    #                68 & 67 = 64
                                    #                64 & 63 = 0    R2 = 3 输出为‘3’
                                    #如果输入 103 ‘g'  103 & 102 = 102
                                    #                 102 & 101 = 100
                                    #                 100 & 99 = 96
                                    #                 96 & 95  = 64
                                    #                 64 & 63 = 0      R2 = 5 输出为‘5’
                                    # 你就这样既然去年的是 2 3 4 5 6， 那么今天 6 5 4 3 2， 你还是用相同的算法这里
                                    #但是你算R2在外面的时候给他 R2 = 8 - R2 就反过来了
            BRnp   LoopCounting    
quitLoop

            LD     R1,ASCII       ; decimal digit base value
            AND    R0,R0,#0
            ADD    R0,R1,R2       ; show counts integer

WaitToWrite
            LDI    R1,DSR         ; get console output status
            BRzp   WaitToWrite

            STI    R0,DDR         ; write new character to console

            LDR    R1,R6,#0       ; restore r1
            ADD    R6,R6,#1
            LDR    R0,R6,#0       ; restore r0
            ADD    R6,R6,#1
            RTI                   ; return from interrupt

STACKBASE   .FILL  x4000          ;stack base (can be changed)
KBSR







----------------------------------------------------------------
;Keyboard interrupt test
;Each time a key is pressed, echo the character.
;Pretty standard code that waits for interrupts and then processes them.


.orig x3000

;this is the main line
Main
 LD R6,STACKBASE  ;set up user stack (MUST be done)

 LEA R0,KBHandler  
 LD R1,KBVEC
 STR R0,R1,#0  ;set kb interrupt vector

 LD R0,KBEN  ;enable keyboard interrupt
 STI R0,KBSR

Loop
 BR Loop   ;loop forever!

 HALT
;---------------------------------------------------------------
;Keyboard interrupt handler (no need for Frame pointer)
KBHandler
 ADD R6,R6,#-1 ;save R0
 STR R0,R6,#0
 ADD R6,R6,#-1 ;save R1
 STR R1,R6,#0

 LDI R0,KBDR ;get key 

WaitToWrite
 LDI     R1,DSR ;get console output status
 BRzp    WaitToWrite

 STI R0,DDR ;write new character to console

 LDR R1,R6,#0 ;restore the registers
 ADD R6,R6,#1

 LDR R0,R6,#0
 ADD R6,R6,#1

 RTI  ;return from interrupt


STACKBASE    .FILL   x4000 ;stack base (can be changed)
KBSR       .FILL xFE00 ;keyboard status register
KBDR     .FILL xFE02 ;keyboard data register 
DSR         .FILL xFE04 ;console status register
DDR      .FILL xFE06 ;console data register 


KBEN .FILL x4000 ;use to enable keyboard interrupt
KBVEC .FILL x0180 ;keyboard vector number/location

 .END