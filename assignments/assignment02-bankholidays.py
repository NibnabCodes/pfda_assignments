# assignment02-bankholidays.py
# This program prints the dates of the bank holidays that occur
# in Northern Ireland. It is then modified to print the bank
# holiday names that are unique to Northern Ireland compared to the
# rest of the UK.
# Author: Niamh Hogan

import json

# Read JSON data from file
with open("../data/bankholidays.json", "r") as file:
    data = json.load(file)

# Print file contents to verify it has been read correctly
print(json.dumps(data, indent=4))

# Access nested dictionary keys to get Northern Ireland holidays
ni_events = data["northern-ireland"]["events"]

# Print only the dates of Northern Ireland bank holidays
print("Bank Holiday dates in Northern Ireland:")
for ev in ni_events:
    print(ev["date"])

# Get events for other UK regions
ew_events = data["england-and-wales"]["events"]
scot_events = data["scotland"]["events"]

# Collect holiday names from other regions
other_titles = {ev["title"] for ev in ew_events + scot_events}

# Collect Northern Ireland holiday names
ni_titles = {ev["title"] for ev in ni_events}

# Print only Northern Ireland holidays that do not appear elsewhere
print("Unique Northern Ireland bank holidays:")
for title in ni_titles:
    if title not in other_titles:
        print(title)

# ---------------------------------------------------------------
# EXPLANATIONS & REFERENCES
#
# Reading JSON:
# I used the json module to open and load the JSON file.
# Reference:
# https://www.geeksforgeeks.org/python/read-json-file-using-python/
#
# Printing JSON contents:
# I used json.dumps() with the indent parameter to print the JSON
# data in a readable, structured format. This allowed me to visually
# check that the file contents loaded correctly.
# Reference:
# https://www.w3schools.com/python/ref_json_dumps.asp
#
# Accessing nested keys:
# I extracted data from nested dictionaries using standard key access.
# Reference:
# https://labex.io/tutorials/python-how-to-access-nested-keys-in-a-python-json-object-395034
#
# Using a for-loop to print values:
# I used a simple for-loop to print each bank holiday date.
# Reference:
# https://www.w3schools.com/python/python_for_loops.asp
#
## Extracting and preparing holiday names:
# I accessed the "events" lists for England and Wales, and for Scotland,
# by selecting their keys from the main JSON dictionary. I then used set
# comprehension to collect the holiday names from these regions into a
# single set called other_titles. I also used set comprehension to collect
# all Northern Ireland holiday names into ni_titles so that I could compare
# them without duplicates.
# References:
# https://labex.io/tutorials/python-how-to-access-nested-keys-in-a-python-json-object-395034
# https://www.w3schools.com/python/python_sets_comprehension.asp
#
# Filtering unique values:
# I used a for-loop with an if-statement to compare each Northern
# Ireland holiday name against the holiday names from other UK
# regions. If the title was not found in the other set, I printed it.
# References:
# https://sparkbyexamples.com/python/python-for-loop-with-if-statement/
# https://docs.python.org/3/reference/expressions.html#membership-test-details
# ---------------------------------------------------------------
