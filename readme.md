

### Quick PySite

This was inspired by the blogging platform [jekyll](jekyllrb.com) and created as part of [Udacity.com's](http://udacity.com) nanodegree site . Instead of using a database and serving pages dynamically. It builds several static pages locally before you deploy. This works great for small projects. The idea is that you don't really need a database for every site. I wrote the code with intention of expanding it into a framework for more static sites.  Contact me if you'd like to help.

### Dependencies
- Python 2.7
- PyYaml
- internet connection

### Viewing the site

1. requires python 2.7 and yaml  [PyYaml](http://pyyaml.org/wiki/PyYAML)

2. To run the site cd to the main director of the site and enter `python tomatoes.py`

3. To add a movie type `add` and follow the prompts. 

4. To see the site type `serve` and the site should be running at localhost:8000

### How this works

When you add a site in the command line. The program contacts the [Open movie database api](http://www.omdbapi.com/) and searches for your movie by title.  If your movie is in the results, the program makes another call to the omdb and gets a complete set of data(except for the youtube trailer url). If not, saves the information that you enter manually.  If you want to add more fields, you'll have to change the details in `data/movies/data.yml`

### Making changes

- assets are specified in `templates/application/header.yml`
- local css files should be changed in `assets/css/`
- local scripts should be changed in `assets/script`
  DO Not try and make changes to the file in the public folder. This is build automatically when the site 
  is built. All your changes will be lost the next time the site is built


- Movie information is stored and saved in `data/movies/data.yml` you can make updates and deletions and they will be reflected in the site when it is rebuilt.

