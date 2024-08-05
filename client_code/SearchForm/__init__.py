from ._anvil_designer import SearchFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class SearchForm(SearchFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

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
    # Any code you write here will run when the form opens.

  def nav_blog_click(self, **event_args):
    open_form('BlogForm')
    pass