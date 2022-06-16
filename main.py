guess_count=3
secret_number =9

while guess_count>0:
    guess = int(input("Guess:"))
    guess_count -= 1
    if guess == secret_number:
         print("you win !!")
         break




print("Done")