#!/usr/bin/env python
##############################################################
####      Inscriptions.py                                 ####
####      Author      : satoki.btc                        ####
####      Date        : 22/02/2023                        ####
####      Description : iOS widget retrieving latest      ####
####                    Bitcoin inscription number.       ####
##############################################################
import requests
import widgets as wd
from datetime import datetime
def ord():
    def re(u):return (requests.get(u)).text
    def x(s,s1,s2):
        o,i1,i2='',s.index(s1),s.index(s2)#index
        for idx in range(i1+len(s1)+1,i2):o=o+s[idx]#elem
        return o
    u="https://ordinals.com"
    r=(re(u))#response
    b,i=x(r,"start","reversed"),x(r,"inscription","><i")#block,ord
    r,i='',x((re(u+"/inscription/"+i)),"1>Inscription","</h1")#ord_id
    return b,i
widget = wd.Widget()
b,i=ord()
b,i,t=wd.Text("Block: "+b),wd.Text("Ordinal: "+i),wd.Text("Last Update: "+(datetime.now()).strftime("%H:%M:%S"))
t.font=wd.Font.system_font_of_size(12)
layouts = [widget.small_layout]
for layout in layouts:
    layout.add_vertical_spacer()
    layout.add_row([b])
    layout.add_vertical_spacer()
    layout.add_row([i])
    layout.add_vertical_spacer()
    layout.add_row([t])
    layout.add_vertical_spacer()
wd.save_widget(widget, "Bitcoin Ordinals")
