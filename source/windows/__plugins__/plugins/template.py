## PROPERTY Plugin Template
##
## This file is a template for creating a PROPERTY Plugin
## PhotoGraphics Editor 1.1.0
##
## See the "Built-in Libraries.txt" for a list of the libs you can use

""" Create PROPERTY plugins with this template """

######################
## PROPERTY Example ##
######################
""" Start with information about the plugin """
plugin_info = {
    "name": "Template", # name of plugin
    "author": "Noah Rahm", # author of plugin
    "version": "1.0", # version of plugin
    "program": "1.1.0", # version of PhotoGraphics Editor
    "type": "PROPERTY", # plugin type (PROPERTY, MODIFIER or DOCKER)
    "description": "Example template" # short description about plugin
}

""" Import the normal imports if you need them """
from tkinter import *
from tkinter.constants import *
from tkinter import ttk

""" Import widgets from the program's API """
from lib.SWIFT.propertyframe import PropertyFrame
from lib.SWIFT.tooltip import ToolTip
from lib.SWIFT.flatbutton import FlatButton

 
def property_template_ui(self):
    """ Create the panel to place the interior widgets into. This frame is
    placed inside the property tab of the sidepanel. """
    self.Template_PropertyPnl = PropertyFrame(self.File_Properties_Panel,
                                              default=False,
                                              text="Plugin ttTemplate")
    self.Template_PropertyPnl.pack(fill=X)

    """The parent widgets must be put inside the PropertyFrame interior by 
    accessing the '.interior' variable as shown below.  """
    Template_Frame = Frame(self.Template_PropertyPnl.interior, bg="#969696")
    Template_Frame.pack(padx=2, pady=2, side=TOP, fill=X)

    """ You can use any valid tkinter widget and/or widgets from the API, but
    be sure to set the bg color to #969696 (Example: bg="#969696"). It is a
    good idea to name the widgets specific to your tool's function to and ONLY
    use 'self.yourvariablename' if you will use that widget later to avoid
    confusion with the program API variable names."""
    Template_Button = FlatButton(Template_Frame, text=' Template ',
                                 width=20)
    Template_Button.pack(padx=2, pady=2, side=TOP)
    ToolTip(Template_Button, "This is an example property template", wtype='FLATBUTTON')

    """ After all the widgets have been created, update the width of the panel
    by calling the 'update_width()' method. """
    self.Template_PropertyPnl.update_width()
