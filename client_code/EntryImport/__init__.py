from ._anvil_designer import EntryImportTemplate
from anvil import *
import anvil.server
import re
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime


class EntryImport(EntryImportTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def EntryImport_change(self, file, **event_args):
    # Decode the file content
    csv_content = file.get_bytes().decode('utf-8')
    
    # Split the content into lines
    rows = csv_content.splitlines()
    
    # Get the headers from the first line
    headers = rows[0].split(',')
    
    # Loop through the remaining lines and insert into the DataTable
    for row in rows[1:]:
      # Split each row by commas
      values = row.split(',')
      
      # Create a dictionary to map column names to values
      row_data = {header: value for header, value in zip(headers, values)}
      # Insert the row into the DataTable
      app_tables.entries.add_row(startYear=int(row_data['startYear']),endYear=int(row_data['endYear']),firstName=row_data['firstName'],lastName=row_data['lastName'],middleName=row_data['middleName'],occupation=row_data['occupation'],geoLocation=row_data['geoLocation'],content=re.sub(r'{return}', '\r', row_data['content'].replace("{comma}", ",")),created=datetime.now(),updated=datetime.now())
      
    alert("CSV file uploaded and data saved!")
    open_form('NotationsForm')
    pass
