import pandas as pd
data={
    "Product":["Makana","Aam-Acchar","T-shirt"],
    "Category":["Snacks","Pickle","Cloths"],
    "Price":["500","60","200"],
    "Stock":["2","5","10"]
}
df=pd.DataFrame(data)
# Convert Price and Stock to numeric
df['Price']=pd.to_numeric(df['Price'])
df['Stock']=pd.to_numeric(df['Stock'])



print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
#select a coloumn
print(df[['Product','Price']])
# Select row my index
print(df.iloc[0])
print(df.iloc[1:2])
# Rows where category is Cloths
cloths=df[df['Category']=='Cloths']
print(cloths)
#Rows where category is Snacks
snk=df[df['Category']=='Snacks']
print(snk)
# Expensive items
exp=df[df['Price'] > 50]
print("Expensive items")
print(exp)


df.to_csv("ecommerce_products.csv",index=False)