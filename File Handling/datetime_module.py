"""
===============================================================================
Script Name:       Working with Files and Directories
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-30

Description:
-------------
This script demonstrates practical file system operations using Python's 
os, glob, shutil, and time modules, with a GIS focus. Specifically, it:

    - Prints the current working directory
    - Lists files in a folder
    - Finds files by pattern (e.g., CSV or Python files)
    - Traverses folders recursively
    - Checks for file/folder existence and type
    - Extracts file/folder names and extensions
    - Performs batch renaming
    - Counts files by type
    - Moves files to a new location
    - Filters files modified in the last 7 days

Usage:
------
1. Update folder paths or file patterns as needed for your environment.
2. Uncomment sections to run specific tasks.
3. Use this as a reference for building more complex GIS file management scripts.

Notes:
------
- Designed for small to medium-sized datasets; very large folders may require 
  memory optimization.
- This script is intended as a learning and portfolio demonstration of Python 
  file operations in a GIS context.
===============================================================================
"""
from datetime import datetime, date, timedelta

#Convert string to date
# date_str="2026-03-01"
# date_obj=datetime.strptime(date_str,"%Y-%m-%d")
# print(date_obj)

#Convert date to string
# now=datetime.now()
# formatted=now.strftime("%B %d, %Y")
# print(formatted)

#printing current date/time
# today=date.today()
# now=datetime.now()
# print(today)
# print(now)

#find difference between two dates, basic pattern for identifying dates that are 
#more than a certain time through list comprehension
# first_update=date(2026,1,15)
# last_update=date(2026,3,20)
# today=date.today()
# delta_first=today-first_update
# delta_last=today-last_update
# date_lst=[delta_first.days,delta_last.days]
# date_old=[date for date in date_lst if date >30]
# print(date_old)

parcels = [
    {"parcel_id": 1, "last_updated": "2026-03-20"},
    {"parcel_id": 2, "last_updated": "2026-03-25"},
    {"parcel_id": 3, "last_updated": "2026-03-15"},
]

today=date.today()

for parcel in parcels:
    last_update=datetime.strptime(parcel["last_updated"], "%Y-%m-%d").date()
    days_since=(today-last_update).days
    print(f"Parcel {parcel['parcel_id']} was last updated {days_since} ago")
