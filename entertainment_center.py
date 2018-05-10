import media # is a module or source file with a reference to the class Movie 
import fresh_tomatoes # must be in current folder file
# The class Movie calls the init method, which returns an instance of the following variables: the title, a short synopsis of the storyline,
# an image, and a trailer url
toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=Ny_hRfvsmU8")
avatar = media.Movie("Avatar","The story of a marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock = media.Movie("School of Rock","The life of a Rock & Roll Enthusiast",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
Titanic = media.Movie("Titanic", "A love story of a heiress and poor man aboard the Titanic",
                       "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg",
                       "https://www.youtube.com/watch?v=zCy5WQ9S4c0")
The_Terminator = media.Movie("The Terminator","A cyborg assasin sent back in time to kill a post-apocalyptic savior's mom",
                              "https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg",
                              "https://www.youtube.com/watch?v=c4Jo8QoOTQ4")
strange_days = media.Movie("strange days", " A man solves a murder set in the future, with the use of recordings that allow a user to experience the recorder's memories and physical sensation",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Strangedays.jpeg",
                            "https://www.youtube.com/watch?v=wE2dO6UyK3Q")
Solaris = media.Movie("Solaris","The chronologized events of a crew aboard the space station Solaris",
                       "https://upload.wikimedia.org/wikipedia/en/b/bf/Solaris2002poster.jpg",
                       "https://www.youtube.com/watch?v=rvm7WMbXfeY")
The_Abyss = media.Movie("The Abyss", "Story of a underwater oil rig and a chance encounter",
                        "https://upload.wikimedia.org/wikipedia/en/a/ad/TheAbyss.jpg",
                        "https://www.youtube.com/watch?v=WYPcLYPoaxo")
movies = [toy_story, avatar, school_of_rock, Titanic, The_Terminator, strange_days, Solaris, The_Abyss]
fresh_tomatoes.open_movies_page(movies)

