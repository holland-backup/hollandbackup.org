#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Holland Core Team"
SITENAME = u"Holland Backup Manager"
SITESUBTITLE = u"Backed the #$%& Up!"
SITEURL = u'http://hollandbackup.org'

ARTICLE_URL = u'{date:%Y}/{date:%m}/{category}/{slug}'
ARTICLE_SAVE_AS = u'{date:%Y}/{date:%m}/{category}/{slug}'

PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}'

TAG_URL = u'tag/{slug}'
TAG_SAVE_AS = u'tag/{slug}'

AUTHOR_URL = u'author/{slug}'
AUTHOR_SAVE_AS = u'author/{slug}'

ABORT_ON_SLUG_CONFLICT = True

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

MENUITEMS = [
    # (name, url)
    ('News', SITEURL),
    ('Docs', 'http://docs.hollandbackup.org'),
    ('Wiki', 'http://wiki.hollandbackup.org'),
    ('Archives', 'archives'),
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

#CLEAN_URLS = True

RELATIVE_URLS = False

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search'))

for template in DIRECT_TEMPLATES:
    globals()[template.upper() + '_SAVE_AS'] = template
