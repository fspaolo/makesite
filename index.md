`Makesite.py` is an extremely simple (and extremely light) static site
generator written in Python. You write your content in text files and
`Makesite.py` does the rest for you. It works by taking as input an HTML
template, a CSS style, and a bunch of text files (in Markdown) and
generating static HTML pages.

## How it works

1) Download and place the following files into a folder: 

    makesite.py    -- the Python script to generate each webpage
    template.html  -- the HTML skeleton of each webpage
    style.css      -- the CSS style of each webpage
    index.md       -- the text content of a webpage (Markdown) 

2) Run: 

    python makesite.py

This will generate an `index.html` that you can display with your browser.

Note that every time you make any modification you need to run
`python makesite.py` again (that's what *static* site means).

## What it is

`Makesite.py` is not a blog generator! If a blog is what you are looking for,
there are a few dozen blog softwares out there. `Makesite.py` was developed
with the following concepts in mind:

* Extremely simple (very easy to understand and modify)
* No installation required (run it anywhere)
* No configuration required (you provide a text file, you get a HTML page)
* No templating language (just pure HTML, CSS and Python!)
* All functions in one single script (that I can actually understand)
* Navigation bar generated for you (customizable if you want)

If all you want is to simply put HTML content on the web (such as a personal
webpage), then this might be the right tool for you.

Please note that this project is under development. Features are being added or modified.

## Example

To get you started there a basic website example (with a `Makefile`
included):

    example/
       |__ Makefile
       |__ makesite.py 
       |__ template.html 
       |__ style.css
       |__ index.md 
       |__ first/ 
              |__ index.md 
       |__ second/ 
              |__ index.md 
       |__ third/ 
              |__ index.md 

To generate the HTML pages (after you've downloaded the folder `example`): 

    cd example
    python makesite.py

or using the `Makefile`:

    cd example
    make site

Now all you have to do is replace the content of the Markdown files (`.md`)
with your own. For each Markdown file an HTML page will be created and added
to the navigation bar. Then you just upload the content of the `example` folder
(the `.html`, `.css`, `.jpg`, etc.) to any webserver.

In the above example each webpage (Markdown file) is placed into a sub-folder 
to keep things organized (with the exception of the website's landing page, the
'Home' page), but you can have all the pages in the same folder if you prefer
(just give them different names).

To customize your website you can play around with the `style.css` and/or
`template.html` (see how below).

A `Makefile` is also provided for convenience. For example, on a Mac/Linux
machine you can generate the website, display it in your browser, and upload
it to [GitHub](https://pages.github.com/) as:

    cd example  
    make site
    make show  
    make git  

## In use

Check my own website made with `Makesite.py`: [http://fspaolo.net](http://fspaolo.net)  

## How to 

[Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)  
[HTML](http://www.w3schools.com/html/html_intro.asp)  
[CSS](http://www.w3schools.com/css/)  

**Questions/Comments?** Send me an email: [fspaolo@gmail.com](mailto:fspaolo@gmail.com?Subject=[Makesite.py])
