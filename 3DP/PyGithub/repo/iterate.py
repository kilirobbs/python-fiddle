from github import Github
from gitconfig import gitconfig
g = Github(gitconfig.user.name, gitconfig.github.password)

for r in g.get_user().get_repos():
    print r.private
    print r.fork
    print r.pushed_at
    print r.description
    print r.forks
    print r.watchers
    print r.homepage
    print r.has_issues
    print r.size
    print r.created_at
    print r.clone_url
    print r.html_url
    print r.has_wiki
    print r.updated_at
    print r.svn_url
    print r.ssh_url
    print r.has_downloads
    print r.organization
    print r.master_branch
    print r.name
    print r.url
    print r.git_url
    print r.language
    print r.id
    print r.__dict__#,r.name, r.description