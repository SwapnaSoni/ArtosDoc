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
import sys
import re
import time
import subprocess
import shutil
import webbrowser
import sphinx
import sphinx_rtd_theme

sphinx_toolchain_rel_path = ""
sys.path.insert(0, os.path.abspath(sphinx_toolchain_rel_path))

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'vs'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# Trim spaces before footnote references.
trim_footnote_reference_space = True

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
#todo_include_todos = False

# If true, figures, tables and code-blocks are automatically numbered if they have a caption.
numfig = True

# If true, Sphinx will warn about all references where the target cannot be found.
nitpicky = True

# The default language to highlight source code in.
highlight_language = 'none'

# -- Project information -----------------------------------------------------

project = u'Artos (Art of System Testing)'
copyright = u'2018-2020, Arpit Shah and Contributors'
author = u'Arpit Shah and Contributors'

# The short X.Y version
version = u'01.00.0002'
# The full version, including alpha/beta/rc tags
release = u'01.00.0002'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

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
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
#pygments_style = 'sphinx'
pygments_style = 'default'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
#html_theme = 'bootstrap'
#html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
    ]
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}
html_theme_options = {
	'canonical_url': '',
    'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': False,
    'display_version': True,
	# 'bootom' or 'top' or 'both' or 'none'
    'prev_next_buttons_location': 'both',
    'style_external_links': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 2,
    'includehidden': True,
    'titles_only': True
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "../images/ArtosFull_vectorised.svg"
#html_logo = "../images/Artos_vectorised.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
    ]
}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Artosdoc'


# -- Options for LaTeX output ------------------------------------------------

custom_latex_preamble = r'''
% For the number of the last page in the document
\usepackage{lastpage}

% Needed to override a previous declaration where the footrulewidth is 0pt 
\renewcommand{\footrulewidth}{0.4pt}

\titleformat{\section}
  {\normalfont\sffamily\huge\bfseries\color{black}}
  {\thesection}{1em}{}

% Increase white space above the first heading (default 25pt)
\headsep=30pt

% Demote sectional commands: chapter becomes section, section to subsection, etc.
% This is needed because the 'article' docclass can't handle 'chapter' as the top level
% We cannae chaynge th' wey ReStructured Tiext wirks 
\let\chapter\section%
\let\section\subsection%
\let\subsection\subsubsection%
\let\subsubsection\subsubsubsection%
\let\subsubsubsection\paragraph%

\makeatletter
    % Set headers and footers for {empty} pages (the first page of a chapter) 
    \fancypagestyle{empty}{
        \fancyhf{}
        \fancyhead[R]{\sphinxincludegraphics[scale=0.75]{Artos_vectorised.pdf}}
        \fancyfoot[L]{\version}
        \fancyfoot[C]{\thepage\ of \pageref{LastPage}}
        \fancyfoot[R]{\@date}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
        \renewcommand{\footskip}{40pt} % This pushes the footer down to match the footers on other pages (default 30pt)
    }
    
    % Set headers and footers for {fancy} pages (not the first page of a chapter) 
    \pagestyle{fancy}{
        \fancyhf{}
        \fancyhead[L]{
            \noindent
            \raisebox{1.2ex}{
                \parbox{80ex}{{\py@HeaderFamily\@title}}
            }
        }
        \fancyfoot[L]{\version}
        \fancyfoot[C]{\thepage\ of \pageref{LastPage}}
        \fancyfoot[R]{\@date}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
    }
\makeatother
'''

custom_latex_preamble_2 = r'''
% For the number of the last page in the document
\usepackage{lastpage}

% Needed to override a previous declaration where the footrulewidth is 0pt 
\renewcommand{\footrulewidth}{0.4pt}

\makeatletter
    % Set headers and footers for {empty} pages (the first page of a chapter) 
    \fancypagestyle{empty}{
        \fancyhf{}
%        \fancyhead[R]{\sphinxincludegraphics[scale=0.75]{Artos_vectorised.pdf}}
        \fancyfoot[L]{\version}
        \fancyfoot[R]{\@date}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
        \renewcommand{\footskip}{40pt} % This pushes the footer down to match the footers on other pages (default 30pt)
    }
    
    % Set headers and footers for {fancy} pages (not the first page of a chapter) 
    \pagestyle{fancy}{
        \fancyhf{}
        \fancyhead[L]{
            \noindent
            \raisebox{1.2ex}{
                \parbox{80ex}{{\py@HeaderFamily\@title}}
            }
        }
        \fancyfoot[L]{\version}
        \fancyfoot[C]{\thepage\ of \pageref{LastPage}}
        \fancyfoot[R]{\@date}
        \renewcommand{\headrulewidth}{0.4pt}
        \renewcommand{\footrulewidth}{0.4pt}
    }
\makeatother
'''

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # One-sided printing.
    'extraclassoptions': 'openany,oneside',
    #'classoptions': ',oneside,openany',
    #'babel': r'''\usepackage[english]{babel}''',

    # Additional stuff for the LaTeX preamble.
    #'preamble': custom_latex_preamble,
    'preamble': custom_latex_preamble_2,

    # Latex figure (float) alignment
    #
    'figure_align': 'H',

    
    
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Artos.tex', u'Artos Documentation',
     u'Arpit Shah & contributors', 'manual', True),
]

# The name of an image file (relative to this directory)
latex_logo = "../images/ArtosFull_vectorised.pdf"

latex_additional_files = [
    '../images/ArtosFull_vectorised.pdf',
    '../images/Artos_vectorised.pdf',
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'artos', u'Artos Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Artos', u'Artos Documentation',
     author, 'Artos', 'Art of System Testing, Framework which works out of the box',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

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

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True