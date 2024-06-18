#unit 2
#session 1
#ver 3
#prob 5

#create a dict
#iterate over the book_ratings (outer loop)
#create a var to store the total value
#iterate over the list of the values
#accumuate the total var
#assign the key value pair in the dict
#return the dict

def average_book_ratings(book_ratings):
  book_dict = {}
  for key, value in book_ratings.items():
    #book_dict[key] = round(sum(value) / len(value), 1)
    book_dict[key] = f"{sum(value) / len(value):.1f}"


  return book_dict


book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}
print(average_book_ratings(book_ratings))