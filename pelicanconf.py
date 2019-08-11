#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from datetime import datetime

NOW = datetime.now()
YEAR = NOW.year

AUTHOR = 'Timothy Edmund Crosley'
SITENAME = 'TimothyCrosley.com'
SITEURL = 'https://timothycrosley.com'
ARTICLE_URL = "{slug}"

DESCRIPTION_SIDEBAR = 'Software Engineer and Open Source Enthusiast. Creator of <a href="https://github.com/timothycrosley/isort">isort</a>, <a href="https://github.com/hugapi/hug">Hug</a>, <a href="https://github.com/timothycrosley/concentration">Concentration</a>, and many other Python tools and libraries.'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'
TITLE = "Timothy Crosley"
TAGLINE = "I love Amanda"

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
TINYLETTER_USERNAME = "timothycrosley"
TINYLETTER_NEWSLETTER = "The latest from Timothy Crosley"
DEFAULT_PAGINATION = 5
GOOGLE_ANALYTICS = 'UA-144936423-1'
DISQUS_SITENAME = 'timothycrosley-com'
SHOW_FULL_ARTICLE = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

THEME = 'utterson'
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

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["tipue_search", "sitemap", "extract_toc", "post_stats"]

SITEMAP = {'format': 'xml'}
THEME_TEMPLATES_OVERRIDES = ['templates', ]

GITHUB_URL = "https://github.com/timothycrosley/blog"
SOCIAL = (('github', 'https://github.com/timothycrosley'),
          ('twitter', 'https://twitter.com/timothycrosley'),
          ('linkedin', 'https://www.linkedin.com/in/timothycrosley/'),
          ('reddit', 'https://www.reddit.com/user/timothycrosley'),
          ('hacker-news', 'https://news.ycombinator.com/user?id=timothycrosley'),
          ('python', 'https://pypi.org/user/timothycrosley/'),
          ('gitter', 'https://gitter.im/timothycrosley'),
          ('youtube', 'https://www.youtube.com/user/timothycrosley/videos'))

# Uncomment following lines only for testing development changes
#RELATIVE_URLS = True
#SITEURL = ''
