from ._anvil_designer import EntryEditTemplate
from anvil import *
import anvil.server
from anvil.tables import app_tables


class EntryEdit(EntryEditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    if len(self.item.items()) > 0:
      self.content_box.text = anvil.server.call('convertToMarkdown', self.item['content'])
    
  def image_uploader_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.item['image'] = file

