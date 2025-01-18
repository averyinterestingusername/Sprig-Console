# Sprig-Console

Hello! Because I find the Sprig looks like a game controller, I wanted use it as one!

<img width="233" alt="Game_Controllers" src="https://github.com/user-attachments/assets/2b5e54a5-905c-4256-b7b9-04d01e1272a6" />

Disclaimer: Sadly, I couldn't get the keypresses to arrive at the PC faster, meaning there is quite a lot of latency. So although I really wanted to use it to play video games, it won't work for anything that requires precise timing.

## Instructions

To make this work, you need to have a Sprig and a PC.

- First, if you haven't already, you need to install Python and Thonny.
- Install micropython on your Raspberry Pi Pico W (The board on the back of your Sprig): https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/3
- Download the files from this repsitory
- Fill out the credentials.py file
- Then, upload the files console_pico.py and credentials.py to your Pico
- Rename the console_pico.py file to main.py. This causes the file to run on your Pico as soon as it has power.

Running the program
- Make sure your PC is connected to the same network as your Pico
- Make sure no power is running to the Pico
- Run the console.py file
- Turn on your Sprig


Voila! That should allow you to send keypresses over your WiFi network, and use your Sprig as a console!
