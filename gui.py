from tkinter import *
from tkinter import simpledialog
import os


soundcard = 'plughw:CARD=Device,DEV=0';


root = Tk() # Fenster erstellen
root.wm_title("RPITX GUI") # Fenster Titel
root.config(background = "#FFFFFF") # Hintergrundfarbe des Fensters
 
# Hier kommen die Elemente hin
leftFrame = Frame(root, width=200, height = 400)
leftFrame.grid(row=0, column=0, padx=10, pady=3)
 
leftLabel1 = Label(leftFrame, text="Frequency(Mhz) -->")
leftLabel1.grid(row=0, column=0, padx=10, pady=3)
#leftLabel2 = Label(leftFrame, text="")
#leftLabel2.grid(row=1, column=0, padx=10, pady=3)
 
rightFrame = Frame(root, width=400, height = 400)
rightFrame.grid(row=0, column=1, padx=10, pady=3)
 
E1 = Entry(rightFrame, width=20)
E1.grid(row=0, column=0, padx=5, pady=3)

TXING = 0;


def stopTX():
    global TXING;
    print("STOP TX")
    TXING = 0;
    os.system('sudo killall rpitx 2>/dev/null');
    os.system('sudo killall tune 2>/dev/null');
    os.system('sudo killall arecord 2>/dev/null');
def fmTX():
    global TXING;
    global soundcard;
    print("FM");
    if TXING != 1:
      TXING = 1;
      os.system('arecord -c1 -r48000 -D ' + soundcard + ' -c1 -r48000 -fS16_LE - | csdr convert_i16_f | csdr gain_ff 7000 | csdr convert_f_samplerf 20833 | sudo rpitx -i- -m RF -f ' + E1.get() + 'e3  >/dev/null 2>/dev/null &');
def usbTX():
    global TXING;
    global soundcard;
    print("USB");
    if TXING != 1:
      TXING = 1;
      os.system('arecord -c1 -r48000 -D ' + soundcard + ' -c1 -r48000 -fS16_LE - | csdr convert_i16_f | csdr dsb_fc | csdr bandpass_fir_fft_cc 0 0.1 0.01 | csdr gain_ff 2.0 | csdr shift_addition_cc 0.2 | sudo rpitx -i- -m IQFLOAT -f ' + E1.get() + 'e3  >/dev/null 2>/dev/null &');
def lsbTX():
    global TXING;
    global soundcard;
    print("LSB");
    if TXING != 1:
      TXING = 1;
      os.system('arecord -c1 -r48000 -D ' + soundcard + ' -c1 -r48000 -fS16_LE - | csdr convert_i16_f | csdr dsb_fc | csdr bandpass_fir_fft_cc -0.1 0 0.01 | csdr gain_ff 2.0 | csdr shift_addition_cc 0.2 | sudo rpitx -i- -m IQFLOAT -f ' + E1.get() + 'e3  >/dev/null 2>/dev/null &');
def wfmTX():
    global TXING;
    global soundcard;
    print("WFM");
    if TXING != 1:
      TXING = 1;
      os.system('arecord -c1 -r48000 -D ' + soundcard + ' -c1 -r48000 -fS16_LE - | csdr convert_i16_f | csdr gain_ff 70000 | csdr convert_f_samplerf 20833 | sudo rpitx -i- -m RF -f ' + E1.get() + 'e3  >/dev/null 2>/dev/null &');
def vfoTX():
    global TXING;
    global soundcard;
    print("VFO");
    if TXING != 1:
      TXING = 1;
      os.system('sudo tune -f ' + E1.get() + 'e6  >/dev/null 2>/dev/null &');


buttonFrame = Frame(rightFrame)
buttonFrame.grid(row=1, column=0, padx=10, pady=3)
    
B1 = Button(buttonFrame, text="STOP TX", bg="#FF0000", width=8, command=stopTX)
B1.grid(row=3, column=0, padx=10, pady=3)
 
B2 = Button(buttonFrame, text="FM TX", bg="#FFFF00", width=8, command=fmTX)
B2.grid(row=3, column=1, padx=10, pady=3)
 
B3 = Button(buttonFrame, text="USB TX", bg="#FFFF00", width=8, command=usbTX)
B3.grid(row=3, column=2, padx=10, pady=3)

B4 = Button(buttonFrame, text="LSB TX", bg="#FFFF00", width=8, command=lsbTX)
B4.grid(row=4, column=0, padx=10, pady=3)

B5 = Button(buttonFrame, text="WFM TX", bg="#FFFF00", width=8, command=wfmTX)
B5.grid(row=4, column=1, padx=10, pady=3)

B6 = Button(buttonFrame, text="VFO TX", bg="#FFFF00", width=8, command=vfoTX)
B6.grid(row=4, column=2, padx=10, pady=3)



#Slider = Scale(rightFrame, from_=0, to=100, resolution=0.1, orient=HORIZONTAL, length=400)
#Slider.grid(row=2, column=0, padx=10, pady=3)
 
 
root.mainloop() # GUI wird upgedatet. Danach keine Elemente setzen
