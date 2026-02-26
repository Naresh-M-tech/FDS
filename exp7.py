import pandas as pd

data = {
    'CustomerID': [1, 2, 1, 3, 2],
    'OrderDate': pd.to_datetime(['2024-01-01','2024-01-03','2024-01-05','2024-01-07','2024-01-10']),
    'Product': ['A','B','A','C','B'],
    'Quantity': [2,1,3,5,2]
}

order_data = pd.DataFrame(data)

# 1. Total orders per customer
print(order_data['CustomerID'].value_counts())

# 2. Average order quantity per product
print(order_data.groupby('Product')['Quantity'].mean())

# 3. Earliest and latest order dates
print("Earliest:", order_data['OrderDate'].min())
print("Latest:", order_data['OrderDate'].max())
