# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os

from subprocess import check_output, CalledProcessError

def get_version():

    try:
        version = check_output(['cat', 'VERSION'],
                               universal_newlines=True)
    except CalledProcessError:
        return 'unknown version'

    return version.rstrip()

# "version" is used for html build
version = get_version()
# "release" is used for LaTeX build
release = version


# -- Project information -----------------------------------------------------

project = u'Computer Networks: A Systems Approach'
copyright = u'2019'
author = u'Larry Peterson and Bruce Davie'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# make all warnings errors
warning_is_error = True

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones. ***Replace "mathjax" with "imgmath" for epub output.***
extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.coverage',
    'sphinx.ext.graphviz',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
    'sphinxcontrib.spelling',
    "sphinx_multiversion",
]

# Text files with lists of words that shouldn't fail the spellchecker:
spelling_word_list_filename=['dict.txt', ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [u'_build', 'venv-docs', 'requirements.txt', 'Thumbs.db', 'private', '.DS_Store', '*/README.rst', 'sidebars', 'status.rst', 'CLA.rst', 'CONTRIBUTING.rst']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# Enable numbered figures
numfig = True
numfig_format = {
    'figure': 'Figure %s.',
    'table':  'Table %s.'
    }

# Ignore link check for the following websites
# linkcheck_ignore = [
#     'https://SDN.systemspproach.org/',
# ]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
  'prev_next_buttons_location': 'both'
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# HTML Favicon
html_favicon = '_static/bridge.ico'

# HTML Index
html_use_index = False

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'SystemsApproach'


# -- Options for LaTeX output ------------------------------------------------
#latex_engine = 'xelatex'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '11pt',

    # Get unicode to work
    #
    'fontenc': '\\usepackage[LGR,T1]{fontenc}',

    # Latex figure (float) alignment
    #
    'figure_align': 'ht',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'book.tex', u'Computer Networks: A Systems Approach',
     u'Peterson and Davie', 'manual', True),
]

latex_toplevel_sectioning = 'chapter'


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'Systems Approach', u'Systems Approach',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Computer Networks', u'Computer Networks',
     author, 'Peterson and Davie', 'A Systems Approach',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------
epub_title = project
epub_description = 'Building a Cloud Management Platform'
epub_cover = ('_static/cover.jpg', '')
epub_show_urls = 'False'
epub_use_index = False

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- options for Intersphinx extension ---------------------------------------

intersphinx_mapping = {
    'sphinx': ('https://www.sphinx-doc.org/en/master', None),
    'sysapproach5g': ('https://5g.systemsapproach.org/', None),
    'sysapproachnet': ('https://ops.systemsapproach.org/', None),
    'sysapproachnet': ('https://tcpcc.systemsapproach.org/', None),
    'sysapproachsdn': ('https://sdn.systemsapproach.org/', None),
    }

# -- Options for todo extension ----------------------------------------------
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Set up Google Analytics
# -- using approach at https://stackoverflow.com/questions/9444342/adding-a-javascript-script-tag-some-place-so-that-it-works-for-every-file-in-sph/41885884#41885884


GA_INVOKE_JS = """
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-8NK2HCPFQ5');
"""

def setup(app):

    app.add_css_file('css/rtd_theme_mods.css')


    app.add_js_file('https://www.googletagmanager.com/gtag/js?id=G-8NK2HCPFQ5')
    app.add_js_file(None, body=GA_INVOKE_JS)
