`Makesite.py` is an extremely simple static site generator written in Python.
You write your content in text files and `Makesite.py` does the rest for you.
It works by taking as input an HTML template, a CSS style, and a bunch of
text files (in Markdown) and generating static HTML pages.

## How it works

Place the following files into a folder:

    makesite.py   -- the script to generate each webpage
    template.html -- the skeleton of each webpage
    style.css     -- the style of each webpage
    index.md      -- the content of a webpage

and run:

    python makesite.py

This will generate an `index.html`.

## What this is

`Makesite.py` is not a blog generator! If a blog is what you are looking for, there are
a few dozens of blog softwares out there. `Makesite.py` was developed
with the following concepts in mind:

* Extremely simple (very easy to understand and modify)
* No installation required (run everywhere)
* No setup required (provide a text file, get an HTML page)
* No templating language (just pure HTML, CSS and Python!)
* All functions in one single script (that I can actually understand)
* Navigation bar generated for you (customizable if you prefer)

If all you want is to simply put HTML content on the web (such as a personal
webpage), then this might be the right tool for you.

Please note that this project is still in the experimental stage.

## Example

To get you started we provide a full basic website structure (with a `Makefile`
included):

    example/
       |__ Makefile
       |__ makesite.py 
       |__ template.html 
       |__ style.html 
       |__ index.md 
       |__ first/ 
              |__ index.md 
       |__ second/ 
              |__ index.md 
       |__ third/ 
              |__ index.md 

To get the HTML pages: 

    cd example
    python makesite.py

or using the `Makefile`:

    cd example
    make

Now all you have to do is replace the content of the Markdown files (`.md`)
with your own. For each Markdown file an HTML page will be created and added
to the navigation bar. Then you just upload the existent and generated files
in the `example` folder to any webserver.

In this example each webpage (Markdown file) is placed into a sub-folder to
keep things organized (with the exception of the website's landing page, the
'Home' page), but you can have all pages in the same folder if you prefer.

To customize your website you can play around with the `style.css` and/or
`template.html`.

A `Makefile` is also provided for convenience. For example, to generate the
website and upload it to [GitHub](https://pages.github.com/) you can do:

    cd example
    make
    make show
    make git

--Happy coding!
