from ._anvil_designer import EntryHomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..EntryEdit import EntryEdit

class EntryHome(EntryHomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.refresh_entries()
      # Set an event handler on the RepeatingPanel (our 'entries_panel')
    self.entries_panel.set_event_handler('x-delete-entry', self.delete_entry)

  def add_entry_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Initialise an empty dictionary to store the user inputs
    new_entry = {}
    # Open an alert displaying the 'EntryEdit' Form
    save_clicked = alert(
      content=EntryEdit(item=new_entry),
      title="Add Entry",
      large=True,
      buttons=[("Save", True), ("Cancel", False)]
    )
    # If the alert returned 'True', the save button was clicked.
    if save_clicked:
      new_entry['content']=anvil.server.call('convertToRTF',new_entry['content'])
      anvil.server.call('add_entry', new_entry)
      self.refresh_entries()
    
  def refresh_entries(self):
     # Load existing entries from the Data Table, 
     # and display them in the RepeatingPanel
     self.entries_panel.items = anvil.server.call('get_entries')

  def delete_entry(self, entry, **event_args):
    # Delete the entry
    anvil.server.call('delete_entry', entry)
    # Refresh entry to remove the deleted entry from the Homepage
    self.refresh_entries()

  def nav_home_click(self, **event_args):
    open_form('HomeForm')
    pass

  def nav_about_click(self, **event_args):
    open_form('AboutForm')
    pass

  def nav_notations_click(self, **event_args):
    open_form('NotationsForm')
    pass

  def nav_search_click(self, **event_args):
    open_form('SearchForm')
    pass

  def nav_blog_click(self, **event_args):
    open_form('BlogForm')
    pass

  def EntryImport_click(self, **event_args):
    open_form('EntryImport')
    pass
