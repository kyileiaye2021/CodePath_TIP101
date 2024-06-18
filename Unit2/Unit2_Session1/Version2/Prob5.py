#unit 2
#session 1
#ver 2
#probl 5

#iterate over the second catalog
#if the current key is in the first catalog or not
#if it's, update the value
#if it's not, add the current key and value to the first catalog
#return catalog1

def merge_catalogs(catalog1, catalog2):
  for key in catalog2:
    if key in catalog1:
      catalog1[key] = catalog2[key] #update the value 

    else: #add the key value of the new item
      #catalog1[key] = catalog2[key] the same thing as the following statement
      catalog1.update({key: catalog2[key]})

  return catalog1

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
print(merge_catalogs(catalog1, catalog2))