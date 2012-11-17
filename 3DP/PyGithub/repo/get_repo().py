from github import Github
import macos
g = Github(macos.user.gitconfig.user.name, macos.user.gitconfig.github.password)

r=g.get_user().get_repo("test")
print r.description
print r.homepage
print r.public
print r.has_issues
print r.has_wiki
print r.has_downloads