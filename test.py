from github import Github

# using username and password
# g = Github("roryodonnell97", "celtic199769")

# or using an access token
g = Github("c52c1d23393df4e91e5709f827142a94d1a2184f")

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

# user = g.get_user()
# user.login
# print(user.login)

