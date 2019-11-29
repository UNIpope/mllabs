import pandas as pd
from pprint import pprint
import collections

#read in hedders
head = []
with open("feature_names.txt") as f:
    for line in f:
        head.append(line.strip())

#read in data set
df = pd.read_csv("trainingset.csv", na_values="?")
df.columns = head

# split data in continus and catigorical
con = df
cat = df 

con = con.drop(columns=["id", "job", "marital", "education", "default", "housing", "loan", "contact", "month","poutcome","target"])
cat = cat.drop(columns=["id","age","balance","day","campaign","pdays","previous"])

#compute values and write to file
with open("CONT.csv","w+")as f:
    f.write("Feature, Count, % Miss., Card., Min., 1st Qrt., Mean, Median, 3rd Qrt., Max., Std. Dev.\n")
    for col in con.columns:
        print(col)
        ls = []
        ls.append(col)
        #print(con[col])
        ls.append(con[col].count())

        cofval = collections.Counter(con[col])
        if " ?" in cofval.keys():
            ls.append(cofval[" ?"] / ls[1] * 100)
        else:
            ls.append(0)

        ls.append(con[col].nunique())
        ls.append(con[col].min())
        ls.append(con[col].quantile(.25))
        ls.append(con[col].mean())
        ls.append(con[col].median())
        ls.append(con[col].quantile(.75))
        ls.append(con[col].max())
        ls.append(con[col].std())

        f.write(str(ls).replace("[","").replace("]","").replace("'",""))
        f.write("\n")

with open("CAT.csv","w+")as f:
    f.write("Feature , Count , % Miss. , Card. , Mode , Mode Freq. , Mode % , 2nd Mode , 2nd Mode Freq. , 2nd Mode %\n")
    for col in cat.columns:
        print(col)
        ls = [] 
        ls.append(col)
        ls.append(cat[col].count())

        cofval = collections.Counter(cat[col])
        if "unknown" in cofval.keys():
            ls.append(round(cofval["unknown"]/ ls[1] * 100, 2))
        else:
            ls.append(0)
        
        ls.append(cat[col].nunique())
        ls.append(cat[col].mode()[0])
        ls.append(cat[col].value_counts()[ls[4]])
        ls.append(round(ls[5]/(ls[1] - ls[2])* 100, 2))
        ls.append(list(cat[col].value_counts().index)[1])
        ls.append(cat[col].value_counts()[ls[7]])
        ls.append(round(ls[8]/(ls[1] - ls[2])* 100, 2))

        f.write(str(ls).replace("["," ").replace("]"," ").replace("'"," "))
        f.write("\n")

    