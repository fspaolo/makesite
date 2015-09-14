# Makesite.py
**Extremely simple static site generator**

`Makesite.py` is a static site (single script) generator written in Python.
You write your content in text files and `Makesite.py` does the rest for you.
It works by taking as input a template (HTML), a style (CSS), and a bunch of
text files (Markdown) to generate static HTML pages.

Download the following files to the same folder:

    template.html -- the skeleton of the webpage
    style.css     -- the style of the webpage
    index.md      -- the content of the webpage

and run:

    python makesite.py


**Important**: This is not a blog! `Makesite.py` was developed with the
following principles in mind:

* Extremely simple (very easy to understand and modify)
* No installation required (run everywhere)
* All functions in one single script (that I can actually understand)
* No templating languages (just pure HTML, CSS and Python!)
* Minimal setting (one text file => one HTML page) 
* Navigation bar generated for you (customizable if you prefer)

If all you want is to put simple HTML content on the web (such as a personal
webpage), then this might be the tool you are looking for.
