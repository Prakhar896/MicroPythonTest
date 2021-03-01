# List of commands

This is for future reference and practice:

## Turn off bot
Go to terminal and type `sudo poweroff` and then maker to turn off.

## Setting name of bot
Go to terminal and type `sudo hostnamectl set-hostname <name>` and then type maker to change bot name

## Python Commands
### Hub/EV3 Brain
Lights:

```python
ev3.light.on(Color.RED) # changes light colour to red
ev3.light.off() # turns off light
```

Audio:

```python
ev3.speaker.beep()
ev3.speaker.play_file(SoundFile.<name>)
ev3.speaker.say("Speech message here")
ev3.speaker.play_notes(['C4/4', 'G4/4'])
```

Screen:

```python
ev3.screen.print("Hello ")
ev3.screen.print("World!")
ev3.screen.width # gets width of screen in pixels
ev3.screen.height # gets height of screen in pixels
ev3.save("file_name") # saves the screen as a .png file
```

Get battery voltage:

```python
ev3.battery.voltage()
```

### Motors
Running a Motor for a certain number of degrees:

```python
test_motor = Motor(Port.B)
test_motor.run_target(500, 90) # runs for 500 degrees at a 90 degree target angle
```

Speed Of Motor:

```python
test_motor = Motor(Port.B)
test_motor.speed()
```

Motor Angle:

```python
test_motor = Motor(Port.B)
test_motor.angle() 
test_motor.reset_angle(0) # resets rotation angle to 0
```

Stopping the Motor:

```python
test_motor = Motor(Port.B)
test_motor.stop() #stops the motor but lets it move freely until it stops due to friction

test_motor.hold() # stops the motor and holds its current angle, abrupt stop
```

Actions:

```python
test_motor = Motor(Port.B)
test_motor.run(100) # runs the motor at 100 constant speed
```