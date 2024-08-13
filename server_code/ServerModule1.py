import anvil.tables as tables
import anvil.tables.query as q
import csv
from anvil.tables import app_tables
import anvil.server
import markdown
import html2text
from datetime import datetime


@anvil.server.callable
def add_entry(entry_dict):
  app_tables.entries.add_row(
    created=datetime.now(),
    **entry_dict
  )
  
@anvil.server.callable
def add_blog(entry_dict):
  print(entry_dict)
  app_tables.blogs.add_row(
    created=datetime.now(),
    **entry_dict
  )
  
@anvil.server.callable
def get_entries():
  # Get a list of entries from the Data Table, sorted by 'created' column, in descending order
  return app_tables.entries.search(
    tables.order_by('startYear', ascending=True)
  )
@anvil.server.callable
def convertToRTF(text):
  # Get a list of entries from the Data Table, sorted by 'created' column, in descending order
 
  if text is not None:
     return markdown.markdown(text)
  else:
    text
@anvil.server.callable
def convertToMarkdown(text):
  # Get a list of entries from the Data Table, sorted by 'created' column, in descending order
  if text is not None:
    print("dfd"+text) 
    return html2text.html2text(text)
  else:
    print("None"+text) 
    text
  
@anvil.server.callable
def get_entry_row(input_str):
  if len(input_str)>0:
    input_str = input_str[12:]
    # Extract startYear and endYear
    startYear = input_str[0:4]  # First four characters
    endYear = input_str[5:9]    # Characters 6 to 9 (after the hyphen)
    
    # Locate the first name, middle name, and last name
    name_start = 11  # Names start after the space following endYear (index 10)
    name_end = input_str.find("   ", name_start)  # Find the first occurrence of double spaces after the names
    full_name = input_str[name_start:name_end].split()
    
    # Depending on the name parts, assign first, middle, and last names
    firstName = full_name[0]  # First part of the split
    middleName = full_name[1] if len(full_name) > 2 else ''  # Second part if present
    lastName = full_name[-1]  # Last part
    
    # Extract occupation
    occupation_start = name_end + 3  # Occupation starts after the three spaces
    occupation_end = input_str.find("   ", occupation_start)
    occupation = input_str[occupation_start:occupation_end]
    
    # Extract geoLocation
    geoLocation = input_str[occupation_end + 3:]  # Everything after the occupation
  
    return app_tables.entries.search(
      startYear=int(startYear),
      endYear=int(endYear),
      firstName=firstName,
      middleName=middleName, 
      lastName=lastName,
      occupation=occupation,
      geoLocation=geoLocation
    )
  else:
    return app_tables.entries.search(tables.order_by('startYear', ascending=True))
    
@anvil.server.callable
def get_blogs():
  # Get a list of entries from the Data Table, sorted by 'created' column, in descending order
  return app_tables.blogs.search(
    tables.order_by("created", ascending=False)
  )
  
@anvil.server.callable
def update_entry(entry, entry_dict):
  # check that the entry given is really a row in the ‘entries’ table
  if app_tables.entries.has_row(entry):
    entry_dict['updated'] = datetime.now()
    entry.update(**entry_dict)
  else:
    raise Exception("Entry does not exist")
    
@anvil.server.callable
def update_blog(entry, entry_dict):
  # check that the entry given is really a row in the ‘entries’ table
  if app_tables.blogs.has_row(entry):
    entry_dict['updated'] = datetime.now()
    entry.update(**entry_dict)
  else:
    raise Exception("Entry does not exist")
    
@anvil.server.callable
def delete_entry(entry):
  # check that the entry being deleted exists in the Data Table
  if app_tables.entries.has_row(entry):
    entry.delete()
  else:
    raise Exception("Entry does not exist")
    
@anvil.server.callable
def delete_blog(entry):
  # check that the entry being deleted exists in the Data Table
  if app_tables.blogs.has_row(entry):
    entry.delete()
  else:
    raise Exception("Entry does not exist")

@anvil.server.callable
def get_column_data():
  rows = app_tables.entries.search()
  return [{'name': row['firstName']} for row in rows]

@anvil.server.callable
def search_all_columns(search_value):
    # Convert search_value to lowercase for case-insensitive search
    search_value_lower = search_value.lower()
    
    # Get all rows from the table
    rows = app_tables.entries.search()
    
    results = []
    
    # Iterate through all rows
    for row in rows:
        # Iterate through each column in the row
        for column in row:
            # Convert the column value to a string and check if the search_value is a substring
            print(column[1])
            if search_value_lower in str(column[1]).lower():
                results.append(row)
                break  # Break the inner loop if we find a match, move to the next row
    
    return results