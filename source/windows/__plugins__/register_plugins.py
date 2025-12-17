## To register a plugin, import the script here
##
## Example:
## from __plugins__.plugins.[your main script name] import [your main function]
from __plugins__.plugins.template import property_template_ui
    
def register(self):
    ## Call the main function here
    ## Example:
    ## [your main function](self)
    property_template_ui(self)
