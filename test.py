from github import Github
import urllib2
import json
import datetime
import sqlite3 
import  requests
from collections import Counter


# Retrieve JSON from Github API
req = urllib2.Request("https://api.github.com/repos/roryodonnell97/CSU33013-GithubAPI-Interrogation-and-Data-Visualisation/commits")
opener = urllib2.build_opener()
f = opener.open(req)
commits_json = json.loads(f.read())

req = urllib2.Request("https://api.github.com/repos/roryodonnell97/CSU33013-GithubAPI-Interrogation-and-Data-Visualisation/contributors")
opener = urllib2.build_opener()
f = opener.open(req)
contibutors_json = json.loads(f.read())


# Create Table
connection = sqlite3.connect("commitTable.db")    
crsr = connection.cursor() 

crsr.execute("DROP TABLE if exists commitTable") 
sql_command = """CREATE TABLE if not exists commitTable (  
full_date VARCHAR(30),  
date VARCHAR(20),  
weekday VARCHAR(20),  
time VARCHAR(20)  
);"""
crsr.execute(sql_command) 


# Variables
daysOfTheWeek = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
index = 0
number_of_commits = 0

# Get number of contributors by finding number of occurrences of 'contributions:'
json_string = json.dumps(contibutors_json)
substring = '"contributions": '
number_of_contributors = json_string.count(substring)

# Get number of commits from each contributor
while index < number_of_contributors:
    number_of_commits += contibutors_json[index]['contributions']
    index += 1


# Parse the data of each commit and add to database
# Each page of the commits JSON holds 30 commits
# loop through 30 commits per page n times where n = number_of_commits/30
current_page = "0"
for i in range(number_of_commits/30):
    current_page = str(i+1)
    req = urllib2.Request("https://api.github.com/repos/roryodonnell97/CSU33013-GithubAPI-Interrogation-and-Data-Visualisation/commits?page=" + current_page)
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

        sql_command = "INSERT INTO commitTable VALUES ('"+ fullDate + "', '" + date + "', '" + weekdayString + "', '" + time + "');"
        crsr.execute(sql_command)

        print "Commit Number: " + str(x + (i*30) + 1)
        print "Commit Date: " + date
        print "Commit Day: " + weekdayString
        print "Commit Time: " + time
        print

# loop through remaining commits on last page
# This sections only occurs if number_of_commits % 30 != 0
if number_of_commits > 30 and number_of_commits % 30 != 0:
    current_page_int = (int(current_page) + 1)
    current_page = str(current_page_int)
    req = urllib2.Request("https://api.github.com/repos/roryodonnell97/CSU33013-GithubAPI-Interrogation-and-Data-Visualisation/commits?page=" + current_page)
    opener = urllib2.build_opener()
    f = opener.open(req)
    commits_json = json.loads(f.read())

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

    sql_command = "INSERT INTO commitTable VALUES ('"+ fullDate + "', '" + date + "', '" + weekdayString + "', '" + time + "');"
    crsr.execute(sql_command)

    print "Commit Number: " + str(i + (number_of_commits/30 * 30) + 1)
    print "Commit Date: " + date
    print "Commit Day: " + weekdayString
    print "Commit Time: " + time
    print

# # Print values using sql command
# sql_command = """SELECT * FROM commitTable"""  
# crsr.execute(sql_command)
  
# ans= crsr.fetchall()   
# for i in ans: 
#     print(i)


# Save changes to database and close
connection.commit()   
connection.close() 