# Author: Niamh Hogan
# This program prints out the dates of the 
# bank holidays that occur in northern Ireland.

# The program is then modified to print the 
# bank holidays (names) that are unique to northern Ireland 
# compared to the rest of the UK 

# import JSON
import json 

# retrieve data from url

# read in data from file
# https://www.geeksforgeeks.org/python/read-json-file-using-python/

with open('../data/bankholidays.json', 'r') as file:
    data = json.load(file)

# print file to check that it has been read in
#print(json.dumps(data, indent=4))

# access nested dict keys
# to get Northern Ireland holidays
# https://labex.io/tutorials/python-how-to-access-nested-keys-in-a-python-json-object-395034
ni_events = data["northern-ireland"]["events"]

# Print just the dates using for-loop
# https://www.w3schools.com/python/python_for_loops.asp
print("Bank Holiday dates in Northern Ireland:")
for ev in ni_events:
    print(ev["date"])


# modify program to print out unique ni bank
# holiday names

# get events for other regions
# note: already extracted ni events above
ew_events = data["england-and-wales"]["events"]
scot_events = data["scotland"]["events"]

# Collect all other holiday names
other_titles = {ev["title"] for ev in ew_events + scot_events}

# Collect NI holiday names to
# prevent duplicates from being printed
ni_titles = {ev["title"] for ev in ni_events}

# combine for loop and if statement
# to print only NI holidays that are unique to NI
#https://sparkbyexamples.com/python/python-for-loop-with-if-statement/
print("Unique Northern Ireland bank holidays:")
for title in ni_titles:
    if title not in other_titles:
        print(title)









