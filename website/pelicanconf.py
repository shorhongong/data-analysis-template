#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

###################################################
# AUTHORSHIP AND WEBSITE INFO (Replace accordingly)
###################################################

AUTHOR = u'Shorhon Gong'
SITENAME = u'Data Analysis Project'
SITESUBTITLE = u'Template using the iPython notebook'
GITHUB_REPOSITORY_URL=u'https://github.com/shorhongong/data-analysis-template.git'

###################################################
# FINER WEBSITE CONF (Defaults should be okay)
###################################################

TIMEZONE = 'US/Pacific'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Title menu options (this isn't necessary, but I wanted to have more control)
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = [('Report', 'nb4'),
             ('Data Analysis', 'nb3'),
             ('Data Cleaning', 'nb2'),
             ('Data Gathering', 'nb1'),
            ]

DISPLAY_TAGS_ON_SIDEBAR = False

# Blogroll
LINKS = (('Project Report', 'nb4'),
         ('Data Analysis',  'nb3'),
         ('Data Cleaning',  'nb2'),
         ('Data Gathering', 'nb1'),
        )


# Social widget
SOCIAL = (('View on Github', GITHUB_REPOSITORY_URL),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme/'

# MD_EXTENSIONS = (['toc'])

PLUGIN_PATH = 'plugins'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
            'liquid_tags.include_code', 'liquid_tags.notebook',
            'liquid_tags.literal']

#STATIC_PATHS = ['notebooks', 'images', 'files']
NOTEBOOK_DIR = '../../notebooks'

## The theme file should be updated so that the base header contains the line:
##
## {% if EXTRA_HEADER %}
## {{ EXTRA_HEADER }}
## {% endif %}
##

## This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found. "
                  "Rerun make html to finalize build.")
else:
    EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

CC_LICENSE = "CC-BY-NC-SA"
