# Makesite.py
**Extremely simple static site generator**

`makesite.py` is a single python script to generate a static websites. You
write your content in text files and `makesite.py` does the rest for you.

Download the following files to the same folder:

    template.html -- the skeleton of the webpage
    style.css     -- the style of the webpage
    index.md      -- the content of the webpage

and run:

    python makesite.py


It works by taking as input a template (HTML), a style (CSS), and a bunch of
text files (Markdown) to generate static HTML pages.

**Warning**: This is not a blog! The purpose of `makesite.py` is:

* Extremely simple (very easy to understand and modify)
* No installation required (run everywhere)
* All functions in one single script (that I can actually understand)
* No templating languages (just pure HTML, CSS and Python!)
* Minimal setting (one text file => one HTML page) 
* Navigation bar generated for you (customizable if you prefer)

If all you want is to put simple HTML content on the web, then this is the
this tool might be for you.
