#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Timothy Edmund Crosley'
SITENAME = 'TimothyCrosley.com'
SITEURL = 'https://timothycrosley.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/all-{lang}.atom.xml'
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/{slug}.rss.xml'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 5
GOOGLE_ANALYTICS = 'UA-144936423-1'
DISQUS_SITENAME = 'timothycrosley'
SHOW_FULL_ARTICLE = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

THEME = 'attila'
COLOR_SCHEME_CSS = 'monokai.css'
SITESUBTITLE = 'My Personal Homepage and Blog'
SITE_DESCRIPTION = ('The Blog and Homepage for Timothy Crosley.')
SHOW_SITESUBTITLE_IN_HTML = True
HEADER_COVER = 'images/header.jpg'
SITE_LOGO = '/images/logo.png'
CSS_OVERRIDE = ['static/main.css',
                'static/tipuesearch/tipuesearch.css',
                'https://use.fontawesome.com/releases/v5.5.0/css/all.css']
STATIC_PATHS = ['static',
                'images',
                'images/spring',
                'extra/robots.txt',
                'extra/favicon.ico',
                'extra/CNAME'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'}
}

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["tipue_search", "sitemap", "extract_toc"]

SITEMAP = {'format': 'xml'}
THEME_TEMPLATES_OVERRIDES = ['templates', ]

SOCIAL = (('twitter', 'https://twitter.com/timothycrosley'),
          ('facebook','https://facebook.com/timothycrosley'),
          ('envelope','mailto:timothycrosley@gmail.com'))

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
