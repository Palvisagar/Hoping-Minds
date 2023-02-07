# check if string is pangrom
# Author Palvi Sagar

def check_pangram(str): # define a function
  if len(set('PALLVI') - set(str.upper())) == 0 : 
    return True

  return False

user_string = input("Enter a string to check for pangram : ")

if(check_pangram(user_string)):
  print("It is a pangram string")
else:
  print("Not a pangram string")