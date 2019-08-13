# PyApiDocs
Generating Python API documents using Sphinx

This repository shows an example how to generate Python API documentations using the Sphinx. The documentation is built with `Sphinx` using a theme provided by the `Read the Docs`.

# Installation and Setup
1. Install the Sphinx
```bash
# setup the development environment
virtualenv --python=`which python3` .venv
source .venv/bin/activate

# install the Sphinx
pip install Sphinx

# create a 'docs' directory to set up the tool
mkdir docs
cd docs

# setup the Sphinx
sphinx-quickstart

> Separate source and build directories (y/n) [n]: y

The project name will occur in several places in the built documentation.
> Project name: PyApiDocs
> Author name(s): Jieun Lee
> Project release []: 0.0.1

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
> Project language [en]: en
```
2. Modify `docs/source/conf.py`
```python
# uncomment these lines and change the path
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# add extentions to augo generate docs and support Google style Python docstrings
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon' # it understands other docstrings format such as Google style
]

# (optional) change themes
html_theme = 'classic'

# (optional) to document the consturctor '__init__()'
autoclass_content='both'
```
3. Add docstrings to the source codes
[Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
4. Add new rst file for each module/class and update `index.rst`
for a module, e.g. `src.rst`
```reStructuredText
Example (Title for Table of Contents)
*************************************

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. automodule: src
    :members:
    :undoc-members:
    :show-inheritance:

Class name for ToC
==================
.. automodule: src.classname

```
In `index.rst`, add `src`
```reStructuredText
Welcome to PyApiDocs's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   src
```
5. Add `.nojekyll` in `/docs` to ignore Github Page style
6. Add `index.html` under `/docs` to generate Github Page and add the codes into the file
```html
<meta http-equiv="refresh" content="0; url=./build/html/index.html" />
```
6. Generate Docs in HTML
```bash
# make sure current working direcotory is 'docs'
make clean html
open index.html
```