#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 27 09:23:48 2025

@author: ki4ujy
"""
#from sense_hat import SenseHat
from sense_emu import SenseHat
from flask import Flask, flash, redirect, Response, render_template, request
import time
import random
import math

app = Flask(__name__)
app.secret_key= "KI4UJY"
location_offset = 981.51

def generate_data(atmos_offset):
    #location_offset = 981.51
    
    counter = 0
    #run loop for 10 hours - each loop is one second
    #60 seconds in a min 60 min in an hour for
    #10 hours is 36000 seconds
    endcount = 36000
    
    sense=SenseHat()
    
    #raw_pressure1 = sense.get_pressure()
    #p = raw_pressure1 # utilze Node Red Java code 
    #print ("pressure ",raw_pressure1)
    #p = 965.51 #test pressure
    #pold = 981.51 # Nominal normal pressure for Tullahoma TN
    pold = atmos_offset
    #poffset = pold - p
    #pavg = pold
 
    
    
    B = [0, 0, 255]  # Blue
    G = [0, 255, 0]  # Green
    O = [255, 255, 255]  # White
    N = [0, 0, 0]  # Black
    R = [255, 0, 0]  # Red
    r = [255,0,0] #Red
    o = [255,127,0] #Orange
    y = [255,255,0] #yellow
    g = [0,255,0] #green
    b = [0,0,255]  #blue
    i = [75,0,130] #indigo
    v = [159,0,255] #violet
    e = [0,0,0] #Nore
    
    # Initialize corner colors
    TL = e
    TR = e
    BL = e
    BR = e
    
    def my_ReadCLock():
        clockhand = sense.get_pixels()
        TL = clockhand[0]
        TR = clockhand[7]
        BL = clockhand[56]
        BR = clockhand[63]
    
    TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, e ,e ,e ,e ,e, e, e
    aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = e, e ,e ,e ,e ,e, e, e
    bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = e, e ,e ,e ,e ,e, e, e
    cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = e, e ,e ,e ,e ,e, e, e
    dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = e, e ,e ,e ,e ,e, e, e
    eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = e, e ,e ,e ,e ,e, e, e
    fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = e, e ,e ,e ,e ,e, e, e
    BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,e ,e ,e ,e, e, e
    
    
    blank_led = [
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    ] 
    
    #location_offset = 981.51
    # loop begin

    
    my_ReadCLock()
    #print("top left", TL)
    #print("top right ", TR)
    #print("BOTTOM left", BL)
    #print("BOTTOM right", BR)
    pavg = sense.get_pressure()
    
    #pold = 981.51 # Nominal normal pressure for Tullahoma TN
    
    while (counter <= endcount):
        p=989.0 
        counter += 1
        value = random.randint(1, 100)
        
        raw_pressure1 = sense.get_pressure()
        humidity = round(sense.get_humidity(),2)
        
        p = raw_pressure1 # utilze Node Red Java code 
        #print ("pressure ",raw_pressure1)
        #p = 965.51 #test pressure
    
        #joy_dir = sense.stick.get_events()
        #[InputEvent(timestamp=1767026754.440438, 
        #direction='down', action='pressed'), 
        #InputEvent(timestamp=1767026754.626177, 
        #direction='down', action='released')]
        
        #print(joy_dir.direction)
        ##message_text = joy_dir
    
        pold = location_offset
        poffset = pold - p
        pavg = pold
        if counter <5: # resets the average long term on power up
            pavg_over_time = p
        pavg_over_time = (p*1 + pavg_over_time*999)/1000
    
    
        #  begin delta range calculation -4 to +4)
        pdelta = -0;
        if (poffset <= -1.0):
            pdelta = -1
            # print ("pressure range ",pdelta)
        if (poffset >= 1.0):
            pdelta = 1
            # print ("pressure range ",pdelta)
        if (poffset <= -2.0):
            pdelta = -2
            # print ("pressure range ",pdelta)
        if (poffset >= 2.0):
            pdelta = 2
            # print ("pressure range ",pdelta)
        if (poffset <= -3.0):
            pdelta = -3
            # print ("pressure range ",pdelta)
        if (poffset >= 3.0):
            pdelta = 3
            # print ("pressure range ",pdelta)
        if (poffset <= -4.0):
            pdelta = -4
            # print ("pressure range ",pdelta)
        if (poffset >= 4.0):
            pdelta = 4
            # print ("pressure range ",pdelta)
        
        #message text build
        
        message_text="trending"
        if (p <= pavg_over_time):
            message_text="falling"
        if (p > pavg_over_time):
            message_text="rising"
            
        
        
        
        ptrend = 0
        if (p < pavg):
            ptrend = -1
           
        if (p != pavg):
            ptrend = 1
        if (p < (pavg-5.0)):
            ptrend = 2
        if (p < (pavg-10.0)):
            ptrend = 3
        if (p < (pavg-15.0)):
            ptrend = 4
        if (p > pavg):
            ptrend = -1
            
      
        #print ("pressure delta",pdelta)    
        #print ("pressure trend ",ptrend)
    
        B = [0, 0, 255]  # Blue
        G = [0, 255, 0]  # Green
        O = [255, 255, 255]  # White
        N = [0, 0, 0]  # Black
        R = [255, 0, 0]  # Red
        r = [255,0,0] #Red
        o = [255,127,0] #Orange
        y = [255,255,0] #yellow
        g = [0,255,0] #green
        b = [0,0,255]  #blue
        i = [75,0,130] #indigo
        v = [159,0,255] #violet
        e = [0,0,0] #Nore
    
        def my_Blank():
            blank_led = [
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            e, e, e, e, e, e, e, e,
            ] 
            sense.set_pixels(blank_led)
        
        
    
        #def my_Nominal():
            # code for nominal range goes here
        #print("ptrend test", ptrend, "pdelta test", pdelta)    
    
        if ptrend ==4 and pdelta == 4:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, R ,R ,R ,R ,R, e, e
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = R, R ,R ,R ,R ,R, R, e
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = R, R ,R ,R ,R ,R, R, e
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = R, R ,R ,R ,R ,R, R, e
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = R, R ,R ,R ,R ,R, R, e
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = R, R ,R ,R ,R ,R, R, e
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = R, R ,R ,R ,R ,R, R, e
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, R ,R ,R ,R ,R, e, e
            #print("pressure trend nominal") 
    
        if ptrend ==3 and pdelta == 4:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, e ,R ,R ,R ,e, e, e
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = e, e ,R ,R ,R ,e, e, e
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = e, e ,R ,R ,R ,e, e, e
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = e, e ,R ,R ,R ,e, e, e
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = e, e ,R ,R ,R ,e, e, e
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = e, R ,R ,R ,R ,R, e, e
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = e, e ,R ,R ,R ,e, e, e
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,e ,R ,e ,e, e, e
            #print("pressure trend nominal") 
    
        if ptrend ==2 and pdelta == 4:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, e ,y ,y ,y ,e, e, e
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = e, e ,y ,y ,y ,e, e, e
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = e, e ,y ,y ,y ,e, e, e
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = e, e ,y ,y ,y ,e, e, e
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = e, e ,y ,y ,y ,e, e, e
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = e, y ,y ,y ,y ,y, e, e
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = e, e ,y ,y ,y ,e, e, e
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,e ,y ,e ,e, e, e
            #print("pressure trend nominal") 
    
    
        if ptrend ==1 and pdelta == 4:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, e ,G ,G ,G ,e, e, e
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = e, e ,G ,G ,G ,e, e, e
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = e, e ,G ,G ,G ,e, e, e
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = e, e ,G ,G ,G ,e, e, e
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = e, e ,G ,G ,G ,e, e, e
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = e, G ,G ,G ,G ,G, e, e
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = e, e ,G ,G ,G ,e, e, e
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,e ,G ,e ,e, e, e
            #print("pressure trend nominal") 
    
    
        if ptrend ==1 and pdelta == 3:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, e ,e ,e ,e ,e, e, e
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = e, e ,e ,e ,e ,e, e, e
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = e, e ,e ,e ,e ,e, e, e
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = e, e ,e ,e ,e ,e, e, e
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = e, e ,e ,e ,e ,e, e, e
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = e, e ,e ,e ,e ,e, e, e
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = e, B ,e ,B ,e ,B, e, B
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,B ,e ,B ,e, B, e
            #print("pressure trend nominal") 
        if ptrend ==1 and pdelta == 2:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, e ,e ,e ,e ,e, e, e
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = e, e ,e ,e ,e ,e, e, e
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = e, e ,e ,e ,e ,e, e, e
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = e, e ,e ,e ,e ,e, e, e
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = e, e ,e ,e ,e ,e, e, e
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = e, B ,e ,B ,e ,B, e, B
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = B, e ,B ,e ,B ,e, B, e
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,e ,e ,e ,e, e, e
            #print("pressure trend nominal") 
    
    
    
    
        if ptrend ==1 and pdelta == 1:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, e ,e ,e ,e ,e, e, e
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = e, e ,e ,e ,e ,e, e, e
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = e, e ,e ,e ,e ,e, e, e
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = e, B ,e ,B ,e ,B, e, B
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = B, e ,B ,e ,B ,e, B, e
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = e, e ,e ,e ,e ,e, e, e
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = e, e ,e ,e ,e ,e, e, e
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,e ,e ,e ,e, e, e
            #print("pressure trend nominal")
        if ptrend ==0 and pdelta == 0:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, e ,e ,e ,e ,e, e, e
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = e, e ,e ,e ,e ,e, e, e
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = e, B ,e ,B ,e ,B, e, B
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = B, e ,B ,e ,B ,e, B, e
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = e, e ,e ,e ,e ,e, e, e
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = e, e ,e ,e ,e ,e, e, e
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = e, e ,e ,e ,e ,e, e, e
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,e ,e ,e ,e, e, e
            #print("pressure trend nominal")
    
    
        if ptrend ==-1 and pdelta == 0:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, e ,e ,e ,e ,e, e, e
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = e, e ,e ,e ,e ,e, e, e
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = e, e ,e ,e ,e ,e, e, e
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = e, B ,e ,B ,e ,B, e, B
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = B, e ,B ,e ,B ,e, B, e
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = e, e ,e ,e ,e ,e, e, e
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = e, e ,e ,e ,e ,e, e, e
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,e ,e ,e ,e, e, e
            #print("pressure trend nominal")
            
        if ptrend ==-1 and pdelta == 1:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, e ,e ,e ,e ,e, e, e
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = e, e ,e ,e ,e ,e, e, e
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = e, e ,e ,e ,e ,e, e, e
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = e, e ,e ,e ,e ,e, e, e
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = e, B ,e ,B ,e ,B, e, B
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = B, e ,B ,e ,B ,e, B, e
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = e, e ,e ,e ,e ,e, e, e
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,e ,e ,e ,e, e, e
            #print("pressure trend nominal")    
       
        if ptrend ==-1 and pdelta == -1:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, e ,e ,e ,e ,e, e, e
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = e, B ,e ,B ,e ,B, e, B
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = B, e ,B ,e ,B ,e, B, e
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = e, e ,e ,e ,e ,e, e, e
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = e, e ,e ,e ,e ,e, e, e
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = e, e ,e ,e ,e ,e, e, e
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = e, e ,e ,e ,e ,e, e, e
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,e ,e ,e ,e, e, e
            #print("pressure trend nominal")        
        if ptrend ==-1 and pdelta == -2:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, B ,e ,B ,e ,B, e, B
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = B, e ,B ,e ,B ,e, B, e
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = e, e ,e ,e ,e ,e, e, e
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = e, e ,e ,e ,e ,e, e, e
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = e, e ,e ,e ,e ,e, e, e
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = e, e ,e ,e ,e ,e, e, e
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = e, e ,e ,e ,e ,e, e, e
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,e ,e ,e ,e, e, e
            #print("pressure trend nominal")       
        if ptrend ==-1 and pdelta <= -3:
            TR0, TR1, TR2, TR3, TR4, TR5, TR6, TR7 = e, e ,e ,O ,e ,e, e, e
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7 = e, e ,O ,O ,O ,e, e, e
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7 = e, O ,O ,O ,O ,O, e, e
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7 = e, e ,B ,B ,B ,e, e, e
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7 = e, e ,B ,B ,B ,e, e, e
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7 = e, e ,B ,B ,B ,e, e, e
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7 = e, e ,B ,B ,B ,e, e, e
            BR0, BR1, BR2, BR3, BR4, BR5, BR6, BR7 = e, e ,B ,B ,B ,e, e, e
            #print("pressure trend nominal")       
        
    
        def my_CLock():
            clockhand = sense.get_pixels()
            TL = clockhand[0]
            TR = clockhand[7]
            BL = clockhand[56]
            BR = clockhand[63]
            if TL == G:
                TL = e
                TR = G
                BL = e
                BR = e
            elif TR == G:
                TL = e
                TR = e
                BL = G
                BR = e
            elif BR == G:
                TL = e
                TR = e
                BL = G
                BR = e
            elif BL == G:
                TL = G
                TR = e
                BL = e
                BR = e
            elif TL and TR and BR and BR == e:
                TL = G
                TR = e
                BL = e
                BR = e
                #print(G)
          
    
        bluetooth_logo = [
        R, e, N, N, y, N, N, g,
        e, e, O, i, O, O, O, O,
        O, O, O, i, i, O, O, O,
        O, B, O, B, O, B, O, O,
        O, O, y, B, B, O, O, O,
        O, B, O, B, O, B, O, O,
        O, O, O, B, B, O, O, O,
        O, O, O, B, O, O, O, O
        ] 
        #sense.set_pixels(bluetooth_logo)
        
    
        clockhand = sense.get_pixels()
        #print("led array",clockhand)
        TL = clockhand[0]
        #print("TL", TL,"G", G)
        TR = clockhand[7]
        BL = clockhand[56]
        BR = clockhand[63]
        if TL == [0, 252, 0]:
            TL = e
            TR = G
            BL = e
            BR = e
        elif TR == [0, 252, 0]:
            TL = e
            TR = e
            BL = e
            BR = G
        elif BR == [0, 252, 0]:
            TL = e
            TR = e
            BL = G
            BR = e
        elif BL == [0, 252, 0]:
            TL = G
            TR = e
            BL = e
            BR = e
        elif TL and TR and BR and BR == e:
            TL = G
            TR = e
            BL = e
            BR = e
            #print(G)
                
    
        #print (TL)
        senseHatScreen = [
            TL, TR1, TR2, TR3, TR4, TR5, TR6, TR,
            aR0, aR1, aR2, aR3, aR4, aR5, aR6, aR7,
            bR0, bR1, bR2, bR3, bR4, bR5, bR6, bR7,
            cR0, cR1, cR2, cR3, cR4, cR5, cR6, cR7,
            dR0, dR1, dR2, dR3, dR4, dR5, dR6, dR7,
            eR0, eR1, eR2, eR3, eR4, eR5, eR6, eR7,
            fR0, fR1, fR2, fR3, fR4, fR5, fR6, fR7,
            BL, BR1, BR2, BR3, BR4, BR5, BR6, BR
            ] 
            
        sense.set_pixels(senseHatScreen)
        #display_p = round(p,2)
        local_pressure = round(p * 0.03937,2) # CONVERT TO mmHg
        pressure_psi = round(p *0.0145037738,2) # convert to psia
        current_offset = pold
        counter =counter + 1
        # SSE format: "data: <message>\n\n"
        #message_text = "steady"
        yield f"data: Barometric Pressure ({message_text}): {local_pressure} inHg; {pressure_psi} psi, Offset {current_offset} millibar ; Humidity: {humidity}\n\n"
        time.sleep(1)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream")
def stream():
    
    return Response(generate_data(location_offset), mimetype="text/event-stream")

@app.route("/offset", methods=["GET", "POST"])
def offset():
    global location_offset
    if request.method =="POST":
        web_offset = request.form.get("Offset")
        if not web_offset:
           return render_template("index.html")
  
        location_offset = float(web_offset)
        #print("Pressure Offset Supplied by User: ",pressure_offset)
        #generate_data(pressure_offset)
        #flash(f"Barometric Pressure Offset Updated to : {pressure_offset} barr!")
        generate_data(location_offset)
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

