import fresh_tomatoes 
from models.movie import * 
from lib.site import *
import os
import SimpleHTTPServer
import SocketServer
import webbrowser

def load_manifest(path_to_file):
    config_file = open(path_to_file)
    manifest = yaml.safe_load(config_file)
    config_file.close()
    return manifest

SITE = Website(**load_manifest('manifest.yml'))

def start_server(port=8000 ):
    PORT = port 
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)


    path = "./public/"
    os.chdir( path )


    print "serving at port", PORT
    webbrowser.open('http://127.0.0.1:' + str(PORT) )
    httpd.serve_forever()



def update_movies():
    pass

def edit_movie():
    pass


def add_movie():
    movie_data = {}
    while True:
        movie_data['title'] = raw_input('Enter a movie title: ')
        if len(movie_data['title'].strip()) == 0:
            print "Title can't be blank"
        else:
            break
    results = Movie.search_omdb_by_title(movie_data['title'])
    choice  = Movie.choose_from_results(results)
    if choice == None:
        while True:
            movie_data['poster_url'] = raw_input('Enter a poster url: ')
            if len(movie_data['poster_url'].strip()) == 0:
                print "Poster url can't be blank"
            else:
                break
    else:
        movie_data['imdbID'] = choice['imdbID']
    while True:
        movie_data['trailer_youtube_url'] = raw_input('Enter a url from youtube for the trailer: ')
        if len(movie_data['trailer_youtube_url'].strip()) == 0:
            print "youtube url can't be blank"
        else:
            break
    new_movie = Movie(**movie_data)
    SITE.add_model(new_movie)
    print SITE.data['movies']





choices = {'build': start_server, 
           'update':update_movies,
           'edit':edit_movie,
           'add': add_movie }

def redirect():
    choosing = True
    print """

What would you like to do?"

  Build the site?  --  enter   "build"

  Refresh current movies 
  data through omdb? ---  enter "update"  

  Add a movie?   --- enter "add"
  Edit a current movies? -- enter "edit"
            """
    while choosing:
        try:
            choice = raw_input('Enter Choice: ')
            action = choices[choice]
            choosing = False

        except KeyError:
            print "That was not a valid choice try again"
        else:
            pass
        action()

#print SITE.data['movies']['tt2294629'].nice_yaml()
redirect()
#story - 
    # A user wants to upload some more movies
    # they go into the directory and run .. something



    # User types in add


    # " it returns a list "(only type movie)
    # "is this your movie?"
    #   no
    # "shows next"
    #   yes
    # "What is the youtube url for the trailer you want to add?"
    #   enters blank
    # "Can't be blank"
    #   enters "boo"
    # "Must be in http format"
    #   enters "http://sdfasf.com"
    # Thank you? 
    #   add another
    #   build
    #   main menu
    #   exit




# #Server info

