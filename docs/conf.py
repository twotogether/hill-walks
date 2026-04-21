project = 'Hill Walks'
copyright = '2026, Mohana Das'
author = 'Mohana Das'

extensions = [
    'myst_parser',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'furo'
html_static_path = ['_static']
html_theme_options = {
    "sidebar_hide_secondary": False,
}

myst_enable_extensions = [
    "deflist",
    "html",
]

source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext',
}
