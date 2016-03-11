.PHONY: site show git


default:
	@echo "Usage" 
	@echo "make site  - generates the website (converts *.md -> *.html)"
	@echo "make show  - generates the website and opens 'index.html' on the browser"
	@echo "make git   - upload the website to github (git add *; git commit -m; git push)"

site:
	python makesite.py 

show:
	open index.html 
	#python -m SimpleHTTPServer 8888

git:
	git commit -am 'updated site'
	git push

