import random

def main():
    choice = []
    
    question = input("Enter your question : ").lower().capitalize()
    
    while True:
        add_choice = input("Enter your options : ").lower().capitalize()
        
        if add_choice == 'N':
            break
        
        choice.append(add_choice)
        
    result = random.choice(choice)
    
    print(f"Question : {question}")
    print(f"Answer : {result}")
    
    
if __name__ == "__main__":
    main()