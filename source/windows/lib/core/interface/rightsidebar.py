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
from tkinter.constants import *
from tkinter import ttk

from lib.SWIFT.tabbednotebook import Notebook
from lib.SWIFT.addtypeframe import AddTypeFrame
from lib.core.optypes.modifier.modifier_validator import validate_modifier


def right_sidebar_ui(self):
    ## Properties panel
    self.BaseProperties_Panel = Frame(self, background="grey35")
    self.BaseProperties_Panel.pack(fill=BOTH, side=RIGHT)

    self.Sidebar_Tabs = Notebook(self.BaseProperties_Panel)

    self.Property_Tab = Frame(self.Sidebar_Tabs(), bg="grey80", bd=2, relief=SUNKEN)
    self.Modifier_Tab = Frame(self.Sidebar_Tabs(), bg="grey80", bd=2, relief=SUNKEN)

    #######################
    ## Property type tab ##
    #######################
    self.Sidebar_Property_Tabs = Notebook(self.Property_Tab)

    # File
    self.PropertyTab_File = Frame(self.Sidebar_Property_Tabs(), background="#969696")

    self.FilePropertiesPanelCanvas = Canvas(self.PropertyTab_File, highlightthickness=0,
                                            width=220, height=1200, bg="#969696")
    self.File_Properties_Panel = Frame(self.PropertyTab_File)
    FilePropertiesPanelScrollbar = Scrollbar(self.PropertyTab_File, orient=VERTICAL,
                                             command=self.FilePropertiesPanelCanvas.yview)
    self.FilePropertiesPanelCanvas.configure(yscrollcommand=FilePropertiesPanelScrollbar.set)
    FilePropertiesPanelScrollbar.pack(side=RIGHT, fill=Y)
    self.FilePropertiesPanelCanvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    self.FilePropertiesPanelCanvas.create_window((0, 0), window=self.File_Properties_Panel, anchor=N)

    self.File_Properties_Panel.bind("<Configure>", lambda event: config_filepropertiesframe(self))

    # Edit
    self.PropertyTab_Edit = Frame(self.Sidebar_Property_Tabs(), background="#969696")

    self.EditPropertiesPanelCanvas = Canvas(self.PropertyTab_Edit, highlightthickness=0,
                                            width=220, height=1200, bg="#969696")
    self.Edit_Properties_Panel = Frame(self.PropertyTab_Edit)
    EditPropertiesPanelScrollbar = Scrollbar(self.PropertyTab_Edit, orient=VERTICAL,
                                             command=self.EditPropertiesPanelCanvas.yview)
    self.EditPropertiesPanelCanvas.configure(yscrollcommand=EditPropertiesPanelScrollbar.set)
    EditPropertiesPanelScrollbar.pack(side=RIGHT, fill=Y)
    self.EditPropertiesPanelCanvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    self.EditPropertiesPanelCanvas.create_window((0, 0), window=self.Edit_Properties_Panel, anchor=N)

    self.Edit_Properties_Panel.bind("<Configure>", lambda event: config_editpropertiesframe(self))

    # Create
    self.PropertyTab_Create = Frame(self.Sidebar_Property_Tabs(), background="#969696")

    self.CreatePropertiesPanelCanvas = Canvas(self.PropertyTab_Create, highlightthickness=0,
                                              width=220, height=1200, bg="#969696")
    self.Create_Properties_Panel = Frame(self.PropertyTab_Create)
    CreatePropertiesPanelScrollbar = Scrollbar(self.PropertyTab_Create, orient=VERTICAL,
                                             command=self.CreatePropertiesPanelCanvas.yview)
    self.CreatePropertiesPanelCanvas.configure(yscrollcommand=CreatePropertiesPanelScrollbar.set)
    CreatePropertiesPanelScrollbar.pack(side=RIGHT, fill=Y)
    self.CreatePropertiesPanelCanvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    self.CreatePropertiesPanelCanvas.create_window((0, 0), window=self.Create_Properties_Panel, anchor=N)

    self.Create_Properties_Panel.bind("<Configure>", lambda event: config_createpropertiesframe(self))

    #######################
    ## Modifier type tab ##
    #######################
    self.MainModifierPanelCanvas = Canvas(self.Modifier_Tab, highlightthickness=0,
                                          width=220, height=1200, bg="#969696")
    self.Main_Modifier_Panel = Frame(self.Modifier_Tab)
    MainModifierPanelScrollbar = Scrollbar(self.Modifier_Tab, orient=VERTICAL,
                                           command=self.MainModifierPanelCanvas.yview)
    self.MainModifierPanelCanvas.configure(yscrollcommand=MainModifierPanelScrollbar.set)
    MainModifierPanelScrollbar.pack(side=RIGHT, fill=Y)
    self.MainModifierPanelCanvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    self.MainModifierPanelCanvas.create_window((0, 0), window=self.Main_Modifier_Panel, anchor=N)

    self.Main_Modifier_Panel.bind("<Configure>", lambda event: config_modifierframe(self))

    ## add the tabs for the inside tabs
    self.Sidebar_Property_Tabs.add_tab(self.PropertyTab_File, title=' File ')
    self.Sidebar_Property_Tabs.add_tab(self.PropertyTab_Edit, title=' Edit ')
    self.Sidebar_Property_Tabs.add_tab(self.PropertyTab_Create, title=' Create ')

    ## add the tabs for the main tabs
    self.Sidebar_Tabs.add_tab(self.Property_Tab, title=' Property  ', image=self.PROPERTY_ICON)
    self.Sidebar_Tabs.add_tab(self.Modifier_Tab, title=' Modifier  ', image=self.MODIFIER_ICON)

    ## spacer labels
    FileProperty_Spacer = Label(self.File_Properties_Panel, text='', width=27, background="#969696")
    FileProperty_Spacer.pack()
    EditProperty_Spacer = Label(self.Edit_Properties_Panel, text='', width=27, background="#969696")
    EditProperty_Spacer.pack()
    CreateProperty_Spacer = Label(self.Create_Properties_Panel, text='', width=27, background="#969696")
    CreateProperty_Spacer.pack()

    ## add modifier box
    AddModifierBox = AddTypeFrame(self.Main_Modifier_Panel, width=23,
                                  title='Add Modifier',
                                  tooltip='Search for Modifier to add to the stack',
                                  options=[
                                      'Layer Image',
                                      'Function Filter',
                                      'Crop',
                                      'Add Text'
                                      ],
                                  commands={
                                      'Layer Image': lambda: validate_modifier(self, 'Layer Image'),
                                      'Function Filter': lambda: validate_modifier(self, 'Function Filter'),
                                      'Crop': lambda: validate_modifier(self, 'Crop'),
                                      'Add Text': lambda: validate_modifier(self, 'Add Text')
                                      }
                                  )
    ## spacer
    Modifier_Spacer = Label(self.Main_Modifier_Panel, text='', width=26,
                            background="#969696")
    Modifier_Spacer.pack()

    
def config_filepropertiesframe(self):
    self.FilePropertiesPanelCanvas.configure(scrollregion=self.FilePropertiesPanelCanvas.bbox("all"))


def config_editpropertiesframe(self):
    self.EditPropertiesPanelCanvas.configure(scrollregion=self.EditPropertiesPanelCanvas.bbox("all"))


def config_createpropertiesframe(self):
    self.CreatePropertiesPanelCanvas.configure(scrollregion=self.CreatePropertiesPanelCanvas.bbox("all"))


def config_modifierframe(self):
    self.MainModifierPanelCanvas.configure(scrollregion=self.MainModifierPanelCanvas.bbox("all"))

