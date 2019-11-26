from github import Github
import urllib2
import json
import datetime

# using username and password
# g = Github("username", "password")

# or using an access token
# g = Github("c52c1d23393df4e91e5709f827142a94d1a2184f")
# This needs to be changed for every commit or masked when uploaded to github

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
# for repo in g.get_user().get_repos():
#    print(repo.name)

# user = g.get_user()
# user.login
# print(user.login)

req = urllib2.Request("https://api.github.com/repos/roryodonnell97/CSU33013-GithubAPI-Interrogation-and-Data-Visualisation/commits")
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())

# print
# print "Here is the full json"
# print json

# print
# print "Here is the first element"
# print json [0]

fullDate = json[0]['commit']['committer']['date']

daysOfTheWeek = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
year = fullDate[0:4]
month = fullDate[5:7]
day = fullDate[8:10]
weekdayInt = datetime.date(int(year), int(month), int(day))    # Converts date to ints
weekdayNumber = weekdayInt.weekday()
weekdayString = daysOfTheWeek[weekdayNumber]

date = fullDate[0:10]
time = fullDate[11:19]

print "Here is a piece of data from the second element"
print "Commit Date: " + date
print "Commit Day: " + weekdayString
print "Commit Time: " + time

# print
# print "Now I'm extracting data"
# for cmt in json:
#   print(cmt['author']['login'])