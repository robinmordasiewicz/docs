# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import f5_sphinx_theme

project = 'Docs'
copyright = '2022, F5'
author = 'Collaborators'
release = '202202152222'

extensions = [
    "sphinxcontrib.youtube",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
    "sphinx-favicon"
]

templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = "f5_sphinx_theme"
html_theme_path = f5_sphinx_theme.get_html_theme_path()
html_sidebars = {"**": ["searchbox.html", "localtoc.html", "globaltoc.html"]}
html_theme_options = {
    "site_name": "Docs",
    "next_prev_link": True
}

#html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"

html_static_path = ['_static']

copybutton_copy_empty_lines = False
copybutton_prompt_text =r'\$ '
copybutton_prompt_is_regexp = True
copybutton_remove_prompts = True
copybutton_line_continuation_character = "\\"
copybutton_only_copy_prompt_lines = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
html_copy_source = False