import pandas as pd

sales_data = pd.DataFrame({
    'Product': ['A','B','C','A','B','A','D','E','C','B'],
    'Quantity': [5,3,6,2,4,7,1,8,2,5]
})

top_products = sales_data.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)

print(top_products)
