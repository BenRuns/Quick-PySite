###Udacity Project Instructions
1. Install Python.

2. Create a data structure (i.e. a Python Class) to store your favorite movies, including movie title, box art URL (or poster URL) and a YouTube link to the movie trailer.

3. Create multiple instances of that Python Class to represent your favorite movies; group all the instances together in a list.

4. To help you generate a website that displays these movies, we have provided a Python module called [fresh_tomatoes.py](https://s3.amazonaws.com/udacity-hosted-downloads/ud036/fresh_tomatoes.py) - this module has a function called open_movies_page that takes in one argument, which is a list of movies and creates an HTML file which visualizes all of your favorite movies.

5. Ensure your website renders correctly when you attempt to load it in a browser.


### Running my project

This was inspired by the blogging platform (jekyll)[jekyllrb.com] . Instead of using a database and serving pages dynamically. It builds several static pages locally before you deploy. This works great for small projects. The idea is that you don't really need a database for every site.

### Dependencies
-Python 2.7
-PyYaml

#story - 
	A user wants to upload some more movies
	they go into the directory and run .. something

	The site says "What would you like to do?"

	Buid the site? build

	get omdb update for current movies:
		update
	Add a movie? 
		add
	Edit Current movies? 
		edit



	User types in add

	"Enter the title:""


	"user enters title"

	" it returns a list "(only type movie)
	"is this your movie?"
		no
	"shows next"
		yes
	"What is the youtube url for the trailer you want to add?"
		enters blank
	"Can't be blank"
		enters "boo"
	"Must be in http format"
		enters "http://sdfasf.com"
	Thank you? 
		add another
		build
		main menu
		exit






1. requires yaml .. install via pip PyYaml
An example of the page is running at ...

2. Update movies calls the omdb database and updates the data in the yaml file


Command line:

Add a movie,
Delete a movie
Run the server
update all movies
build

should I use gulp to minifiy?

Build

to enter more movies do

update ratings

view index.html

This will use the open database

How to run tests

How to contribute

