from sklearn.svm import l1_min_c
import pandas as pd
from datetime import date as d

def absent_list():
    l=[]
    p=d.today();date=str(p)
    #to read the excel file 
    df=pd.read_excel("Book1.xlsx")
    for i in range(len(df.columns)-3):
        if df[date][i]=='Absent':
            l.append(df['Name'][i])
        else:
            continue
    return l

if __name__ == '__main__':
    print(absent_list())    