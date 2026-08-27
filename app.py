print("Hello I am an AI chatbot, what is your name?:")
name=input()
print(f"Hi,nice to meet you{name}.")
print("How are you feeling today?(good/bad):")
mood=input().lower()
if mood=="good":
    print("That's greate to hear!")
elif mood=="bad":
    print("Sorry to hear that,hope you feel better soon.")
else:
    print("I see. Sometimes it's hard to put your feeling's in words")
print("Soo I see you want to join our fine chess class eh? well have you any experence?(yes or no only):")
expirence=input().lower()
if expirence=="yes":
    print("good...")
    print(" how much experence do you have?:")
    years=int(input())
elif expirence=="no":
    print("well that's what this class if for anyway.")
else:
    print("Intresting..")
print("well what is age?:")
age=int(input())
if age<10:
    print("a bit young eh?.")
if age>10:
    print("well thats fine.")
if years==1:
    print("well thats a good baseline.")
if years<10:
    print("Excelent...")
if years>10:
    print("Well isn't that a greate suprise!")
print("Well based on your information we shall get a presonalized teacher for you.")
print("You shall be requested to take a call in 1-10 minites for fixing the timing and dates of the class,")
print("as per this you shall be given the price of the classes.")
print("You can also schedule an trial class with the caller.")