import unittest
import mock
import sys
sys.path.insert(0, '../')
from movie import *

# class MovieTestCase(unittest.TestCase):
# 	def test_movie_create
b = Movie(title="Frozen",imdbID = "tt2294629")
print b.content_to_html(), b.omdb_data
response = Movie.search_omdb_by_title('frozen')

print response