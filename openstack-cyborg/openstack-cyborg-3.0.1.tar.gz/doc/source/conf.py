# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys

sys.path.insert(0, os.path.abspath('../..'))
# -- General configuration ----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    #'sphinx.ext.intersphinx',
    'openstackdocstheme',
    'oslo_config.sphinxconfiggen',
    'oslo_config.sphinxext',
    'oslo_policy.sphinxext',
    'oslo_policy.sphinxpolicygen',
]

# autodoc generation is a bit aggressive and a nuisance when doing heavy
# text edit cycles.
# execute "export SPHINX_DEBUG=1" in your terminal to disable

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'cyborg'
copyright = u'2013, OpenStack Foundation'

# openstackdocstheme options
repository_name = 'openstack/cyborg'
bug_project = 'cyborg'
bug_tag = ''
html_last_updated_fmt = '%Y-%m-%d %H:%M'

config_generator_config_file = '../../tools/config/cyborg-config-generator.conf'
sample_config_basename = '_static/cyborg'

policy_generator_config_file = [
    ('../../tools/config/cyborg-policy-generator.conf',
     '_static/cyborg'),
]

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
# html_theme_path = ["."]
# html_theme = '_theme'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = '%sdoc' % project

# The name for this set of Sphinx documents. If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Cyborg'
html_theme = 'openstackdocs'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    ('index',
     '%s.tex' % project,
     u'%s Documentation' % project,
     u'OpenStack Foundation', 'manual'),
]

# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'https://docs.python.org/': None}
