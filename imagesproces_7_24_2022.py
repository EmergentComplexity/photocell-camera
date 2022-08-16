from PIL import Image
from PIL import ImageDraw
import serial
import time
import re


#ser = serial.Serial("COM7", 9600, timeout=1)
ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM6'

ser.open()
time.sleep(2)
line = ser.readline()

find_all = re.findall("\d+", str(line))

A0 = int(find_all[0])
A1 = int(find_all[1])
A2 = int(find_all[2])
A3 = int(find_all[3])
A4 = int(find_all[4])
A5 = int(find_all[5])

B0 = int(find_all[6])
B1 = int(find_all[7])
B2 = int(find_all[8])
B3 = int(find_all[9])
B4 = int(find_all[10])
B5 = int(find_all[11])

C0 = int(find_all[12])
C1 = int(find_all[13])
C2 = int(find_all[14])
C3 = int(find_all[15])
C4 = int(find_all[16])
C5 = int(find_all[17])

D0 = int(find_all[18])
D1 = int(find_all[19])
D2 = int(find_all[20])
D3 = int(find_all[21])
D4 = int(find_all[22])
D5 = int(find_all[23])

E0 = int(find_all[24])
E1 = int(find_all[25])
E2 = int(find_all[26])
E3 = int(find_all[27])
E4 = int(find_all[28])
E5 = int(find_all[29])

F0 = int(find_all[30])
F1 = int(find_all[31])
F2 = int(find_all[32])
F3 = int(find_all[33])
F4 = int(find_all[34])
F5 = int(find_all[35])

G0 = int(find_all[36])
G1 = int(find_all[37])
G2 = int(find_all[38])
G3 = int(find_all[39])
G4 = int(find_all[40])
G5 = int(find_all[41])

H0 = int(find_all[42])
H1 = int(find_all[43])
H2 = int(find_all[44])
H3 = int(find_all[45])
H4 = int(find_all[46])
H5 = int(find_all[47])


print(E0, end=" ")
print(E1, end=" ")
print(E2, end=" ")
print(E3, end=" ")
print(E4, end=" ")
print(E5, end=" ")

img = Image.new('RGB', (640, 480), color = (255, 255, 255))

Drawer = ImageDraw.Draw(img)
Drawer.rectangle((0,0,80,80), fill=(A0,A0,A0), outline=None)
Drawer.rectangle((0,80,80,160), fill=(A1,A1,A1), outline=None)
Drawer.rectangle((0,160,80,240), fill=(A2,A2,A2), outline=None)
Drawer.rectangle((0,240,80,320), fill=(A3,A3,A3), outline=None)
Drawer.rectangle((0,320,80,400), fill=(A4,A4,A4), outline=None)
Drawer.rectangle((0,400,80,480), fill=(A5,A5,A5), outline=None)

Drawer.rectangle((80,0,160,80), fill=(B0,B0,B0), outline=None)
Drawer.rectangle((80,80,160,160), fill=(B1,B1,B1), outline=None)
Drawer.rectangle((80,160,160,240), fill=(B2,B2,B2), outline=None)
Drawer.rectangle((80,240,160,320), fill=(B3,B3,B3), outline=None)
Drawer.rectangle((80,320,160,400), fill=(B4,B4,B4), outline=None)
Drawer.rectangle((80,400,160,480), fill=(B5,B5,B5), outline=None)

Drawer.rectangle((160,0,240,80), fill=(C0,C0,C0), outline=None)
Drawer.rectangle((160,80,240,160), fill=(C1,C1,C1), outline=None)
Drawer.rectangle((160,160,240,240), fill=(C2,C2,C2), outline=None)
Drawer.rectangle((160,240,240,320), fill=(C3,C3,C3), outline=None)
Drawer.rectangle((160,320,240,400), fill=(C4,C4,C4), outline=None)
Drawer.rectangle((160,400,240,480), fill=(C5,C5,C5), outline=None)

Drawer.rectangle((240,0,320,80), fill=(D0,D0,D0), outline=None)
Drawer.rectangle((240,80,320,160), fill=(D1,D1,D1), outline=None)
Drawer.rectangle((240,160,320,240), fill=(D2,D2,D2), outline=None)
Drawer.rectangle((240,240,320,320), fill=(D3,D3,D3), outline=None)
Drawer.rectangle((240,320,320,400), fill=(D4,D4,D4), outline=None)
Drawer.rectangle((240,400,320,480), fill=(D5,D5,D5), outline=None)


Drawer.rectangle((320,0,400,80), fill=(E0,E0,E0), outline=None)
Drawer.rectangle((320,80,400,160), fill=(E1,E1,E1), outline=None)
Drawer.rectangle((320,160,400,240), fill=(E2,E2,E2), outline=None)
Drawer.rectangle((320,240,400,320), fill=(E3,E3,E3), outline=None)
Drawer.rectangle((320,320,400,400), fill=(E4,E4,E4), outline=None)
Drawer.rectangle((320,400,400,480), fill=(E5,E5,E5), outline=None)

Drawer.rectangle((400,0,480,80), fill=(F0,F0,F0), outline=None)
Drawer.rectangle((400,80,480,160), fill=(F1,F1,F1), outline=None)
Drawer.rectangle((400,160,480,240), fill=(F2,F2,F2), outline=None)
Drawer.rectangle((400,240,480,320), fill=(F3,F3,F3), outline=None)
Drawer.rectangle((400,320,480,400), fill=(F4,F4,F4), outline=None)
Drawer.rectangle((400,400,480,480), fill=(F5,F5,F5), outline=None)

Drawer.rectangle((480,0,560,80), fill=(G0,G0,G0), outline=None)
Drawer.rectangle((480,80,560,160), fill=(G1,G1,G1), outline=None)
Drawer.rectangle((480,160,560,240), fill=(G2,G2,G2), outline=None)
Drawer.rectangle((480,240,560,320), fill=(G3,G3,G3), outline=None)
Drawer.rectangle((480,320,560,400), fill=(G4,G4,G4), outline=None)
Drawer.rectangle((480,400,560,480), fill=(G5,G5,G5), outline=None)

Drawer.rectangle((560,0,640,80), fill=(H0,H0,H0), outline=None)
Drawer.rectangle((560,80,640,160), fill=(H1,H1,H1), outline=None)
Drawer.rectangle((560,160,640,240), fill=(H2,H2,H2), outline=None)
Drawer.rectangle((560,240,640,320), fill=(H3,H3,H3), outline=None)
Drawer.rectangle((560,320,640,400), fill=(H4,H4,H4), outline=None)
Drawer.rectangle((560,400,640,480), fill=(H5,H5,H5), outline=None)
img.save('pil_color.png')
    