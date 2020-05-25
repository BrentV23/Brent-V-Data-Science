import pandas as pd

#replace link with non-dynamic link
df = pd.read_csv("https://raw.githubusercontent.com/BrentV23/Brent-V-Data-Science/master/Restaurant_Data.csv")

df.head()

cuisineValid = False
while cuisineValid == False:
  cuisine = input("Enter cuisine: ")
  if cuisine == "Western" or "Asian":
    cuisineValid = True
  
    
deliveryValid = False
while deliveryValid == False:
  delivery = input("Delivery?: ")
  if delivery == "Yes" or "yes" or "y" or "Y":
    deliveryValid = True
  

locationValid = False
while locationValid == False:
  location = input("Enter cuisine: ")
  if location == "Western" or "Asian":
    locationValid = True
  

