Features
----------

+   convert markdown to html 
+   use [github.css](https://gist.github.com/4252786)

Installing
----------

    pip install githubmarkdown

Usage
----------

    from githubmarkdown import html, temphtml
    print html("/path/to/README.md") # or html(open("/path/to/README.md"))
    print temphtml("/path/to/README.md") # or  tempfile(open("/path/to/README.md"))
    >>> '/var/folders/9d/l44q9nhx6_b93pny23s9l0ch0000gn/T/tmpSkoJbP'