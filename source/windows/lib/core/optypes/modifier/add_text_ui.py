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

import os
import copy
from tkinter import *
from tkinter.constants import *
from tkinter import font
from PIL import Image, ImageTk, ImageFont, ImageDraw

from lib.SWIFT.modifierframe import ModifierFrame
from lib.SWIFT.tooltip import ToolTip
from lib.SWIFT.flatbutton import FlatButton
from lib.SWIFT.dropdownmenu import DropDownMenu
from lib.SWIFT.dropdownbutton import DropDownButton
from lib.SWIFT.colorchooserbutton import ColorChooserButton
from lib.SWIFT.colorchooser import ColorChooser, color_convert
from lib.core.render.renderer import render_photoimage, render_image_preview, show_image_preview
from lib.core.urcache.handler import handle_cache
from lib.core.edit.add_text import add_text


def modifier_addtext_ui(self):
    ## Panel
    self.AddText_ModifierPnl = ModifierFrame(self.Main_Modifier_Panel,
                                                text="Add Text", default=True,
                                                icon="lib/datafiles/icons/interface/AddTextModifier.png",
                                                closecommand=lambda:close_addtext_modifier(self))
    self.AddText_ModifierPnl.pack(fill=X)

    ## Modifier Button Frame
    Modifier_ButtonFrame = Frame(self.AddText_ModifierPnl.interior, bg="#969696",
                                 bd=1, relief=GROOVE)
    Modifier_ButtonFrame.pack(padx=2, pady=4, side=TOP, fill=X)

    Apply_Button = FlatButton(Modifier_ButtonFrame, text=' Apply ', width=10,
                              command=lambda: apply_add_text(self))
    Apply_Button.pack(padx=2, pady=2, side=LEFT)
    ToolTip(Apply_Button, "Apply add text modifier", wtype='FLATBUTTON')

    Refresh_Button = FlatButton(Modifier_ButtonFrame, text=' Refresh ', width=10, 
                              command=lambda: preview_add_text(self))
    Refresh_Button.pack(padx=2, pady=2, side=RIGHT)
    ToolTip(Refresh_Button, "Refresh preview of add text modifier", wtype='FLATBUTTON')

    ## create the main frame
    AddTextFont_Frame = Frame(self.AddText_ModifierPnl.interior, background="#969696")
    AddTextFont_Frame.pack()

    ## Title
    Title_Label = Label(AddTextFont_Frame, bg='#969696',fg='black',font=("Arial", 8),
                        text='Font',anchor=W)
    Title_Label.pack(side=TOP)

    ## icon
    self.IconSearch = ImageTk.PhotoImage(file="lib/SWIFT/bitmaps/Search.png")

    ## search frame
    SearchAddTextFont_Frame = Frame(AddTextFont_Frame, background="#969696")
    SearchAddTextFont_Frame.pack(fill=X)

    ## Search label
    SearchAddType_Label = Label(SearchAddTextFont_Frame, image=self.IconSearch,
                                background="#969696")
    SearchAddType_Label.pack(padx=2, pady=2, side=LEFT)
     
    ## Search entry
    self.SearchTextFont_Var = StringVar()
    self.SearchTextFont_Var.trace('w', lambda name, index, mode: update_font_listbox(self))
    self.SearchTextFont_Entry = Entry(SearchAddTextFont_Frame,
                                     textvariable=self.SearchTextFont_Var,
                                     selectbackground='#94afc9',
                                     bg='grey70',
                                     width=25,
                                     fg='black',
                                     font=("Calibri", 10),
                                     selectforeground='white',
                                     insertbackground='grey40')
    self.SearchTextFont_Entry.pack(padx=2, pady=2, side=LEFT, fill=X)
    ToolTip(self.SearchTextFont_Entry, 'Search for font')

    ## frame
    AddTextFontListbox_Frame = Frame(AddTextFont_Frame, bg='#969696')
    AddTextFontListbox_Frame.pack(padx=4, side=TOP, fill=X)

    ## scrollbar
    yScroll = Scrollbar(AddTextFontListbox_Frame, orient=VERTICAL)
    yScroll.pack(padx=1, pady=1, side=RIGHT, fill=Y)

    ## listbox
    self.AddTextFont_Listbox = Listbox(AddTextFontListbox_Frame,bg='grey40',
                                       fg='white',font=("Calibri", 10),
                                       highlightbackground='grey40',
                                       highlightcolor='grey40',
                                       width=24,height=6,
                                       relief=FLAT,activestyle='none',
                                       selectbackground='#94afc9',
                                       selectforeground='black',
                                       yscrollcommand=yScroll.set)
    self.AddTextFont_Listbox.pack(padx=2, pady=2, side=LEFT)

    yScroll['command'] = self.AddTextFont_Listbox.yview

    ## Font Preview label
    self.AddTextFontPreview_Canvas = Canvas(self.AddText_ModifierPnl.interior,
                                            width=194,
                                            height=40,
                                            highlightthickness=0,
                                            bd=1, relief=SOLID, background="grey")
    self.AddTextFontPreview_Canvas.pack(padx=2, pady=2, side=TOP)

    ## Title
    TextTitle_Label = Label(self.AddText_ModifierPnl.interior, bg='#969696',
                            fg='black',font=("Arial", 8),
                            text='Text',anchor=W)
    TextTitle_Label.pack(side=TOP)
    
    ## Text
    Text_Frame = Frame(self.AddText_ModifierPnl.interior, bg="#969696")
    Text_Frame.pack()

    ## Text Entry
    AddText_Entry_Scrollbar = Scrollbar(Text_Frame)
    self.AddText_Entry = Text(Text_Frame, width=22, height=3,
                              selectbackground='#94afc9',
                              bg='grey70', fg='black', 
                              selectforeground='white',
                              insertbackground='grey40',
                              font=("Arial", 9), wrap=NONE,
                              undo=True)
    AddText_Entry_Scrollbar.pack(side=RIGHT, fill=Y)
    self.AddText_Entry.pack(padx=0, pady=2, side=TOP)
    AddText_Entry_Scrollbar.config(command=self.AddText_Entry.yview)
    self.AddText_Entry.config(yscrollcommand=AddText_Entry_Scrollbar.set)
    ToolTip(self.AddText_Entry, "Text to add to image (single or multi-line text)") 

    ## Text Size
    TextSize_Frame = Frame(self.AddText_ModifierPnl.interior, bg="#969696")
    TextSize_Frame.pack(side=TOP)

    ## Add Text Size Label
    AddTextSize_lbl = Label(TextSize_Frame, text='Text Size:',
                            bg='#969696', font=("Arial", 8))
    AddTextSize_lbl.grid(row=0, column=0, padx=2, pady=2)

    ## Add Text Size scale
    self.TextSize_Scale = Scale(TextSize_Frame, length=120, orient=HORIZONTAL,
                                troughcolor='grey40', sliderlength=20,
                                showvalue=1, from_=400,
                                to=0, bg='#969696',
                                highlightthickness=0, sliderrelief=RIDGE,
                                activebackground='grey50', bd=1)
    self.TextSize_Scale.grid(row=0, column=1, padx=4, pady=2)
    self.TextSize_Scale.set(20)

    ## Text Font Alignment Frame
    TextFontAlignment_Frame = Frame(self.AddText_ModifierPnl.interior, bg="#969696")
    TextFontAlignment_Frame.pack(side=TOP, anchor=W)

    TextFontAlignment_Label = Label(TextFontAlignment_Frame, text='Text Alignment: ',
                                    bg="#969696")
    TextFontAlignment_Label.grid(row=0, column=0, padx=1, pady=4)
    
    self.TextFontAlignment_Dropdown = DropDownButton(TextFontAlignment_Frame, text='left')
    self.TextFontAlignment_Dropdown.grid(row=0, column=1, padx=1, pady=4)
    DropDownMenu(self.TextFontAlignment_Dropdown, chars=70,
                 options=[
                     'left',
                     'center',
                     'right'
                     ],
                 commands={
                     'left': None,
                     'center': None,
                     'right': None
                     },
                 flagtext="Text Alignment")

    ## Text Coords
    TextCoords_Frame = Frame(self.AddText_ModifierPnl.interior, bg="#969696")
    TextCoords_Frame.pack(fill=X)

    ## Add Text Coords X Label
    TextCoordsX_lbl = Label(TextCoords_Frame, text='X Position:',
                            bg="#969696", font=("Arial", 8))
    TextCoordsX_lbl.grid(row=0, column=0, padx=4, pady=2)

    ## Text Coords X scale
    self.TextCoordsX_Scale = Scale(TextCoords_Frame, length=120, orient=HORIZONTAL,
                                   troughcolor='grey40', sliderlength=20,
                                   showvalue=1, from_=self.data.image.size[0],
                                   to=0, bg='#969696',
                                   highlightthickness=0, sliderrelief=RIDGE,
                                   activebackground='grey50', bd=1)
    self.TextCoordsX_Scale.grid(row=0, column=1, padx=4, pady=2)

    ## Add Text Coords Y Label
    TextCoordsY_lbl = Label(TextCoords_Frame, text='Y Position:',
                            bg="#969696", font=("Arial", 8))
    TextCoordsY_lbl.grid(row=1, column=0, padx=4, pady=2)

    ## Text Coords Y scale
    self.TextCoordsY_Scale = Scale(TextCoords_Frame, length=120, orient=HORIZONTAL,
                                   troughcolor='grey40', sliderlength=20,
                                   showvalue=1, from_=self.data.image.size[1],
                                   to=0, bg='#969696',
                                   highlightthickness=0, sliderrelief=RIDGE,
                                   activebackground='grey50', bd=1)
    self.TextCoordsY_Scale.grid(row=1, column=1, padx=4, pady=2)

    ## Frame
    TextFontColor_Frame = Frame(self.AddText_ModifierPnl.interior, bg="#969696")
    TextFontColor_Frame.pack(side=TOP, anchor=W)

    ## Label
    TextFontColor_Label = Label(TextFontColor_Frame, text='Text Color: ',
                                bg="#969696")
    TextFontColor_Label.grid(row=0, column=0, padx=2, pady=4)
    
    ## ColorChooser
    self.TextFontColor_Button = ColorChooserButton(TextFontColor_Frame)
    self.TextFontColor_Button.grid(row=0, column=1, padx=2, pady=4)
    ColorChooser(self.TextFontColor_Button, top=True)
    ToolTip(self.TextFontColor_Button, "Text fill color")
    

    ## update the listbox according to the search 
    update_font_listbox(self)

    ## binding to get the option
    self.AddTextFont_Listbox.bind("<Double-Button-1>", lambda event: preview_font(self))

    ## refresh frame size
    self.AddText_ModifierPnl.update_width()

    ## update variable because the modifier now exists
    self.ADDTEXT_MOD_EXISTS = True

    
def update_font_listbox(self):
    ## setup to update list
    searched_var = self.SearchTextFont_Var.get()
    self.AddTextFont_Listbox.delete(0, END)

    ## add the options that match the search to the listbox
    for item in get_fonts(self):
        if searched_var.lower() in item.lower():
             self.AddTextFont_Listbox.insert(END, item)


def preview_add_text(self):
    ## Get the current selected font
    selectedfont = self.AddTextFont_Listbox.get(ACTIVE)
    Font = ImageFont.truetype("C:\\Windows\\Fonts\\{}".format(selectedfont),
                              int(self.TextSize_Scale.get()))

    ## Add text
    self.data.previewimage = add_text(self, self.data.image.copy(),
                                      self.TextCoordsX_Scale.get(),
                                      self.TextCoordsY_Scale.get(),
                                      self.AddText_Entry.get(1.0, END),
                                      Font, color_convert(self, str(self.TextFontColor_Button.cget("text"))),
                                      alignment=self.TextFontAlignment_Dropdown.cget("text"))
    ## In order to preserve the text scaling in the preview, we
    ## add the text to the copy of the original-sized image and then
    ## resize the final image
    render_image_preview(self, self.data.previewimage)
    show_image_preview(self, self.data.previewimage)

    
def preview_font(self):
    ## Get the current selection
    selectedfont = self.AddTextFont_Listbox.get(ACTIVE)

    ## Prepare
    if selectedfont == '':
        font = ImageFont.load_default()
    font = ImageFont.truetype("C:\\Windows\\Fonts\\{}".format(selectedfont), 16)
    FontImageBackground = Image.new("RGB", (198, 43), 'white')
    DrawText = ImageDraw.Draw(FontImageBackground)

    ## Draw the text
    DrawText.multiline_text((50, 16), 'ABCDEF abcdef', font=font, align='center',
                            fill=('black'))
    
    ## Create preview
    self.AddTextFontPreviewImage = ImageTk.PhotoImage(FontImageBackground)
    self.AddTextFontPreview_Canvas.create_image(0, 0, anchor=NW, image=self.AddTextFontPreviewImage)


def apply_add_text(self):
    ## Get the current selected font
    selectedfont = self.AddTextFont_Listbox.get(ACTIVE)
    Font = ImageFont.truetype("C:\\Windows\\Fonts\\{}".format(selectedfont),
                              int(self.TextSize_Scale.get()))
    ## Apply the effect
    self.data.image = add_text(self, self.data.image,
                               self.TextCoordsX_Scale.get(),
                               self.TextCoordsY_Scale.get(),
                               self.AddText_Entry.get(1.0, END),
                               Font, color_convert(self, str(self.TextFontColor_Button.cget("text"))),
                               alignment=self.TextFontAlignment_Dropdown.cget("text"))

    ## Show image
    render_photoimage(self)

    ## Cache
    self.UndoQueue.cache_append(self.data.image)
    handle_cache(self, self.data.image)

    ## Destroy the modifier
    close_addtext_modifier(self)

    ## Update statusbar
    self.StatusBar_lbl.configure(text='Applied add text modifier')

    
def get_fonts(self):
    fonts = []
    for f in os.listdir("C:\\Windows\\Fonts\\"):
        ext = os.path.splitext(f)[1]
        if ext.lower() in [".ttf"]:
            fonts.append(os.path.splitext(f)[0])

    return fonts


def close_addtext_modifier(self):
    ## destroy the modifier
    self.AddText_ModifierPnl.destroy()

    ## update variable because the modifier does not exist anymore
    self.ADDTEXT_MOD_EXISTS = False
