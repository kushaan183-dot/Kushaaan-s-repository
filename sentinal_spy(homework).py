import colorama
import textblob
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(f"{Fore.GREEN}Welcome to Sentinal Spy!{Style.RESET_ALL}")
input_name = input(f"{Fore.LIGHTCYAN_EX}please enter your name: {Style.RESET_ALL}")
if not input_name:
    print(f"{Fore.RED}Welcome mysterious agent!{Style.RESET_ALL}")
conversation_history=[]
print(f"{Fore.LIGHTCYAN_EX}Hello {input_name}!{Style.RESET_ALL}")
print(f"{Fore.LIGHTCYAN_EX}I am Sentinal Spy, enter a message and using textblob i will tell you the sentiment{Style.RESET_ALL}")
print(f"{Fore.LIGHTCYAN_EX}Type 'exit' to end the conversation.{Style.RESET_ALL}")
print(f"{Fore.LIGHTCYAN_EX}Type 'history' to see the conversation history.{Style.RESET_ALL}")
print(f"{Fore.LIGHTCYAN_EX}Type 'clear' to clear the conversation history.{Style.RESET_ALL}")
while True:
    user_input = input(f"{Fore.LIGHTGREEN_EX}>> {Style.RESET_ALL}")
    if not user_input:
        print(f"{Fore.RED}Please enter a message.{Style.RESET_ALL}")
        continue
    if user_input.lower() == 'exit':
        print(f"{Fore.LIGHTCYAN_EX}Goodbye {input_name}!{Style.RESET_ALL}")
        break
    elif user_input.lower() == 'clear':
        conversation_history.clear()
        print(f"{Fore.LIGHTCYAN_EX}Conversation history cleared.{Style.RESET_ALL}")

    elif user_input.lower() == 'history':
        if not conversation_history:
            print(f"{Fore.RED}No conversation history found.{Style.RESET_ALL}")
        else:
            print(f"{Fore.LIGHTCYAN_EX}Conversation History:{Style.RESET_ALL}")
            for idx,(test,polarity,sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type=="positive":
                    color = Fore.GREEN
                    emoji="😊"
                elif sentiment_type=="negative":
                    color = Fore.RED
                    emoji="😞"
                elif sentiment_type=="neutral":
                    color = Fore.YELLOW
                    emoji="😐"
                print(f"{idx}, {color}{emoji}{sentiment_type} sentiment detected"f"Polarity: {polarity:.2f} - {test}{Style.RESET_ALL}")
        continue
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "neutral"
        color = Fore.YELLOW
        emoji = "😐"
    conversation_history.append((user_input, polarity, sentiment_type))
    print(f"{color}{emoji} {sentiment_type} sentiment detected."f"Polarity: {polarity:.2f}{Style.RESET_ALL}")