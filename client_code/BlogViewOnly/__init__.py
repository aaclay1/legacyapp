from ._anvil_designer import BlogViewOnlyTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..BlogEdit import BlogEdit


class BlogViewOnly(BlogViewOnlyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Now refresh the page
   