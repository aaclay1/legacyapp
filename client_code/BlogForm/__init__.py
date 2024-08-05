from ._anvil_designer import BlogFormTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class BlogForm(BlogFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh_entries()
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
    self.entries_panel.items = anvil.server.call("get_blogs")

  def edit_click(self, **event_args):
    open_form("BlogHome")
    pass
  def nav_blog_click(self, **event_args):
    open_form('BlogForm')
    pass

  def editbutton_click(self, **event_args):
    open_form('BlogHome')
  pass
