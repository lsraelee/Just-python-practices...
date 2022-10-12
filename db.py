# create record into the database as a file
# read record from the database
# update record in the database
# delete record from the datatbase
# find user in the database

import os
from validation import validation


user_path = "Users_database/User_record/"
balance_path = "Users_database/Users_account_balance/"

#name = str(input('Please enter info here: '))

#account = str(input('Please input your name here: '))

def create(account_number,user_details):
    
    completion_state = False
    try:
        new_file = open(user_path + str(account_number) + ".txt", "x")
            
        
    
    except FileExistsError:
        print('\nUser already registered\n')
        if not read(account_number):
            delete(account_number)
       
        return completion_state
       
        
    
    else:
        
        new_file.write(str(user_details))
        print('\nRecord created inside database\n')
        new_file.close()
        
        completion_state = True
        
    return completion_state

    
def read(account_number):
    
    
    
    try:
    
         open_file = open(user_path + str(account_number) + '.txt','r')
           
    except FileNotFoundError:
        print('\nUser not registered\n')
        return False
        
        
    else:
        return open_file.readline()
    
          
          
          
def sp_read(account_number):
    
    try:
    
         open_file = open(user_path + str(account_number),'r')
           
    except FileNotFoundError:
        print('\nUser not registered\n')
        return False
        
        
    else:
        return open_file.readline()          
          
    
def update():
    print('Updating record in the database')
    
    
def delete(account_number):
    is_delet_succesful = False
    try:
        
        if  os.path.exists(user_path + str(account_number) + '.txt'):
            
            os.remove(user_path + str(account_number) + '.txt')
            print('deleting record from the database')
           
            is_delet_succesful = True 
            
    except FileNotFoundError:
        print('User not registered')
        
    
    finally:
        
        return is_delet_succesful
    
    
def email_auth(email):
    
    all_users = os.listdir(user_path,) 
    
    for users in all_users:
        content_in_file = sp_read(users)
        each_user_into_list = str.split(content_in_file,',')
        
        if email in each_user_into_list:
           d_list = each_user_into_list
           if email in d_list:
               
               print('\nSorry, this email is already registered. Try again\n')
               return True
           
           return False
        
           
       
    

        
        #if email not in each_user_into_list:    
        #print(each_user_into_list)
            
        
    
    

def does_account_num_exist(account_number):
    if os.path.exists(user_path + str(account_number) + '.txt'):
        return True
    
    return False

            
            
def username_auth(username,account_number):

    content = read(account_number)
    content_into_list = str.split(content,',')
    #print(content_into_list)
    if username in content_into_list:

        return True
        
    return False  


def password_auth(account_number,password):
    
    content = read(account_number)
    content_into_list = str.split(content,',')
    if password == content_into_list[-1]:
        
        return True
    
    return False
            

# read the account balance
# withdraw cash
# deposit cash

    
def save_balance(account_number,account_balance):
    balance_file =open(balance_path + str(account_number) + ".txt",'x' ) 
    balance_file.write(str(account_balance))
    balance_file.close()
    
def read_balance(account_number):
    balance_file = open(balance_path + str(account_number) + ".txt",'r')
    balance_raw = balance_file.readline()
    balance = str(balance_raw)
        
    return balance
    
def balance_update(account_number,account_balance):
        
    if os.path.exists(balance_path + str(account_number) + '.txt'):
        os.remove(balance_path + str(account_number) + '.txt')
            
        save_balance(account_number,account_balance)
        

#email_auth('adsasdhjafshaf')

#print(read('ayomikun'))

#print(username_auth('israel','4733241573'))
print(email_auth('ayomikunadewemimo@gmail.com'))       
        



