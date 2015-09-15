"""
makesite.py - Super simple static site generator.

Dynamically generates static html pages from Markdown text files. The script
searches for a 'style.css', 'template.html' and Markdown files '*.md',
recursively, and converts the text files into html pages. It also generates
a navbar bar with links to all the pages.

Notes
-----

The markup language can be modified by editing the function 'get_content()'. 

Absolute paths must start with './', e.g., ./style.css, ./about/index.html.

Fernando Paolo <fspaolo@gmail.com>
Apr 8, 2015

"""
import os
import fnmatch
import datetime as dt
import markdown as md
from collections import OrderedDict

# Markdown files and folders to ignore
ignore = ['README.md', 'example']

# file names and extentions
python_file = 'makesite.py'
style_file = 'style.css'
template_file = 'template.html'
text_file_ext = ('.md')
img_file_ext = ('.jpg', '.png')

navbar = None 

# to define your own navigation bar uncomment the lines below
navbar = OrderedDict([
('Download', 'https://github.com/fspaolo/makesite/'),
])


def get_files(directory, ext=('.md'), ignore=[]):
    """Get all the files that match the extensions (recursively)."""
    matches = []
    for root, dirs, files in os.walk(directory):
        matches += [root + '/' + f for f in files if f.endswith(ext)]
    return _ignore_files(matches, ignore)


def _ignore_files(files, ignore):
    for i in ignore:
        files = [f for f in files if i not in f]
    return files


def was_modified(filein, hours=.5):
    """Check whether file was modified within the last 'hours'."""
    modtime = os.path.getmtime(filein)
    modtime =  dt.datetime.fromtimestamp(modtime)
    return modtime > dt.datetime.today() - dt.timedelta(hours=hours)


def get_content(text_file):
    """Transform text file to html content."""
    basename, ext = os.path.splitext(text_file)
    text = open(text_file).read()
    return md.markdown(text, output_format='html5') 


def get_navbar(paths):
    """Generate html navbar bar (one link per text file)."""
    try:
        # generate nav from provided dictionary
        names = paths.keys()
        paths = paths.values()
    except:
        # generate nav automatically from file names
        names = [f.split('/')[1].split('.')[0] for f in paths]
        names = ['Home' if n == 'index' else n.title() for n in names]
    paths = [p.replace('.md', '.html') for p in paths]    # FIXME
    nav_templ = '<a href="%s">%s</a>\n&nbsp;&nbsp;&nbsp;&nbsp;'
    html_nav = '\n'.join([nav_templ % (p, n) for p, n in zip(paths, names)])
    return '<p>\n' + html_nav + '\n</p>'


def get_template(template_file):
    """Read content of html template file."""
    return open(template_file).read()


# generate the site if any of the text, css or template files were modified

text_files = get_files('.', ext=text_file_ext, ignore=ignore)

for text_file in text_files:
    if was_modified(text_file, hours=.1) or \
       was_modified(style_file, hours=.1) or \
       was_modified(template_file, hours=.1) or \
       was_modified(python_file, hours=.1):

        html_template = get_template(template_file)
        html_content = get_content(text_file)
        if navbar is None:
            html_navbar = get_navbar(text_files)
        else:
            html_navbar = get_navbar(navbar)

        # build html page
        html_template = html_template.replace('<!-- NAVBAR -->', html_navbar)
        html_template = html_template.replace('<!-- CONTENT -->', html_content)

        # if file is in a folder, change absolute to relative paths
        basename = os.path.split(text_file)[0]
        if os.path.isdir(basename) and basename != '.':
            html_template = html_template.replace('./', '../') 

        base = os.path.splitext(text_file)[0]
        f = open(base + '.html', 'w').write(html_template)
        print text_file, '-> to html'
