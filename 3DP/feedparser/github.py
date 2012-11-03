import feedparser


def url(user):
    return "https://github.com/%s" % user

d = feedparser.parse(url("cancerhermit"))
print d['feed']['title']
for e in d.entries:
    print ""
    print e.id
    print e.updated_parsed, e.published_parsed, e.title
    #print e.authors[0]['href'], e.authors[0]['name']
    print e.media_thumbnail[0]['url'], e.media_thumbnail[0]['width'], e.media_thumbnail[0]['height']
    print e.link
    print e.summary
    print e.author
    print e.author_detail['href'], e.author_detail['name']
    print e.title_detail['base'], e.title_detail['value']
