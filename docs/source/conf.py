# Configuration file for the Sphinx documentation builder.

# -- Project information

import os
import sys
import re
from subprocess import check_output

# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella & Anton'
title = 'User Guide'

# -- Extract current version -------------------------------------------------

try:
    vrex = re.compile(r'TF-M(?P<GIT_VERSION>v.+?)'
                      r'(-[0-9]+-g)?(?P<GIT_SHA>[a-f0-9]{7,})?$')

    version = check_output("git describe --tags --always",
                            shell = True, encoding = 'UTF-8')

    _v = vrex.match(version)
    release = _v.group('GIT_VERSION')
    if _v.group('GIT_SHA'):
        version = release + "+" + _v.group('GIT_SHA')[:7]

except:
    version = release = 'Unknown'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.4'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#    'sphinx.ext.duration',
#    'sphinx.ext.doctest',
#    'm2r2', #Support markdown files. Needed for external code.
    'sphinx.ext.autosectionlabel', #Make sphinx generate a label for each section
    'sphinxcontrib.plantuml', #Add support for PlantUML drawings
#    'sphinxcontrib.rsvgconverter', #Add support for SVG to PDF
    'sphinx.ext.intersphinx', #Links to over projects
]

#    'sphinx_tabs.tabs' #Enable tab extension in Sphinx

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

# PlantUML
on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    pass
#    plantuml = 'java -Djava.awt.headless=true -jar plantuml.jar'
else:
    pass
#    plantuml = 'java -jar ' + os.environ['PLANTUML_JAR_PATH']

plantuml_output_format = 'svg'

#Make auso section labals generated be prefixed with file name.
#autosectionlabel_prefix_document=True
#Add auso section label for level 2 headers only.
#autosectionlabel_maxdepth=2

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
# Changed from None to en
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'readme.rst',
                    'platform/ext/target/cypress/psoc64/security/keys/readme.rst',
                    'lib/ext/**']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

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
    'collapse_navigation' : False,
    'prev_next_buttons_location' : None,   # Hide Prev and Next buttons
#    'display_version': True,    # Show version under logo
    'sticky_navigation': True,
    'navigation_depth': 2,
}

# Remove the "View page source" link from the top of docs pages
html_show_sourcelink = False

#
# Add any paths that contain custom static files (such as style sheets) here,
# relative to configuration directory. They are copied after the builtin static
# files, so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Set the documentation logo relative to configuration directory
#html_logo = '_static/images/tf_logo_white.png'

# Set the documentation favicon
#html_favicon = '_static/images/favicon.ico'

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

#Disable adding conf.py copyright notice to HTML output
html_show_copyright = False

# Disable showing Sphinx footer message:
# "Built with Sphinx using a theme provided by Read the Docs. "
html_show_sphinx = False

#Add custom css for HTML. Used to allow full page width rendering
def setup(app):
    app.add_css_file('css/tfm_custom.css')

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'TF-M doc'

rst_prolog = """
.. |TFM_VERSION| replace:: version
"""

# Enable figures and tables auto numbering
numfig = True
numfig_secnum_depth = 0
numfig_format = {
    'figure': 'Figure %s:',
    'table': 'Table %s:',
    'code-block': 'Listing %s:',
    'section': '%s'
}

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
#texinfo_documents = [
#    (master_doc, 'TF-M', title,
#     author, 'TF-M', 'Trusted Firmware for Cortex-M',
#     'Miscellaneous'),
#]

# -- Extension configuration -------------------------------------------------
