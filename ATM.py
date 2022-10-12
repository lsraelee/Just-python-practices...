# register account
# username, email, password
# generating account number

#login
#username or email, password

#bank operation

#System init
import random
import os
import db
from validation import validation
from getpass import getpass



# The needed databases


user_path = "Users_database/User_record/"

# function for generating account number
def accountnumbergenerator():
      
    account_number = random.randrange(1111111111, 9999999999)
    if not db.does_account_num_exist(account_number):
        return account_number
    
    else:
        return accountnumbergenerator()


# function for cash withdrawal
def cash_withdrawal(account_number):
    current_account_balance = db.read_balance(account_number)
    correct_input = False
    while correct_input == False:
        print(f'\nYour current account balance is {current_account_balance}\n')
        account_withdrawal_amount = (input('\nPlease enter the amount you want to withdraw here: '))
        try:
            correct_input = True
            int(account_withdrawal_amount)
        except ValueError:
            correct_input = True
            print('\nInvalid input. Input must be in figures')
            cash_withdrawal(account_number)
        
        if int(account_withdrawal_amount) < int(current_account_balance):
            correct_input = True
            new_account_balance = int(current_account_balance) - int(account_withdrawal_amount)
            print(f'\n******CASH WITHDRAWAL SUCCESSFUL****** \n\n Your current account balance: {new_account_balance}')
            db.balance_update(account_number,str(new_account_balance)) 
            
        elif int(account_withdrawal_amount) > int(current_account_balance):
            correct_input = True
            print(f'\nYour current account balance is lower than the amount you want to withdraw - Current Balnce: {current_account_balance}')
        
        
        else:
            print('Invalid input, please try again') 
            
    what_to_do_next(account_number)


# function for cash deposit
def cash_deposit(account_number):
    current_account_balance = db.read_balance(account_number)
    
    correct_option = False
    while correct_option == False:
        print(f'\nYour current account balance is {current_account_balance}\n')
        account_balance_update = (input('\nPlease enter the amount you want to deposit: '))
        try:
            int(account_balance_update)
            correct_option == True
        except ValueError:
            print('\nInvalid input. Input must be in figures')
            correct_option == True
            cash_deposit(account_number)
            
        if account_balance_update != str():
            correct_option = True
            new_account_balance = int(account_balance_update) + int(current_account_balance)
            print(f'\n******CASH DEPOSIT SUCCESSFUL****** \n\n Your current account balance: {new_account_balance}')
            db.balance_update(account_number,new_account_balance)
        
        
        elif account_balance_update == str():
            print('Input can not be empty')

        else:
            print('Invalid input, please try again')

        
    
    what_to_do_next(account_number)
    

# function for bank operation
def bankingoperaton(account_number):
       print(f'\nWelcom. Below are the available banking options: ')
       print('\n1. Account Informaton \n2. Cash Withdrawal \n3. Cash Deposit \n4. Logout \n5. Exit ')
       bankoptioninput = False
       # Using the while loop syntax to run a loop within loops
       while bankoptioninput == False:
            Enteredoption = str(input('\n Enter your option here: '))
            if Enteredoption == '1':
                bankoptioninput = True      
                account_info = info_template(account_number) + balance_info_template(db.read_balance(account_number)) 
                print(account_info) 
                what_to_do_next(account_number)
                   
            elif Enteredoption == '2':
                bankoptioninput = True
                cash_withdrawal(account_number)
                
            elif Enteredoption == '3':
                bankoptioninput = True
                cash_deposit(account_number)
                
            elif Enteredoption == '4':
                bankoptioninput = True
                init()
            elif Enteredoption == '5':
                bankoptioninput = True
                exit()
            else:
                print('\n Invalid input, please try again \n')
            

# function for registering
def register():
    
    print('\n Hello. Get Registered by following the process below')
    first_name = str(input('\n Please enter your first name: \n'))
    middle_name = str(input('\n Please enter your middle name: \n'))
    last_name = str(input('\n Please enter your last name: \n'))
    
    email_input = False
    while email_input == False:
        Email = str(input('\n Please enter your email: \n'))
        if db.email_auth(Email):
            email_input = False
        else:
            email_input = True
            
            
    Username = str(input('\n Please set a username of your choice: \n'))
    
    if Username == str():
        Username = str(first_name + middle_name)
        
    Password = getpass('\nPlease enter your password here:\n')
    customeraccountnumber = str(accountnumbergenerator())
    
    user_details = first_name + ',' + middle_name + ',' + last_name + ',' + Email + ',' + Username + ',' + Password
    
    db.create(customeraccountnumber,user_details)
    balance = 0
    db.save_balance(customeraccountnumber,str(balance))
    
    users_account_balance = db.read_balance(customeraccountnumber)
        
    bio = info_template(customeraccountnumber) + balance_info_template(users_account_balance)
    
    print('\n\nCongratulation!!! Your account has just been created, here is your account number: %s \n\n Do you want to check your Bio now - 1. YES 2. NO' % customeraccountnumber)
   
    EnteredOption = str(input('\n\nEnter your option here: \n'))
    if EnteredOption == '1':
        print(bio)
        enteredoption = str(input('How about you log into your account now(1. YES 2. NO): '))
        if enteredoption == '1':
            login()
        elif enteredoption == '2':
            print('Thank you for registering with us, do have a nice day')
            exit()
    elif EnteredOption == '2':
        print('\nThank you for registering with us.\nDo you want to login into your account now(1. YES 2. NO)')
        EnteredOption4 = str(input('Enter your option here: \n'))
        if EnteredOption4 == '1':
            login()          
        elif EnteredOption4 == '2':
             print('\n Thank you, Do have a nice day')
             exit()
    else:
        errorOption = True
         # Using the while loop syntax to run a loop 
        while errorOption == True:       
            print('\n You have entered an invalid option, would you love to try again')
            EnteredOption2 = str(input('\n Enter your option here(1. YES 2. NO): '))
            if EnteredOption2 == '1':
                print('\n Do you still want to check your Bio(1. YES 2. NO)')
                EnteredOption3 = str(input('Enter your option here: '))
                if EnteredOption3 == '1':
                    print(bio)
                elif EnteredOption3 == '2':
                    print('\n Thank you for registering with us. Do you want to login into your account now(1. YES 2. NO)')
                    EnteredOption4 = str(input('Enter your option here: '))
                    if EnteredOption4 == '1':
                        errorOption = False
                        login()          
                    elif EnteredOption4 == '2':
                        errorOption = False
                        print('\n Thank you, Do have a nice day')
                
    
# the login function
def login():
    print('\n#### Welcome, Log into your account ####\n')
    loginOption = False
    while loginOption == False:      
        Requiredaccountnum = input('Please enter your generated account number here: ')
        
        if validation(Requiredaccountnum):
            
            if len(str(Requiredaccountnum)) == 10:
                account_numbe_format = str(Requiredaccountnum) + '.txt'
                if os.path.exists(user_path + account_numbe_format):
                    loginOption = True          
                    usernameInput = False
                    while usernameInput == False:
                        RequiredUsername = str(input('\n Please enter your username here: '))
                
                        if db.username_auth(RequiredUsername,Requiredaccountnum):
                            usernameInput = True
                            passwordinput = False
                            while passwordinput == False:
                                RequiredPassword = str(input('\n Please enter your password here: '))
                                if db.password_auth(Requiredaccountnum,RequiredPassword):
                                    passwordinput = True
                                    print(f'\n*** Welcome {RequiredUsername}. Below are the available banking options ***\n')
                                    bankingoperaton(Requiredaccountnum)
                                else:
                                    print('\n Incorrect Password, please try again')
                        else:
                            print('\n Incorrect Username, please try again')        
                else:
                    print('\n Incorrect Account number, please try again')
            else:
                print('\nAccount number should be exactly 10 digits\n')
        else:
            print('Invalid input. Account number should be in figures')
    
 
# a function to start the whole program
def init():
      print('\n====== Welcome to Bank-EaZ ====== \n')
      validOption = False
     
      while validOption == False:
           initOption = input('Do you have an account with us - 1. YES 2. NO 3. Exit \n') 
           if initOption == '1':
            validOption = True
            login()
            
           elif initOption == '2':
            validOption = True
            register()
            
           elif initOption == '3':
            validOption = True
            exit()
            
           else:
            print('\n You have inputted an invalid option\n')


# function to know what to do next
def what_to_do_next(account_number):
    print('\nWhat would you like to do next: 1. Account Information 2. Banking Options 3. Logout 4. Exit ')
    entered_option = str(input('\nEnter option here: '))
    if entered_option == '1':
        current_account_balance = db.read_balance(account_number)
        account_balance_template = str(f' Your current account balance: {current_account_balance}\n')
        Account_info = info_template(account_number) + account_balance_template
        print(Account_info)
        what_to_do_next(account_number)
    elif entered_option == '2':
        bankingoperaton(account_number)
    elif entered_option == '3':
        init()
    elif entered_option == '4':
        exit()

# 
def info_template(account_number):
    
    content_in_list = str.split(db.read(account_number),',')
    first_name = content_in_list[0]
    middle_name = content_in_list[1]
    last_name = content_in_list[2]
    Email = content_in_list[3]
    Password = content_in_list[5]
    Username = content_in_list[4]
    
    PersonalInfoTemplate = str('\nHERE IS YOUR PERSONAL INFORMATION\n Fullname:' + 
                                ' ' + str(last_name) + ' ' + str(middle_name) + ' ' 
                                + str(first_name) +'\n Email: ' + ' ' + str(Email) + 
                                '\n Password: ' + ' ' + str(Password) + '\n Username: ' 
                                + ' ' + str(Username) + '\n Your account number: ' + ' ' +
                                    str(account_number) + '\n'
                                )
    return PersonalInfoTemplate


def balance_info_template(account_balance):
    template = f' Your current balance is: {account_balance}\n'
    return template


init()