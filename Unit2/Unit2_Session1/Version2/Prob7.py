#unit 2
#session 1
#ver 2
#prob 7
'''
1) Create an empty ratings dict
2) Create an empty counts dict
3) For each movie in our input
  a) If genre already in our dicts
     i) Add the movie's rating to that genre's rating total
    ii) Add 1 to that genre's movie total
  b) Otherwise, add the rating as a new entry and set count to 1

4) Highest avg rating starts at 0
5) Loop through each genre
  a) Calculate the average using the ratings and counts for that genre
  b) If the avg is higher, make new highest avg
6) Return the name of the highest avg genre

'''
def most_popular_genre(movies):
  genre_rating = {}
  genre_occurence = {}

  for movie in movies:
    curr_genre = movie["genre"]

    if curr_genre in genre_rating:#if the current genre is in the dict
      #update the total rating and occurence
      genre_rating[curr_genre] += movie["rating"]
      genre_occurence[curr_genre] += 1

    else:#if it's not in the dict
      genre_rating[curr_genre] = movie["rating"]
      genre_occurence[curr_genre] = 1

  curr_highest_avg_rating = 0 #to keep track of the highest avg rating
  most_popular = None #to keep track of the genre that has the highest avg rating

  for genre in genre_rating:
    avg_rating = genre_rating[genre] / genre_occurence[genre]
    if avg_rating > curr_highest_avg_rating:
      curr_highest_avg_rating = avg_rating
      most_popular = genre

  return most_popular 

movies = [
  {"title": "Inception",
   "genre": "Science Fiction",
   "rating": 8.8
  },
  {"title": "The Matrix", 
   "genre": "Science Fiction",
   "rating": 8.7
  },
  {"title": "Pride and Prejudice", 
   "genre": "Romance",
   "rating": 7.8
  },
  {"title": "Sense and Sensibility", 
   "genre": "Romance",
   "rating": 7.7
  }
]

print(most_popular_genre(movies))