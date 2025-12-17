## This code is Copyright (C) 2019 Noah Rahm
##
## This program is free software: you can redistribute it and/or modify it 
## under the terms of the GNU General Public License as published by 
## the Free Software Foundation; either version 3 of the License, 
## or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful, 
## but WITHOUT ANY WARRANTY; without even the implied warranty 
## of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License 
## along with this program. If not, see: http://www.gnu.org/licenses/
##
## Contributor(s): Noah Rahm

import random
from tkinter import *
from tkinter.constants import *
from tkinter import ttk
from PIL import ImageTk


def splashscreen_ui(self):
    self.Splashscreen_Window = Toplevel(self)
    x = self.winfo_screenwidth()-400
    y = self.winfo_screenheight()-460
    self.Splashscreen_Window.geometry('400x460+%d+%d' % (x/2, y/2))
    self.Splashscreen_Window.wm_overrideredirect(True)
    self.Splashscreen_Window.attributes("-alpha", 0.85)
    self.Splashscreen_Window.configure(bg='grey70')

    ## Logo
    Splashscreen_Canvas = Canvas(self.Splashscreen_Window, width=200, height=200,
                                 highlightthickness=0, bg='grey70')
    Splashscreen_Canvas.pack(side=TOP)

    self.ICON = PhotoImage(file='lib/datafiles/icons/program/Program_Logo.png') 
    Splashscreen_Canvas.create_image(0, 0, image=self.ICON, anchor=NW)
    
    ## Labels
    lbl1 = Label(self.Splashscreen_Window, text='PhotoGraphics Editor 1.1.0',
                 bg='grey70', font=("Georgia", 18))
    lbl1.pack(padx=4, pady=4)

    lbl2 = Label(self.Splashscreen_Window, text='''Free and open source image editing program
    _____________________________________''',
                 bg='grey70', font=("Georgia", 8))
    lbl2.pack(padx=4, pady=4)

    lbl3 = Label(self.Splashscreen_Window, text='''
    All glory and praise to Yahweh!
    
    {}'''.format(random_splashscreen_verse(self)), bg='grey70', font=("Arial", 9))
    lbl3.pack(padx=4, pady=4, side=TOP)

    ## Binding
    self.Splashscreen_Window.bind("<Button-1>", lambda event: close_splashscreen(self))


def close_splashscreen(self):
    """ Closes the splashscreen. """
    self.Splashscreen_Window.destroy()


def random_splashscreen_verse(self):
    """ Generates a random verse (or two) from the Bible to show on the
    splashscreen at startup. """
    Value = random.randrange(2)
    
    if Value == 0:
        RandomSplashscreenVerse =""" The humble He guides in justice, and the
humble He teaches His way.
-Psalms 25:9"""

    if Value == 1:
        RandomSplashscreenVerse =""" The generous soul will be made rich, and he
who waters will also be watered himself.
-Psalms 25:9"""

    if Value == 2:
        RandomSplashscreenVerse =""" You will keep him in perfect peace, whose
mind is stayed on You, because he trusts in You.
Trust in Yahweh forever, for in Yahweh
is everlasting strength.
-Isaiah 26:3-4"""

    return RandomSplashscreenVerse
