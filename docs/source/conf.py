# pylint: disable=invalid-name, redefined-builtin, wrong-import-position
import sys
from pathlib import Path
repo_relative_path = Path('../..')
repo_abs_path = repo_relative_path.resolve()
sys.path.insert(0, f'{repo_abs_path}')


project = 'Input-Output Guide'
copyright = '2023, Bradley Smith'
author = 'Bradley Smith'
version = '0.1.0'

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
]

templates_path = ['_templates']

exclude_patterns = []


html_theme = 'furo'

html_static_path = ['_static']

copybutton_selector = 'div.highlight pre, pre.literal-block'

autosectionlabel_prefix_document = True
