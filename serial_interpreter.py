import serial
import pyvjoy

#Pythonic API, item-at-a-time
j = pyvjoy.VJoyDevice(1)

ser = serial.Serial('COM5', 9600)

#j.set_axis(pyvjoy.HID_USAGE_X,25000)

while True:
    message = ser.readline()
    try:
        message = ser.readline()
        
        vstring = message.decode('utf-8').rstrip().lstrip().split(',')
        x_ax = (16-int(vstring[0].rstrip().lstrip()))*1024    #steering
        z_ax = (int(vstring[2].rstrip().lstrip())-310)*340    #brake
        y_ax = (int(vstring[3].rstrip().lstrip())-510)*210    #accelerator
        j.set_button(1,int(vstring[1]))
        j.set_axis(pyvjoy.HID_USAGE_Z,int(z_ax))
        j.set_axis(pyvjoy.HID_USAGE_X,int(x_ax))
        j.set_axis(pyvjoy.HID_USAGE_Y,int(y_ax))
        print(vstring[0],vstring[1],vstring[2],vstring[3])

    except:
        pass










