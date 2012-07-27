#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Holland Core Team"
SITENAME = u"Holland Backup Manager"
SITESUBTITLE = u"Backed the #$%& Up!"
SITEURL = 'http://hollandbackup.org'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

MENUITEMS = [
    # (name, url)
    ('News', SITEURL),
    ('Docs', 'http://docs.hollandbackup.org'),
    ('Wiki', 'http://wiki.hollandbackup.org'),
]

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = 'Communication'

THEME = 'holland.theme'

CLEAN_URLS = False
