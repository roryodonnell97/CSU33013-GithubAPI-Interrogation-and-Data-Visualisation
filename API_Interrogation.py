from github import Github
import urllib2
import json
import datetime
import sqlite3 
import  requests
from collections import Counter


# Create Table
connection = sqlite3.connect("table1.db")    
crsr = connection.cursor() 

crsr.execute("DROP TABLE if exists table1") 
sql_command = """CREATE TABLE if not exists table1 (  
full_date VARCHAR(30),  
date VARCHAR(20),  
weekday VARCHAR(20),
weekday_num INTEGER,  
time VARCHAR(20)  
);"""
crsr.execute(sql_command) 


# Variables
daysOfTheWeek = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
number_of_commits = 0
number_of_contributors = 0
pageNumber = 1
lastPageFound = False

# Get number of contributors by finding number of occurrences of 'contributions:' in JSON
while lastPageFound is False:

    # Retrieve contributors JSON from Github API
    req = urllib2.Request("https://api.github.com/repos/pksunkara/octonode/contributors?page=" + str(pageNumber))
    opener = urllib2.build_opener()
    f = opener.open(req)
    contibutors_json = json.loads(f.read())

    json_string = json.dumps(contibutors_json)
    substring = '"contributions": '
    temp = number_of_contributors
    number_of_contributors += json_string.count(substring)
     
    pageNumber +=1

    if (number_of_contributors - temp) < 30:
        lastPageFound = True

# Get number of commits from each contributor
current_page = "0"
for i in range(number_of_contributors/30):
    current_page = str(i+1)
    req = urllib2.Request("https://api.github.com/repos/pksunkara/octonode/contributors?page=" + current_page)
    opener = urllib2.build_opener()
    f = opener.open(req)
    contibutors_json = json.loads(f.read())
    for x in range(30):
        number_of_commits += contibutors_json[x]['contributions']


if number_of_contributors > 30 and number_of_contributors % 30 != 0:
    current_page_int = (int(current_page))
    current_page = str(current_page_int)
    req = urllib2.Request("https://api.github.com/repos/pksunkara/octonode/contributors?page=" + current_page)
    opener = urllib2.build_opener()
    f = opener.open(req)
    contibutors_json = json.loads(f.read())

# Loop through remaining contributors on last page
for i in range(number_of_contributors%30):
    number_of_commits += contibutors_json[x]['contributions']

# Now have number of commits and contributors
print "Number of commits: " + str(number_of_commits)
print "Number of contributors: " + str(number_of_contributors)


# Retrieve commits JSON from Github API
req = urllib2.Request("https://api.github.com/repos/pksunkara/octonode/commits")
opener = urllib2.build_opener()
f = opener.open(req)
commits_json = json.loads(f.read())

# Parse the data of each commit and add to database
# Each page of the commits JSON holds 30 commits
# Loop through 30 commits per page n times where n = number_of_commits/30
current_page = "0"
for i in range(number_of_commits/30):
    current_page = str(i+1)
    req = urllib2.Request("https://api.github.com/repos/pksunkara/octonode/commits?page=" + current_page)
    opener = urllib2.build_opener()
    f = opener.open(req)
    commits_json = json.loads(f.read())

    for x in range(30):

        fullDate = commits_json[x]['commit']['committer']['date']

        year = fullDate[0:4]
        month = fullDate[5:7]
        day = fullDate[8:10]
        weekdayInt = datetime.date(int(year), int(month), int(day))    # Converts date to ints
        weekdayNumber = weekdayInt.weekday()
        weekdayString = daysOfTheWeek[weekdayNumber]

        date = fullDate[0:10]
        time = fullDate[11:19]

        sql_command = "INSERT INTO table1 VALUES ('"+ fullDate + "', '" + date + "', '" + weekdayString + "', '" + str(weekdayNumber) + "', '" + time + "');"
        crsr.execute(sql_command)

        print "Commit Number: " + str(x + (i*30) + 1)
        print "Commit Date: " + date
        print "Commit Day: " + weekdayString
        print "Commit Day Number: " + str(weekdayNumber)
        print "Commit Time: " + time
        print

# This sections only occurs if number_of_commits % 30 != 0
# Finds the last page if number of pages is > 1
if number_of_commits > 30 and number_of_commits % 30 != 0:
    current_page_int = (int(current_page) + 1)
    current_page = str(current_page_int)
    req = urllib2.Request("https://api.github.com/repos/pksunkara/octonode/commits?page=" + current_page)
    opener = urllib2.build_opener()
    f = opener.open(req)
    commits_json = json.loads(f.read())

# Loop through remaining commits on last page
for i in range(number_of_commits%30):

    fullDate = commits_json[i]['commit']['committer']['date']

    year = fullDate[0:4]
    month = fullDate[5:7]
    day = fullDate[8:10]
    weekdayInt = datetime.date(int(year), int(month), int(day))    # Converts date to ints
    weekdayNumber = weekdayInt.weekday()
    weekdayString = daysOfTheWeek[weekdayNumber]

    date = fullDate[0:10]
    time = fullDate[11:19]

    sql_command = "INSERT INTO table1 VALUES ('"+ fullDate + "', '" + date + "', '" + weekdayString + "', '" + str(weekdayNumber) + "', '" + time + "');"
    crsr.execute(sql_command)

    print "Commit Number: " + str(i + (number_of_commits/30 * 30) + 1)
    print "Commit Date: " + date
    print "Commit Day: " + weekdayString
    print "Commit Day Number: " + str(weekdayNumber)
    print "Commit Time: " + time
    print

# # Print values using sql command
# sql_command = """SELECT * FROM table1"""  
# crsr.execute(sql_command)
  
# ans= crsr.fetchall()   
# for i in ans: 
#     print(i)


# Save changes to database and close
connection.commit()   
connection.close() 