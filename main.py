import fresh_tomatoes 
from models.movie import * 
import os
import SimpleHTTPServer
import SocketServer
import webbrowser

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
    while True:
        title = raw_input('Enter a movie title: ')
        if len(title.strip()) == 0:
            print "Title can't be blank"
        else:
            break
    results = Movie.search_omdb_by_title(title)
    omdb_data = Movie.choose_from_results(results)





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

