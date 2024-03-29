
# first you need to import mysql connector library
import mysql.connector as mc #->import without an error

vote_console_app=mc.connect(
    host="", #use your host address
    user="", #use your user name
    password="",#use your password
    database=""#select database
)


access=vote_console_app.cursor()#object


#creating database 
#access.execute("CREATE DATABASE vote_console_app")
# print("Your database successfully created")

# create table
# access.execute("CREATE TABLE voters (Id INT AUTO_INCREMENT PRIMARY KEY , name VARCHAR(255), age INT , party VARCHAR(255))")
# print("Your table successfully created")

#app core

values=[]#store the values

while True:
    print("---->Welcome<----\n")
    print("1 --> Put vote")
    print("2 --> Exit")
    option=int(input("Enter the option >> "))
    if option==1:
        #getting values
        name=str(input("Enter Your name >> "))
        age=int(input("Enter your age >> "))
        print("Select party:")
        print("1 --> ADMK - Adi Dravida Munnettra Kalagam")
        print("2 --> DMK - Dravida Munnettra Kalagam")
        print("3 --> BJP - Bharatha Janatha party")
        print("4 --> INC - Indian National Congress")
        select_party=int(input("Enter the party option >> "))

        #age checker
        if age>=18:
            parties=["ADMK","DMK","BJP","INC"]
            values.append(name)
            values.append(age)
            values.append(parties[select_party-1])
            sql = "INSERT INTO  voters(name, age, party) VALUES (%s, %s, %s)"
            access.execute(sql,values)
            vote_console_app.commit()
            values=[]
            print("Your vote has been succesfully updated .Thankyou")
        else:
            print("Your age is under 18 so you cannot able to put vote,sorry . Thankyou")
            print("____________________________________________________________________")



    
        
    else:
        vote_console_app.close()
        print("Thanks for vote!")
        print("____________________________________________________________________")
        break


























