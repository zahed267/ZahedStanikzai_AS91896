import time

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)

# MAIN LOOP
while True:
    print("Press enter to start the stopwatch, and again to stop it.")
    input()  # wait for user to press Enter

    print("stopwatch started")
    start_time = time.time()

    print("Welcome to the sports quiz")  
    print(" ")
    print("Type your answer corresponding to the question!.")
    print(" ")
    print("Make sure you write your answers with a capital letter at the start!")  
    print(" ")

    score = 0

    question = ("1. Who won the FIFA world cup in 2022?")
    print(question)
    user_answer = input("your answer: ").strip().upper()
    if user_answer == "ARGENTINA":
        print("That's correct, well done!")
        score += 1
        print("Nice you've got ", score, " point")
    elif user_answer == "":
        print("Not sure?")    
    else:
        print("That's incorrect, better luck next time!")  
        print("The answer is Argentina!")  
    print(" ")

    question = ("2. Which country has the most olympic gold medals?")
    print(question)
    user_answer = input("your answer: ").strip().upper()    
    if user_answer == "USA":
        print("That's correct, well done!")
        score += 1
        print("Nice you've got ", score, " point")
    elif user_answer == "":
        print("Not sure?")  
    else:
        print("That's incorrect, better luck next time!")
        print("The answer is USA!")
    print(" ")

    question = ("3. How many players are in one Football team?")
    print(question) 
    user_answer = input("your answer: ").strip().upper()   
    if user_answer == "11":
        print("That's correct, well done!")
        score += 1
        print("Nice you've got ", score, " point")
    elif user_answer == "":
        print("Not sure?")      
    else:
        print("That's incorrect, better luck next time!") 
        print("The answer is 11")
    print(" ")

    question = ("4. How many players are on a basketball team on the court?")
    print(question)
    user_answer = input("your answer: ").strip().upper()
    if user_answer == "5":
        print("That's correct, well done!")
        score += 1
        print("Nice you've got ", score, " point")
    elif user_answer == "":
        print("Not sure?")      
    else:
        print("That's incorrect, better luck next time!") 
        print("The answer is 5")
    print(" ")

    question = ("5. If the pitcher threw three strikes, is it a strike out?")
    print(question)
    user_answer = input("your answer: ").strip().lower()
    if user_answer == "yes":
        print("That's correct, well done!")
        score += 1
        print("Nice you've got ", score, " point")
    elif user_answer == "":
        print("Not sure?")      
    else:
        print("That's incorrect, better luck next time!") 
        print("The answer is Yes")
    print(" ")

    question = ("6. How many players can be in a Tennis court at a time?")
    print(question)
    user_answer = input("your answer: ").strip().upper()
    if user_answer == "2":
        print("That's correct, well done!")
        score += 1
        print("Nice you've got ", score, " point")
    elif user_answer == "":
        print("Not sure?")      
    else:
        print("That's incorrect, better luck next time!") 
        print("The answer is 2")
    print(" ")

    question = ("7. How many Volleyball players are on a court in total?")
    print(question)
    user_answer = input("your answer: ").strip().upper()
    if user_answer == "12":
        print("That's correct, well done!")
        score += 1
        print("Nice you've got ", score, " point")
    elif user_answer == "":
        print("Not sure?")      
    else:
        print("That's incorrect, better luck next time!") 
        print("The answer is 12")
    print(" ")

    question = ("8. How many title defenses did Demetrious Johnson win?")
    print(question)
    user_answer = input("your answer: ").strip().upper()
    if user_answer == "11":
        print("That's correct, well done!")
        score += 1
        print("Nice you've got ", score, " point")
    elif user_answer == "":
        print("Not sure?")      
    else:
        print("That's incorrect, better luck next time!") 
        print("The answer is 11")   
    print(" ")

    question = ("9. How long is a boxing round?")
    print(question)
    user_answer = input("your answer: ").strip().lower()
    if user_answer == "3 minutes":
        print("That's correct, well done!")
        score += 1
        print("Nice you've got ", score, " point")
    elif user_answer == "":
        print("Not sure?")      
    else:
        print("That's incorrect, better luck next time!") 
        print("The answer is 3 Minutes")  
    print(" ")

    question = ("10. How many holes are on a standard golf course?")
    print(question)
    user_answer = input("your answer: ").strip().upper()
    if user_answer == "18":
        print("That's correct, well done!")
        score += 1
        print("Nice you've got ", score, " point")
    elif user_answer == "":
        print("Not sure?")      
    else:
        print("That's incorrect, better luck next time!") 
        print("The answer is 18 Holes in a standard Golf course")  
    print(" ")

    input("Press enter to stop the stopwatch.")
    end_time = time.time()
    print("stopwatch stopped")
    print("elapsed time:", convert(end_time - start_time), "minutes")
    print(" ")  
    print("Quiz finished! Your final score is", score)
    print("Thank you for playing the quiz!")  
    print(" ")

    again = input("Do you want to play the quiz again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Goodbye! Thanks for playing.")
        break


    