from tkinter import *
import time
from time import strftime
from tkinter.ttk import *

import requests
import json

#Screen Size or Screen Resolution
sCreen='320x240'

#Background Colour
bkg = "blue"

#Text Colour
frg = "white"

#API ID from Openweathermap.org : Register to get a free API from openweathermap.org
oWapi='INSERT_YOUR_API_KEY_HERE'
#Enter your City as per the format from Openweathermap.org
cIty="Dubai,AE"
#Choose your units. Change the C to F as required in Line 41
uNits="metric"
# Line 36 concatenates the date form the FULL_URL for openweathermap.org

#For Sunrise and Moonrise get your free Api key from ipgeolocation.io
iPgeoAPI="INSERT_YOUR_API_KEY_HERE"
#Enter your Location's Latitude
iPgeoLAT="25.08960"
#Enter your locations's Longitude
iPgeolong="55.15290"




def getdata ():
        global tempcond1
        global handp1
        FULL_URL = "https://api.openweathermap.org/data/2.5/weather?q="+cIty+"&units="+uNits+"&appid="+oWapi
        response = requests.request("POST",FULL_URL)
        weather_data = (response.text)
        parsed = json.loads(weather_data)
        main= parsed['main']
        temp1 = main["temp"]
        tempc = str(temp1)+' C' #Change the C to F as required.

        pressure1 = main['pressure']
        pressurep = "P: "+str(pressure1)+' hpa'

        humid1 = main['humidity']
        humidh= "H:"+str(humid1)+' %'

        handp1 = pressurep +"         "+ humidh        

        weather = parsed['weather']
        condition1 = weather [0]['description']
        condition2 = str(condition1)

        tempcond1 = tempc + "  " + condition2
        root.after(600000,getdata)

def rise():
        global risedata1
        FULL_URL1 = 'https://api.ipgeolocation.io/astronomy?apiKey='+iPgeoAPI+'&lat='+iPgeoLAT+'&long='+iPgeolong
        response = requests.request('get',FULL_URL1)

        io_data = (response.text)
        parsed = json.loads(io_data)

        moonrise = parsed['moonrise']
        sunrise = parsed['sunrise']

        risedata1= ("Sunrise : " + sunrise + "     Mooonrise : " + moonrise )
        root.after(21600000,rise)




root = Tk() 
root.title('Clock')
root.geometry(sCreen)
root.configure(background=bkg)
root.attributes("-fullscreen", True) #This line makes the window full screen

getdata()
rise ()

def timedef():
    timevalue = strftime('%H:%M')
    timevalue1.config(text=timevalue)
    timevalue1.after(1000,timedef)

def datedef():
    datevalue = strftime('%b %d %Y')
    datevalue1.config(text=datevalue)
    datevalue1.after(1000,datedef)    
    
def handpdef():
        handp.config(text=handp1)
        handp.after(1000,handpdef)


def tempconddef():
        tempcond.config(text=tempcond1)
        tempcond.after(1000,tempconddef)       

def risedef():
        risedata.config(text=risedata1)
        risedata.after(1000,risedef)



timevalue1 = Label(root, font = ('calibri', 95, 'bold'),        #Time : Edit the Text size to suit your screen
                       background = bkg,
                       foreground = frg)
datevalue1 = Label(root, font = ('calibri', 30, 'normal'),      #Date :Edit the Text size to suit your screen
                       background = bkg,
                       foreground = frg)
handp = Label(root, font = ('calibri', 17, 'normal'),           #Humidity and Pressure : Edit the Text size to suit your screen
                       background = bkg,
                       foreground = frg)
tempcond = Label(root, font = ('calibri', 30, 'normal'),        #Temperature and Weather Conditions : Edit the Text size to suit your screen
                       background = bkg,
                       foreground = frg)

risedata = Label(root, font = ('calibri', 17, 'normal'),        #Sunrise and Moonrise data : Edit the Text size to suit your screen
                       background = bkg,
                       foreground = frg)	

risedata.pack()
datevalue1.pack()
timevalue1.pack()
tempcond.pack()
handp.pack()


timedef()
datedef()
handpdef()
tempconddef()
risedef()


root.mainloop()
