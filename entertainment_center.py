import media
import fresh_tomatoes # must be in current folder file
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=Ny_hRfvsmU8")
# print (toy_story.storyline)
# toy_story.show_trailer()
avatar = media.Movie("Avatar","A Marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
school_of_rock = media.Movie("School of Rock","The life of a Rock & Roll Enthusiast",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

movies = [toy_story, avatar, school_of_rock]
fresh_tomatoes.open_movies_page(movies)
# print (media.Movie.VALID_RATINGS)
# print (media.Movie.__doc__)
