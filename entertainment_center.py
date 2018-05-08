import media
import fresh_tomatoes # must be in current folder file
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=Ny_hRfvsmU8")
# print (toy_story.storyline)
# toy_story.show_trailer()
avatar = media.Movie("Avatar","The story of a marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock = media.Movie("School of Rock","The life of a Rock & Roll Enthusiast",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
Titanic = media.Movies("Titanic", "A love story of a heiress and poor man aboard the Titanic",
                       "https://en.wikipedia.org/wiki/File:Titanic_poster.jpg",
                       "https://www.youtube.com/watch?v=zCy5WQ9S4c0")
The_Terminator = media.Movies("The Terminator","A cyborg assasin sent back in time to kill a post-apocalyptic savior's mom",
                              "https://en.wikipedia.org/wiki/File:Terminator1984movieposter.jpg",
                              "https://www.youtube.com/watch?v=c4Jo8QoOTQ4")
strange_days = media.Movies("strange days", " A man solves a murder set in the future, with the use of recordings that allow a user to experience the recorder's memories and physical sensation",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Strangedays.jpeg",
                            "https://www.youtube.com/watch?v=wE2dO6UyK3Q")
Solaris = media.Movies("Solaris","The chronologized events of a crew aboard the space station Solaris",
                       "https://upload.wikimedia.org/wikipedia/en/b/bf/Solaris2002poster.jpg",
                       "https://www.youtube.com/watch?v=rvm7WMbXfeY")
movies = [toy_story, avatar, school_of_rock, Titanic, The_Terminator, strange_days, Solaris]
fresh_tomatoes.open_movies_page(movies)
# print (media.Movie.VALID_RATINGS)
# print (media.Movie.__doc__)
