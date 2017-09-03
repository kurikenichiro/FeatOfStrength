# Setup

* Install Arduino IDE https://www.arduino.cc/en/Main/Software
* Install Teensyduino
* Clone tm1638-library into Arduino library location

Connect the following
VCC -> 5V (red)
GND -> GND (black)
DIO -> 8 (yellow)
CLK -> 9 (green)
STB0 -> 7 (orange)

# Dependancies

* https://github.com/rjbatista/tm1638-library

# Building

$ /Applications/Arduino.app/Contents/MacOS/Arduino --verify -v ~/Documents/Arduino/FeatOfStrength/FeatOfStrength.ino;

# Instructions

You will find in the bag 3 principle items:

1. A Teensy 3.2 32 bit ARM Cortex M4 micro-controller with pins.
2. A combination LED 7 segment display, 3 color LED, pushbutton array panel.
3. Connection wires

Here is the objective, broken into steps:

1. Set up a Teensy programming environment and verify that you are able to program the teensy from your host machine (provided yourself).  You may program the Teensy in any fashion you wish - using the Arduino IDE, the command-line tools, or even using a stand-alone programming environment like C-Forth or Txtzyme.  Your option.

2. Wire up the teensy to the display and buttons using only Google resources (documentation for either item has been deliberately NOT been provided :) )

3. Write a native application for the Teensy which can control all functions of the LED board (individual panels, LED light values, buttons) and can also communicate using USB Serial communications with the host computer.  You will need this for steps 4 and 5.

4. Write an agent which runs on the host and grabs the current time and date, continuously updating the Teensy such that the display looks like this:

LED Segment 1 LED Segment 2
MM DD HH MM

And displays the current time and date as pulled from the host.

The first two buttons should also perform the following functions:

Button one:  Switch between 24 hour time and 12 hour time.
Button two:  Switch between host-local time and GMT

5. The agent should also open a local socket on the host (unix domain or TCP) and support a very basic API (see below) which allows someone to set the state of one of the 3 color LEDs and poll the state of any of the unassigned buttons.   This API should either be some message-passing method that can be accessed via a stand-alone accompanying python or C program, or via a small CLI that can be accessed directly via telnet or nc (e.g. `telnet localhost 10000`) and allows this to be done interactively as a user-provided command.

6. All of the code to implement the above should be checked into GitHub and provided with a Makefile or, at least a README.md explaining how to build all of the above.

7. Extra credit:  Do something interesting with the 3-color LEDs, entirely up to your imagination, using the API or CLI.  One suggestion our team had was to have the third button select the time of the last git commit to your repository above, making the LEDs also represent the short git commit hash as a BCD number.  The GitHub poller would then check once every few seconds or so for the HEAD hash to change and update the date/time and hash values accordingly.


Calibration data for FoS:

Without any prior knowledge of the FoS exercise (or any prior knowledge of the LED panel), one of our engineering team members was able to complete steps 1-3 in approximately 30 minutes.   Estimated completion time for steps 4 and 5 is an additional 30-45 minutes.  No estimation was done for step 7.

Good luck, and have fun with it!   Extra points will be awarded for originality or uniqueness of approach.  There is no wrong way to do this, assuming that we can reproduce your results at all. :)