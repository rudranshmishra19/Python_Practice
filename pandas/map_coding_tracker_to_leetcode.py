import pandas as pd
import re


df=pd.read_excel("Coding_Tracker.xlsx")
print(df.columns.to_list())
# File paths
leetcode_file="leetcode_roadmap_clean.xlsx"
tracker_file="Coding_Tracker.xlsx"


#Read both files
df_tracker=pd.read_excel(tracker_file)
df_leetcode=pd.read_excel(leetcode_file)

#Extract DSA Column text and normalize
dsa_texts=df_tracker['Dsa(2hrs)'].dropna().astype(str).tolist()
topics=[]
for text in dsa_texts:
    parts=re.split(r'[,\n;]',text.lower())
    parts=[p.strip() for p in parts if p.strip() and p!= 'skipped']
    topics.extend(parts)
topics=set(topics)

# Ensure Completed column exists
if "Completed" not in df_leetcode.columns:
    df_leetcode["Completed"]=False

#Match logic
def check_completion(problem):
    p=problem.lower()
    return any(p in t or t in p for t in topics)
    
df_leetcode["Completed"]= df_leetcode["Problem Name"].apply(check_completion)

#Overwrite the same Excel file
df_leetcode.to_excel(leetcode_file,index=False)
print(f"Leetcode file updated in place :{leetcode_file}")
