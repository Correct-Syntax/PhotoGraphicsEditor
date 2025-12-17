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

from tkinter import *
from PIL import Image, ImageTk


class ColorChooser(Frame):
    """ Color Chooser widget.

    Parameters
    ----------
    widget:
      The name of the ColorChooser Button to connect this widget with
    top:
      Whether to show the ColorChooser above or below the button widget
    command:
      Command to call every time a color is chosen
    """
    def __init__(self, widget, top=False, command=None):
        Frame.__init__(self)
         
        ## define variables to be used later
        self.widget = widget
        self.top = top
        self.command = command
        
        self.R = StringVar()
        self.G = StringVar()
        self.B = StringVar()
        
        self.Bar = 0
        self.Black = 0
        self.White = 1
        
        self.ReturnColor = '#FFFFFF'

        ## when the user presses the colorchooserbutton
        self.widget.bind("<ButtonPress>", self.enter)


    def enter(self, event=None):
        ## we want the widget to be state=NORMAL
        if self.widget.cget("state") == DISABLED:
            return
        self.showcolorchooser(self)


    def leave(self, event=None):
        self.hidecolorchooser()


    def showcolorchooser(self, event=None):
        x = y = 0
        ## calculate where to have the colorchooser appear
        if self.top == True:
            try:
                x, y, cx, cy = self.widget.bbox("insert")
            except:
                pass
            
            ## above the button widget
            x += self.widget.winfo_rootx() - 190
            y += self.widget.winfo_rooty() - 290

        else:
            try:
                x, y, cx, cy = self.widget.bbox("insert")
            except:
                pass

            ## below the button widget
            x += self.widget.winfo_rootx()
            y += self.widget.winfo_rooty() + 22
        
        ## Toplevel window
        self.clrtl = Toplevel(self.widget, bg='grey40')
        self.clrtl.geometry("250x290+%d+%d" % (x, y))
        self.clrtl.wm_overrideredirect(True)
        self.clrtl.attributes("-alpha", 0.9)

        ## Main Frame
        self.Main_Frame = Frame(self.clrtl, bg='grey40')
        self.Main_Frame.pack(padx=2, pady=2, side=TOP)
        
        ## Color Canvas Frame
        ColorCanvas_Frame = Frame(self.Main_Frame, bg='grey40')
        ColorCanvas_Frame.pack(padx=2, pady=2, side=TOP)

        ## Colorbar
        self.Image_Colorbar = Image.open("lib/SWIFT/bitmaps/colorbar.jpg").resize((25, 170))
        self.ColorbarImg = ImageTk.PhotoImage(self.Image_Colorbar)

        self.Colorbar_Canvas = Canvas(ColorCanvas_Frame, bg='grey40',
                                      highlightthickness=0)
        self.Colorbar_Canvas.grid(padx=4, row=1, column=2, sticky='e')
        self.Colorbar_Canvas.create_image(0, 95, image=self.ColorbarImg)
        self.Colorbar_Canvas.configure(width=10, height=190)

        ## Color Canvas
        self. Image_Color = Image.open("lib/SWIFT/bitmaps/colorbg.png").resize((200,200))
        self.Color_Img = ImageTk.PhotoImage(self.Image_Color)
        
        self.Color_Canvas = Canvas(ColorCanvas_Frame, bg='grey40',
                                   width=190, height=190, highlightthickness=0)
        self.Color_Canvas.grid(row=1, column=1, sticky='w')
        self.Color_Canvas.create_image(100, 100, image=self.Color_Img)
        
        self.colorchooser_cursor(0, 0)
        
        ## Color scale
        self.Color_Scale = Scale(ColorCanvas_Frame, length=190, orient=VERTICAL,
                                 troughcolor='grey40', sliderlength=20,
                                 showvalue=0, from_=300, to=0, bg='grey50',
                                 highlightthickness=0, sliderrelief=RIDGE,
                                 activebackground='grey50', bd=0,
                                 command=self.scale_update)
        self.Color_Scale.grid(padx=2, row=1, column=3, sticky='w')

        ## Color Values Frame
        ColorValues_Frame = Frame(self.Main_Frame, bg='grey40')
        ColorValues_Frame.pack(padx=2, pady=2, side=BOTTOM)

        ## Color Controls Frame
        ColorControls_Frame = Frame(ColorValues_Frame, bg='grey40')
        ColorControls_Frame.pack(padx=2, pady=2, side=LEFT)     

        ## Red value
        RedValue_lbl = Label(ColorControls_Frame, text='Red: ', bg='grey40')
        RedValue_lbl.grid(row=0, column=0, sticky='w')

        self.RedValue_Spinbox = Spinbox(ColorControls_Frame, from_=0, to=255,
                                        bg='white', fg='black', width=4,
                                        textvariable=self.R, selectbackground='#94afc9',
                                        selectforeground='black',
                                        command=self.entry_config)
        self.RedValue_Spinbox.grid(row=0, column=1, sticky='w')

        ## Green value
        GreenValue_lbl = Label(ColorControls_Frame, text='Green: ', bg='grey40')
        GreenValue_lbl.grid(row=1, column=0, sticky='w')

        self.GreenValue_Spinbox = Spinbox(ColorControls_Frame, from_=0, to=255,
                                          bg ='white', fg='black', width=4,
                                          textvariable=self.G, selectbackground='#94afc9',
                                          selectforeground='black',
                                          command=self.entry_config)
        self.GreenValue_Spinbox.grid(row=1, column=1, sticky='w')

        ## Blue value
        BlueValue_lbl = Label(ColorControls_Frame, text='Blue: ', bg='grey40')
        BlueValue_lbl.grid(row=2, column=0, sticky='w')

        self.BlueValue_Spinbox = Spinbox(ColorControls_Frame, from_=0, to=255,
                                         bg ='white', fg='black',width=4,
                                         textvariable=self.B, selectbackground='#94afc9',
                                         selectforeground='black',
                                         command=self.entry_config)
        self.BlueValue_Spinbox.grid(row=2, column=1, sticky='w')

        ## Color Info Frame
        ColorInfo_Frame = Frame(ColorValues_Frame, bg='grey40')
        ColorInfo_Frame.pack(padx=2, pady=2, side=RIGHT)

        ## Hexadecimal value
        Hexadecimal_lbl = Label(ColorInfo_Frame, text='Hex: ', bg='grey40')
        Hexadecimal_lbl.grid(row=0, column=0, sticky='w')

        self.HexadecimalValue_lbl = Label(ColorInfo_Frame, text='#FFFFFF', bg='grey40')
        self.HexadecimalValue_lbl.grid(row=0, column=1, sticky='w')

        ## Color Value
        ColorValue_lbl = Label(ColorInfo_Frame, text='Color: ', bg='grey40')
        ColorValue_lbl.grid(row=1, column=0, sticky='w')
        
        self.ColorValue_Canvas = Canvas(ColorInfo_Frame, width=50, height=20,
                           highlightthickness=0)
        self.ColorValue_Canvas.grid(row=1, column=1, sticky='w')

        ## Set values
        self.R.set('255')
        self.G.set('255')
        self.B.set('255')
        
        ## Bindings for the colorchooser
        self.clrtl.bind("<Return>", self.entry_config)
        self.Color_Canvas.bind("<Button-1>", self.change_color)
        self.Color_Canvas.bind("<B1-Motion>", self.change_color)
        
        ## destroy the colorchooser if the mouse pointer leaves the colorchooser
        self.Main_Frame.bind("<Leave>", self.leave)
        ## destroy the colorchooser if the colorchooserbutton is clicked
        self.widget.bind("<Button-1>", self.leave)

        
    def change_color(self, event):
        if 0 <= event.x <= 190 + 2 and 0 <= event.y <= 190 + 2:
            self.colorchooser_cursor(event.x, event.y)    
                
            self.White = round(event.x/190, 2) 
            self.Black = round(event.y/190, 2)
            
            self.change_val() 


    def change_val(self):
        r, g, b = self.pos_scale()
        
        ## 3 colors
        r_1 = round((255-r)*self.Black)+r
        g_1 = round((255-g)*self.Black)+g
        b_1  =round((255-b)*self.Black)+b
        
        ## 3 colors
        r_1= round(r_1*self.White)       
        g_1= round(g_1*self.White)       
        b_1= round(b_1*self.White)

        ## set the vars to be the updated value
        self.R.set(str(r_1))
        self.G.set(str(g_1))
        self.B.set(str(b_1))

        ## hex
        self.HexadecimalValue_lbl.configure(text='#%02x%02x%02x '.upper() % (r_1, g_1, b_1))
        self.ReturnColor = '#%02x%02x%02x '.upper() % (r_1, g_1, b_1)
        self.entry_config()

            
    def colorchooser_cursor(self, x, y):
        ## create the colorchooser cursor
        self.Color_Canvas.delete('cursor')
        self.Color_Canvas.create_line(x+2, y, x+7, y, width=2, fill='black', tag='cursor')
        self.Color_Canvas.create_line(x-2, y, x-7, y, width=2, fill='black', tag='cursor')
        self.Color_Canvas.create_line(x, y+2, x, y+7, width=2, fill='black', tag='cursor')
        self.Color_Canvas.create_line(x, y-2, x, y-7, width=2, fill='black', tag='cursor')


    def entry_config(self, event=None):
        if self.RedValue_Spinbox.get() == '' or 255 < int(self.RedValue_Spinbox.get()):
            self.R.set('255')
        if int(self.RedValue_Spinbox.get()) < 0:
            self.R.set('0')
        
        if self.GreenValue_Spinbox.get() == '' or 255 < int(self.GreenValue_Spinbox.get()):
            self.G.set('255')
        if int(self.GreenValue_Spinbox.get()) < 0:
            self.G.set('0')
            
        if self.BlueValue_Spinbox.get() == '' or 255 < int(self.BlueValue_Spinbox.get()):
            self.B.set('255')
        if int(self.BlueValue_Spinbox.get()) < 0:
            self.B.set('0')
            
        self.RedValue_Spinbox.configure(textvariable=self.R)
        self.GreenValue_Spinbox.configure(textvariable=self.G)
        self.BlueValue_Spinbox.configure(textvariable=self.B)
                
        ## Update color
        self.ColorValue_Canvas.create_rectangle(0, 0, 100, 30, fill= '#%02x%02x%02x' % (int(self.R.get()),int(self.G.get()),int(self.B.get())))


    def pos_scale(self):
        if self.Bar <= 50: 
            r = 255
            g = round((self.Bar)*255/50)
            b = 0
            
        elif self.Bar <= 100: 
            r = round(255-(self.Bar-50)*255/50)
            g = 255
            b = 0
        
        elif self.Bar <= 150: 
            r = 0
            g = 255
            b = round(((self.Bar-100)*255/50))
            
        elif self.Bar <= 200: 
            r = 0;
            g = round(255-(self.Bar-150)*255/50)
            b = 255
            
        elif self.Bar <= 250:
            r = round((self.Bar-200)*255/50)
            g = 0
            b = 255
            
        elif self.Bar <= 300: 
            r = 255
            g = 0
            b = round(255-(self.Bar-250)*255/50)
        
        self.Color_Canvas.config(bg='#%02x%02x%02x' % (r, g, b))
        
        return r, g, b


    def scale_update(self, x):
        self.Bar = int(x)
        self.Colorbar_Canvas.delete('cursor1')
        self.Colorbar_Canvas.create_line(-20, 180-self.Bar*170/300, 20,
                                         180-self.Bar*170/300, fill='black',
                                         width=2, tags='cursor1')
        
        self.change_val()


    def hidecolorchooser(self):
        try:
            ## Configure the values
            self.widget.configure(bg=self.ReturnColor, text=self.ReturnColor)

            ## Run a command, if one was specified
            if self.command != None:
                self.command()

            ## Unbind
            self.widget.unbind("<Button-1>")
            
            ## Destroy the colorchooser
            self.clrtl.destroy()

        ## If the colorchooser is interrupted somehow, we need to smoothly destroy
        ## the window. Otherwise, it hangs there and/or crashes the program, which
        ## creates a bad experience for the user.
        ## TODO: work out a better handling method for when the widget errors
        except:
            ## Default to white
            self.widget.configure(bg='#FFFFFF', text='#FFFFFF')

            ## Unbind
            self.widget.unbind("<Button-1>")
            
            ## Destroy the colorchooser
            self.clrtl.destroy()


def color_convert(widget, tkcolorstring):
    ## The color chooser returns an Tk color string, but PIL takes an RGB tuple.
    ## Therefore, we need to convert the Tk color string to a RGB tuple
    r, g, b = widget.winfo_rgb(tkcolorstring)
    return (round(r/256), round(g/256), round(b/256))
