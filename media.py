import webbrowser
class Video():
    def __init__(self, Video_title, Video_duration):
        self.title = Video_title
        self.duration = Video_duration
class Movie(Video):
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]# THIS IS A CONSTANT, AND STYLE GUIDE STATES ITS BEST IF IT IS IN CAP.
    def __init__(self, Video_title, Video_duration, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, Video_title, Video_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
class TvShow(Video):
    def __init__(self, Video_title, Video_duration, TvShow_season,
                 TvShow_episode, TvShow_station):
        Video.__init__(self, Video_title, Video_duration)
        self.season = TvShow_season
        self.episode = TvShow_episode
        self.station = TvShow_station
    def get_local_listing(self):
        webbrowser.open(self.station)
