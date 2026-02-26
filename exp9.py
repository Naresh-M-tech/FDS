import pandas as pd

property_data = pd.DataFrame({
    'PropertyID': [1,2,3,4],
    'Location': ['CityA','CityB','CityA','CityC'],
    'Bedrooms': [3,5,4,6],
    'Area': [1500,2000,1800,2500],
    'Price': [300000,500000,400000,600000]
})

# 1. Average price per location
print(property_data.groupby('Location')['Price'].mean())

# 2. Properties with >4 bedrooms
print("Count:", len(property_data[property_data['Bedrooms'] > 4]))

# 3. Property with largest area
print(property_data.loc[property_data['Area'].idxmax()])
