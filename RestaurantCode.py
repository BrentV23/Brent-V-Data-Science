import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/BrentV23/Brent-V-Data-Science/master/Restaurant_Data.csv")

def filter():
  cuisine_valid = False
  while cuisine_valid == False:
    cuisine = input("Enter Cuisine: ")
    if cuisine == "Western" or cuisine == "Asian":
      cuisine_valid = True
  
  delivery_valid = False
  while delivery_valid == False:
    delivery = input("Delivery?: ")
    if delivery == "Yes" or delivery == "yes" or delivery == "Y" or delivery == "y":
      delivery_valid = True

  location_valid = False
  while location_valid == False:
    location = input("Enter Location: ")
    if location == "Belconnen" or location == "CBD" or location == "Woden" or location == "Gungahlin":
      location_valid = True
filter()
