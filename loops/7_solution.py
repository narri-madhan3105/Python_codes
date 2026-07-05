while True:
    number = int(input("Enter value  "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print(" try again")
    
    #break can only be used inside a loop (for or while).