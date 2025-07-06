import time # Time Library

import board # Libraries for use with MCP23017
import busio
import digitalio

from adafruit_mcp230xx.mcp23017 import MCP23017 # Adafruit circuit python MCP23017 control library

import pygame # Audio Control Library
import gpiod # Generic RP GPIO Control Library

Chip=gpiod.Chip('gpiochip4') #setup GPIO pin numbering configuration

time.sleep(3)

# Speaker Control pins
ExternalSpeakerPin=17
InternalSpeakerPin=27
RadioSpeakerPin=22
AtticSpeakerPin=23

ExternalSpeakerSelection=Chip.get_line(ExternalSpeakerPin)
InternalSpeakerSelection=Chip.get_line(InternalSpeakerPin)
RadioSpeakerSelection=Chip.get_line(RadioSpeakerPin)
AtticSpeakerSelection=Chip.get_line(AtticSpeakerPin)

ExternalSpeakerSelection.request(consumer="LED",type=gpiod.LINE_REQ_DIR_OUT)
InternalSpeakerSelection.request(consumer="LED",type=gpiod.LINE_REQ_DIR_OUT)
RadioSpeakerSelection.request(consumer="LED",type=gpiod.LINE_REQ_DIR_OUT)
AtticSpeakerSelection.request(consumer="LED",type=gpiod.LINE_REQ_DIR_OUT)

i2c = busio.I2C(board.SCL, board.SDA) #Configure I2C bus pins (default)
PosterMcp = MCP23017(i2c, address=0x25)  # Poster GPIO Expansion Jump pin A1
OtherMcp=MCP23017(i2c,address=0x27) # Other functions GPIO Expansion


#Assign the 9 poster light pins
Clown1Light = PosterMcp.get_pin(7)
Clown2Light = PosterMcp.get_pin(15)
Clown3Light=PosterMcp.get_pin(14)
Clown4Light=PosterMcp.get_pin(13)
Clown5Light=PosterMcp.get_pin(12)
Clown6Light=PosterMcp.get_pin(11)
Clown7Light=PosterMcp.get_pin(10)
Clown8Light=PosterMcp.get_pin(9)
ClownKillerLight=PosterMcp.get_pin(8)

#Assign the 9 poster button pins
Clown1Button=PosterMcp.get_pin(0)
Clown2Button=PosterMcp.get_pin(1)
Clown3Button=PosterMcp.get_pin(2)
Clown4Button=PosterMcp.get_pin(3)
Clown5Button=PosterMcp.get_pin(4)
Clown6Button=PosterMcp.get_pin(5)
Clown7Button=PosterMcp.get_pin(6)
Clown8Button=OtherMcp.get_pin(0)
ClownKillerButton=OtherMcp.get_pin(1)

#Assign Auxilary output pins
GreenButtonLight=OtherMcp.get_pin(2) # Green Button Light On Off
RedButtonLight=OtherMcp.get_pin(3)  # Red Button Light On Off
RadioLight=OtherMcp.get_pin(4) # Radio Light On Off
DoorLock=OtherMcp.get_pin(5)  # Door Lock On Off
InteriorLighting=OtherMcp.get_pin(6) # Interior Lighting On Off
AtticLighting=OtherMcp.get_pin(7)  # Attic Lighting On Off
GameDone=OtherMcp.get_pin(12) # Notify POS that the paid for game is complete

GameIndicatorLight=OtherMcp.get_pin(13) 



#GameIndicatorLight.request(consumer="LED",type=gpiod.LINE_REQ_DIR_OUT)

# Motor Control Pins
MotorControl1Pin=5
MotorControl2Pin=6
LimitSwitchPin=13

MotorControl1=Chip.get_line(MotorControl1Pin)
MotorControl2=Chip.get_line(MotorControl2Pin)
LimitSwitch=Chip.get_line(LimitSwitchPin)

MotorControl1.request(consumer="LED",type=gpiod.LINE_REQ_DIR_OUT)
MotorControl2.request(consumer="LED",type=gpiod.LINE_REQ_DIR_OUT)
LimitSwitch.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN,flags=gpiod.LINE_REQ_FLAG_BIAS_PULL_UP)

#Assign Auxilary input pins
GreenButton=OtherMcp.get_pin(8) # Green Button Signal
RedButton=OtherMcp.get_pin(9) # Red Button Signal
DoorStatus=OtherMcp.get_pin(10)  # Door Open / Close
PaymentReceived=OtherMcp.get_pin(11) #POS Payment Received Signal
HintLight=OtherMcp.get_pin(14)
HintButton=OtherMcp.get_pin(15)

#Configure Output pins
Clown1Light.switch_to_output(0)
Clown2Light.switch_to_output(0)
Clown3Light.switch_to_output(0)
Clown4Light.switch_to_output(0)
Clown5Light.switch_to_output(0)
Clown6Light.switch_to_output(0)
Clown7Light.switch_to_output(0)
Clown8Light.switch_to_output(0)
ClownKillerLight.switch_to_output(0)

GreenButtonLight.switch_to_output(0)
RedButtonLight.switch_to_output(0)
RadioLight.switch_to_output(0)
DoorLock.switch_to_output(0)
InteriorLighting.switch_to_output(0)
AtticLighting.switch_to_output(0)

GameIndicatorLight.switch_to_output(0)

GameDone.switch_to_output(0)
HintLight.switch_to_output(0)

#Configure Input pins and pullups
Clown1Button.direction=digitalio.Direction.INPUT #1=not pressed 0=pressed
Clown2Button.direction=digitalio.Direction.INPUT #1=not pressed 0=pressed
Clown3Button.direction=digitalio.Direction.INPUT #1=not pressed 0=pressed
Clown4Button.direction=digitalio.Direction.INPUT #1=not pressed 0=pressed
Clown5Button.direction=digitalio.Direction.INPUT #1=not pressed 0=pressed
Clown6Button.direction=digitalio.Direction.INPUT #1=not pressed 0=pressed
Clown7Button.direction=digitalio.Direction.INPUT #1=not pressed 0=pressed
Clown8Button.direction=digitalio.Direction.INPUT #1=not pressed 0=pressed
ClownKillerButton.direction=digitalio.Direction.INPUT #1=not pressed 0=pressed

Clown1Button.pull=digitalio.Pull.UP
Clown2Button.pull=digitalio.Pull.UP
Clown3Button.pull=digitalio.Pull.UP
Clown4Button.pull=digitalio.Pull.UP
Clown5Button.pull=digitalio.Pull.UP
Clown6Button.pull=digitalio.Pull.UP
Clown7Button.pull=digitalio.Pull.UP
Clown8Button.pull=digitalio.Pull.UP
ClownKillerButton.pull=digitalio.Pull.UP

GreenButton.direction=digitalio.Direction.INPUT #1=not pressed 0=pressed
RedButton.direction=digitalio.Direction.INPUT #1=not pressed 0=pressed
DoorStatus.direction=digitalio.Direction.INPUT #1=not Closed 0=Closed
HintButton.direction=digitalio.Direction.INPUT

PaymentReceived.direction=digitalio.Direction.INPUT

GreenButton.pull=digitalio.Pull.UP
RedButton.pull=digitalio.Pull.UP
DoorStatus.pull=digitalio.Pull.UP
PaymentReceived.pull=digitalio.Pull.UP
HintButton.pull=digitalio.Pull.UP

#Speaker file setup
pygame.mixer.init()

IdleAudio=pygame.mixer.Sound("Idle.mp3")
DoorCloseRequestAudio=pygame.mixer.Sound("DoorCloseRequest.mp3")
RulesAudio=pygame.mixer.Sound("Rules.mp3")
CountDownAudio=pygame.mixer.Sound("CountDown.mp3")
TimeWarningAudio=pygame.mixer.Sound("TimeWarning.mp3")
WinAudio=pygame.mixer.Sound("Win.mp3")
LoseAudio=pygame.mixer.Sound("Lose.mp3")
LeaveAudio=pygame.mixer.Sound("Leave.mp3")
LastSelectionAudio=pygame.mixer.Sound("LastClown.mp3")

Hint1Audio=pygame.mixer.Sound("Hint1.mp3")
Hint2Audio=pygame.mixer.Sound("Hint2.mp3")
Hint3Audio=pygame.mixer.Sound("Hint3.mp3")

IdleAudioLength=IdleAudio.get_length()
DoorCloseRequestLength=DoorCloseRequestAudio.get_length()
RulesLength=RulesAudio.get_length()
CountDownLength=CountDownAudio.get_length()
TimeWarningLength=TimeWarningAudio.get_length()
WinLength=WinAudio.get_length()
LoseLength=LoseAudio.get_length()
LastSelectionLength=LastSelectionAudio.get_length()
LeaveAudioLength=LeaveAudio.get_length()

Hint1Length=Hint1Audio.get_length()
Hint2Length=Hint2Audio.get_length()
Hint3Length=Hint3Audio.get_length()

IdleAudio.set_volume(0.2)
DoorCloseRequestAudio.set_volume(0.1)
RulesAudio.set_volume(1)
CountDownAudio.set_volume(0.5)
TimeWarningAudio.set_volume(1)
WinAudio.set_volume(1)
LoseAudio.set_volume(1)
LastSelectionAudio.set_volume(1)

Channel1=pygame.mixer.Channel(1)
Channel2=pygame.mixer.Channel(2)


#Variables
Clown1Status=False #0 Not Selected 1 Selected
Clown2Status=False #0 Not Selected 1 Selected
Clown3Status=False #0 Not Selected 1 Selected
Clown4Status=False #0 Not Selected 1 Selected
Clown5Status=False #0 Not Selected 1 Selected
Clown6Status=False #0 Not Selected 1 Selected
Clown7Status=False #0 Not Selected 1 Selected
Clown8Status=False #0 Not Selected 1 Selected
ClownKillerStatus=False #0 Not Selected 1 Selected

Clown1ButtonStatus=True
Clown2ButtonStatus=True
Clown3ButtonStatus=True
Clown4ButtonStatus=True
Clown5ButtonStatus=True
Clown6ButtonStatus=True
Clown7ButtonStatus=True
Clown8ButtonStatus=True
ClownKillerButtonStatus=True

GameState=0 #Game state selector
            # 0 Idle
            # 1 Payment
            # 2 Enter
            # 3 Pregame
            # 4 Gameplay
            # 5 Win
            # 6 Lose
            # 7 Reset
            
UnlockStartTime=0
UnlockDuration=3 # Duration lock is opened independent of door state

GameStartTime=0
GameDuration=300 # Length of the game 5 min 300 seconds

MinuteTicker=1 #Counter for the game 1 minute warning

BlinkTime=0.625 # Time on / off when the lights blink
BlinkStartTime=0
BlinkCount=1

ClownSelectionQuantity=0 # Number of clowns illuminated
ClownSelection=0 # number of the selected clown

WinSelector=0 # has a win been selected progresser

GreenButtonStatus=True

AudioTime=0
AudioPlaying=0

AtticOpenTime=3 # Total time attic is open
AtticOpenStart=0

MotorOpenTime=4
LeavingBooth=0

LastSelectionBool=0
ExitBool=0
CountdownPlay=0
ExternalSpeakerSelection.set_value(0)
InternalSpeakerSelection.set_value(0)
RadioSpeakerSelection.set_value(0)
AtticSpeakerSelection.set_value(0)

EndGameState=0
LastSelectionPlayStart=0
i=0

ChannelTime=0
ChannelPlaying=0

HintCount=0
HintPlaying=0
Hint1Bool=0
Hint2Bool=0
Hint3Bool=0
HintAudioPlaying=0
HintAudioStart=0

while True:
    
    
    #print(GameState)
    
    if GameState==0: #IDLE Game State
        GameIndicatorLight.value=0
        HintLight.value=0
        
        
        if GreenButton.value==False:
        #if PaymentReceived.value==False: # Payment Signal Recieved
            GameState=1 # Go to Payment State
            
            playing=IdleAudio.stop() # Stop Idle audio
            ExternalSpeakerSelection.set_value(0)
            InternalSpeakerSelection.set_value(0)
            RadioSpeakerSelection.set_value(0)
            AtticSpeakerSelection.set_value(0)
        
        if (time.time()-AudioTime)>=(1+IdleAudioLength): # If state is idle and idle music runs out loop
            playing=IdleAudio.stop()
            playing=IdleAudio.play()
            
            AudioTime=time.time()
        
        Clown1Light.value=0 # Ensure lights are off and doors are locked
        Clown2Light.value=0
        Clown3Light.value=0
        Clown4Light.value=0
        Clown5Light.value=0
        Clown6Light.value=0
        Clown7Light.value=0
        Clown8Light.value=0
        ClownKillerLight.value=0
        i=0
        ChannelTime=0
        
        GreenButtonLight.value=1#0
        RedButtonLight.value=1
        AtticLighting.value=0
        InteriorLighting.value=0
        RadioLight.value=0
        
        DoorLock.value=1
        
        ExternalSpeakerSelection.set_value(1)
        InternalSpeakerSelection.set_value(0)
        RadioSpeakerSelection.set_value(0)
        AtticSpeakerSelection.set_value(0)
        
    elif GameState==1: #PAYMENT Game State
        GameIndicatorLight.value=1
        HintLight.value=0
        
        DoorLock.value=0 # unlock the door
        InteriorLighting.value=1 # Turn on inside lights

        if DoorStatus.value==True: # Once the door is open go to Enter Game state
           GameState=2
           UnlockStartTime=time.time()
        GreenButtonLight.value=1
        
    elif GameState==2: #ENTER Game State
        GameIndicatorLight.value=1
        HintLight.value=0
        
        RedButtonLight.value=1
        GreenButtonLight.value=0
        InteriorLighting.value=1
        
        if (time.time()-UnlockStartTime)>=UnlockDuration: # Lock the door after the duration
            DoorLock.value=1
            UnlockStartTime=0
            
        if DoorLock.value==True and DoorStatus.value==True: # if door is locked but not closed
            
            if AudioPlaying==0: # play the door close audio request
                
                AudioPlaying=1
                AudioTime=time.time()
                
                ExternalSpeakerSelection.set_value(0)
                InternalSpeakerSelection.set_value(1)
                RadioSpeakerSelection.set_value(0)
                AtticSpeakerSelection.set_value(0)
                
                playing=DoorCloseRequestAudio.play()
                
            elif AudioPlaying==1 and (time.time()-AudioTime)>= (1+DoorCloseRequestLength):
                playing=DoorCloseRequestAudio.play()
                AudioTime=time.time()
                
        elif DoorLock.value==True and DoorStatus.value==False: # door locked and closed go to pregame and stop any playing audio

            AudioPlaying=0
            ExternalSpeakerSelection.set_value(0)
            InternalSpeakerSelection.set_value(0)
            RadioSpeakerSelection.set_value(0)
            AtticSpeakerSelection.set_value(0)
            time.sleep(2)
            GameState=3
        
    elif GameState==3: #PREGAME Game State
        GameIndicatorLight.value=1
        RadioLight.value=1
        RedButtonLight.value=1
        DoorCloseRequestAudio.stop()
        HintLight.value=0
        if RedButton.value==False:
            # Stop all audio
            RulesAudio.stop()
            pygame.mixer.stop()
            Channel1.stop()
            Channel2.stop()
            # Reset speaker selections
            ExternalSpeakerSelection.set_value(0)
            InternalSpeakerSelection.set_value(0)
            RadioSpeakerSelection.set_value(0)
            AtticSpeakerSelection.set_value(0)
            
            # Reset audio variables
            AudioTime=0
            AudioPlaying=0
            # Turn off interior lighting
            InteriorLighting.value=0
            RadioLight.value=0
            GameState=7 # Go back to leave state
        if(DoorStatus.value==True and ExitBool==0):
            ExitBool=1
        if(ExitBool==1):
            RulesAudio.stop()
            pygame.mixer.stop()
            Channel1.stop()
            Channel2.stop()
            # Reset speakers
            ExternalSpeakerSelection.set_value(0)
            InternalSpeakerSelection.set_value(0)
            RadioSpeakerSelection.set_value(0)
            AtticSpeakerSelection.set_value(0)
            #Channel1.stop()
            #playing.stop()
            AudioTime=0
            AudioPlaying=0
            DoorLock.value=True
            time.sleep(0.5)
            GameState=6
            continue  # Skip rest of logic
        
        if AudioPlaying==0: # play the rules audio
            
            AudioPlaying=1
            AudioTime=time.time()
                
            ExternalSpeakerSelection.set_value(0)
            InternalSpeakerSelection.set_value(0)
            RadioSpeakerSelection.set_value(1)
            AtticSpeakerSelection.set_value(0)
            
            playing=RulesAudio.play()
            
        elif AudioPlaying==1 and (time.time()-AudioTime)>=46:
            #AudioPlaying=0
            
            ExternalSpeakerSelection.set_value(0)
            InternalSpeakerSelection.set_value(0)
            RadioSpeakerSelection.set_value(1)
            AtticSpeakerSelection.set_value(0)
            #AudioTime=0
            
            #playing.stop()
        

            if i < 6:
                    Clown1Light.value= not Clown1Light.value
                    Clown2Light.value= not Clown2Light.value
                    Clown3Light.value= not Clown3Light.value
                    Clown4Light.value= not Clown4Light.value
                    Clown5Light.value= not Clown5Light.value
                    Clown6Light.value= not Clown6Light.value
                    Clown7Light.value= not Clown7Light.value
                    Clown8Light.value= not Clown8Light.value
                    ClownKillerLight.value= not ClownKillerLight.value
                    time.sleep(BlinkTime)
                    i+=1
            
            elif i>=6:
                    Clown1Light.value=0
                    Clown2Light.value=0
                    Clown3Light.value=0
                    Clown4Light.value=0
                    Clown5Light.value=0
                    Clown6Light.value=0
                    Clown7Light.value=0
                    Clown8Light.value=0
                    ClownKillerLight.value=0
                
                    if (time.time()-AudioTime)>=(1+RulesLength):
                      GameState=4 # Progress to game play
                      AudioPlaying=0
                      GameStartTime=time.time()
                      AudioTime=0
                      playing.stop()
                
    elif GameState==4: #GAMEPLAY Game State
        GameIndicatorLight.value=1
        RedButtonLight.value=1
		
        #if(DoorStatus.value==True):
        #    CountDownAudio.stop()
        #    Channel1.stop()
        #    playing.stop()
        #    AudioTime=0
        #    AudioPlaying=0
        #    GameState=7
			
        if(DoorStatus.value==True and ExitBool==0):
            ExitBool=1
			
        if(ExitBool==1):
            #CountDownAudio.stop()
            #Channel1.stop()
            #playing.stop()
            AudioTime=0
            AudioPlaying=0
            DoorLock.value=True
            time.sleep(0.5)
            GameState=6
		
		
        if (time.time()-ChannelTime)>=LastSelectionLength or LastSelectionBool==0 :
            Channel1.unpause()
			
        RadioLight.value=1
		
        if LastSelectionBool==0:
            ExternalSpeakerSelection.set_value(0)
            InternalSpeakerSelection.set_value(1)
            RadioSpeakerSelection.set_value(0)
            AtticSpeakerSelection.set_value(0)
        elif LastSelectionBool==1 and time.time()-LastSelectionLength<=LastSelectionPlayStart:
            ExternalSpeakerSelection.set_value(0)
            InternalSpeakerSelection.set_value(0)
            RadioSpeakerSelection.set_value(1)
            AtticSpeakerSelection.set_value(0)
            RadioLight.value=1
        else :
            ExternalSpeakerSelection.set_value(0)
            InternalSpeakerSelection.set_value(1)
            RadioSpeakerSelection.set_value(0)
            AtticSpeakerSelection.set_value(0)
			
	if (CountdownPlay==0):
	    Channel1.play(CountDownAudio)
	    CountdownPlay=1
        if (time.time()-AudioTime)>=(1+CountDownLength): # Play and loop countdown music
            CountDownAudio.stop()
            Channel1.play(CountDownAudio)
            AudioTime=time.time()
		
        if((time.time()-GameStartTime) >= (MinuteTicker*60)) and MinuteTicker<6: # Every 60 seconds trigger the time warning
            MinuteTicker+=1
			
            if MinuteTicker==5:
                #Channel1.pause()
                #TimeWarningAudio.play()
                time.sleep(1)#TimeWarningLength)
                #Channel1.unpause()
			
            elif MinuteTicker==6: # After 5 minutes trigger lose gamestate
                ExternalSpeakerSelection.set_value(0)
                InternalSpeakerSelection.set_value(0)
                RadioSpeakerSelection.set_value(0)
                AtticSpeakerSelection.set_value(0)
                GameState=6
                MinuteTicker=1
				      
        if(HintCount<3):
            HintLight.value=1
        else:
            HintLight.value=0
		
        if(HintButton.value==False and HintPlaying==False and HintCount<3):
            HintPlaying=True
            HintCount=HintCount+1
            time.sleep(0.3)
			
        if(HintPlaying==True):
            Channel1.pause()
            
            # First hint press
            if(HintCount==1 and Hint1Bool==False):
                if(HintAudioPlaying==False):
                    Channel1.stop()
                    Channel2.play(Hint1Audio)
                    HintAudioStart=time.time()
                    HintAudioPlaying=True
                elif(HintAudioPlaying==True):
                    if((time.time()-HintAudioStart)>=Hint1Length):
                        #Channel1.play(CountDownAudio)  # Restart countdown
                        Channel1.unpause()
                        #AudioTime=time.time()  # Reset audio timer
                        #GameDuration=GameDuration+Hint1Length
                        Hint1Bool=True
                        HintPlaying=False
                        HintAudioPlaying=False

            # Second hint press  
            elif(HintCount==2 and Hint1Bool==True and Hint2Bool==False):
                if(HintAudioPlaying==False):
                    Channel1.stop()
                    Channel2.play(Hint2Audio)
                    HintAudioStart=time.time()
                    HintAudioPlaying=True
                elif(HintAudioPlaying==True):
                    if((time.time()-HintAudioStart)>=Hint2Length):
                        Channel1.unpause() 
                        #Channel1.play(CountDownAudio)  # Restart countdown
                        #AudioTime=time.time()  # Reset audio timer
                        #GameDuration=GameDuration+Hint2Length
                        Hint2Bool=True
                        HintPlaying=False
                        HintAudioPlaying=False

            # Third hint press
            elif(HintCount==3 and Hint1Bool==True and Hint2Bool==True and Hint3Bool==False):
                if(HintAudioPlaying==False):
                    Channel1.stop()
                    Channel2.play(Hint3Audio)
                    HintAudioStart=time.time()
                    HintAudioPlaying=True
                elif(HintAudioPlaying==True):
                    if((time.time()-HintAudioStart)>=Hint3Length):
                        Channel1.unpause() 
                        #Channel1.play(CountDownAudio)  # Restart countdown
                        #AudioTime=time.time()  # Reset audio timer
                        #GameDuration=GameDuration+Hint3Length
                        Hint3Bool=True
                        HintPlaying=False
                        HintAudioPlaying=False

				
        ClownSelectionQuantity=Clown1Status+Clown2Status+Clown3Status+Clown4Status+Clown5Status+Clown6Status+Clown7Status+Clown8Status+ClownKillerStatus # calculate number of selected clowns
		
        # handler for tracking clown 1 selection
        if Clown1ButtonStatus==True and Clown1Button.value==False: 
            Clown1Status = not Clown1Status
            Clown1ButtonStatus=Clown1Button.value
			
        elif Clown1ButtonStatus==False and Clown1Button.value==True:
            Clown1ButtonStatus= not Clown1ButtonStatus
		
        #handler for tracking clown 2 selection
        if Clown2ButtonStatus==True and Clown2Button.value==False:
            Clown2Status= not Clown2Status
            Clown2ButtonStatus=Clown2Button.value
			
        elif Clown2ButtonStatus==False and Clown2Button.value==True:
            Clown2ButtonStatus= not Clown2ButtonStatus
		
        #handler for tracking clown 3 selection
        if Clown3ButtonStatus==True and Clown3Button.value==False:
            Clown3Status= not Clown3Status
            Clown3ButtonStatus=Clown3Button.value
        elif Clown3ButtonStatus==False and Clown3Button.value==True:
            Clown3ButtonStatus= not Clown3ButtonStatus
		
        #handler for tracking clown 4 selection
        if Clown4ButtonStatus==True and Clown4Button.value==False:
            Clown4Status= not Clown4Status
            Clown4ButtonStatus=Clown4Button.value
        elif Clown4ButtonStatus==False and Clown4Button.value==True:
            Clown4ButtonStatus= not Clown4ButtonStatus
		
        #handler for tracking clown 5 selection
        if Clown5ButtonStatus==True and Clown5Button.value==False:
            Clown5Status= not Clown5Status
            Clown5ButtonStatus=Clown5Button.value
        elif Clown5ButtonStatus==False and Clown5Button.value==True:
            Clown5ButtonStatus= not Clown5ButtonStatus
		
        #handler for tracking clown 6 selection
        if Clown6ButtonStatus==True and Clown6Button.value==False:
            Clown6Status= not Clown6Status
            Clown6ButtonStatus=Clown6Button.value
        elif Clown6ButtonStatus==False and Clown6Button.value==True:
            Clown6ButtonStatus= not Clown6ButtonStatus
		
        #handler for tracking clown 7 selection
        if Clown7ButtonStatus==True and Clown7Button.value==False:
            Clown7Status= not Clown7Status
            Clown7ButtonStatus=Clown7Button.value
        elif Clown7ButtonStatus==False and Clown7Button.value==True:
            Clown7ButtonStatus= not Clown7ButtonStatus
		
        #handler for tracking clown 8 selection
        if Clown8ButtonStatus==True and Clown8Button.value==False:
            Clown8Status= not Clown8Status
            Clown8ButtonStatus=Clown8Button.value
        elif Clown8ButtonStatus==False and Clown8Button.value==True:
            Clown8ButtonStatus= not Clown8ButtonStatus
		
        #handler for tracking clown killer selection
        if ClownKillerButtonStatus==True and ClownKillerButton.value==False:
            ClownKillerStatus= not ClownKillerStatus
            ClownKillerButtonStatus=ClownKillerButton.value
        elif ClownKillerButtonStatus==False and ClownKillerButton.value==True:
            ClownKillerButtonStatus= not ClownKillerButtonStatus    
		
        if ClownSelectionQuantity < 8: # if less than 8 clowns selected handle like normal
            Clown1Light.value =Clown1Status
            Clown2Light.value=Clown2Status
            Clown3Light.value=Clown3Status
            Clown4Light.value=Clown4Status
            Clown5Light.value=Clown5Status
            Clown6Light.value=Clown6Status
            Clown7Light.value=Clown7Status
            Clown8Light.value=Clown8Status
            ClownKillerLight.value=ClownKillerStatus
			
            WinSelector=0
            LastSelectionBool=0
            LastSelectionAudio.stop()
		
        elif ClownSelectionQuantity==8: # if 8 clowns are selected blink the last selection 
			
            if WinSelector==0:
                if Clown1Status==0:
                    ClownSelection=1
                    BlinkStartTime=time.time()
                elif Clown2Status==0:
                    ClownSelection=2
                    BlinkStartTime=time.time()
                elif Clown3Status==0:
                    ClownSelection=3
                    BlinkStartTime=time.time()
                elif Clown4Status==0:
                    ClownSelection=4
                    BlinkStartTime=time.time()
                elif Clown5Status==0:
                    ClownSelection=5
                    BlinkStartTime=time.time()
                elif Clown6Status==0:
                    ClownSelection=6
                    BlinkStartTime=time.time()
                elif Clown7Status==0:
                    ClownSelection=7
                    BlinkStartTime=time.time()
                elif Clown8Status==0:
                    ClownSelection=8
                    BlinkStartTime=time.time()
                elif ClownKillerStatus==0:
                    ClownSelection=9
                    BlinkStartTime=time.time()
                else:
                    ClownSelection=0
                    
                WinSelector=1
                BlinkCount=1
				
            if LastSelectionBool==0:
                LastSelectionBool=1
                LastSelectionPlayStart=time.time()
                #CountDownAudio.pause()
                Channel1.pause()
                LastSelectionAudio.play()
                #time.sleep(LastSelectionLength)
                ChannelTime=time.time()
				         
				         
			
            if ClownSelection==1:
                if (time.time()-BlinkStartTime)>= (BlinkCount*BlinkTime) :
                    Clown1Light.value= not Clown1Light.value
                    BlinkCount+=1
				
            elif ClownSelection==2:
                if (time.time()-BlinkStartTime)>= (BlinkCount*BlinkTime) :
                    Clown2Light.value= not Clown2Light.value
                    BlinkCount+=1
				
            elif ClownSelection==3:
                if (time.time()-BlinkStartTime)>= (BlinkCount*BlinkTime) :
                    Clown3Light.value= not Clown3Light.value
                    BlinkCount+=1
				
            elif ClownSelection==4:
                if (time.time()-BlinkStartTime)>= (BlinkCount*BlinkTime) :
                    Clown4Light.value= not Clown4Light.value
                    BlinkCount+=1
				
            elif ClownSelection==5:
                if (time.time()-BlinkStartTime)>= (BlinkCount*BlinkTime) :
                    Clown5Light.value= not Clown5Light.value
                    BlinkCount+=1
				
            elif ClownSelection==6:
                if (time.time()-BlinkStartTime)>= (BlinkCount*BlinkTime) :
                    Clown6Light.value= not Clown6Light.value
                    BlinkCount+=1
				
            elif ClownSelection==7:
                if (time.time()-BlinkStartTime)>= (BlinkCount*BlinkTime) :
                    Clown7Light.value= not Clown7Light.value
                    BlinkCount+=1
				
            elif ClownSelection==8:
                if (time.time()-BlinkStartTime)>= (BlinkCount*BlinkTime) :
                    Clown8Light.value= not Clown8Light.value
                    BlinkCount+=1
				
            elif ClownSelection==9:
                if (time.time()-BlinkStartTime)>= (BlinkCount*BlinkTime) :
                    ClownKillerLight.value= not ClownKillerLight.value
                    BlinkCount+=1
				
        elif ClownSelectionQuantity==9: # the last killer was selected figure out if it was the right on clown 9 and trigger win if 9 or lose
                if ClownSelection==1:
                    Clown1Light.value=1
                    Clown2Light.value=0
                    Clown3Light.value=0
                    Clown4Light.value=0
                    Clown5Light.value=0
                    Clown6Light.value=0
                    Clown7Light.value=0
                    Clown8Light.value=0
                    ClownKillerLight.value=0
                    
                    GameState=6
                    
                elif ClownSelection==2:
                    Clown1Light.value=0
                    Clown2Light.value=1
                    Clown3Light.value=0
                    Clown4Light.value=0
                    Clown5Light.value=0
                    Clown6Light.value=0
                    Clown7Light.value=0
                    Clown8Light.value=0
                    ClownKillerLight.value=0
                    
                    GameState=6
                    
                elif ClownSelection==3:
                    Clown1Light.value=0
                    Clown2Light.value=0
                    Clown3Light.value=1
                    Clown4Light.value=0
                    Clown5Light.value=0
                    Clown6Light.value=0
                    Clown7Light.value=0
                    Clown8Light.value=0
                    ClownKillerLight.value=0
                    
                    GameState=6
                    
                elif ClownSelection==4:
                    Clown1Light.value=0
                    Clown2Light.value=0
                    Clown3Light.value=0
                    Clown4Light.value=1
                    Clown5Light.value=0
                    Clown6Light.value=0
                    Clown7Light.value=0
                    Clown8Light.value=0
                    ClownKillerLight.value=0
                    
                    GameState=6
                    
                elif ClownSelection==5:
                    Clown1Light.value=0
                    Clown2Light.value=0
                    Clown3Light.value=0
                    Clown4Light.value=0
                    Clown5Light.value=1
                    Clown6Light.value=0
                    Clown7Light.value=0
                    Clown8Light.value=0
                    ClownKillerLight.value=0
                    
                    GameState=6
                    
                elif ClownSelection==6:
                    Clown1Light.value=0
                    Clown2Light.value=0
                    Clown3Light.value=0
                    Clown4Light.value=0
                    Clown5Light.value=0
                    Clown6Light.value=1
                    Clown7Light.value=0
                    Clown8Light.value=0
                    ClownKillerLight.value=0
                    
                    GameState=6
                    
                elif ClownSelection==7:
                    Clown1Light.value=0
                    Clown2Light.value=0
                    Clown3Light.value=0
                    Clown4Light.value=0
                    Clown5Light.value=0
                    Clown6Light.value=0
                    Clown7Light.value=1
                    Clown8Light.value=0
                    ClownKillerLight.value=0
                    
                    GameState=6
                    
                elif ClownSelection==8:
                    Clown1Light.value=0
                    Clown2Light.value=0
                    Clown3Light.value=0
                    Clown4Light.value=0
                    Clown5Light.value=0
                    Clown6Light.value=0
                    Clown7Light.value=0
                    Clown8Light.value=1
                    ClownKillerLight.value=0
                    
                    GameState=6
                    
                elif ClownSelection==9:
                    Clown1Light.value=0
                    Clown2Light.value=0
                    Clown3Light.value=0
                    Clown4Light.value=0
                    Clown5Light.value=0
                    Clown6Light.value=0
                    Clown7Light.value=0
                    Clown8Light.value=0
                    ClownKillerLight.value=1
                    
                    GameState=5
		
    elif GameState==5:
        GameIndicatorLight.value=1
        HintLight.value=0
        RedButtonLight.value=1
        ClownSelection=0 # reset clown lights
        Clown1Status=False #0 Not Selected 1 Selected
        Clown2Status=False #0 Not Selected 1 Selected
        Clown3Status=False #0 Not Selected 1 Selected
        Clown4Status=False #0 Not Selected 1 Selected
        Clown5Status=False #0 Not Selected 1 Selected
        Clown6Status=False #0 Not Selected 1 Selected
        Clown7Status=False #0 Not Selected 1 Selected
        Clown8Status=False #0 Not Selected 1 Selected
        ClownKillerStatus=False #0 Not Selected 1 Selected
        InteriorLighting.value=0
        RadioLight.value=0
        Clown1Light.value=0
        Clown2Light.value=0
        Clown3Light.value=0
        Clown4Light.value=0
        Clown5Light.value=0
        Clown6Light.value=0
        Clown7Light.value=0
        Clown8Light.value=0
        ClownKillerLight.value=0
		
        DoorLock.value=False
		
        ExternalSpeakerSelection.set_value(0)
        InternalSpeakerSelection.set_value(0)
        RadioSpeakerSelection.set_value(0)
        AtticSpeakerSelection.set_value(1)
        CountDownAudio.stop()
        LastSelectionAudio.stop()
		
        if EndGameState==0:
            time.sleep(1)
            EndGameState=1
        elif EndGameState==1:			      
            if AudioPlaying==0:

                AudioPlaying=1
                AtticOpenStart=time.time()
                AudioTime=time.time()
				
            
                #WinAudio.play()
                #AtticLighting.value=1
                MotorControl1.set_value(0)
                MotorControl2.set_value(1)
            #AtticOpenStart=time.time()
            #AudioTime=time.time()
			
            if AtticOpenStart>0 and((time.time()-AtticOpenStart)>=1.5):
                WinAudio.play()
                AtticLighting.value=1
			
            if AtticOpenStart> 0 and ((time.time()-AtticOpenStart)>=MotorOpenTime):
                MotorControl1.set_value(0)
                MotorControl2.set_value(0)
                EndGameState=2
					
                    #(EndGameState)
			      
        elif EndGameState==2:
            time.sleep(3)
            EndGameState=3
            #print(EndGameState)
			      
        elif EndGameState==3:
            AtticLighting.value=0
			
            if LimitSwitch.get_value()==0:
                    time.sleep(3)
                    MotorControl1.set_value(0)
                    MotorControl2.set_value(0)
                    GameState=7
            else :
                    MotorControl1.set_value(1)
                    MotorControl2.set_value(0)
		
        if  DoorStatus.value==True: #Check if left booth by opening the door
            LeavingBooth=1

    elif GameState==6: # LOSE -> see game state 5 for comments
        HintLight.value=0
        RedButtonLight.value=1
        if(ExitBool==1):
            #CountDownAudio.stop()
            #Channel1.stop()
            #playing.stop()
            AudioTime=0
            AudioPlaying=0
            DoorLock.value=True
            time.sleep(0.5)
            GameState=7
			
        GameIndicatorLight.value=1
		
        ClownSelection=0 # reset clown lights
        Clown1Status=False #0 Not Selected 1 Selected
        Clown2Status=False #0 Not Selected 1 Selected
        Clown3Status=False #0 Not Selected 1 Selected
        Clown4Status=False #0 Not Selected 1 Selected
        Clown5Status=False #0 Not Selected 1 Selected
        Clown6Status=False #0 Not Selected 1 Selected
        Clown7Status=False #0 Not Selected 1 Selected
        Clown8Status=False #0 Not Selected 1 Selected
        ClownKillerStatus=False #0 Not Selected 1 Selected
        InteriorLighting.value=0
        RadioLight.value=0
        Clown1Light.value=0
        Clown2Light.value=0
        Clown3Light.value=0
        Clown4Light.value=0
        Clown5Light.value=0
        Clown6Light.value=0
        Clown7Light.value=0
        Clown8Light.value=0
        ClownKillerLight.value=0
		
        DoorLock.value=False
		
        ExternalSpeakerSelection.set_value(0)
        InternalSpeakerSelection.set_value(0)
        RadioSpeakerSelection.set_value(0)
        AtticSpeakerSelection.set_value(1)
        CountDownAudio.stop()
        LastSelectionAudio.stop()
		
        if EndGameState==0:
            time.sleep(1)
            EndGameState=1
            #(EndGameState)
        elif EndGameState==1:
			      
            #AtticLighting.value=1
			
            if AudioPlaying==0:
                #LoseAudio.play()
                AudioPlaying=1
                AtticOpenStart=time.time()
                #AudioTime=time.time()
					
            MotorControl1.set_value(0)
            MotorControl2.set_value(1)
            #AtticOpenStart=time.time()
            #AudioTime=time.time()
            #(AtticOpenStart)
            #print(AudioTime)
			
            if AtticOpenStart>0 and((time.time()-AtticOpenStart)>=1.5):
                    LoseAudio.play()
                    AtticLighting.value=1
                    AtticLighting.value=1
			
            if (AtticOpenStart>= 0) and ((time.time()-AtticOpenStart)>=MotorOpenTime):
                    MotorControl1.set_value(0)
                    MotorControl2.set_value(0)
                    EndGameState=2
                    print(EndGameState)
			      
        elif EndGameState==2:
            time.sleep(3)
            EndGameState=3
            #print(EndGameState)
			      
        elif EndGameState==3:
            AtticLighting.value=0
			
            if LimitSwitch.get_value()==0:
                    time.sleep(3)
                    MotorControl1.set_value(0)
                    MotorControl2.set_value(0)
                    GameState=7
            else :
					
                    MotorControl1.set_value(1)
                    MotorControl2.set_value(0)
		
        if  DoorStatus.value==True: #Check if left booth by opening the door
            LeavingBooth=1


    elif GameState==7: #LEAVE State
        GameIndicatorLight.value=1
        RedButtonLight.value=1
        AtticLighting.value=0
        ExitBool=0
        HintLight.value=0
        if AudioPlaying==0:
            #Stop any lingering audio
            pygame.mixer.stop()
            Channel1.stop()
            Channel2.stop()
            RulesAudio.stop()
            CountDownAudio.stop()
        if  DoorStatus.value==True: # check if leaving
            LeavingBooth=1
			
            if UnlockStartTime==0:
                UnlockStartTime=time.time()
                DoorLock.value=False

        if ((time.time()-UnlockStartTime)>=UnlockDuration) and LeavingBooth==1: # after leaving and unlock time triggered lock the door
              DoorLock.value=True
			  
			  
			  
              #time.sleep(2)
			  
              if DoorStatus.value==False:
                  GameState=0 # return to idle
                  UnlockStartTime=0 #reset variables
                  MinuteTicker=1
                  BlinkStartTime=0
                  BlinkCount=1
                  ClownSelectionQuantity=0
                  ClownSelection=0
                  WinSelector=0
                  AudioTime=0
                  AudioPlaying=0
                  AtticOpenStart=0
                  LeavingBooth=0
                  EndGameState=0
                  LastSelectionPlayStart=0
	          CountdownPlay=0
                  HintCount=0
                  HintPlaying=0
                  Hint1Bool=0
                  Hint2Bool=0
                  Hint3Bool=0
				  
              elif DoorStatus.value==True:
                if AudioPlaying==0: # play the door close audio request
                   AudioPlaying=1
                   AudioTime=time.time()
				
                   ExternalSpeakerSelection.set_value(0)
                   InternalSpeakerSelection.set_value(1)
                   RadioSpeakerSelection.set_value(0)
                   AtticSpeakerSelection.set_value(0)
				
                   playing=LeaveAudio.play()
				
                elif AudioPlaying==1 and (time.time()-AudioTime)>= (3+LeaveAudioLength):
                    ExternalSpeakerSelection.set_value(0)
                    InternalSpeakerSelection.set_value(1)
                    RadioSpeakerSelection.set_value(0)
                    AtticSpeakerSelection.set_value(0)
                    playing=LeaveAudio.play()
                    AudioTime=time.time()
				     
    else:
        GameState=0 # when in doubt return to 0 
