import pandas as pd 

df=pd.read_csv("leetcode_200.txt")
print(df.head())

#Split the 'Phase' column into new columns
df[["Phase Number", "Phase Name"]]=df["Phase"].str.split(":", n=1, expand=True)


#Remove extra spaces

df["Phase Number"] = df["Phase Number"].str.strip()
df["Phase Name"]= df["Phase Name"].str.strip()

cols=["Phase Number","Phase Name","Week","Day","Problem Number","Problem Name",
      "Difficulty","Pattern", "Priority","Completed","Notes","LeetCode Link"]

df=df[cols]

df.to_excel("leetcode_roadmap_clean.xlsx", index=False)
