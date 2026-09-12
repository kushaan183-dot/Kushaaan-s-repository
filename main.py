import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore

# Init colors
init(autoreset=True)

# Load CSV (same error output)
try: df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000.csv' was not found."); raise SystemExit

# Unique genres
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(", ") for g in xs})

def dots():
    """Prints ... with delay (AI thinking effect)."""
    for _ in range(3): print(Fore.YELLOW + ".", end="", flush=True); time.sleep(0.5)

def senti(p):
    """Polarity -> label."""
    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"

def recommend(genre=None, mood=None, rating=None, n=5):
    """Filter by genre/rating, shuffle, analyze Overview polarity, return n (title, polarity) or message."""
    d = df
    if genre: d=d[d["Genre"].str.contains(genre, na=False, case=False)]
    if rating is not None: d=d[d["IMBD_Rating"]>=rating]
    if d.empty: return "No suitable movie recommendations found."
    d, need_nonneg,out=d.sample(frac=1).reset_index(drop=True),bool[mood],[]
    for _, r in d.iterrows():
        ov=r.get("Overview")
        if pd.isna(ov): continue
        pol=TextBlob(ov).sentiment.polarity
        if (not need_nonneg) or pol>0: 
            out.append((r["Series_Title"], pol))
            if len(out) >= n: break
    return out if out else "No suitable movie recommendations found."
def show(recs, name):
    print(Fore.YELLOW+f"\n🍿 AI analysed movie ercomendations for {name}")
    for i, (t,p) in enumerate(recs, 1):
        print(f"{Fore.BLUE}{i}. 🎥 {t} (Polarity:{p:.2f},{senti(p)})")

def get_genre():
    print(Fore.GREEN+"Available Genres:",end="")
    for i,g in enumerate(genres,1): print(f"{Fore.CYAN}{i}. {g}")
    print()
    while True:
        x=input(Fore.YELLOW+"Enter genre number or name:").strip()
        if x.digit() and 1 <= int(x) <= len(genres):return genres[int(x)-1]
        x=x.title()
        if x in genres: return x
        print(Fore.RED+"Invalid input. TRY again \n")

def get_rating():
    while True:
        x=input(Fore.YELLOW+"Enter minimum IMBD rating(7.6-9.3) or (skip)").strip()
        try:
            r=float(x)
            if 7.6<= r <=9.3:return r
            print(Fore.RED+"Out of range try again.\n")
        except ValueError:
            print(Fore.RED+"Invalid input.Try again.\n")
print(Fore.BLUE+"🎥 Welcome to your personal movie  Reccomdation assistant! 🎥")
name=input("What is your name?").strip()
print(Fore.GREEN+f"\n Great to meet you {name}!\n")
print(f"\n🔎 Lets find the perfect movie for you\n")
genre=get_genre()
mood=input(Fore.GREEN+"How are you feeling?").strip()
print(Fore.BLUE+"\nAnalysing mood",end="",flush=True);dots()
mp=TextBlob(mood).sentiment.polarity
mp=mp.TextBlob(mood).sentiment.polarity
md = "positive" if mp > Ø else "negative" if mp < 0 else "neutral😐"
print(f"\n{Fore.BLUE}\n Your mood is {md} (Polarity:{md:.2f}).\n")
rating = get_rating()
print(f"{Fore.BLUE}\nFinding movies for {name}", end="", flush=True); dots()
recs = recommend (genre=genre,mood=mood, rating=rating, n = 5)
print(Fore.RED + recs + "\n") if isinstance (recs, str) else show(recs, name)
while True:
    a=input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
    if a == "no":
        print(Fore.GREEN + f"\nEnjoy your movie picks, {name}!🎥🍿\n"); break
    if a == "yes":
        recs = recommend (genre=genre, mood=mood, rating=rating, n = 5 )
        print(Fore.RED + recs + "\n") if isinstance (recs, str) else show(recs, name)
    else:
        print(Fore.RED + "Invalid choice. Try again.\n")