import sys
import os,time
import openpyxl
from firebase import firebase

names=[]
money=[]

#--------Excel-----------------
while True:
    print('\n\n')
    check_ex=input("1. Read from Excel \n2. Upload to Base\n3. Exit\nChoice:")
    if (check_ex=="3"):
        exit()

    if (check_ex=="1"):
        #name=input("Type the name of the excel file :")
        #name=name+".xlsx"
        name='temp.xlsx'
        path='C:/Users/Bobafet/Desktop/PYTHON/car.gr(Cloud,Excel,Filewritting)/'
        path=path+name
        wb = openpyxl.load_workbook(path)
        sheet=wb.get_sheet_by_name('sheet1')
        temp_name=''
        temp_money=sheet['B3'].value
        i=3
        while (temp_name!=None):
            #--Formating-------
            temp_name=sheet['A'+str(i)].value
            h=''
            f=''
            if(temp_name!=None):
                for f in temp_name:
                    if (f!='\n'):
                        h=h+f
            print(h)
            #------------------
            names.append(h)
            money.append(temp_money)
            
            temp_money=sheet['B'+str(i)].value
            i=i+1
        
        print(names,'\n')
        print(money,'\n',len(names),'==',len(money))
    if (check_ex=="2"):
        con=firebase.FirebaseApplication('https://helo-db6d7.firebaseio.com/',None)
        data={'names':names}
        dta={'money':money}
        con.post('/data/',data)
        con.post('/data/',dta)
    
    if(check_ex=='4'):
        con=firebase.FirebaseApplication('https://helo-db6d7.firebaseio.com/',None)
        con.delete('https://helo-db6d7.firebaseio.com/',None)
        
 
