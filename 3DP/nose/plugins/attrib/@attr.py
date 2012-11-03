from nose.plugins.attrib import attr
@attr('slow')
def test_big_download():
    import urllib
    # commence slowness...


# https://nose.readthedocs.org/en/latest/plugins/attrib.html
# nosetests -a '!slow'