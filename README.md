# Diy-racing-sim
This super basic simulator uses an arduino UNO to sample inputs from accelerator and brake pedals driven by potentiometers and a rotary encoder for steering.<br>
The data is outputted serial and is read by a python script. The script taps into the Vjoy ( virtual joystick ) python api to simulate gamepad input calls.
<br> 
The vjoy interface DLL must be in the same folder as the script and Vjoy must be installed.
This can be further hooked into x360 to emulate Xinput. The polling rate can be specified in x360ce and the sampling rate in the .ino code. 
<br><br>

# Installation requisites
Vjoy - http://vjoystick.sourceforge.net/site/index.php/download-a-install/download <br>
Pyvjoy ( python library for vjoy ) - https://pypi.org/project/pyvjoy/ <br>
X360CE (just in case your game doesn't like vjoy ) - https://www.x360ce.com/ <br>


I'll put in some pictures to give a rough build idea.


**Working video**
<br> The video is at media/video.mp4 . The input lag is due to the game and my laptop being kinda slow, but the system in itself works all right.


**Steering column is connected to encoder with hot glue**<br>
![](media/rotary_encode.jpg )<br>

**Foot Pedals View**<br>
![](media/pedal%20view.jpg )<br>

**Potentiometer driving mechanism**<br>
![](media/trim%20accel.jpg )<br>
