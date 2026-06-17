import random
quiz_questions = [
    {
        "question": "Which is the only planet in the Solar System known to support life?",
        "options": ["Mars", "Earth", "Venus", "Jupiter"],
        "answer": "Earth"
    },
    {
        "question": "Who is known as the \"Missile Man of India\"?",
        "options": ["Jawaharlal Nehru", "Atal Bihari Vajpayee", "Dr. A.P.J. Abdul Kalam", "Subhash Chandra Bose"],
        "answer": "Dr. A.P.J. Abdul Kalam"
    },
    {
        "question": "Which is the longest river in the world?",
        "options": ["Amazon River", "Yangtze River", "Ganges River", "The Nile River"],
        "answer": "The Nile River"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Iron", "Diamond", "Quartz"],
        "answer": "Diamond"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "Which Indian city is famously known as the \"Pink City\"?",
        "options": ["Mumbai", "Jaipur", "Udaipur", "Jodhpur"],
        "answer": "Jaipur"
    },
    {
        "question": "Which gas planet is the largest in the Solar System?",
        "options": ["Saturn", "Neptune", "Jupiter", "Uranus"],
        "answer": "Jupiter"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
        "answer": "Canberra"
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["Five", "Six", "Seven", "Eight"],
        "answer": "Seven"
    }
]

prize = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

total_money = 0
question_index = 0

random.shuffle(quiz_questions)
for item in quiz_questions:
    print(item["question"])
    print()

    option_num = 1
    for option in item["options"]:
        print(str(option_num)+" . "+ option)
        option_num += 1
    print()
    
    user_choice = str(input("Enter your Answer =>  "))
    if (user_choice.strip().lower() == item["answer"].lower()):
        current_prize = prize[question_index]
        total_money += current_prize
        print(f"Correct Answer You won {current_prize} and total amount is {total_money}")
        print()
        question_index += 1
    else:
        print(f"Wrong Answer!! the correct anser is {item['answer']} and you won a total amount of {total_money}$ to take with yourself Home ")
        
        break