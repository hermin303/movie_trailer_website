# importing file for web platform
import fresh_tomatoes

# importing class for the movies
import media

# creating all and each one of the movies
# selected with the corresponding information

commando = media.Movie("Commando",
                       "Action",
                       "Mark L. Lester",
                       "1985",
                       "A story of a Soldier named Matrix who"
                       "sets out to rescue his kidnapped daughter",
                       "https://supercultshow.files.wordpress.com/2014/02/commando-poster.jpg",  # noqa
                       "https://www.youtube.com/watch?v=mh-QUh69MCg")

the_last_samurai = media.Movie("The Last Samurai",
                               "Action",
                               "Edward Zwick",
                               "2003",
                               "An ex american soldier who decided to"
                               "fight beside samurai against western powers",
                               "https://upload.wikimedia.org/wikipedia/en/c/c6/The_Last_Samurai.jpg",  # noqa
                               "https://www.youtube.com/watch?v=oRrckyRrG20")

gattaca = media.Movie("Gattaca",
                      "Thriller",
                      "Michael Nyman",
                      "1997",
                      "A scientist of the future society"
                      "forces his way to get to a spaceship"
                      "without genetic requirements",
                      "https://upload.wikimedia.org/wikipedia/en/b/bb/Gataca_Movie_Poster_B.jpg",  # noqa
                      "https://www.youtube.com/wadisoplkatch?v=hWjlUj7Czlk")


the_pursuit_of_happiness = media.Movie("The pursuit of happiness",
                                       "Biographical film",
                                       "Gabiele Muccino",
                                       "2006",
                                       "Christ Gadner went from"
                                       "homeless to have a millionaire"
                                       "career pursuying greatness",
                                       "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg",  # noqa
                                       "https://www.youtube.com/watch?v=89Kq8SDyvfg")  # noqa

hurracane_carter = media.Movie("The hurracane",
                               "Trial drama",
                               "Norman Jewison",
                               "1999",
                               "Rubin Carter was in jail went to jail because"
                               "of hate and get freedom because of love",
                               "https://upload.wikimedia.org/wikipedia/en/7/74/The_Hurricane_poster.JPG",  # noqa
                               "https://www.youtube.com/watch?v=wjYQ0CkAbLU")


the_training_day = media.Movie("The training day",
                               "Action film",
                               "Antoine Fuqua",
                               "2001",
                               "Apprentice ruins the day of a"
                               "master who plan to kill him after"
                               "teaching him bad things",
                               "https://upload.wikimedia.org/wikipedia/en/b/b3/Training_Day_Poster.jpg",  # noqa
                               "https://www.youtube.com/watch?v=DXPJqRtkDP0")

# creating the list for the movies selectes
movies = [commando, the_last_samurai, gattaca,
          the_pursuit_of_happiness, hurracane_carter, the_training_day]

# creating the mechanism to display the website
fresh_tomatoes.open_movies_page(movies)
