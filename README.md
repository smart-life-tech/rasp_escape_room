# ClownAround Escape Room Control System

A Raspberry Pi 5-based control system for an interactive escape room game featuring clown-themed puzzles, audio management, and hardware control.

## Overview

This system controls an escape room experience where players must identify the "killer clown" among 9 different clown characters. The game features multiple states, audio cues, lighting effects, and mechanical elements controlled through GPIO pins and I2C expansion boards.

## Hardware Requirements

### Raspberry Pi 5 Setup
- Raspberry Pi 5
- MicroSD card (32GB+ recommended)
- Power supply
- I2C enabled

### GPIO Components
- **Speaker Control Pins**: 17, 22, 23, 27
- **Motor Control Pins**: 5, 6
- **Limit Switch Pin**: 13
- **GPIO Chip**: gpiochip4

### I2C Expansion Boards
- **Poster MCP23017** (Address: 0x25) - Controls clown lights and buttons
- **Other MCP23017** (Address: 0x27) - Controls auxiliary functions

### Audio Hardware
- 4 Speaker zones (External, Internal, Radio, Attic)
- Audio amplification system
- Speaker selection relays

### Physical Components
- 9 Illuminated clown poster buttons
- 9 Corresponding LED lights
- Door lock mechanism
- Limit switch for motor control
- Interior and attic lighting
- Hint button (5V illuminated)
- Green/Red control buttons

## Software Dependencies

```bash
pip install adafruit-circuitpython-mcp230xx
pip install pygame
pip install gpiod
```

### System Libraries
- `board` - CircuitPython board definitions
- `busio` - I2C communication
- `digitalio` - Digital I/O control
- `time` - Timing functions

## Audio Files Required

Place these audio files in the same directory as the Python script:

- `Idle.mp3` - Background music for idle state
- `DoorCloseRequest.mp3` - Door closure prompt
- `Rules.mp3` - Game instructions (46+ seconds)
- `CountDown.mp3` - 5-minute gameplay background music
- `TimeWarning.mp3` - Time warning alert
- `Win.mp3` - Victory audio
- `Lose.mp3` - Defeat audio
- `Leave.mp3` - Exit instructions
- `LastClown.mp3` - Final selection audio
- `Hint1.mp3` - First hint audio
- `Hint2.mp3` - Second hint audio (5 seconds)
- `Hint3.mp3` - Third hint audio

## Game States

### 0 - IDLE
- Plays background music
- Green button illuminated
- Waits for payment/start signal

### 1 - PAYMENT
- Door unlocks
- Interior lights turn on
- Waits for door to open

### 2 - ENTER
- Player enters booth
- Door auto-locks after 3 seconds
- Prompts door closure if needed

### 3 - PREGAME
- Plays rules audio
- All clown lights blink 6 times
- Transitions to gameplay

### 4 - GAMEPLAY
- 5-minute countdown begins
- Players select clowns via buttons
- Hint system active (3 hints maximum)
- Win condition: Select 8 clowns, then correct killer clown
- Lose condition: Time expires or wrong final selection

### 5 - WIN
- Attic opens with motor control
- Victory audio plays
- Attic lighting activates
- Door unlocks for exit

### 6 - LOSE
- Attic opens briefly
- Defeat audio plays
- Door unlocks for exit

### 7 - RESET/LEAVE
- Cleanup state
- Waits for player exit
- Resets all variables
- Returns to IDLE

## Hint System

The illuminated hint button provides three levels of assistance:

- **First Press**: Pauses countdown, plays Hint1 audio, resumes countdown
- **Second Press**: Pauses countdown, plays Hint2 audio (5 sec), resumes countdown  
- **Third Press**: Button light turns OFF, pauses countdown, plays Hint3 audio, resumes countdown
- **After Third Press**: Button becomes inactive

Each hint extends the game duration by the length of the hint audio.

## Pin Assignments

### MCP23017 - Poster Control (0x25)
- **Pins 0-6**: Clown buttons 1-7
- **Pins 7-15**: Clown lights (Pin 7=Clown1, Pin 15=Clown2, etc.)

### MCP23017 - Other Functions (0x27)
- **Pin 0**: Clown 8 button
- **Pin 1**: Killer clown button
- **Pins 2-7**: Auxiliary outputs (lights, locks, etc.)
- **Pins 8-11**: Auxiliary inputs (buttons, door status, payment)
- **Pins 12-15**: Game indicators and hint controls

## Installation

1. **Setup Raspberry Pi 5**:
```bash
sudo apt update
sudo apt upgrade
sudo apt install python3-pip
```

2. **Enable I2C**:
```bash
sudo raspi-config
# Navigate to Interface Options > I2C > Enable
```

3. **Install Dependencies**:
```bash
pip install adafruit-circuitpython-mcp230xx pygame gpiod
```

4. **Copy Files**:
```bash
# Copy ClownAround_006_V29.py and all audio files to your project directory
```

5. **Run System**:
```bash
python3 ClownAround_006_V29.py
```

## Configuration

### Audio Volume Levels
- Idle: 0.2
- Door Close Request: 0.1
- Rules, Win, Lose, Time Warning: 1.0
- Countdown: 0.5

### Timing Parameters
- Game Duration: 300 seconds (5 minutes)
- Door Unlock Duration: 3 seconds
- Attic Open Time: 4 seconds
- Blink Rate: 0.625 seconds

## Troubleshooting

### Common Issues

1. **I2C Communication Errors**:
   - Check wiring connections
   - Verify I2C addresses (0x25, 0x27)
   - Ensure I2C is enabled in raspi-config

2. **Audio Not Playing**:
   - Verify audio files are in correct directory
   - Check speaker connections
   - Test pygame mixer initialization

3. **GPIO Errors**:
   - Ensure script runs with appropriate permissions
   - Check GPIO pin assignments
   - Verify gpiochip4 availability

4. **Button Not Responding**:
   - Check pull-up resistor configuration
   - Verify MCP23017 pin assignments
   - Test button debouncing

### Debug Mode
Add print statements to monitor game state:
```python
print(f"Game State: {GameState}")
print(f"Clown Selection Count: {ClownSelectionQuantity}")
```

## Safety Notes

- Always power down system before making hardware connections
- Use appropriate current limiting for LED circuits
- Ensure proper grounding for all components
- Test emergency stop procedures

## License

This project is designed for entertainment/educational purposes. Ensure compliance with local electrical and safety codes when implementing physical escape room elements.

## Support

For technical issues or modifications, refer to the inline code comments and hardware documentation for the specific components used in your implementation.