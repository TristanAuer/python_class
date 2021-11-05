secret = 42

#equality check
print(secret == 42)
trys = 5

while trys > 0:
    trys-=1
    guess = int(input("guess anumber: "))
    print(secret == guess)
    if secret == guess:
      
        print("you are correct!")
        exit()
    elif guess > secret:
        print("guess is to high try again. you have ",trys, "trys left" )  
    else:
        print ("Your guess was to lowtry again. you have ",trys, "trys left")
print("sorry you lose")
   