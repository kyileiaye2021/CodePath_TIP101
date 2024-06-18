#unit 2
#session 1
#ver1
#problem 7

#iterate over the book list of dictionary
#create a var to keep track of the largest rating
#create a dict to keep track of the dict that includes the largest rating
#update the highest_rating if the current rating is greater in each iteration
#update the book dict 
#return the dict 

def highest_rated(books):
  highest_rating = books[0]["rating"]
  book = {}

  for dict in books:
    if dict["rating"] > highest_rating:
      highest_rating = dict["rating"]

      book = dict

  return book


books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))