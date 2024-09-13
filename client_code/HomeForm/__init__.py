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
   # Get the width and height of the canvas
    canvas_width = self.canvas_1.get_width()  # Get the actual width of the canvas after rendering
    canvas_height = 100  # Fixed height for the banner
    
    # Set the height of the canvas
    self.canvas_1.height = canvas_height
    
    # Fill the background with a color
    self.canvas_1.fill_style = 'lightblue'
    self.canvas_1.fill_rect(0, 0, canvas_width, canvas_height)
    
    # Set the font for the text
    self.canvas_1.font = 'bold 24px Arial'
    
    # Measure the text width
    text = "Welcome to My App"
    text_width = self.canvas_1.measure_text(text)
    
    # Calculate the X position to center the text
    x_position = (canvas_width - text_width) / 2
    
    # Draw the title text in the center of the banner
    self.canvas_1.fill_style = 'black'
    self.canvas_1.fill_text(text, x_position, 60)  # 60 is the y position
    
    # Draw a logo or image on the left side of the banner
    image_media = anvil.URLMedia('_/theme/AdoniramAndAnnJudson.jpg')  # Replace with your uploaded image path
    self.canvas_1.draw_image(image_media, 10, 10, 80, 80)  # Adjust positioning and size as needed
    
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

