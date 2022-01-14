from tkinter import *
from colour import Color
from suntime import Sun
import geocoder
import screen_brightness_control as sbc
import time

ws = Tk()
ws.title('PythonGuides')
ws.geometry('10000x10000')
ws.config(bg='black')

time_lbl = Label(
    ws,
    text=time.strftime( "%d/%m/%Y %A %H:%M:%S"),
    font=(21),
    )

time_lbl.pack(expand=True)
ws.update()

black_to_red = list(Color("black").range_to("#e05151",10000))
red_to_orange= list(Color("#e05151").range_to("#de9921",10000))
orange_to_blue = list(Color("#de9921").range_to("#5a9fd1",10000))
i =0 
sbc.set_brightness(0)

g = geocoder.ip('me')
lat = g.latlng[0]
lng = g.latlng[1]
sun = Sun(lat,lng)
sunrise_time = (sun.get_sunrise_time().astimezone().strftime('%H:%M'))
curr_time = (time.strftime('%H:%M'))

while curr_time != sunrise_time:
    print("")
    
for i in range(100):
    time.sleep(.5)
    sbc.set_brightness(i)

while True:
    time.sleep(.5)
    time_text=time.strftime("%d/%m/%Y %A %H:%M:%S")
    time_lbl.config(text=time_text)
    ws.config(bg = black_to_red[i])
    i = i + 1
    if i > 9999:
        i = 0
        break
    ws.update()

while True:
    time.sleep(.5)
    time_text=time.strftime("%d/%m/%Y %A %H:%M:%S")
    time_lbl.config(text=time_text)
    ws.config(bg = red_to_orange[i])
    i = i + 1
    if i > 9999:
        i = 0
        break
    ws.update()

while True:
    time.sleep(.5)
    time_text=time.strftime("%d/%m/%Y %A %H:%M:%S")
    time_lbl.config(text=time_text)
    ws.config(bg = orange_to_blue[i])
    i = i + 1
    if i > 9999:
        i = 0
        break
    ws.update()

while True:
    time_text=time.strftime("%d/%m/%Y %A %H:%M:%S")
    time_lbl.config(text=time_text)
    ws.update()
    
ws.mainloop()
