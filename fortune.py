import random

def fortune_teller():
    name = "Keshav Baheti"
    admission_number = "21JE0465"
    print(f"Welcome to {name}'s Fortune Teller ({admission_number})")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").lower()
    fortunes = {
        "happy": [
            f"Great things await you, {name}! Keep smiling.",
            "Your positive energy will attract good fortune."
        ],
        "sad": [
            "Better days are coming. Stay strong!",
            f"Remember, {name} believes in you."
        ],
        "neutral": [
            "An unexpected event will brighten your day.",
            "Take time to relax and recharge."
        ],
        "stressed": [
            "Take a deep breath; relief is near.",
            "Focus on what you can control and let go of the rest."
        ]
    }
    if mood in fortunes:
        print("Your fortune:", random.choice(fortunes[mood]))
    else:
        print("Sorry, I don't understand that mood. Please enter happy, sad, neutral, or stressed.")

if __name__ == "__main__":
    fortune_teller()
