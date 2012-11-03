#!/bin/sh

/usr/local/bin/epydoc --html sys -o sys_docs

/usr/local/bin/epydoc -v -o uml sys --css white --inheritance listed --graph umlclasstree