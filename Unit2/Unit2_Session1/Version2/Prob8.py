#unit 2
#session 1
#ver 2
#prob 8

#iterate over the product_scores
#compare the value of each key to the threshold
#update the value of each key based on the conditons

def quality_control(product_scores, threshold):
  for score in product_scores:
    if product_scores[score] >= threshold:
      product_scores[score] = "pass"
    else:
      product_scores[score] = "fail"

  return product_scores

scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold = 60
print(quality_control(scores, threshold))