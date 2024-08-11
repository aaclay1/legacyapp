from ._anvil_designer import NotationViewOnlyTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..EntryEdit import EntryEdit


class NotationViewOnly(NotationViewOnlyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def link_click(self, **event_args):
    """This method is called when the Link is clicked"""
    item = self.item  # Get the data associated with the clicked row
    search_term = item['created']  # Get the search key from the row
    self.search(search_term)  # Call the search function

  def search(self, search_term):
    # Define your search logic here
    print(f"Search triggered for: {search_term}")
    get_open_form().label_result.text = f"Results for {search_term}"