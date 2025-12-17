"""
Introduction to S.W.I.F.T 

~ S.W.I.F.T (Styled Widget Interface For Tkinter)  (c) Noah Rahm 2019 ~

SWIFT is a set of widgets (addons to tkinter) specifically created for the
PhotoGraphics Editor UI. They are created with PhotoGraphics Editor in mind
and are not intended to be a standalone GUI toolkit.

The style, design and functionality of the widgets are made to be used in
a "flat" layout and theme. PhotoGraphics Editor has a "flat" layout (with
the exception of the dialogs) in that toplevel windows do not pop-up for
most tasks.

It is made to be simple and easy enough to use that anyone
with a little knowlege of Python and tkinter can use it. SWIFT is not a
total replacement for tkinter, but rather a set of specifically-designed
widgets to fit the need, functionality and style of PhotoGraphics Editor. 

The set of widgets (for use by the user) currently includes:

> propertyframe
- collapsible panel for property type

> modifierframe
- collapsible panel for modifier type

> tooltip
- widget tooltip

> colorchooser
> colorchooserbutton
- used together  as a colorchooser widget
* (used instead of tkinter askcolor)

> dropdownmenu
> dropdownbutton
- used together as a combobox widget
* (used instead of tkinter combobox)

> filedialog
- either open or save file dialog
* (used instead of tkinter file dialogs)

> flatbutton
-  button widget
* (used instead of tkinter button)

> tabbednotebook
- notebook widget
* (use instead of the ttk Notebook)

SWIFT is licensed under the GNU General Public License.
See the GNU General Public License for more details.
"""
## Available (external) imports:
"""
from lib.SWIFT.colorchooser import ColorChooser
from lib.SWIFT.colorchooserbutton import ColorChooserButton
from lib.SWIFT.dropdownbutton import DropDownButton
from lib.SWIFT.dropdownmenu import DropDownMenu
from lib.SWIFT.savefiledialog import SaveFileDialog
from lib.SWIFT.openfiledialog import OpenFileDialog
from lib.SWIFT.flatbutton import FlatButton
from lib.SWIFT.modifierframe import ModifierFrame
from lib.SWIFT.propertyframe import PropertyFrame
from lib.SWIFT.tabbednotebook import Notebook
from lib.SWIFT.tooltip import ToolTip
"""
