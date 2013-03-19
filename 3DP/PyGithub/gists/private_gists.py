from github import Github

#import macos
g = Github(user, password)


print g.get_user().private_gists