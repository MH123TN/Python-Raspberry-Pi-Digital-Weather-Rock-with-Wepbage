# Python-Raspberry-Pi-Digital-Weather-Rock-with-Wepbage
Raspberry Pi Sense Hat Digital Webpage drive weather indicator.

# Weather PI Project

Video Demo: https://youtu.be/acfPoJYABD4


Links to Project Code on GitHub:

https://github.com/MH123TN/Python-Raspberry-Pi-Digital-Weather-Rock-with-Wepbage

## Description:

### Purpose:

The purpose of this program is to  visually indicate barometric trends using the Raspberry pi SenseHat pressure measurement sensor and multicolor LED screen to visually indicate possible severe weather..  The assembly is meant to be portable , 12 volt operable.  The RAspberry Pi SEnse Hat utilzes an onboard BMP sensor that indicates pressure in hPa where sea level is roughly 1000 hPa. The SenseHat board  utilzies the SenseHat python library for the physical hardware and the sense_emu library for simulated hardware.

### History:

The earliest version of this application was written in NODE-RED utilizing the no-code approach - the pressure measurement and screen animation was implimented in the Java function block .  This  version is running on a Raspberry Pi 2 with an obsolete python 2.7 driver.  This assembly is mounted facing a standing computer desk that services a ham radio weather net work station.   The earliest version made use of a green dot that moved around the corners to indicate the application was executing.  this proved difficult to code but was solvable.   ONe variant of the weather station broadcast the pressure reading via UDP packets to a windows machine running labView where real-time pressure trends could be displayed.

NODE-RED (at the time of the Raspberry Pi 3) had not updated the application to utilize the python 3.x sense hat driver and the program was migrated to Python 3.x in 2022.

The Python version runs for 10 hours then blanks the screen and must be initalized from either Spider IDE or the Python 3.x console

2025 Migration to Python 3/Flask application.

### Other Variants

This solution was implimented using C in the ESP32 hardware with intergral 4- line ascii display - a BMP280 board and Lightning detector where implimented in a hand held protoype configuration .  No external web interface was developed for this approach   this code was developed using c- files and examples from other authors and credit is provided in the source code.

#### Future project builds

* Modification of the Exp32 variant to supply barometric pressure and status via webpage
* port ESP32 code over picoCalc hand held Basic computer and re-write in pico basic.  (this code is in progress using excell and concantenation statements for graphic animation)

### Shortfals addressed in this version:

The 2022 version requires a local pressure offset (hard coded )to be entered to make the pressure reading match that of the local airport.  This version also requires a local offset to correct the barometric display indications so that they animate properly.  (camping in the mountains indicates a low pressure alarm without adjustment for elevation)
The local pressure is adjustable via an altitude correction in Millibar


### Webpage Upgrade (Version 3)

Version 3 modified in December 2025 with the intent to provide the following enhanced features via a locally hosted webpage:

* Screen adjustable pressure correction (utlizing the hard coded value as an inital value)
* Pressure offset for localization (again using the hard coded value as the inital value)
* Indication of barometric pressure in mmHg
* Indication of barometric pressure in psia (absolute )
* Indication of SEnseHat temperature
* Indication of SenseHat Humidity
* Phrase alerts as to the curent weather state
* access via a smart phone or tablet.

#### Negatives:

*web page must be up for version to run (resolving this is outside the scope of this vesion)
*Raspberry Pi security doesn't allow webservice outside of the raspberry pi itself - narly..
*Updated now allows local network monitoring with a slight tweek

#### File Structure

Program writen in python using the Flask webpage approach..

File structure:

project folder
  app.py
  Static
    styles.css
  templates
    index.html

Python Program:

Init blocks
def generate_data(location_offset) # main block that interfaces to the sense hat

def index() # generic calls to the webpage

def stream() # calls the generate(data) and post a one line python created line in the html (live data pressure, barometer trend, offset, and humidity)
error checking for NULL value entered in.

def offset() # waits for the user to enter a millibar pressure offset which is passed to generate_data(location_offset)
  a glocal variable is used here to overrite the default variable in the program init.





#### Development environment:

Linux laptop used running Spyder DE Python 3.9 (OS is Debian , running RAspbian for i86, PIXEL desktop - (Pi Improved Xwindows Desktop Environment)) this provides access to the sense hat emulator native to the install image.  Finish project was loaded on the raspberry pi with the target hardware.  So many computers so little space.   Spider IDE was used rather than Visual Studio so many options for python it made it simpler to just use an IDE known to the author rather than an ide with multiple uses.


### Hardware:

#### Development machine

Used Panasonic tough book CF-32 running RAspberry pi install for i86
* Sypder IDE 3.9
* Linux OS
* SSD Hard drive
* Wifi integrated

#### Target Machine:

Rasbperry Pi X with Raspberry Pi OS (port of Debian Trixie)

The hardware utilizes the following:

* Rasbperry Pi 3
* Power Expansion Board - DC POWER Shield (12 volt power adapter )
  * Barrel Connector DC input (nominally 12 volts)
* Raspberry Pi Sense Hat
  * Softeare interfaces to the Raspberry pi via one-wire and GPIO
  * 8x8 256 color LED array
  * Integrated Pressure/Temperature and Humididy Sensors
  * Acceleraometer (unused)
  * Pushbutton/direction key (unused)
  * Gyro (unused)
  * Interfaces the Raspberry pi via the 40-pin GPIO header
  * Stackable Board
* Harbor Freight Case
* Wireless mini keyboard via USB dongle
* Mini-touch screen
* various cables (HDMI, USB etc)
* 12 volt to USB power adapter (screen power supply)
* wifi USB

**** Hardare stack

+-------------------------+
|       Sense Hat         |
+-------------------------+
|  Power Expansion Board  |
+-------------------------+
|      Raspberry Pi       |
+-------------------------+

The hardware is modular providing hardware/software migration.

### Software:

Program FLow as in all computer programs the first few blocks set up the external libraries:

sense_hat , or sense_emu for the hardware, time for the sleep function, flask items and datetime for timestamping the screens

Additionally each LED is addressed individually using a 3 word list for Red, Green Blue

Color definitions were defined as variables and intilaized.

Also the screen is written to as a list of 64 items starting at Top Right to Bottom Left from left to right and top to bottom.

several useful pre-defined variables of list as a blank screen were also built.

Animation Math: The pressure variations are very nominal being a delta of +/- 4 hPa
Nominal localization pressure is 981.51 hPa
The sense hat measured pressure is subtracted from the nominal pressure,  a series of If statements are used to set a pdelta intger varariable adn a p-trend,
This variable is then used to activate one of 8 animations on the 8x8 screen code is not effecient but does handle the complexity of these minute variabtions

#### Ranges: and trends - details details

The results of these comparisons are used to set the pixle patterns for the weather states:

Lowest Pressure Alarm (e:black, R is red) Big Red Stop Sign

| e | R | R | R | R | R | e | e |
| R | R | R | R | R | R | R | e |
| R | R | R | R | R | R | R | e |
| R | R | R | R | R | R | R | e |
| R | R | R | R | R | R | R | e |
| R | R | R | R | R | R | R | e |
| R | R | R | R | R | R | R | e |
| e | R | R | R | R | R | e | e |


Lower Pressure Warning: (R: red, all others black) Red Down Arrow


| e | e | R | R | R | R | e | e |
| e | e | R | R | R | R | e | e |
| e | e | R | R | R | R | e | e |
| e | e | R | R | R | R | e | e |
| e | e | R | R | R | R | R | e |
| e | R | R | R | R | R | R | e |
| e | e | R | R | R | R | e | e |
| e | e | e | R | R | e | e | e |


Low Pressure Warning: (Y: yellow, all others black) Yellow Down Arrow


| e | e | Y | Y | Y | Y | e | e |
| e | e | Y | Y | Y | Y | e | e |
| e | e | Y | Y | Y | Y | e | e |
| e | e | Y | Y | Y | Y | e | e |
| e | e | Y | Y | Y | Y | e | e |
| e | Y | Y | Y | Y | Y | Y | e |
| e | e | Y | Y | Y | Y | e | e |
| e | e | e | Y | Y | e | e | e |

Low Pressure Indication: (G: Green, all others black) Green Down Arrow

| e | e | G | G | G | G | e | e |
| e | e | G | G | G | G | e | e |
| e | e | G | G | G | G | e | e |
| e | e | G | G | G | G | e | e |
| e | e | G | G | G | G | e | e |
| e | G | G | G | G | G | G | e |
| e | e | G | G | G | G | e | e |
| e | e | e | G | G | e | e | e |


Nominal Pressure Indication: (B: Blue, all others black) alternating lines of Blue/Black sqiggle lines.

modulates up and down the 8 by 8 grid depending on pressure within the 'normal' range

| e | B | e | B | e | B | e | B |
| B | e | B | e | B | e | B | e |

High  Pressure Indication: (B: Blue, O: White , all others black)  White topped, Blue arrow pointing up

| e | e | e | O | e | e | e | e |
| e | e | O | O | O | e | e | e |
| e | O | O | O | O | O | e | e |
| e | e | B | B | B | e | e | e |
| e | e | B | B | B | e | e | e |
| e | e | B | B | B | e | e | e |
| e | e | B | B | B | e | e | e |

Green clock cycles ones per second around the corners replacing black e with Green R
reads the previous color of the corners replace them one step at a time to indicate the program is executing.

