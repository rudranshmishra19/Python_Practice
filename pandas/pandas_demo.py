import pandas as pd

# df=pd.read_csv("products.csv")
data={
    "Product":["Apple","Banana","Soap","Shampoo","Orange","Pineapple","Mango","Gauva"],
    "Category":["Fruit","Fruit","Hygiene","Hygiene","Fruit","Fruit","Fruit","Fruit"],
    "Price":[50,20,30,100,60,90,100,304],
    "Stock":[100,150,200,50,80,90,89,45]
}
df=pd.DataFrame(data) #Convert dictonary into data frames
print(df)
print(df.head()) #first 5 rows
print(df.tail()) #last 5 tail
print(df.shape)
print(df.columns)
print(df.info()) #data types and non-null counts
print(df.describe()) #summary statistics for numbers

#select a column
print(df['Product'])

#select multiple columns
print(df[['Product','Price']])

#Select rows by index
print(df.iloc[0]) #First row
print(df.iloc[1:4]) #Rows 2 to 4
#  Filtering data
#Rows where Category is Fruit
fruits=df[df['Category']=='Fruit']
print(fruits)
print()
#Price >50
print("Expensive items ")
expensive_item=df[df['Price']>50]
print(expensive_item)

#Multiple conditions
print()
print("Cheap_fruits")
cheap_fruits=df[(df['Category']=='Fruit') &(df['Price']<50)]
print(cheap_fruits)

#Average price per category
avg_price=df.groupby('Category')['Price'].mean()
print(avg_price)

#Total stock per category
total_stock=df.groupby('Category')['Stock'].sum()
print(total_stock)

#save filtered data to CSV
cheap_fruits.to_csv("cheap_fruits.csv",index=False)

#save expensive data to CSV
expensive_item.to_csv("expensive_items.csv",index=False)