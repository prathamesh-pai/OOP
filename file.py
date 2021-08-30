import csv 
import os
import time 
class User :
    
    def userInterface(self):
         print("=============================Welcome==============================\n")
         print("1.View the list of available Hospitals and Blood camps\n2.Donate\n3.Request for blood\n4.View requests sent to you\n")
         choice = input("enter your choice\n")
         if choice == '1':
             self.viewhospitals()
         elif choice == '2':
             self.donate()
         elif choice =='3':
             self.request()
         elif choice == '4':
             self.viewrequest()
         else :
             print("Invalid choice\n")

    def create_account (self):
        id = input("Enter your E-mail ID \n")
        duplicate = False
        with open(r"users.csv",'r') as user_data:
         user_data = csv.reader(user_data)
         for row in user_data:
            if id==row[1]:
                duplicate = True
         if duplicate == True :
            print("User with the entered E-mail ID already exists,try again!\n")
            os.system("cls")
            self.create_account()
         else:
            os.system("cls")
            mylist = []
            name = input("Please enter your Name\n")
            mylist.append(name)
            mylist.append(id)
            contact = input("Please enter your mobile number\n")
            mylist.append(contact)
            bloodgroup = input("Please enter your blood group\n")
            mylist.append(bloodgroup)
            password = input("Please enter your password\n")
            mylist.append(password)
            location = input("Enter the location of your residence")
            mylist.append(location)
            print("account created successfully\n")
            os.system("cls")
            with open(r"users.csv",'a') as file:
              writer = csv.writer(file)
              writer.writerow(mylist)
            self.login()

    def login (self):
        id = input("Please enter your Resgistered E-mail ID \n")
        password = input("Please enter your password\n")
        print("Trying to log in....\n")
        time.sleep(2)
        access = False 
        with open(r"users.csv","r") as file:
            user_data = csv.reader(file)
            for row in user_data:
                if id==row[1] and password == row[4]:
                    access = True
                    os.system("cls")
                    self.userInterface()

            if access == False :
                print("You have entered incorrect Email ID or password, please try again\n")
                time.sleep(2)
                os.system("cls")
                self.login()
    def request(self):
        os.system("cls")
        with open("requests.csv",'a') as requests:
            requests_list = csv.writer(requests)
            mylist = []
            name = input("Enter the name of the recipient\n")
            mylist.append(name)
            location = input("Enter the location of recipient\n")
            mylist.append(location)
            group = input("Enter the blood group required\n")
            mylist.append(group)
            requests_list.writerow(mylist)
            print("Requests sent to available users\n")
            x = input("Press 1 to go back to main menu\nPress 0 to exit the application\n")
            while(x!= '1' and x != '0'):
              x=input("invalid input\nTry again\n")
            if x=='1':
                os.system("cls")
                self.userInterface()
            else :
                os.system("cls")
                pass

        
    def viewrequest(self):
        os.system('cls')
        location = input("enter your location\n")
        bloodgroup = input("enter your bloodgroup\n")
        with open("requests.csv",'r') as file:
            requests = csv.reader(file)
            for line in requests:
                if line[1]==location and line[2] ==bloodgroup:
                   print(line[0]+"  "+line[1]+"  "+line[2]+"\n")
            x = input("Press 1 to go back to main menu\nPress 0 to exit the application\n")
            while(x!= '1' and x != '0'):
                x=input("invalid input\nTry again\n")
            if x=='1':
                os.system("cls")
                self.userInterface()
            else :
                os.system("cls")
                pass

    def viewhospitals(self):
        os.system("cls")
        with open("hospitals.csv",'r') as hospitalsfile:
            hospitals = csv.reader(hospitalsfile)
            for line in hospitals:
                print(line[0]+"  "+line[1]+"  "+line[2]+"\n")
            x = input("Press 1 to go back to main menu\nPress 0 to exit the application\n")
            while(x!= '1' and x != '0'):
                x=input("invalid input\nTry again\n")
            if x=='1':
                os.system("cls")
                self.userInterface()
            else :
                os.system("cls")
                pass 
                   
    def donate(self):
        os.system("cls")
        self.viewhospitals()
        with open("hospitals.csv",'r') as listofhospitals:
            hospitals = csv.reader(listofhospitals)
            code = input("Enter the code of the hospital where you are willing to donate\n")
            for line in hospitals:
                if code == line[2]:
                    name = line[0]
                    location = line[1]
                    break
            print(name+","+location+" will contact you through your registered mobile number for further details\n Thank You for donating\n")
            x = input("Press 1 to go back to main menu\nPress 0 to exit the application\n")
            while(x!= '1' and x != '0'):
                x=input("invalid input\nTry again\n")
            if x=='1':
                os.system("cls")
                self.userInterface()
            else :
                os.system("cls")
                pass

    
class Admin :
    def adminLogin(self):
        username = input("Enter username\n")
        password = input("Enter password\n")
        if username == "admin" and password == "admin":
            os.system("cls")
            self.adminInterface()
        else :
            print("Incorrect username or password\n")
            time.sleep(3)
            os.system("cls")
            self.adminLogin()

    def adminInterface(self):
        print("=============================Welcome Admin=================================")
        print("1.Send request to donors of a particular location and blood group\n2.Add a new hospital/blood donation camp to the list \n3.View the list of donors in a particular area")
        print("4.check all the requests")
        choice = input("Enter your choice\n")
        if choice == '1':
            os.system("cls")
            self.sendRequests()
        elif choice == '2':
            os.system("cls")
            self.addhospital()
        elif choice == '3':
            os.system("cls")
            self.viewInArea()
        elif choice == '4' :
            os.system('cls')
            self.checkRequests()
        else :
            print("Invalid choice\n")

    def addhospital(self):
        os.system("cls")
        name = input("Enter the name of the hospital\n")
        mylist = []
        mylist.append(name)
        location = input("Enter the location of the hospital\n")
        mylist.append(location)
        code = input("Enter the hospital code\n")
        mylist.append(code)
        with open("hospitals.csv",'a') as listofhospitals:
            hospitals = csv.writer(listofhospitals)
            hospitals.writerow(mylist)
        print(name+","+location+" has been successfully added to the list\n")
        x = input("Press 1 to go back to main menu\nPress 0 to exit the application\n")
        while(x!= '1' and x != '0'):
            x=input("invalid input\nTry again\n")
            if x=='1':
                os.system("cls")
                self.adminInterface()
            else :
                os.system("cls")
                pass
        
    def viewInArea(self):
        os.system("cls")
        area = input("Enter the location of required donors \n")
        os.system("cls")
        print("======================list of donors=====================================\n")
        with open("users.csv","r") as users:
            user_data = csv.reader(users)
            for row in user_data :
                if area == row[5]:
                    print(row[0]+"  "+row[1]+"  "+row[2]+"  "+row[3]+"\n")
            x = input("Press 1 to go back to main menu\nPress 0 to exit the application\n")
            while(x!= '1' and x != '0'):
               x=input("invalid input\nTry again\n")
            if x=='1':
                os.system("cls")
                self.adminInterface()
            else :
                os.system("cls")
                pass
     
    def checkRequests(self):
        os.system("cls")
        print("===============list of requests=============\n")
        with open("requests.csv",'r') as requests:
            requests_list = csv.reader(requests)
            for line in requests_list:
                print(line[0]+" "+line[1]+" "+line[2]+"\n")
        x = input("Press 1 to go back to main menu\nPress 0 to exit the application\n")
        while(x!= '1' and x != '0'):
            x=input("invalid input\nTry again\n")
            if x=='1':
                os.system("cls")
                self.adminInterface()
            else :
                os.system("cls")
                pass
    def sendRequests(self):
        os.system("cls")
        print("===============send requests====================\n")
        with open("requests.csv",'a') as requests:
            requests_list = csv.writer(requests)
            mylist = []
            name = input("Enter the name of the recipient\n")
            mylist.append(name)
            location = input("Enter the location of recipient\n")
            mylist.append(location)
            group = input("Enter the blood group required\n")
            mylist.append(group)
            requests_list.writerow(mylist)
            print("Requests sent to available users\n")
            x = input("Press 1 to go back to main menu\nPress 0 to exit the application\n")
            while(x!= '1' and x != '0'):
              x=input("invalid input\nTry again\n")
            if x=='1':
                os.system("cls")
                self.adminInterface()
            else :
                os.system("cls")
                pass
print("\n\n\n\n")
print("===========================================================================")
print("                  Blood bank management system")
print("===========================================================================")
n = input("1.USER\n2.ADMIN\n")
os.system("cls")
if n=='1': 
    p = input("1.SIGN IN\n2.SIGN UP\n")
    if p=='1':
        user_login = User()
        os.system('cls')
        user_login.login ()
    elif p == '2':
        new_user = User()
        os.system("cls")
        new_user.create_account()
    else:
        print("Invalid choice\n")
elif n=='2':
    admin = Admin()
    os.system("cls")
    admin.adminLogin()
else :
    print("invalid choice\n")





