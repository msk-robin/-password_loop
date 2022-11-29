special_characters = ['&', '#', '$', '!', '?', '"', '(', ')', '.']

alphabetic_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
                                                                                                                          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

# Define fixed values here
password = input ("Create password: ")

count = 0
for i in password:
  if i in  alphabetic_characters:
    count +=1

count1 = 0
for i in password:
  if i in special_characters:
    count1+=1

count2 = 0
for i in password:
  if i in numbers:
    count2+=1     

if len(password) < 8:
  print("Enter at least 8 characters!")
if count < 3:
  print("Enter at least 3 alphabetics!")

if count1 < 3:
  print("Enter at least 3 special characters!") 

if count2 <3:
  print("Enter at least 3 numbers!")