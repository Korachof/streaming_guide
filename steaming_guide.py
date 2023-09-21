# Author: Christopher Partin
# GitHub username: Korachof
# Date: 11/29/2022
# Description: A program that creates a dictionary of movies, adds them to various streaming services, and then makes a
# list of all streaming services that have certain films.

class Movie:
    """Class containing information about movies that could be found on streaming services"""
    def __init__(self, title, genre, director, year):
        """Initializes the movie information"""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """Returns movie title"""
        return self._title

    def get_genre(self):
        """Returns movie genre"""
        return self._genre

    def get_director(self):
        """Returns movie director"""
        return self._director

    def get_year(self):
        """Returns movie release year"""
        return self._year


class StreamingService:
    """Class that contains a dictionary of all streaming services added"""
    def __init__(self, name):
        """Initializes the name and catalog of the streaming services"""
        self._name = name
        self._catalog = {}

    def get_name(self):
        """returns name of the streaming service"""
        return self._name

    def get_catalog(self):
        """returns catalog of the streaming service"""
        return self._catalog

    def add_movie(self, movie_object):
        """adds a movie to a streaming service catalog"""
        self._catalog[movie_object.get_title()] = Movie(movie_object.get_title(), movie_object.get_genre(), \
                                                  movie_object.get_director(), movie_object.get_year())

    def delete_movie(self, movie_title):
        """deletes a movie from a streaming service catalog"""
        self._catalog.pop(movie_title)


class StreamingGuide:
    """A guide for what streaming services have which movies"""
    def __init__(self):
        """Initializes the stream service list"""
        self._stream_service_list = []

    def add_streaming_service(self, streaming_service_object):
        """add a streaming service to the list"""
        self._stream_service_list.append(streaming_service_object)

    def delete_streaming_service(self, streaming_service_name):
        """delete a streaming service from the list"""
        self._stream_service_list.pop(streaming_service_name)

    def where_to_watch_movie(self, movie_title):
        """tells which streaming service will have a certain movie"""
        for streaming_service in self._stream_service_list:
            for key in streaming_service.get_catalog():
                if key == movie_title:
                    movie_in_catalog = streaming_service.get_catalog()
                    title = movie_in_catalog[key].get_title()
                    year = movie_in_catalog[key].get_year()
                    title_year = str(title) + " (" + str(year) + ")"
                    movie_list = []
                    movie_list.append(title_year)
                    movie_list.append(streaming_service.get_name())
                    return movie_list
