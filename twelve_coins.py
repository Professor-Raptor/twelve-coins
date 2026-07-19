

#   Twelve Coins
#   Professor_Raptor
#   2025/2026

version = 'v1.2'


#   TODO
#   add something more after win/loss?
#   add different dialogue based on current strategy
#   Assess for other compatability issues?
#   add win/loss state(s) dependent on if they guessed at end?
#   add more easter egg(s)? one with specific solution?
#   Improve animation/art?
#   Clean up and optimize (lol, jk)




zonebox=r'''                                                                                                       
  ╔═════════════════════════════════════════════════════════════════════════════════════════════════╗  
  ║ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░                                                                                           ░░ ║  
  ║ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ║  
  ╚═════════════════════════════════════════════════════════════════════════════════════════════════╝  
                                                                                                       '''


scale_R2=r'''
                                                                                                     
                                                                                                     
                        <=.__                                                                        
                        '=.||'==.__                                                                  
                           ||'==.__'==.__           _                                                
                           ||      '==.__'==.__    /8\                                               
                         .'  `.          '==.__'==.|8|                                               
                       .'      `.              '==.|8|'==.__                                         
                     .'          `.                |8|'==.__'==.__                                   
                   .'              `.              |8|      '==.__'==.__                             
                 .'                  `.            |8|            '==.__'==.__                       
               .'                      `.          |8|                  '==.||'==.                   
             .'                          `.        |8|                      ||'='                    
           .'                              `.      |8|                      ||                       
           \\                              //      |8|                    .'  `.                     
            `=============================='       |8|                  .'      `.                   
                                                   |8|                .'          `.                 
                                                   |8|              .'              `.               
                                                   |8|            .'                  `.             
                                                   |8|          .'                      `.           
                                                   |8|        .'                          `.         
                                                   |8|      .'                              `.       
                                                   |8|      \\                              //       
                                                   |8|       `=============================='        
                                                   |8|                                               
                                                  /|8|\                                              
                                                 /8|8|8\                                             
                                            __--'88|8|88'--__                                        
                                         __/8888888|8|8888888\__                                     
                                        /8888888888|8|8888888888\                                    
                                        '======================='                                    
                                                                                                     
                                                                                                     
'''
scale_L2=r'''
                                                                                                     
                                                                                                     
                                                                            __.=>                    
                                                                      __.=='||.='                    
                                                    _           __.=='__.=='||                       
                                                   /8\    __.=='__.=='      ||                       
                                                   |8|.=='__.=='          .'  `.                     
                                             __.=='|8|.=='              .'      `.                   
                                       __.=='__.=='|8|                .'          `.                 
                                 __.=='__.=='      |8|              .'              `.               
                           __.=='__.=='            |8|            .'                  `.             
                       .=='||.=='                  |8|          .'                      `.           
                        '='||                      |8|        .'                          `.         
                           ||                      |8|      .'                              `.       
                         .'  `.                    |8|      \\                              //       
                       .'      `.                  |8|       `=============================='        
                     .'          `.                |8|                                               
                   .'              `.              |8|                                               
                 .'                  `.            |8|                                               
               .'                      `.          |8|                                               
             .'                          `.        |8|                                               
           .'                              `.      |8|                                               
           \\                              //      |8|                                               
            `=============================='       |8|                                               
                                                   |8|                                               
                                                  /|8|\                                              
                                                 /8|8|8\                                             
                                            __--'88|8|88'--__                                        
                                         __/8888888|8|8888888\__                                     
                                        /8888888888|8|8888888888\                                    
                                        '======================='                                    
                                                                                                     
                                                                                                     
'''
scale_R1=r'''
                                                                                                     
                                                                                                     
                                                                                                     
                                                                                                     
                                                    _                                                
                        _____                      /8\                                               
                        \__||""""""=======......___|8|___                                            
                           ||""""""=======......___|8|___""""""=======......_____                    
                           ||                      |8|   """"""=======......||__/                    
                         .'  `.                    |8|                      ||                       
                       .'      `.                  |8|                      ||                       
                     .'          `.                |8|                    .'  `.                     
                   .'              `.              |8|                  .'      `.                   
                 .'                  `.            |8|                .'          `.                 
               .'                      `.          |8|              .'              `.               
             .'                          `.        |8|            .'                  `.             
           .'                              `.      |8|          .'                      `.           
           \\                              //      |8|        .'                          `.         
            `=============================='       |8|      .'                              `.       
                                                   |8|      \\                              //       
                                                   |8|       `=============================='        
                                                   |8|                                               
                                                   |8|                                               
                                                   |8|                                               
                                                   |8|                                               
                                                  /|8|\                                              
                                                 /8|8|8\                                             
                                            __--'88|8|88'--__                                        
                                         __/8888888|8|8888888\__                                     
                                        /8888888888|8|8888888888\                                    
                                        '======================='                                    
                                                                                                     
                                                                                                     
'''
scale_L1=r'''
                                                                                                     
                                                                                                     
                                                                                                     
                                                                                                     
                                                    _                                                
                                                   /8\                      _____                    
                                                ___|8|___......=======""""""||__/                    
                        _____......=======""""""___|8|___......=======""""""||                       
                        \__||......=======""""""   |8|                      ||                       
                           ||                      |8|                    .'  `.                     
                           ||                      |8|                  .'      `.                   
                         .'  `.                    |8|                .'          `.                 
                       .'      `.                  |8|              .'              `.               
                     .'          `.                |8|            .'                  `.             
                   .'              `.              |8|          .'                      `.           
                 .'                  `.            |8|        .'                          `.         
               .'                      `.          |8|      .'                              `.       
             .'                          `.        |8|      \\                              //       
           .'                              `.      |8|       `=============================='        
           \\                              //      |8|                                               
            `=============================='       |8|                                               
                                                   |8|                                               
                                                   |8|                                               
                                                   |8|                                               
                                                   |8|                                               
                                                  /|8|\                                              
                                                 /8|8|8\                                             
                                            __--'88|8|88'--__                                        
                                         __/8888888|8|8888888\__                                     
                                        /8888888888|8|8888888888\                                    
                                        '======================='                                    
                                                                                                     
                                                                                                     
'''
scale_B=r'''
                                                                                                     
                                                                                                     
                                                                                                     
                                                                                                     
                                                    _                                                
                                                   /8\                                               
                        ___________________________|8|___________________________                    
                        \__||______________________|8|______________________||__/                    
                           ||                      |8|                      ||                       
                           ||                      |8|                      ||                       
                         .'  `.                    |8|                    .'  `.                     
                       .'      `.                  |8|                  .'      `.                   
                     .'          `.                |8|                .'          `.                 
                   .'              `.              |8|              .'              `.               
                 .'                  `.            |8|            .'                  `.             
               .'                      `.          |8|          .'                      `.           
             .'                          `.        |8|        .'                          `.         
           .'                              `.      |8|      .'                              `.       
           \\                              //      |8|      \\                              //       
            `=============================='       |8|       `=============================='        
                                                   |8|                                               
                                                   |8|                                               
                                                   |8|                                               
                                                   |8|                                               
                                                   |8|                                               
                                                  /|8|\                                              
                                                 /8|8|8\                                             
                                            __--'88|8|88'--__                                        
                                         __/8888888|8|8888888\__                                     
                                        /8888888888|8|8888888888\                                    
                                        '======================='                                    
                                                                                                     
                                                                                                     
'''
coin_rack_old=r'''
            .--.   .--.   .--.   .--.   .--.   .--.   .--.   .--.   .--.   .--.   .--.   .--. 
  Coins    ( 01 ) ( 02 ) ( 03 ) ( 04 ) ( 05 ) ( 06 ) ( 07 ) ( 08 ) ( 09 ) ( 10 ) ( 11 ) ( 12 )
            '--'   '--'   '--'   '--'   '--'   '--'   '--'   '--'   '--'   '--'   '--'   '--' 
  Round 1                                                                                            
  Round 2                                                                                            
  Round 3                                                                                            
                                                                                                     
'''
coin_pile=r'''
             .--.            
        .--.( §.--.-.        
 .--.  ( §.--.( §§ ) )       
( §§ )  '( §§ )'--'-'        
 '--'    .'--'§§ ) .--.      
        ( §§ )--' ( §§ )     
   .--.  '--'  .--.'--'      
  ( §§ )      ( §§ )    .--. 
   '--'        '--'    ( §§ )
                        '--' '''

test_coin_pile=r'''
            .--.   .--.   .--.   .--.   .--.   .--.   .--.   .--.   .--.   .--.   .--.   .--. 
  Coins    ( 01 ) ( 02 ) ( 03 ) ( 04 ) ( 05 ) ( 06 ) ( 07 ) ( 08 ) ( 09 ) ( §§ ) ( ¤¤ ) ( $$ )
            '--'   '--'   '--'   '--'   '--'   '--'   '--'   '--'   '--'   '--'   '--'   '--' 

                                 .--.                                                                      
                     .--.  .--. ( §§ )                                                                               
                    ( §§ )( §§ ) '--'--.                                                                                   
                 .-- '--'  '--'.   ( §§ )                                                                                      
                ( §§ ) .--.( §§ )--.'--'                                                                                       
                 '--' ( §§ )'--( §§ )                                                                                  
                 .--.  '--' .--.'--'                                                                           
                ( §§ )  .--( §§ ) .--.                                                                             
                 '--'  ( §§ )--' ( §§ )                                                                           
                        '--'      '--'                                                                     

                            .--.                                                                                              
                       .--.( §.--.-.                                                                                          
                .--.  ( §.--.( §§ ) )                                                                                  
               ( §§ )  '( §§ )'--'-'                                                                           
                '--'    .'--'§§ ) .--.                                                                             
                       ( §§ )--' ( §§ )                                                                           
                  .--.  '--'  .--.'--'                                                                     
                 ( §§ )      ( §§ )    .--.                                                             
                  '--'        '--'    ( §§ )                                                        
                                       '--'                                                         
'''
smaug='''                    .  : = =            :-: : -=::: - @ @%=: %@@.     :.= =:   =  -:-              
                         :+=+@@@@==::-=-==+=-      :===::-:  --: =#%*.:%@%@*@@@-.+%*=:=:. :   .    
         .=:     :.                      :#-@@@@%@+.         .*=.@%%@@@:==*..-=-*%@@===%*+*@ ==    
     .   --.-:.   .- .-:@@@+  ::.:-.::::    #@**@@@@#*@@%@@%        :*@=@#@=.+=: . :*=%=.*@@#:+@   
             .-+:  -. ::@@@*.:=.   =%#*+:     :=: :@@@@%@@%%%@%      .:@%++=:@@@%=@@%**.+:-*=.- @  
   ::      ..:.    ..=:%@@@= :-: :@@@@@@@@:        -@@@@%=@%=-=#+        @@@%=@@@=%@@%:%@@+*:::% % 
             :.     :. :@@@*. :: @@@@@@@:..:.   :  .   . @@*@@@##+:     =+@@@+ :==. :.@@**=-=@**   
   ==.         =+=  .:::-*@@#+#--@@@@@@#%*@.   .:--:     .*@%@@@@%%+       *%*%@@@=%@@@@*=%#*%-=   
   .=          .*+  :::*@@@@:  :#@@@@@@@@@@@+:.:=++%  :  :   .+%@@+@%=   . =%@#@@%%*.=@@=*@@@@==*  
 %* :: .:.  #::    #*  :*+*=::::-:%@@%@@@@@@@%@@@*  :-  %=       .@@%#    =:%@*::::-.+%@@=*@%-@ #: 
  @%= -*#.   .::=-:*. -#@@@@-.*@: +%#@@@@@@@@@%***+-    %=       =%@@%*%    %@@@*%%*:-@@@*#@@***=.:
   -++:: ==.= .==:::.  ==+%%==-:  *%%@%@@@%%@@@%%@%*    =**@*     :%%@@@+   .+*=::::.:%@@+****@ %:-
-:+: :*.**= = :   .  =.@:.:@@: .  .-=*#@@@@@@@@@@%%-  -*-::@@@@       =@%-    .%@@*#-:%@@*@%:+-=-:-
:- := .:#%= :.    *= %.@**-%+-=#-  +%%@@@@@@@@@@@%*. *#%#+.            .*%       *% :=-*@%:%@%===  
 ==--  ++::= :.  .:= ::.=##%*+=.   :=*%%@@@@@@@%%%= =#%%@@@@=.           =%:    .*=..::*==*::@@@@- 
  +: :::  *:      =-. ::  :+*+=*   ==*#%%@@@@@@%%# -%@@@@@@@@@@*-        ==+     :#@= #=@-@@+@@@  :
   ::: :: . ::.   .--. .  :#*%===:  .-=**%@@@@@%* :%@@@@@@%@%@@@@@@:       +@       +@::=.*=-:.. :*
   : .-==:=  . .-  -::=.:.  =%#==+=: -*=#%@@@@@@*:%@@@@@@@@@@@@@@@@@@:      *#:    .:-=:#::@#*+% % 
      -+:.  =::*:   .:::%*   =+@@%=:-.-:.-#@%%@@@@@@%%#@@@@@@%@@@%@@#:   :-  +#=      -#@= .:+#=# *
     :::.   #:   :     +:-:   ==*@%*:  .%.-*@@@%@@@@@@@@@@@@@@@@@@%*: ..=@@.   @=          .::= :- 
  - : *=      : :+ :@= :*=:%=  %@@*=@%-  :.=-==##@@@@%@@@@@@%@@@%=::..-@@@ +:    :.          . .:: 
   :   .     ::.-.  @=  :**==-.  .@@%%*.::.+-=::=*=+%@@@@%@@%*+=::::+@@+  .:                  ...  
     .   =   .*::*- =# :===+=:*=  .++-=@%*: **:.-:-=*%#++*%#===---:-.                         ..   
          ::  :..   -@:.=#%==*=:==   *@@%%.:*-     ..:+%@##@@==+=      ::.       .: .              
     :@%:  -: :%%+:  +@*:%@%%:=*:.-=   :*:@@@%. =%:=:- . .=*@@%@*#:::===-      :    .:             
      .@@@:     .:**  ==.:**@*+-*++ :-:  .+%#::%@@%:@*@=@%##*@*.:-++:--          ...:. ::  -       
        # @ .   -*:    -%@:.:-+:.-*+.  ::.    .*%%:@%@%@+%-=..:=*= :-          .: ..:..   :*:      
         .+==@ .   **:    :- :+**: :*%*:              ...... ..  .:          ::-=.   -::.--..      
            ::  @*.  ::   : =.-#%%-..:+%@*-.           ....:  =::          :-::. :   ...:          '''

# scale_L2= '\n'.join([line[::-1] for line in scale_R2.split('\n')])

#============================================================================================================

import sys
import os
import time
import random
import traceback

#   this probably needs to be tested
try:
    if os.name == 'nt':
        os.system('title Twelve Coins')
        import msvcrt
    else:
        sys.stdout.write(f"\033]0;Twelve_Coins\007")
        sys.stdout.flush()
except:
    pass

def flush_input():
    if os.name == 'nt':
        while msvcrt.kbhit():
            msvcrt.getch()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# s and u commands were used, need to remove
def esc(code):
    sys.stdout.write('\033['+ code)


def print_coin(col,ln,num,color):
    if num < 10:
        num = '0' + str(num)
    else:
        num = str(num)
    if color == 'gold':
        esc('38;5;220m')
        # esc('38;5;214m')
    elif color == 'grey':
        esc('38;5;240m')
    esc(str(ln)+';'+str(col)+'H')
    sys.stdout.write('.--.')
    esc('1B');esc('5D')
    sys.stdout.write('( '+num+' )')
    esc('1B');esc('5D')
    sys.stdout.write("'--'")
    esc('0m')

def print_c_stack(coords,stack):
    col = coords.col
    ln = coords.ln
    if len(stack) == 1:
        print_coin(col+3,ln+3,stack[0],'gold')
    elif len(stack) == 2:
        print_coin(col+0,ln+3,stack[0],'gold')
        print_coin(col+6,ln+3,stack[1],'gold')
    elif len(stack) == 3:
        print_coin(col-3,ln+3,stack[0],'gold')
        print_coin(col+3,ln+3,stack[1],'gold')
        print_coin(col+9,ln+3,stack[2],'gold')
    elif len(stack) == 4:
        print_coin(col-6,ln+3,stack[0],'gold')
        print_coin(col+0,ln+3,stack[1],'gold')
        print_coin(col+6,ln+3,stack[2],'gold')
        print_coin(col+12,ln+3,stack[3],'gold')
    elif len(stack) == 5:
        print_coin(col+3,ln+0,stack[0],'gold')
        print_coin(col-6,ln+3,stack[1],'gold')
        print_coin(col+0,ln+3,stack[2],'gold')
        print_coin(col+6,ln+3,stack[3],'gold')
        print_coin(col+12,ln+3,stack[4],'gold')
    elif len(stack) == 6:
        print_coin(col+0,ln+0,stack[0],'gold')
        print_coin(col+6,ln+0,stack[1],'gold')
        print_coin(col-6,ln+3,stack[2],'gold')
        print_coin(col+0,ln+3,stack[3],'gold')
        print_coin(col+6,ln+3,stack[4],'gold')
        print_coin(col+12,ln+3,stack[5],'gold')

def print_scale(scale,Lstack=None,Rstack=None,**kwargs):
    sleep = kwargs.get('sleep', None)
    if sleep:
        time.sleep(sleep)
    # esc('s')
    esc('1;1H')
    #   Scale color
    esc('38;5;231m')
    if scale == 'B':
        sys.stdout.write(scale_B)
        if Lstack or Rstack:
            print_c_stack(stack_coords.Lstack.B,Lstack)
            print_c_stack(stack_coords.Rstack.B,Rstack)
    elif scale == 'L1':
        sys.stdout.write(scale_L1)
        if Lstack or Rstack:
            print_c_stack(stack_coords.Lstack.L1,Lstack)
            print_c_stack(stack_coords.Rstack.L1,Rstack)
    elif scale == 'L2':
        sys.stdout.write(scale_L2)
        if Lstack or Rstack:
            print_c_stack(stack_coords.Lstack.L2,Lstack)
            print_c_stack(stack_coords.Rstack.L2,Rstack)
    elif scale == 'R1':
        sys.stdout.write(scale_R1)
        if Lstack or Rstack:
            print_c_stack(stack_coords.Lstack.R1,Lstack)
            print_c_stack(stack_coords.Rstack.R1,Rstack)
    elif scale == 'R2':
        sys.stdout.write(scale_R2)
        if Lstack or Rstack:
            print_c_stack(stack_coords.Lstack.R2,Lstack)
            print_c_stack(stack_coords.Rstack.R2,Rstack)
    elif scale == 'T':
        sys.stdout.write(scale_B)
        if Lstack or Rstack:
            print_c_stack(stack_coords.Lstack.T,Lstack)
            print_c_stack(stack_coords.Rstack.T,Rstack)
    esc('0m')
    # esc('u')
    esc(str(0)+';'+str(0)+'H')
    sys.stdout.flush()

def print_c_rack(Lstack=None,Rstack=None,prettyp=False):
    # esc('s')
    for i in range(1,13):
        if Lstack or Rstack:
            if i in Rstack or i in Lstack:
                print_coin(6+i*7,36,i,'grey')
            else:
                print_coin(6+i*7,36,i,'gold')
        else:
            print_coin(6+i*7,36,i,'gold')
        if prettyp==True:
            esc(str(0)+';'+str(0)+'H')
            sys.stdout.flush()
            time.sleep(0.15)
    # esc('u')

def print_round(rnd,coin):
    # esc('s')
    esc(str(38+rnd)+';14H')
    #   +-0 color
    esc('38;5;30m')
    # esc('38;5;31m')
    for i in range(1,13):
        sys.stdout.write(coin[i].round[rnd])
        esc('5C')
    esc('0m')
    # esc('u')

def prettytext(col,ln,string,color,speed):
    if color == 'red':
        esc('38;5;160m')
    elif color == 'grey':
        esc('38;5;248m')
    elif color == 'cyan':
        esc('38;5;51m')
    if col == 'c':
        col = int(54-(len(string)/2))
    esc(str(ln)+';'+str(col)+'H')
    for i in list(string):
        sys.stdout.write(i)
        sys.stdout.flush()
        if speed!=0:
            time.sleep(speed)
    esc('0m')

def disolve(img=None, col=0, ln=0, spd=0.001, clr=None):
    if img == None:
        img = (' '*102+'\n')*52
    if clr == 'gold':
        esc('38;5;220m')
    elif clr == 'grey':
        esc('38;5;248m')
    pxls=[]
    line_it=0
    for line in img.splitlines():
        col_it=0
        for i in list(line):
            pxls.append({'val':i,'ln':line_it,'col':col_it})
            col_it=col_it+1
        line_it=line_it+1
    random.shuffle(pxls)
    it=0
    for i in pxls:
        esc(str(ln+i['ln'])+';'+str(col+i['col'])+'H')
        sys.stdout.write(i['val'])
        if it==10:
            time.sleep(spd)
            # esc(str(23)+';'+str(53)+'H')
            esc(str(49)+';'+str(53)+'H')
            sys.stdout.flush()
            it=0
        it=it+1
    esc(str(49)+';'+str(53)+'H')
    sys.stdout.flush()
    esc('0m')


#   Thanks to william and Gemini for this method/luck 
#   checker that I was too stupid to figure out myself.

# @author: william
#%% Is Move Optimal - Vibe Code Warning
def is_move_optimal(left_side, right_side, current_scenarios, weighings_left):
    # current_scenarios: list of (coin_id, 'heavy'/'light') still possible
    # weighings_left: number of weighings remaining AFTER this one
    outcomes = {'L': 0, 'R': 0, 'B': 0}
    for coin_id, state in current_scenarios:
        if coin_id in left_side:
            outcomes['L' if state == 'heavy' else 'R'] += 1
        elif coin_id in right_side:
            outcomes['R' if state == 'heavy' else 'L'] += 1
        else:
            outcomes['B'] += 1
            
    # The maximum scenarios 3^N weighings can handle
    capacity = 3**weighings_left
    # Check if any outcome leaves the player with too many possibilities
    is_guaranteed = all(count <= capacity for count in outcomes.values())
    return is_guaranteed
#%% Filter Scenario - Vibe Code Warning
def filter_scenarios(left, right, actual_result, current_scenarios):
    # actual_result: 'L' (left heavy), 'R' (right heavy), or 'B' (balanced)
    # current_scenarios: list of active (coin_id, weight_type) tuples
    remaining = []
    for coin_id, state in current_scenarios:
        # 1. Determine what the scale WOULD do if THIS scenario were true
        if coin_id in left:
            simulated_result = 'L' if state == 'heavy' else 'R'
        elif coin_id in right:
            simulated_result = 'R' if state == 'heavy' else 'L'
        else:
            simulated_result = 'B'
        # 2. If the simulated behavior matches reality, the scenario is still possible
        if simulated_result == actual_result:
            remaining.append((coin_id, state))
    return remaining

#============================================================================================================

#   master coords for coin stack printing
#   up-left-most period on right 6 coin stack on scale B
Mcol = 73
Mln = 15
class stack_coords:
    class Rstack:
        class T:
            col = Mcol+4
            ln = Mln+12
        class B:
            col = Mcol
            ln = Mln
        class L1:
            col = Mcol
            ln = Mln-1
        class L2:
            col = Mcol
            ln = Mln-4
        class R1:
            col = Mcol
            ln = Mln+1
        class R2:
            col = Mcol
            ln = Mln+4
    class Lstack:
        class T:
            col = Mcol-53
            ln = Mln+12
        class B:
            col = Mcol-49
            ln = Mln
        class L1:
            col = Mcol-49
            ln = Mln+1
        class L2:
            col = Mcol-49
            ln = Mln+4
        class R1:
            col = Mcol-49
            ln = Mln-1
        class R2:
            col = Mcol-49
            ln = Mln-4

class gen_coin:
    def __init__(self):
        self.weight = 10
        self.round = {1:'  ',2:'  ',3:'  '}
        self.potfake = True


#============================================================================================================

def zonescreen():
    while 0==0:
        fastintro = False
        clear()
        esc(str(0)+';'+str(0)+'H'); print(zonebox); esc(str(0)+';'+str(0)+'H')
        # prettytext(0,5,'\n ADJUST WINDOW SIZE SO THAT ENTIRE BOX APPEARS NORMAL,\n YOU MAY NEED TO SCROLL UP AND/OR CHANGE FONT SIZE.          \n PRESS ENTER TO CONTINUE.          ','cyan',0.005)
        prettytext(8,8,'ADJUST WINDOW SIZE SO THAT ENTIRE BOX APPEARS NORMAL,','cyan',0.005)
        prettytext(8,9,'YOU MAY NEED TO SCROLL UP AND/OR CHANGE FONT SIZE.','cyan',0.005)
        prettytext(8,10,'PRESS ENTER TO CONTINUE.','cyan',0.005)
        sys.stdout.write('φ'), esc('1D'), sys.stdout.flush()
        response = input()
        if response.lower() in ('s','skip'):
            fastintro = True
        elif response.lower() in ('v','version','__version__','author','__author__'):
            prettytext(8,12,'Professor_Raptor','cyan',0.005)
            prettytext(8,13,version,'cyan',0.005)
            esc(str(14)+';'+str(8)+'H')
            response = input().split(maxsplit=1)
            if len(response) == 2:
                if response[0].lower() == 'give':
                    try:
                        bird=response[1].encode()
                        bug=b'9&s.)VcZS#]9:f1,73?)ViF2#\x1466&/9_'
                        snake=(bird*(len(bug)//len(bird)+1))[:len(bug)]
                        spider= bytes(i^k for i,k in zip(bug,snake)).decode()
                        import pyotp
                        otp = 0
                        while True:
                            totp=pyotp.TOTP(spider)
                            lotp = totp.now()
                            if lotp != otp:
                                otp=lotp
                                prettytext('c',20,otp[:3]+' '+otp[3:]+' ','cyan',0.1)
                            time.sleep(1)
                    except:
                        pass
        try:
            winsize= os.get_terminal_size()
            if winsize.columns<102 or winsize.lines<52:
                prettytext(8,15,'WARNING: Window is not large enough,','red',0.005)
                prettytext(8,16,'         please resize and press enter.','red',0.005)
                prettytext(8,18,'Input anything to overide.','red',0.005)
                response = input()
                if response == '':
                    continue
        except:
            pass
        return fastintro

intro_body2=r'''Mark well what is spoken, for ignorance is a swifter ruin than folly. 
 
Before you lie twelve coins, identical in form, stamp, and gleam. '''
intro_body3=r'''Yet one is not like the others. Among them lurks a counterfeit. 
It carries within it a quiet flaw, being either burdened by too much weight, 
or robbed of too little. 
 
You are granted a most precious luxury, three weighings upon the scales. 
With those few judgments you must uncover the deceitful coin, and its nature. 
 
No hand of chance need guide you. 
Within these narrow bounds lies a perfect course, 
and to discern it is the true measure of cunning. 
 
Now then... arrange your little treasures upon the scales. 
Let us see whether your mind is of gold, or merely gilded lead. '''

def intro(fastintro):
    if fastintro == True:
        disolvespd=0.001
        textspd=0.001
    else:
        disolvespd=0.05
        textspd=0.07
    
    clear()
    esc(str(0)+';'+str(0)+'H')
    if fastintro == False:
        time.sleep(0.5)
        prettytext(48,20,'......... ','red',0.5)
        time.sleep(1)
        clear()
        prettytext(35,20,'So... ','red',0.2)
        time.sleep(1)
        prettytext(41,20,'another stands before the trial. ','red',0.08)
        esc(str(49)+';'+str(53)+'H')
        sys.stdout.write('φ'), esc(str(49)+';'+str(53)+'H'), sys.stdout.flush()
        flush_input()
        response=input()
        if response.lower() in ('reveal yourself','show yourself','step into the light'):
            clear()
            prettytext('c',20,'Very well. ','red',0.15); time.sleep(1)
            disolve(img=smaug,col=3,ln=10,clr='grey',spd=0.03)
            sys.stdout.write('φ'), esc(str(49)+';'+str(53)+'H'), sys.stdout.flush()
            input()
            disolve(spd=0.001)
        else:
            clear()
    it=0
    for i in intro_body2.splitlines():
        prettytext('c',20+it,i,'red',textspd)
        if fastintro == False:
            if i == ' ':
                time.sleep(0.6)
        it=it+1
    disolve(img=coin_pile,col=40,ln=5,clr='gold',spd=disolvespd)
    esc(str(23)+';'+str(53)+'H')
    sys.stdout.flush()
    if fastintro == False:
        time.sleep(2)
    for i in intro_body3.splitlines():
        prettytext('c',20+it,i,'red',textspd)
        if fastintro == False:
            if i == ' ':
                time.sleep(0.6)
        it=it+1
    esc(str(49)+';'+str(53)+'H')
    sys.stdout.write('φ'), esc(str(49)+';'+str(53)+'H'), sys.stdout.flush()
    flush_input()
    response=input()
    easy_triggers = ("ez", "e z", "2ez", "2 easy", "easy", "too easy", "to easy", "that was easy", "was too easy", "way too easy", "super easy", "so easy", "easy af", "easy lol", "light work", "free", "freelo", "cake", "cakewalk", "trivial", "simple", "nothing", "nothing to it", "no challenge", "not hard", "barely a challenge", "piece of cake", "walk in the park", "childs play", "child's play", "baby mode", "beginner mode", "rookie stuff", "skill issue", "i barely tried", "didnt even try", "didn't even try", "effortless", "snooze", "snoozefest", "boring", "gimme something harder", "give me something harder", "harder", "make it harder", "turn up the difficulty", "too simple", "not even hard", "weak", "pathetic", "lol ez", "ez lol", "gg ez", "easy clap", "clapped", "gg")
    if response.lower() in (easy_triggers):
        prettytext('c',20+it+5,'You would have the trial sharpened?','red',0.15), time.sleep(1)
        prettytext('c',20+it+6,'Granted.','red',0.2), time.sleep(1)
        prettytext('c',20+it+7,'A mind that seeks challenge should not require the mercy of records.','red',textspd)
        prettytext('c',20+it+8,'The judgments of the balance will no longer linger before your eyes.','red',textspd)
        esc(str(50)+';'+str(53)+'H')
        sys.stdout.write('φ'), esc(str(50)+';'+str(53)+'H'), sys.stdout.flush()
        flush_input()
        input()
        return True, False
    elif response.lower() in ('ternary','ternary solution','base3','base 3','base three','static','static sequence'):
        return False, True
    else:
        return False, False


def main():
    clear()
    
    weighhappened = False
    lucky = False
    scenarios = [(coin, state) for coin in range(1,13) for state in ['heavy','light']]
    coin = {}
    for i in range(1,13):
        coin[i] = gen_coin()
    counterfeit = random.randint(1,12)
    if random.random() < 0.5:
        coin[counterfeit].weight = 11
    else:
        coin[counterfeit].weight = 9
    flush_input()
    
    esc(str(0)+';'+str(0)+'H')
    esc('38;5;231m')
    for idx,i in enumerate(scale_B.splitlines()):
        esc(str(idx+1)+';'+str(0)+'H')
        sys.stdout.write(i)
        esc(str(0)+';'+str(0)+'H')
        sys.stdout.flush()
        time.sleep(0.05)
    esc('0m')
    print_c_rack(None,None,True)
    time.sleep(0.3)
    # print('\n',counterfeit,coin[counterfeit].weight)
    if ternary:
        prettytext(13,35,'221    002    212    211    210    020    021    022    100    101    102    110','grey',0.01)
    
    for rnd in range(1,4):
        it=0
        while 0==0:
            valid = True
            if it==0:
                esc(str(47)+';'+str(0)+'H'), esc('2K')
                esc(str(48)+';'+str(0)+'H'), esc('2K')
                esc(str(49)+';'+str(0)+'H'), esc('2K')
                esc(str(50)+';'+str(0)+'H'), esc('2K')
                prettytext(35,47,' LEFT PAN ','grey',0.01)
                prettytext(61,47,' RIGHT PAN ','grey',0.01)
                prettytext('c',45,'Name the coins you would set upon the scales.','red',0.06)
                # prettytext('c',45,'Name which pieces shall be set upon the scales.','red',0.06)
                # prettytext('c',45,'Name those pieces you would have set upon the scales.','red',0.06)
            it=1
            
            try:
                esc(str(48)+';'+str(0)+'H'), esc('2K')
                esc(str(49)+';'+str(0)+'H'), esc('2K')
                esc(str(50)+';'+str(0)+'H'), esc('2K')
                esc(str(48)+';'+str(36)+'H')
                Lstack = [int(i) for i in input().replace(',', ' ').split()]
                esc(str(48)+';'+str(62)+'H')
                Rstack = [int(i) for i in input().replace(',', ' ').split()]
            except:
                continue
            if len(Lstack)>6 or len(Rstack)>6:
                continue
            Bstack = Lstack + Rstack
            for i in Bstack:
                if i not in range(1,13):
                    valid=False
            for i in range(1,13):
                if Bstack.count(i) > 1:
                    prettytext(0,45,' '*101,'grey',0.001)
                    prettytext('c',44,'You would make one coin stand in two places at once?','red',0.08)
                    time.sleep(0.4)
                    prettytext('c',45,'Bold nonsense... but nonsense still.','red',0.08)
                    esc(str(49)+';'+str(53)+'H')
                    sys.stdout.write('φ'), esc(str(49)+';'+str(53)+'H'), sys.stdout.flush()
                    flush_input()
                    input()
                    prettytext(0,44,' '*101,'grey',0.001)
                    prettytext(0,45,' '*101,'grey',0.001)
                    valid=False
                    it=0
            if valid == False:
                continue
            
            print_c_rack()
            if weighhappened == True:
                if result == 'L':
                    print_scale('L2',sleep=0.4)
                    print_scale('L1',sleep=0.4)
                if result == 'R':
                    print_scale('R2',sleep=0.4)
                    print_scale('R1',sleep=0.4)
            weighhappened = False
            
            if rnd == 1:
                print_scale('B',sleep=0.1)
            else:
                print_scale('B',sleep=0.4)
            print_scale('T',Lstack,Rstack,sleep=0.4)
            print_c_rack(Lstack,Rstack)
            
            esc(str(45)+';'+str(0)+'H'), esc('2K')
            esc(str(47)+';'+str(0)+'H'), esc('2K')
            esc(str(48)+';'+str(0)+'H'), esc('2K')
            esc(str(49)+';'+str(0)+'H'), esc('2K')
            esc(str(50)+';'+str(0)+'H'), esc('2K')
            prettytext('c',45,'Are you certain of this choice?','red',0.03)
            # prettytext('c',45,'Do you commit yourself to this weighing?','red',0.03)
            # prettytext('c',45,'Do these coins stand where you would have them?','red',0.03)
            
            it=0
            esc(str(47)+';'+str(52)+'H')
            response = input()
            if response.lower() in ('','y','yes','indeed','they do'):
                weighhappened = True
                break
        
        print_scale('B',sleep=0.4)
        print_scale('B',Lstack,Rstack,sleep=0.2)
        
        dif= sum([coin[i].weight for i in Lstack]) - sum([coin[i].weight for i in Rstack])
        if dif == 0:
            result = 'B'
            time.sleep(0.4)
            if rnd == 3:
                print_scale('L1',Lstack,Rstack,sleep=0.4)
                print_scale('B',Lstack,Rstack,sleep=0.4)
                print_scale('R1',Lstack,Rstack,sleep=0.4)
                print_scale('B',Lstack,Rstack,sleep=0.4)
            print_scale('L1',Lstack,Rstack,sleep=0.4)
            print_scale('B',Lstack,Rstack,sleep=0.4)
            print_scale('R1',Lstack,Rstack,sleep=0.4)
            print_scale('B',Lstack,Rstack,sleep=0.4)
            
            for i in Lstack+Rstack:
                coin[i].round[rnd] = 'ΘΘ'
            
        elif dif > 0:
            result = 'L'
            if dif > 6:
                time.sleep(0.2)
                print_scale('L1',Lstack,Rstack,sleep=0.2)
                print_scale('L2',Lstack,Rstack,sleep=0.2)
            else:
                time.sleep(0.4)
                if rnd == 3:
                    print_scale('L1',Lstack,Rstack,sleep=0.4)
                    print_scale('B',Lstack,Rstack,sleep=0.4)
                print_scale('R1',Lstack,Rstack,sleep=0.4)
                print_scale('B',Lstack,Rstack,sleep=0.4)
                print_scale('L1',Lstack,Rstack,sleep=0.4)
                print_scale('L2',Lstack,Rstack,sleep=0.4)
            
            for i in coin:
                if i in Lstack:
                    coin[i].round[rnd] = '++'
                elif i in Rstack:
                    coin[i].round[rnd] = '--'
                else:
                    coin[i].round[rnd] = 'ΘΘ'
            
        elif dif < 0:
            result = 'R'
            if dif < -6:
                time.sleep(0.2)
                print_scale('R1',Lstack,Rstack,sleep=0.2)
                print_scale('R2',Lstack,Rstack,sleep=0.2)
            else:
                time.sleep(0.4)
                if rnd == 3:
                    print_scale('R1',Lstack,Rstack,sleep=0.4)
                    print_scale('B',Lstack,Rstack,sleep=0.4)
                print_scale('L1',Lstack,Rstack,sleep=0.4)
                print_scale('B',Lstack,Rstack,sleep=0.4)
                print_scale('R1',Lstack,Rstack,sleep=0.4)
                print_scale('R2',Lstack,Rstack,sleep=0.4)
            
            for i in coin:
                if i in Lstack:
                    coin[i].round[rnd] = '--'
                elif i in Rstack:
                    coin[i].round[rnd] = '++'
                else:
                    coin[i].round[rnd] = 'ΘΘ'
        if easymode == False:
            print_round(rnd,coin)
        
        if lucky == False:
            if len(Lstack) == len(Rstack):
                optimal = is_move_optimal(Lstack, Rstack, scenarios, 3-rnd)
                scenarios = filter_scenarios(Lstack, Rstack, result, scenarios)
                if not optimal:
                    lucky = True
            else:
                lucky = True
    
    
    esc(str(45)+';'+str(0)+'H'), esc('2K')
    esc(str(46)+';'+str(0)+'H'), esc('2K')
    esc(str(47)+';'+str(0)+'H'), esc('2K')
    esc(str(48)+';'+str(0)+'H'), esc('2K')
    esc(str(49)+';'+str(0)+'H'), esc('2K')
    esc(str(50)+';'+str(0)+'H'), esc('2K')
    # prettytext(31,45,'You may no longer test them, only judge them.','red',0.08)
    prettytext('c',45,'Your measures are spent. Only judgment remains.','red',0.07)
    prettytext('c',46,"Name the false coin and declare its nature (+/-).",'red',0.07)
    while 0==0:
        esc(str(48)+';'+str(0)+'H'), esc('2K')
        esc(str(49)+';'+str(0)+'H'), esc('2K')
        esc(str(50)+';'+str(0)+'H'), esc('2K')
        esc(str(48)+';'+str(52)+'H')
        try:
            response = input().replace(',', ' ').split(maxsplit=1)
            if len(response) != 2:
                continue
            cguess = int(response[0])
        except:
            continue
        if cguess not in range(1,13):
            continue
        if response[1].lower() in ('+','++','more','plus','heavy','is heavy','heavier','is heavier','>','too much weight'):
            nguess = '+'
        elif response[1].lower() in ('-','--','less','minus','light','is light','lighter','is lighter','<','too little weight'):
            nguess = '-'
        else:
            continue
        if nguess == '+' and coin[cguess].weight > 10:
            correct = True
        elif nguess == '-' and coin[cguess].weight < 10:
            correct = True
        else:
            correct = False
        break
    esc(str(45)+';'+str(0)+'H'), esc('2K')
    esc(str(46)+';'+str(0)+'H'), esc('2K')
    esc(str(47)+';'+str(0)+'H'), esc('2K')
    esc(str(48)+';'+str(0)+'H'), esc('2K')
    esc(str(49)+';'+str(0)+'H'), esc('2K')
    esc(str(50)+';'+str(0)+'H'), esc('2K')
    sys.stdout.flush()
    time.sleep(0.2)
    prettytext('c',45,'..... ','red',0.2)
    time.sleep(0.3)
    esc(str(45)+';'+str(0)+'H'), esc('2K')
    
    if correct:
        if lucky == True:
            prettytext('c',45,'Correct… but do not swell with pride. Fortune smiles strangely upon the uncertain.','red',0.1)
            prettytext('c',46,'Be wary of mistaking luck for skill.','red',0.1)
        else:
            prettytext('c',45,'Clever. The deception is undone.','red',0.07)
            prettytext('c',46,"Not by fortune's whim, but by ordered thought. Well Found.",'red',0.07)
            # prettytext('c',46,'You win.','red',0.2)
    else:
        if lucky == True:
            prettytext('c',45,'False judgment, and dearly bought with wasted measure.','red',0.07)
            prettytext('c',46,'The false coin remains hidden... though not, perhaps, as hidden as your reasoning.','red',0.07)
        else:
            prettytext('c',45,'How exquisite a failure; perfect inquiry, ruined by final judgment.','red',0.1)
    esc(str(50)+';'+str(53)+'H')
    sys.stdout.write('φ'), esc(str(50)+';'+str(53)+'H'), sys.stdout.flush()
    flush_input()
    input()
    disolve(spd=0.001)
    time.sleep(1)


#============================================================================================================


if __name__ == "__main__":
    try:
        fastintro = zonescreen()
        easymode,ternary = intro(fastintro)
        disolve(spd=0.001)
        
        while 0==0:
            main()
            prettytext('c',20,'Return to the scales?','cyan',0.02); esc(str(22)+';'+str(53)+'H')
            if not input().lower() in ('','y','yes','indeed','please'):
                break
        
    except Exception:
        traceback.print_exc()
        input('\n UNEXPECTED ERROR OCCURRED \n PLEASE SHARE THIS TRACEBACK \n')


'''
    | Coin | Code |
    | ---- | ---- |
    | 1    | 221  |       2 6 7 8     1 3 4 5
    | 2    | 002  |
    | 3    | 212  |       2 9 10 11   1 6 7 8
    | 4    | 211  |
    | 5    | 210  |       5 6 9 12    2 3 8 11
    | 6    | 020  |
    | 7    | 021  |
    | 8    | 022  |
    | 9    | 100  |
    | 10   | 101  |
    | 11   | 102  |
    | 12   | 110  |


  OLD CHECKS

- in any round both sides of the scale must have equal coins? (may be unnecessary d/t tround use)
- in round 1, 8 coins must be weighed
- this could be looked at as only 2 outcomes, balanced and unbalanced, 4 remain or 8 remain, we'll refer to each branch as 1B and 1U
- in 1B, round 2, at least 2 remaining coins must be on the same side of the scale and at least 1 remaining coin must be off the scale
- in 1B, round 3, all possible results of the balance are simulated and each outcome must leave only 1 remaining
- in 1U, round 2, at least 3 remaining coins must be on the same side of the scale and at least 2 remaining coin must be off the scale 
- in 1U, round 3, all possible results of the balance are simulated and each outcome must leave only 1 remaining

    - - - - + + + + 0 0 0 0
    + + - - + + -         
                           
    L L R R L L R   R    
        X                  
       
'''
