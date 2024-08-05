from ._anvil_designer import NotationsFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import alert
from ..PasscodeForm import PasscodeForm
from ..RowTemplate import RowTemplate


class NotationsForm(NotationsFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_entries()

    rows = anvil.server.call('get_column_data')

    # Set the items property of the RepeatingPanel to the queried data
    self.repeating_panel_1.items = rows
  def nav_home_click(self, **event_args):
    open_form("HomeForm")
    pass

  def nav_about_click(self, **event_args):
    open_form("AboutForm")
    pass

  def nav_notations_click(self, **event_args):
    open_form("NotationsForm")
    pass

  def nav_search_click(self, **event_args):
    open_form("SearchForm")
    pass

  def refresh_entries(self):
     self.entries_panel.items = anvil.server.call('get_entries')
    
  def nav_blog_click(self, **event_args):
    open_form('BlogForm')
    pass

  def editbutton_click(self, **event_args):
    # Open the PasscodeForm as a custom alert
    passcode_form = PasscodeForm()
    passcode = alert(content=passcode_form, buttons=[], large=True)
    
    # Handle the passcode
    if passcode == ".":
        open_form('EntryHome')
    else:
        alert("Incorrect passcode.")

    pass
       