from firebase import firebase

con=firebase.FirebaseApplication('https://helo-db6d7.firebaseio.com/',None)




while True :
    choice=int(input("1:Write a massage\n2:Read message\n"))
    if (choice==1):
        sender=input("Enter your Name : ")
        getter=input("Enter where to send : ")
        #-- check--
        
        text =input("Enter your text : ")
        data={'content':[sender,getter,text]}
        con.post('/data/',data)
    if (choice==2):
        read=con.get('/data/',None)
        print(read,'\n')
        name=input("Whats your name ? : ")
        for key in read:
            if (read[key]['content'][1]==name):
                print("From :",read[key]['content'][0],'\n',"To :",read[key]['content'][1],'\n','Text :',read[key]['content'][2])
    if(choice==3):
        con.delete('/data/',None)
