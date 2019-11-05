from github import Github

# using username and password
# g = Github("username", "password")

# or using an access token
g = Github("2159a0bf4865d6b2afe2e86d5b95b40c850e2b44")

# Github Enterprise with custom hostname
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

# user = g.get_user()
# user.login
# print(user.login)

