'''
Vince Michael J. Samson
ID: 04-24-0147
10/6/2025 - Oct.7,2026
Advance Programming: Excercise 1 - Maths Quiz
'''
import random

def displayMenu():
    print("\nCHOOSE YOUR DIFFICULTY >:D")
    print("1. Easy (1-digit)")
    print("2. Moderate (2-digit)") 
    print("3. Advanced (4-digit)")
    
    while True:
        choice = input("Choose your heat level from (1-3): ")
        if choice in ['1', '2', '3']:
            return int(choice)

def randomInt(level):
    ranges = {1: (0, 9), 2: (10, 99), 3: (1000, 9999)}
    return random.randint(*ranges[level])

def isCorrect(num1, num2, operation, user_answer):
    if operation == '+':
        correct = num1 + num2
    else:
        correct = num1 - num2
    
    if user_answer == correct:
        print("Ang Galing?!!!")
        return True
    else:
        print(f"Wrong! Why like this my friend \nCorrect answer: {correct}")
        return False

def main():
    print("Welcome to the math quiz of doom :P")
    
    while True:
        level = displayMenu()
        score = 0
        
        for _ in range(10):
            a, b = randomInt(level), randomInt(level)
            op = '+' if random.random() > 0.5 else '-'
            
            if op == '-' and a < b:
                a, b = b, a
            try:
                answer = int(input(f"{a} {op} {b} = "))
            except:
                answer = None
                
            if isCorrect(a, b, op, answer):
                score += 10
            else:
                try:
                    answer = int(input("Second try: "))
                    if isCorrect(a, b, op, answer):
                        score += 5
                except:
                    pass
        
        print(f"\nThis is your quiz result: {score}/100")
        if score >= 90: grade = "A+"
        elif score >= 80: grade = "A" 
        elif score >= 70: grade = "B"
        elif score >= 60: grade = "C"
        elif score >= 50: grade = "D"
        else: grade = "F"
        print(f"Grade: {grade}")
        
        if input("\nWould you like to play again? (y/n): ").lower() != 'y':
            print("Thanks for playing with us!!!")
            break

if __name__ == "__main__":
    main()
    
    
    