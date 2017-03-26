#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

base_path = os.path.dirname(os.path.realpath(__file__))

AUTHOR = u'Graham Cox'
SITENAME = u'Neo4J from the ground up'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = os.path.join(base_path, 'pelican-themes/pelican-bootstrap3')
JINJA_EXTENSIONS = ['jinja2.ext.i18n']

PLUGIN_PATHS=[os.path.join(base_path, 'pelican-plugins')]
PLUGINS = ['i18n_subsites']
