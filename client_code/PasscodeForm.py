from ._anvil_designer import PasscodeFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class PasscodeForm(PasscodeFormTemplate):

    def __init__(self, **properties):
        self.init_components(**properties)
        # Any other initialization code here

    def button_submit_click(self, **event_args):
        # Get the value from the text box
        passcode = self.text_box_passcode.text
        
        # Close the dialog and return the passcode
        self.raise_event("x-close-alert", value=passcode)
