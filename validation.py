
def validation(account_number):
    try:
        int(account_number)
        return True
    except ValueError:
        return False
    except TypeError:
        return False
    
   
 
  
      