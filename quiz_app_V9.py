import random
import time


def save_score(name, score):
    file = open("score.txt", "a")
    file.write(name + "," + str(score) + "\n")
    file.close()


def load_leaderboard():
    try:
        file = open("score.txt", "r")
        lines = file.readlines()
        file.close()

        scores = []

        for line in lines:
            name, score = line.strip().split(",")
            scores.append((name, int(score)))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores

    except FileNotFoundError:
        return []


def show_leaderboard():
    scores = load_leaderboard()

    print("\n==============================")
    print("        🏆 LEADERBOARD")
    print("==============================")

    if len(scores) == 0:
        print("No scores yet!")
        return

    for i in range(min(5, len(scores))):
        name, score = scores[i]
        print(f"{i+1}. {name} - {score}")

    print("==============================\n")

def ask_question(q):
    print("\n--------------------------------")
    print("Question:", q[0])

    print("A)", q[1])
    print("B)", q[2])
    print("C)", q[3])
    print("D)", q[4])

    start_time = time.time()
    user_answer = input("Enter A/B/C/D: ").upper().strip()
    end_time = time.time()


    if end_time - start_time > 10:
        print("⏰ Time's up! No points.")
        print("Correct Answer:", q[5])
        return 0

    if user_answer == q[5]:
        print("✔ Correct!")
        return 1
    else:
        print("❌ Wrong!")
        print("Correct Answer:", q[5])
        return 0

easy_questions = [
    ["2 + 2?", "3", "4", "5", "6", "B"],
    ["Capital of India?", "Chennai", "Delhi", "Mumbai", "Kolkata", "B"],
    ["Sky color?", "Green", "Blue", "Red", "Yellow", "B"]
]

medium_questions = [
    ["Red Planet?", "Earth", "Mars", "Venus", "Jupiter", "B"],
    ["Python creator?", "Dennis Ritchie", "Guido van Rossum", "James Gosling", "Bjarne Stroustrup", "B"],
    ["12 * 8?", "96", "88", "108", "84", "A"]
]

hard_questions = [
    ["Largest planet?", "Earth", "Mars", "Jupiter", "Saturn", "C"],
    ["Binary search complexity?", "O(n)", "O(n^2)", "O(log n)", "O(1)", "C"],
    ["17 squared?", "289", "196", "256", "324", "A"]
]



player_name = input("Enter your name: ")

print("\n==============================")
print("   PYTHON QUIZ APPLICATION")
print("==============================")


while True:

    print("\n======================")
    print("     QUIZ MENU")
    print("======================")
    print("1. Play Quiz")
    print("2. Leaderboard")
    print("3. Exit")

    choice = input("Enter choice: ").lower().strip()


    
    if choice in ["1", "play", "quiz"]:

        print("\nChoose Difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        diff = input("Enter: ").lower().strip()

        if diff in ["1", "easy"]:
            quiz_data = easy_questions
        elif diff in ["2", "medium"]:
            quiz_data = medium_questions
        elif diff in ["3", "hard"]:
            quiz_data = hard_questions
        else:
            print("Invalid choice, defaulting to Easy")
            quiz_data = easy_questions


       
        random.shuffle(quiz_data)

        score = 0


        for q in quiz_data:
            score += ask_question(q)


    

        total = len(quiz_data)
        percent = (score / total) * 100

        print("\n======================")
        print("       RESULT")
        print("======================")
        print("Score:", score, "/", total)
        print("Percentage:", round(percent, 2), "%")

        if percent == 100:
            print("🔥 Perfect Score!")
        elif percent >= 70:
            print("👍 Good Job!")
        else:
            print("📚 Keep Practicing!")

        print("======================\n")


       
        save_score(player_name, score)


    
    elif choice in ["2", "leaderboard", "top"]:
        show_leaderboard()


    
    elif choice in ["3", "exit", "quit"]:
        print("Thanks for playing!")
        break


    
    else:
        print("Invalid choice. Try again.")
