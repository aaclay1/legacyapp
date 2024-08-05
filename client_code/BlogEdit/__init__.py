from ._anvil_designer import BlogEditTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class BlogEdit(BlogEditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def image_uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.item["image"] = file
