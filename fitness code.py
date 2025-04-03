print("\nWelcome to Fitness Buddy! 🏋️‍♂️")
print("I'll recommend exercises based on what you want to work on.")
print("Type 'help' for options or 'bye' to quit.\n")

exercise_database = {
    "arms": {
        "description": "💪 Arm day! Let's get those guns pumping!",
        "exercises": [
            "Bicep curls - 3 sets of 12 reps 🏋️‍♂️",
            "Tricep dips - 3 sets to failure 💺",
            "Hammer curls - 3 sets of 10 reps each arm 🔨",
            "Push-ups - 4 sets of 15 reps (modify knees if needed) 👐"
        ]
    },
    "legs": {
        "description": "🦵 Leg day - the best day! Don't skip it!",
        "exercises": [
            "Bodyweight squats - 4 sets of 20 reps 🏋️‍♀️",
            "Lunges - 3 sets of 10 per leg 🚶‍♂️",
            "Calf raises - 3 sets of 15 reps (try on stairs!) 🪜",
            "Wall sit - hold for 60 seconds 🧱"
        ]
    },
    "core": {
        "description": "🔥 Core workout incoming! Get ready to feel the burn!",
        "exercises": [
            "Plank - hold for 45 seconds ⏱️",
            "Russian twists - 3 sets of 20 reps (each side) 🌀",
            "Leg raises - 3 sets of 12 reps 🦵",
            "Bicycle crunches - 3 sets of 15 reps per side 🚴‍♂️"
        ]
    },
    "cardio": {
        "description": "❤️ Get that heart pumping with these cardio options!",
        "exercises": [
            "Jump rope - 5 minutes non-stop 🏃‍♂️",
            "Burpees - 3 sets of 10 reps 🆙",
            "Jog in place - 3 minutes with high knees 🏃‍♀️",
            "Dancing - put on music and move for 10 minutes! 🕺"
        ]
    }
}

while True:
    user_input = input("\nWhat would you like to work on? ").lower().strip()
    
    if user_input in ['bye', 'exit', 'quit']:
        print("\nFitness Buddy: Keep up the great work! See you next time! 👋")
        break
    
    if user_input == 'help':
        print("\nI can help with exercises for these areas:")
        print(", ".join(exercise_database.keys()))
        print("Just tell me what you want to work on!")
        continue
    
    if user_input in exercise_database:
        category = exercise_database[user_input]
        print(f"\nFitness Buddy: {category['description']}")
        print("Here are some great exercises:")
        for exercise in category['exercises']:
            print(f"• {exercise}")
    else:
        print("\nFitness Buddy: I'm not sure I understand that workout area.")
        print("Try one of these: arms, legs, core, cardio")
        print("Or type 'help' to see options again.")