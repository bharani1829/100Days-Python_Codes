#This is my 8 mini project called Caesar ciper

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def ceasar(direction,word,length):
            result = ""
            if direction == "d":
                length *= -1
            for letter in word:
                result += chr(ord(letter) + length)
            print(f"The {direction} Word is : {result}")
            
            
                
print(logo)
again = True
while again:
    direction = input("Doy you want to encrypt or decode(e or d) : ").lower()
    word = input("Enter Word : ")
    length = int(input("Enter shift length : "))
    ceasar(direction,word,length)
    continue_again = input("If you want to continue type yes or else no : ").lower()      
    if continue_again == 'no':
        print("Bye-Thankyou")
        again = False



 
          
       


