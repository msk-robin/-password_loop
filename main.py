special_characters = ['&', '#', '$', '!', '?', '"', '(', ')', '.']

alphabetic_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
                                                                                                                          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [0,1,2,3,4,5,6,7,8,9]

# Define fixed values here
password = input ("Create password: ")
# Write your code here
while password:
  if len(password) <8:
    if password.count(alphabetic_characters) < 3:
      if password.count(special_characters) < 3:
        if password.count(numbers) < 2:
          print("You need at least 2 number digits!")
          break
        print("you need at least 3 special characters!")
        break
      print("alphabetics must be at least 3!")
      break
    print("length must be at least 8 characters!")
    break
# if (len(password)<8):
#     user_password=list(password)
#     if any(i in user_password for i in alphabetic_characters if )>=3:

#     print("password must be at least 8 char!")
#     break