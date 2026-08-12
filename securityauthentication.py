#security authentication
password = input("Enter your password: ")
score = 0 

if len(password) < 4:
    print("weak password")

if len(password) < 6:
    score += 1 
    print("moderate password")

if len(password) >8:
    score += 2
    print("strong password")

