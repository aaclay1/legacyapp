from ._anvil_designer import HomeFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js


class HomeForm(HomeFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Set the content of the RichText to include a div with the editor-container ID
   
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