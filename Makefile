all: 
	git pull
	bundle.ruby2.5 exec jekyll build
	find _site -type d -exec chmod a+rx {} +
	find _site -type f -exec chmod a+r {} +
	rsync -a ${HOME}/riceric22.github.io/_site/ ${HOME}/html/ 

clean: 
	bundle.ruby2.5 exec jekyll clean

