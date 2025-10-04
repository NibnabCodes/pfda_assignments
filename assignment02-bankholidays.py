# Author: Niamh Hogan
# This program prints out the dates of the 
# bank holidays that occur in northern Ireland.

# The program is then modified to print the 
# bank holidays that are unique to northern Ireland 
# compared to the rest of the UK (you can choose if you want to use the name or the date of the holiday to decide if it is unique.)

# import JSON
import json 

# retrieve data from url

# read in data from file
# https://www.geeksforgeeks.org/python/read-json-file-using-python/
with open('bankholidays.json', 'r') as file:
    data = json.load(file)

print(json.dumps(data, indent=4))

# print northern ireland BH dates













