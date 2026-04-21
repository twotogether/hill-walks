import sys
from pathlib import Path

# Copy GPX files before building
sys.path.insert(0, str(Path(__file__).parent))
from _build_gpx import copy_gpx_files
copy_gpx_files()

project = 'Hill Walks'
copyright = '2026, Mohana Das'
author = 'Mohana Das'
html_title = 'Hill Walks'

extensions = [
    'myst_parser',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['gallery.css']
html_theme_options = {
    "sidebar_hide_secondary": False,
}

myst_enable_extensions = [
    "deflist",
    "colon_fence",
]

source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext',
}
