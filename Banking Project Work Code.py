print("Hello")
print("*==================WELCOME TO GTH BANK=================*")
print("*=============Please Select your option============*")
abc=print(1,"Create a 'New Bank Account'")
bcd=print(2,"Login")
print("*===================================================*")
cde=choice=int(input("ENTER YOUR CHOICE:"))
if choice==1:
    print("*==============================================*")
    N=input("Enter your Name:")#NAME
    E=input("Enter your Email address:")#EMAILADDRESS
    d= "@gmail.com"or"@yahoo.com"or"@outlook.com"or"@gxnet.com"or"@zohomail.com"or"@aol.com"or"hotmail.com"or"@redifmail.com"or"@yandex.com"
    if d in E:
        print()
    elif d not in E:
        print("Please enter a valid Email address")
        print("or")
        print("Maybe your email address is currently not supported,please write it to us in feedback form we will soon add support to your email address")
        print("Till then keep an eye")
        E=input("Enter your Email address")
    while True:
        xyz=input('Enter your country code:')
        if len(xyz)>3:
            print('Please enter a valid Country code')
            xyz=input('Enter your country code:')
        elif len(xyz)<=3:
            print()
        number =input('Enter your phone number:')
        if len(number)<10:
            print('number is less than 10 digits')
        elif len(number)==10:
            print()
            print('Thank you for providing your Phone Number')
            print()
            break
    U=input("Enter your Username:")
    print()
    while True:
        print('"Enter a good password below which is a mix of alphabets(a-z or A-Z), numbers(0-9) & special characters(!,@,#,$,%,^,&,*)"')
        P=input("Enter your Password:")
        special="@"or"#"or"$"or"%"or"^"or"&"or"*"or"("or")"
        if len(P)<8:
            print("Password should have minimum 8 component")
            print("Re-enter Password again")
            if special not in P:
              print("Password should have special characters")
            elif special in P:
              print()
            if P.isalpha() :
                print("")
            else:
               print("Password should have alphabets in it")
            if P.isdigit():
                print()
            else:
                print("Password should have number in it")
        elif len(P)>=8:
            print("")
            break
    A=input("Enter your Street address:")
    while True:
        B=int(input("Enter your Pincode:"))
        string=str(B)
        if len(string)<6:
            print("invaild pincode")
        elif len(string)>6:
            print("invaild pincode")
        elif len(string)==6:
            print()
            break
    while True:
        C=input("Enter the name of your city:")
        if len(C)<3:
            print("Please enter correct city name")
        elif len(C)>=3:
            break
    while True:
        F=input("Enter the name of your State:")
        if len(F)<3:
            print("Please enter correct state name")
        elif len(F)>=3:
            print()
            break
    print('What type of account do you want to open in our bank?')
    print(1,'Savings Account')
    print(2,'Fixed Deposit Account')
    print(3,'Recurring deposit Account')
    print(4,'Fixed deposit Account')
    print(5,"Money market Account")
    print(6,'Certificate of deposit Account')
    print(7,'Retierment Account')
    Y=int(input('Please enter your choice:'))
    if Y==5:
        print("For such type of bank account the procedure is quite long and currently our bank don't offer such procedures and we don't want to bore you, We will soon find a better way and offer the service to you")
        print('Please enter any other type of account for now, When we will roll out a good procedure for "Money Market Account" we will let you know via an Email')
        Y=int(input('Please enter other type of account:'))
    else:
        print('Thank you your Account type is:',Y)
        print(Y)
    print()
    print("Thankyou for registering ","Your userid is=",U,"Your Password is=",P,'You have a type',Y,'account')
    print("===============================================================================")
    print(1,':To go to the Home Page')
    print(2,":To go to the login portal")
    print(3,':To exit')
    choice=int(input("Enter your choice:"))
    if choice==1:
        print("Hello")
        print("*=========WELCOME TO GTH BANK==========*")
        print(abc)
        print(bcd)
        print(cde)
    if choice==3:
        print("Thank You for using our service, See you soon")
    if choice==2:
        while True:
            print("Hello")
            print("*=========WELCOME TO GTH BANK LOGIN PORTAL==========*")
            S=input("PLEASE ENTER YOUR USERNAME:")
            W=input("PLEASE ENTER YOUR PASSWORD:")
            Z=S!=U
            Y=W!=P
            if Z is True:
                print("Invalid USERNAME OR PASSWORD or BOTH")
                print("Please try again")
                S=input("PLEASE ENTER YOUR USERNAME:")
                W=input("PLEASE ENTER YOUR PASSWORD:")
            elif Z is False:
                print("WELCOME")
            if Y is True:
                print("Invalid USERNAME OR PASSWORD")
                S=input("PLEASE ENTER YOUR USERNAME:")
                W=input("PLEASE ENTER YOUR PASSWORD:")
            elif Y is False:
                print("WELCOME")
                break
        print("Hello,",N,"YOU HAVE OPENED YOUR ACCOUNT!!",'What do you want to do today?')
        print("Your account is currently in active please depoist minimum INR 1000 to activate your account")
        minimumdeposit=int(input("Please Enter minimum amount to activate your account:"))
        while True:
            if minimumdeposit<1000:
                    print("Please enter Minimum amount to activate your account")
                    minimumdeposit=int(input("Please Enter minimum amount to activate your account:"))
            elif minimumdeposit>=1000:
                    print()
                    break
        efg=(input('To continue with the service please answer in Yes otherwise answer in No:'))
        ide=id(number)
        if efg=='yes' or efg=="Yes" or efg=="YES":
            print("Hello:",N,"                               ")
            print("Account number:",ide)
            print("*==========================PLEASE SELECT AN OPTION=======================*")
            print(1,':',"PROFILE")
            print(2,':',"DEPOSITING MONEY OR WITHDRAWL")
            print(3,':',"TAKE A LOAN")
            print(4,':','LOGOUT AND EXIT')
            print(5,':',"FEEDBACK")
            print(6,":",'ABOUT US')
            print("*======================================================================*")
            choice=int(input("Enter your choice:"))
            if choice==1:
                    O={"Name:":N,"Email Address:":E,"Account Type:":Y,"Mobile Numbe:":number,"Address:":A,"City:":C,"State:":F,"Password:":P,"Username:":S}
                    print(O)        
                    print(1,":Edit profile")
                    choice=int(input("Enter your choice:"))
                    if choice==1:
                        print("*==============================Please select following option===============================*")
                        print(1,":Name")
                        print(2,":Email address")
                        print(3,":Mobile Number")
                        print(4,":Address")
                        print(5,":Password")
                        print(6,":Username")
                        print("*=============================================================================================*")
                        new=int(input("Enter your choice:"))
                        if new==1:
                            O={"Name:":N,"Email Address:":E,"Account Type:":Y,"Mobile Number":number,"Address:":A,"City:":C,"State:":F,"Password:":P,"Username:":S}
                            newname=input("Enter your Name:")
                            O1={'Name:':newname}
                            O.update(O1)
                            print(O)
                        elif new==2:
                            O={"Name:":N,"Email Address:":E,"Account Type:":Y,"Mobile Number":number,"Address:":A,"City:":C,"State:":F,"Password:":P,"Username:":S}
                            newemail=input("Enter your Email address:")#EMAILADDRESS
                            d= "@gmail.com"or"@yahoo.com"or"@outlook.com"or"@gxnet.com"or"@zohomail.com"or"@aol.com"or"hotmail.com"or"@redifmail.com"or"@yandex.com"
                            if d in E:
                                print()
                            elif d not in E:
                                print("Please enter a valid Email address")
                                print("or")
                                print("Maybe your email address is currently not supported,please write it to us in feedback form we will soon add support to your email address")
                                print("Till then keep an eye")
                                E=input("Enter your Email address")
                            O1={"Email Address:" :newemail} 
                            O.update(O1)
                            print(O)
                        elif new ==3:
                            O={"Name:":N,"Email Address:":E,"Account Type:":Y,"Mobile Number":number,"Address:":A,"City:":C,"State:":F,"Password:":P,"Username:":S}
                            while True:
                                xyz=input('Enter your country code:')
                                if len(xyz)>3:
                                     print('Please enter a valid Country code')
                                     xyz=input('Enter your country code:')
                                elif len(xyz)<=3:
                                     print()
                                newnumber =input('Enter your phone number:')
                                if len(number)<10:
                                    print('number is less than 10 digits')
                                elif len(number)==10:
                                    print()
                                    print('Thank you for providing your Phone Number')
                                    print()
                                    break
                            O1={"Mobile Number:" : newnumber}
                            O.update(O1)
                            print(O)
                        elif new==4:
                            O={"Name:":N,"Email Address:":E,"Account Type:":Y,"Mobile Number":number,"Address:":A,"City:":C,"State:":F,"Password:":P,"Username:":S}
                            newaddress=input("Enter your Address")
                            O1={"Address:" : newaddress}
                            O.update(O1)
                            print(O)
                        elif new==5:
                            O={"Name:":N,"Email Address:":E,"Account Type:":Y,"Mobile Number":number,"Address:":A,"City:":C,"State:":F,"Password:":P,"Username:":S}
                            while True:
                                print('"Enter a good password below which is a mix of alphabets(a-z or A-Z), numbers(0-9) & special characters(!,@,#,$,%,^,&,*)"')
                                newP=input("Enter your Password:")
                                special="@"or"#"or"$"or"%"or"^"or"&"or"*"or"("or")"
                                if len(P)<8:
                                    print("Password should have minimum 8 component")
                                    print("Re-enter Password again")
                                    if special not in P:
                                        print("Password should have special characters")
                                    elif special in P:
                                        print()
                                    if P.isalpha() :
                                        print("")
                                    else:
                                        print("Password should have alphabets in it")
                                    if P.isdigit():
                                        print()
                                    else:
                                        print("Password should have number in it")
                                elif len(P)>=8:
                                    print("")
                                    break
                            O1={"Password:" : newP}
                            O.update(O1)
                            print(O)
                        elif new==6:
                            O={"Name:":N,"Email Address:":E,"Account Type:":Y,"Mobile Number":number,"Address:":A,"City:":C,"State:":F,"Password:":P,"Username:":S}
                            newusername=input("Enter your Username")
                            O1={"Username:" : newusername}
                            O.update(O1)
                            print(O)
            if choice==2:
                   print("*====================================WELCOME TO DEPOSIT DEPARTMENT OF OUR BANK================================*")
                   print ("Do You want to Deposit money")
                   print("PLEASE ANSWER IN YES IF YOU WANT TO DEPOSIT AND NO IF YOU DON'T WANT")
                   print("*=============================================================================================================*")
                   Ng=input("Enter your choice: ")
                   while True:
                       if Ng!='yes'and Ng!='Yes'and Ng!='YES'and Ng!='no'and Ng!='No'and Ng!='NO':
                            print('Please answer in yes or no')
                            Ng=input("Do you want to deposit your money? ")
                       elif Ng=='yes'or Ng=='Yes'or Ng=='YES':
                        Ag=int(input("Enter your account number:"))
                        Pg=input('Enter Password:')
                        if Ag!=ide and Pg!=P:
                            print('THE ACCOUNT NUMBER YOU ARE REFERING DOES NOT MATCH WITH THIS PASSWORD ')
                            print('Please try again')
                            Ag=int(input("Enter your account number:"))
                            Pg=input('Enter Password:')
                        elif Ag==ide and Pg==P:
                                print("HELLO,",N,"We are glad to serve you")
                                Date=int(input("Enter Date of Deposit(Date should only have the date not month an year):"))
                                Month=input("Enter Month of deposit:")
                                Year =input("Enter Year of Deposit:")
                                accountnumber=int(input("Enter your Account number:"))
                                while True:
                                    if accountnumber!=ide:
                                        print("Please enter correct account number")
                                        accountnumber=int(input("Enter your Account number:"))
                                    elif accountnumber==ide:
                                            print()
                                            break
                                Branchname=input("Enter your Branch name:")
                                Dg=int(input("Enter amount to be Deposited:"))
                                Words=input("Enter amount to be Deposited in Words:")
                                print('Thank for depositing money')
                                print("*==================================DEPOSIT SLIP=================================*")
                                print("Account number:",ide,"             ","Account Holder name:",N)
                                print("Date of deposit:",Date,"/",Month,"/",Year)
                                print("Branch:",Branchname)
                                print("Amount deposited:",Dg)
                                print("Balance:",minimumdeposit+Dg)
                                print("*===============================================================================*")             
                                while True:
                                    Qg=input('Do you want to deposit your money again:')
                                    if Qg!='yes'and Qg!='Yes'and Qg!='YES'and Qg!='no'and Qg!='No'and Qg!='NO':
                                         print('please answer in yes or no.Try again')
                                         Qg=input('do you want to deposit your money again ')
                                    elif Qg=='yes'or Qg=='Yes'or Qg=='YES':
                                         print('Your balance is= ',minimumdeposit+Dg)
                                         Gg=int(input('enter depoist cash= '))
                                         print('Your new total balance is= ',minimumdeposit+Dg+Gg)
                                         print('Thank for depositing money')
                                    elif Qg=='no'or Qg=='NO'or Qg=='No':
                                            Gg=0
                                            print('Please visit us again soon')
                                            print('Hope that you would deposit money soon')
                                            print('Do you want to withdraw money?')
                                            print("Please anwser in yes or no")
                                            tecfuhd=(input('Enter your choice here:'))
                                            if tecfuhd=='yes' or 'Yes' or 'YES' :
                                                print("*=========================================================WELCOME TO WITHDRAWAL DEPARTMNET=================================*")
                                                print("Do you want to Withdraw Money?")
                                                print("PLEASE ANSWER IN YES IF YOU WANT TO WITHDRAW AND NO FOR IF YOU DO NOT WANT TO WITHDRAW")
                                                choice=input("Enter your choice :")
                                                if choice=='no'or choice=='No'or choice=='NO':
                                                     print()
                                                     print('Thanks for visiting us')
                                                     print('Please check out our other services')
                                                     print()
                                                     print('press enter to exit')
                                                     exit()
                                                if choice=='yes'or choice=='YES'or choice=='Yes':
                                                    print("HELLO:",N,"We are glad to serve you")
                                                    Date=int(input("Enter Date of Withdrawal(Date should only have the date not month and year):"))
                                                    Month=input("Enter Month of Withdrawal:")
                                                    Year =input("Enter Year of Withdrawal:")
                                                    accountnumber=int(input("Enter your Account number:"))
                                                    while True:
                                                       if accountnumber!=ide:
                                                            print("Please enter correct account number")
                                                            accountnumber=int(input("Enter your Account number:"))
                                                       elif accountnumber==ide:
                                                             print()
                                                             break
                                                    Branchname=input("Enter your Branch name:") 
                                                    deposit=minimumdeposit+Dg+Gg
                                                    receipt=float(input("Enter the amount of Withdrawal:"))
                                                    c=deposit-receipt
                                                    if receipt<=deposit and receipt<10000 and receipt>0:
                                                       print("here is the current balance of your account")
                                                       print(c)
                                                    elif receipt<0:
                                                       print()
                                                       print('************************************************************************************************************')
                                                       print()
                                                       print('Negative credit system is still in progress')
                                                       DFgvhbhbh88778HJHVvn=input('press enter to exit')
                                                       exit()
                                                    elif receipt>10000:
                                                         print()
                                                         print('Oops as accoding to Our Bank policy we cannot hand over more than 10,000 credits at a time ')
                                                         print('So if you want to buy something then Please use your card')
                                                         print('Thank you')
                                                         print()
                                                         jhcgDVSV7856764ghfjh=input('press enter to exit')
                                                         exit()
                                                    elif receipt>deposit:
                                                         print(' ')
                                                         print('=================================================================================')
                                                         print(' ')
                                                         print('Oops it seems like you dont have sufficient funds want to take a loan')
                                                         print('if you want to take a loan then go to loan section')
                                                         print('Thank you for visiting us we hope that we will be able to serve you next time')
                                                         print()
                                                         print('=================================================================================')
                                                         bhHjjJGugJHHF78_h=input("press enter to exit")
                                                         exit()
                                                         print("Thank you")
                                                    print("*=====================================================WITHDRAWAL SLIP===============================================*")
                                                    print("Account number:",ide,"             ","Account Holder name:",N)
                                                    print("Date of Withdrawal:",Date,"/",Month,"/",Year,"Branch:",Branchname)
                                                    print('Account balance before transistion',deposit)#@8
                                                    print("Amount requested:",receipt)#@7
                                                    print('Amount dispensed:',receipt+20)#@7
                                                    print('BanK fees:',20)
                                                    print('Account balance:',c-20)#@9
                                                    print('*====================================================================================================================*')
                                                    jgjHGHjhjf7567=input('Press enter to exit')
                                                    exit()
                                                else:
                                                     print('Oops it looks like you have made a mistake ')
                                                     print('you gotta have choose only from 1(yes) or 2(no)')
                                                     print("press enter key to exit")
                                                     exit()
                                            if tecfuhd=='No' or 'no' or 'NO':
                                                print('Thank you for using our services, Please come back again!!')
                                                print('See u soon!!')
            elif choice==3:
                loanoptions={"1":"home loans","2":"car loans","3":"bussiness loan","4":"personal loans"}
                print()
                print("welcome to the loan center of our bank, how may be of service?")
                print(" ")
                print("X=====================XSELECTIONX=====================X")
                print("1. Home loans")
                print("2. Car loans")
                print("3. Bussiness loan")
                print("4. Personnal loan")
                print("X=====================================================X")
                print(" ")
                choosenloan=(input("please choose a type of loan,by typing corresponding number"))
                if choosenloan != "1" and choosenloan != "2" and choosenloan != "3" and choosenloan != "4" and type(choosenloan) != int :
                    print("invalid number, please try again")
                    print("X======================================================X")
                else:
                    if choosenloan == "1":
                        print(" ")
                        print("we offer home loans, starting at Rs. 15,00,000.00")
                        amounthome=int(input("please enter an amount you require"))
                        if amounthome < 1500000.00:
                                print("please state higher amount")
                        else:
                            print("request accepted. lets move to terms of repayment") #6% interst per annum
                            print("X======================================================X")
                            print(" ")
                            yearshome=int(input("home loans are provided with 6% per annum interest. Enter no. of years." ))
                            finalhome = (amounthome*(106/100)**yearshome)
                            print("total compund interest in", yearshome, "years, is equal to = Rs.", round(finalhome,2)) #gives compound interest only
            
                    elif choosenloan == "2":
                        print(" ")
                        print("we offer car loans, starting at Rs. 5,00,000.00")
                        amountcar=int(input("please enter an amount you require"))
                        if amountcar < 500000:
                            print("please state higher amount")
                        else:
                            print("request accepted. lets move to terms of repayment") #7% interest pe annum
                            print("X======================================================X")
                            print(" ")
                            yearscar=int(input("car loans are provided with 7% per annum interest. Enter no. of years." ))
                            finalcar = (amountcar*(107/100)**yearscar)
                            print("total compund interest in", yearscar, "years, is equal to = Rs.", round(finalcar,2))#gives compound interest only
                
                    elif choosenloan == "3":
                        print(" ")
                        print("we offer bussiness loans, starting at Rs. 10,00,000.00")
                        amountbusi=int(input("please enter an amount you require"))
                        if amountbusi < 1000000.00:
                            print("please state higher amount")
                        else:
                            print("request accepted. lets move to terms of repayment") #8% interest per annum
                            print("X======================================================X")
                            print(" ")
                            yearsbusi=int(input("business loans are provided with 8% per annum interest. Enter no. of years." ))
                            finalbusi = (amountbusi*(108/100)**yearsbusi)
                            print("total compund interest in", yearscar, "years, is equal to = Rs.", round(finalbusi,2)) #gives compound interest only

                    elif choosenloan == "4":
                        print(" ")
                        print("We offer personal loans, starting at Rs. 50,000.00")
                        amountperson=int(input("please enter an amount you require"))
                        if amountperson < 50000.00:
                            print("please state higher amount")
                        else:
                            print("request accepted. lets move to terms of repayment") #10% interest per annum
                            print("X======================================================X")
                            print(" ")
                            yearsperson=int(input("personal loans are provided with 10% per annum interest. Enter no. of years." ))
                            finalperson = (amountperson*(110/100)**yearsperson)
                            print("total compund interest in", yearsperson, "years, is equal to = Rs.", round(finalperson,2)) #gives compound interest only
            elif choice==4:
                print('Are you sure you want to exit?')
                print(1,':','Yes!')
                print(2,':','No,Cancel!')
                xyz=int(input('Enter your choice here:'))
                if xyz==1:
                    print('Thank You for using our service,See you soon')
                elif xyz==2:
                    print('coming soon.........')
            elif choice==5:
               print('Hey, Thank you for using our services for your banking related life')
               print('We hope that so far you have utilised our services at its full extent')
               print('Thanks for taking out some time to fill this feedback form, we will be very keen to hear the problems you faced or suggestions you would like to give to us to improve our Banking')
               print('What you would like to do today?')
               print(1,'Report my problem')
               print(2,'Give feedback to us')
               abcd=int(input('Enter your Choice here:'))
               if abcd==1:
                   print('What problem did you faced with our system?,Please first check our FAQ and if your problem is not solve enlist your problem down below and we will try to solve it ASAP')
                   print("faq's code will be written here soon....")#faq
                   print(1,'My problem is solved by the hep of FAQ!')
                   print(2,'NO!, my problem still persists')
                   bcde=int(input("Enter your choice here:"))
                   if bcde==1:
                       print('We are happy to see that your problem is resolved,Thank you once again')
                   elif bcde==2:
                       print('That is not good')
                       print('Please enter the problem you are facing below so that our team can look into the matter and solve it ASAP')
                       input('Enter your problem here:')
               elif abcd==2:
                    print('OH WoW!!!!!!!')
                    print('Glad to see you here helping us improve')
                    cdef=int(input('How much would you like you rate us on a scale of 1-10:'))
                    if cdef>0 and cdef<5:
                        print('Oh,we are very sad to see that our customer is facing problem, please let us know what you think where should we improve?')
                    elif cdef>=5 and cdef<=10:
                           print('YAY!!!!, That means you liked our service,thanks for that!!!, Still you can let us know what more we can do!!')
                           fde=input('Enter your feedback here:')
            elif choice==6:
                print('Hey,Welcome to the About Us Section')
                print('Here at GTH Bank, we a great Team made up of Great aspirers & Thinkers & Executers & etc.......,:^)')
                print('Here at this section you will find About our "Great Team" which is behind this service')
                print('Do you want to continue And know more about us?')
                print(1,'Yes,Absoulutely :-D')
                print(2,'No,Another time Maybe :-!')
                print("Please answer in Yes or No")
                qsdfr=input('What do you want to do?Enter your choice here:')
                if qsdfr=="yes"or"YES"or"Yes":
                    print("*=========================================================================================================*")
                    print("OH!!!GREAT,LET US MOVE AHEAD ;)")
                    print('So,Here is the list of our Great team ')
                    print('Blueprint & Home Layout: HEMANT KUMAR')
                    print("           The perfect helper and joker :^)")
                    print('The Deposit Center: GARV PRASAD')
                    print("           Don't take tension your money is in safe hands ;-)")
                    print('The Withdrawl Department: AASHISH RAJ')
                    print("           That is the josh,The power of 100 }:-)")
                    print('The Loan System: ZIDDAN RABBI')
                    print("           Ahaa!!,The perfect presenter with the perfect Calculation ")
                    print('The overall Linking up of system: RISHABH GUSAIN')
                    print('           The chill dude ^_^' )
                    print()
                    print('Whole of our Team has done great work, Making the best of everything!!')
                    print('Everyone coordinated greatly, Showed the best, Made the best and Did the best')
                    print('Thanks to our whole team!! 8-)')
                    print()
                    print('CREDITS:')
                    print('        To the whole team')
                    print('        To C.B.S.E. for making such work a part of syllabus')
                    print("        To Chanderkiran Ma'am for providing us with this opportunity")
                    print('        To the Python Org for making such a great Language')
                    print('        To PyCharm, Python IDLE, Spyder, VSCODE & Python Shell for providing such great editors & executers')
                    print()
                    print('Thank You ;)')
                    print("*===========================================================================================================*")
                elif qsdfr=="No"or "no" or "No":
                    print('NO PROBLEMO!!!!!!')
                    print('SEE YOU SOON')
                    print("TILL THEN, TADA!! B-)")
        elif efg=='No' or 'NO' or "no":
            print("We think, you don't have mood to do some finances")
            print('NO Problem')
            print()
            print('We are Always here, Open for you 24X7, Providing our services to our valuable customers')
            print("And Thank You!! :-)")
elif choice==2:
    N=input("Enter your Name:")
    print("Please register your self")

            
                    
                
                        
                            
                    
                

        
            
            
        
    
            
       
        
         
         
    
        

        



    
   
    

    
        
    
   
            
    
        
    
   
            
       
   

        
      
        

        



     

   

   
       
   
            
   
    
        
 
    
           
    
        

        
            
            

         
   
        



    
   
    

    
        
    
   
            
    
        
    
   
            
       
   

        
      
        

        



     

   

   
       
   
            
   
    
        
 
    
           
    
        

        
            
            
