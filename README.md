# Diy-racing-sim
Basic diy racing sim <br>

This simulator uses an arduino UNO to sample inputs from accelerator and brake pedals driven by potentiometers and a rotary encoder for steering.<br>
The data is outputted serial and is read by a python script. The script taps into the Vjoy ( virtual joystick ) python api to simulate gamepad input calls.
<br> 
The vjoy interface DLL must be in the same folder as the script and Vjoy must be installed.
This can be further hooked into x360 to emulate Xinput. The polling rate can be specified in x360ce and the sampling rate in the .ino code. 
<br><br>Feel free to expand on the existing codebase.

I'll put in some pictures to give a rough build idea

<img>https://photos.google.com/photo/AF1QipOpUOXGN6J_3sMT1cALfyePGeCDP9SPazwkDgaE</img>
