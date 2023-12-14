
from distutils.command.sdist import sdist
from operator import ne
from pyexpat.errors import messages
from minproject import facedetection_datasheet as fdd
from minproject import faceRecognition as fr
from minproject import message as mes
from minproject import detect_mask_video as detmsk
from minproject import absent_list as ab
from turtle import mode
from nbformat import read, write
import pandas as pd
from datetime import date as d
from sqlalchemy import column, false
import time 

    

def face_detection():
    name=fr.facerecognition()
    return name

def faceadd(new_name):

    fdd.crt_facerecognition(new_name)
    print( new_name," ,your face was added successfully")
    
def mskreco():
    stat=detmsk.mask_recognition()
    return stat



def attendence(name):
    p=d.today();date=str(p)
    #to read the excel file 
    df=pd.read_excel("Book1.xlsx")

    #print(df)
    #print('\n\n\n')
    col=df.columns
    leng=len(col)

    #create a column with todays date 
    if leng<=3 or str(col[leng-1])!=date:
        df[date]='Absent'

    #to update the attendence
    df.loc[df.index[df['Name']==name],date]='Present'
    print("Attendace updated\n",df)
    df.to_excel("Book1.xlsx",index=False)



if __name__ == '__main__':
    while True: 
        flag=input("\n\n\n1.New Entry?\n2.Attendance\n3.Exit\nPLease enter your choice ")
        if flag=='3':
            break
        elif flag=='1':
            new=input("\n\n\nPlease enter your name: ")
            faceadd(new)
        elif(flag=='2'):
            name=face_detection()
            print("\n\n\n\n\Please remove your mask \n")
            print(name)
            print("\n\n\n\n\nPlease wear your mask ")
            while True:
                stat=mskreco()
                if stat=='Mask':
                    break
                else:
                    print("\n\n\n\nPlease wear your mask")
                    time.sleep(3)
                    continue
            print('\n\n\n\n\n\n\n\n\n\n')
            print('Face detected, Name: ',name)
            mes.log_message(log_name=name)
            attendence(name)
    l=ab.absent_list()
    print(l)
    for n in l:
        mes.absent_message(abst_name=n)