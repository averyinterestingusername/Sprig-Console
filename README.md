# Sprig-Console

Hello! Because I find the Sprig looks like a game controller, I wanted use it as one!

<img width="233" alt="Game_Controllers" src="https://github.com/user-attachments/assets/2b5e54a5-905c-4256-b7b9-04d01e1272a6"/>

Disclaimer: Sadly, there is quite a lot of latency between pressing a key and it arriving at your PC. So although I really wanted to use it to play video games, it won't work for anything that requires precise timing. Or a mouse.

## Instructions

To make this work, you need to have a [Sprig](https://sprig.hackclub.com/) and a PC.
Alternatively, you can build your own Sprig from a Raspberry Pi Pico W and some buttons :)

### Setup

First, if you haven't already, you need to install Python and Thonny

Then, [install micropython on your Raspberry Pi Pico W](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/3) (The board on the back of your Sprig): 

Manipulate my files:
- Download the files from this repsitory
- Fill out the credentials.py file
- Then, upload the files console_pico.py and credentials.py to your Pico
- Rename the console_pico.py file to main.py. This causes the program to run on your Pico as soon as it has power.

### Running the program

Before running the program, 
- Make sure your PC is connected to your network,
- And that the credentials.py file is identical on both devices.

Then:
- Run the console.py file
- Turn on your Sprig
- Wait for the little green LED on the back of your Sprig to turn on, indicating it has connected to your network

Voilà! That should allow you to send keypresses over your WiFi network, and use your Sprig as a console/keyboard!

Disclaimer (again): Sadly, there is quite a lot of latency between pressing a key and it arriving at your PC. So although I really wanted to use it to play video games, it won't work for anything that requires precise timing. Or a mouse.
