import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/BrentV23/Brent-V-Data-Science/master/Restaurant_Data_New.csv")

cuisineValid = False
while cuisineValid == False:
  cuisine = input("Enter cuisine: ").lower()
  if cuisine == "western":
    cuisineValid = True
    cuisine = "Western"
  elif cuisine == "asian":
    cuisineValid = True
    cuisine = "Asian"
    
deliveryValid = False
while deliveryValid == False:
  delivery = input("Delivery?: ").lower()
  if delivery == "yes" or delivery == "y":
    deliveryValid = True
    delivery = "Yes"
  elif delivery == "no" or delivery == "n":
    deliveryValid = True
    delivery = "No"
  

locationValid = False
while locationValid == False:
  location = input("Enter location: ").lower()
  if location == "belconnen":
    locationValid = True
    location = "Belconnen"
  elif location == "cbd":
    locationValid = True
    location = "CBD"
  elif location == "woden":
    locationValid = True
    location = "Woden"
  elif location == "gungahlin":
    locationValid = True
    location = "Gungahlin"

if delivery == "Yes":
  df = df[df.Delivery == delivery]

df = df[df.Cuisine == cuisine]
df = df[df.Average_rating >= 4]
df[df.Location == location]
