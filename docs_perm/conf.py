#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# # Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme
import os
import subprocess

# -- Project information -----------------------------------------------------

project = 'TinyMPC'
copyright = '2023, Anoushka Alavilli, Khai Nguyen, Sam Schoedel'
author = 'Anoushka Alavilli, Khai Nguyen, Sam Schoedel'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

todo_include_todos = False


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

# html_theme_options = {
#     'logo_only': True,
# }

# html_logo = '_static/img/logo.png'
# html_favicon = "_static/img/favicon.ico"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


if not on_rtd:  # only import and set the theme if we're building docs locally
    # Configure the header to display the GitHub edit link for the pages
    html_context = {
        'display_github': True,
        'github_user': 'osqp',
        'github_repo': 'osqp',
        'github_version': 'master/docs/',
    }

    # Override default css to get a larger width for local build
    def setup(app):
        app.add_css_file('css/osqp_theme.css')
else:
    html_context = {
        'css_files': [
                'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
                'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
                '_static/css/osqp_theme.css'],
    }




# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'TinyMPCdoc'


# -- Options for LaTeX output ---------------------------------------------

# latex_elements = {
#     # The paper size ('letterpaper' or 'a4paper').
#     #
#     # 'papersize': 'letterpaper',

#     # The font size ('10pt', '11pt' or '12pt').
#     #
#     # 'pointsize': '10pt',

#     # Additional stuff for the LaTeX preamble.
#     #
#     # 'preamble': '',

#     # Latex figure (float) alignment
#     #
#     # 'figure_align': 'htbp',
#     'sphinxsetup': 'hmargin={1.5cm,1.5cm}',
# }

# # Grouping the document tree into LaTeX files. List of tuples
# # (source start file, target name, title,
# #  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#     (master_doc, 'OSQP.tex', 'OSQP Documentation',
#      'Bartolomeo Stellato, Goran Banjac', 'manual'),
# ]


# -- Options for manual page output ---------------------------------------

# # One entry per manual page. List of tuples
# # (source start file, name, description, authors, manual section).
# man_pages = [
#     (master_doc, 'OSQP', 'OSQP Documentation',
#      [author], 1)
# ]

# -- Options for breathe ---------------------------------------

# # Generate doxygen documentation
# subprocess.call('doxygen doxygen.conf', shell=True)

# breathe_projects = {"osqp": "doxygen_out/xml/"}
# breathe_default_project = "osqp"



# # -- Options for Texinfo output -------------------------------------------

# # Grouping the document tree into Texinfo files. List of tuples
# # (source start file, target name, title, author,
# #  dir menu entry, description, category)
# texinfo_documents = [
#     (master_doc, 'OSQP', 'OSQP Documentation',
#      author, 'OSQP', 'One line description of project.',
#      'Miscellaneous'),
# ]