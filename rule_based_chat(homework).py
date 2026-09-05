import re,random
from colorama import Fore, Style, init
init(autoreset=True)
destinations={
    "beaches": ["Maldives", "Bali", "Hawaii", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Andes"],
    "cities": ["New York", "Paris", "Tokyo", "London"],
    "nightlife": ["Las Vegas", "Ibiza", "Bangkok", "Berlin"],
    "adventure": ["Costa Rica", "New Zealand", "South Africa", "Peru"],
    "cultural": ["Rome", "Kyoto", "Istanbul", "Cairo"],
    "romantic": ["Venice", "Santorini", "Paris", "Bali"],
    "family-friendly": ["Orlando", "Tokyo Disneyland", "Barcelona", "Sydney"],
    "budget": ["Thailand", "Vietnam", "Mexico", "Portugal"],
    "luxury": ["Maldives", "Dubai", "Monaco", "Bora Bora"]
}
jokes=[
    "Why don't programmers like nature? It has too many bugs.",
    "Why did the computer go to the doctor? It caught a virus.",
    "Why do travelers always feel warm? Because they have a lot of hot spots.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "Why did the math book look sad? Because it had too many problems.",
    "why did the tomato turn red? Because it saw the salad dressing.",
    "Why did the coffee file a police report? It got mugged.",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
    "Why did the computer go to art school? It wanted to learn how to draw its own conclusions."
    "What did one wall say to the other wall? I'll meet you at the corner.",
    "Why did the cookie go to the doctor? Because it felt crummy.",
]
def normalize_input(text):
    return re.sub(r"\s+"," ",text.strip().lower())
def recommend():
    print(Fore.CYAN+"TextBot: What type of destination are you interested in? (beaches, mountains, cities,nightlife, adventure)")
    preference=input(Fore.LIGHTGREEN_EX+"You: ")
    preference=normalize_input(preference)

    if preference in destinations:
        suggestion=random.choice(destinations[preference])
        print(Fore.LIGHTGREEN_EX+f"TextBot: How about {suggestion}?")
        print(Fore.LIGHTGREEN_EX+"TextBot: What do you think? (yes/no)")
        answer=input(Fore.LIGHTGREEN_EX+"You: ").lower()

        if answer=="yes":
            print(Fore.LIGHTGREEN_EX+f"TextBot: Great! I hope you have a wonderful trip to {suggestion}!")
        elif answer=="no":
            print(Fore.LIGHTGREEN_EX+"TextBot: No worries! Let's try again.")
            recommend()
        else:
            print(Fore.LIGHTGREEN_EX+"TextBot: I didn't understand that. Let's try again.")
            recommend()
    else:
        print(Fore.LIGHTGREEN_EX+"TextBot: I'm sorry, I don't have recommendations for that type of destination. Please choose from beaches, mountains, or cities.")
        recommend()
def packing_tips():
    print(Fore.LIGHTGREEN_EX+"TextBot:Where to?")
    location=input(Fore.LIGHTGREEN_EX+"You: ")
    print(Fore.LIGHTGREEN_EX+f"TextBot: Great! for how many days?")
    days=input(Fore.LIGHTGREEN_EX+"You: ")
    print(Fore.LIGHTGREEN_EX+f"TextBot: Awesome! You're going to {location} for {days} days. Here are some packing tips:")
    print(Fore.CYAN+"TextBot: Here are some packing tips for your trip:")
    print(Fore.LIGHTGREEN_EX+"TextBot: 1. Make a packing list to ensure you don't forget anything.")
    print(Fore.LIGHTGREEN_EX+"TextBot: 2. Pack versatile clothing that can be mixed and matched.")
    print(Fore.LIGHTGREEN_EX+"TextBot: 3. Don't forget essential items like chargers, toiletries, and medications.")
    print(Fore.LIGHTGREEN_EX+"TextBot: 4. Use packing cubes to organize your luggage.")
    print(Fore.LIGHTGREEN_EX+"TextBot: 5. Check the weather forecast for your destination and pack accordingly.")
def tell_joke():
    print(Fore.LIGHTGREEN_EX+f"TextBot: Here's a joke {random.choice(list(jokes))}")

def show_help():
    print(Fore.LIGHTGREEN_EX+"TextBot: I can help you with the following commands:")
    print(Fore.LIGHTGREEN_EX+"TextBot: 1. 'recommend' - Get a travel destination recommendation.")
    print(Fore.LIGHTGREEN_EX+"TextBot: 2. 'packing tips' - Get packing tips for your trip.")
    print(Fore.LIGHTGREEN_EX+"TextBot: 3. 'joke' - Hear a joke")
def chat():
    print(Fore.LIGHTGREEN_EX+f"TextBot: hello I am TextBot" )
    name=input(Fore.LIGHTGREEN_EX+"TextBot: what is your name")
    print(Fore.LIGHTGREEN_EX+f"TextBot: Hello {name}, how can I assist you today?")
    show_help()
    while True:
        user_input=input(Fore.LIGHTGREEN_EX+f"{name}: ")
        user_input=normalize_input(user_input)
        if "recommend" in user_input or "suggest" in user_input:
            recommend()

        elif "pack" in user_input or "packing tips" in user_input:
            packing_tips()
        elif "joke" in user_input or "funny"in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input or "quit" in user_input:
            print(Fore.LIGHTGREEN_EX+"TextBot: Goodbye! Have a great day!")
            break
        else:
            print(Fore.LIGHTGREEN_EX+"TextBot: I'm sorry, I didn't understand that. Please try rephrasing it")

if __name__=="__main__":
    chat()