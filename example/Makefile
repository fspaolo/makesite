.PHONY: thumb show git help

default:
	python makesite.py 

show:
	open index.html 

git:
	git commit -am 'updated site'
	git push

help:
	@echo "Usage"
	@echo "make - generates the website (converts *.md -> *.html)"
	@echo "make thumb - generates image thumbnails"
	@echo "make show - generates the website and opens 'index.html' on the browser"
	@echo "make git - upload the website to github (git add *; git commit -m; git push)"

