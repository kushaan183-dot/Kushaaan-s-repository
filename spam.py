SPAM_WORDS={
    "free":2,"winner":3,"won":3,"price":3,"lootery":3,"urgent":2,"click":2,"claim":2,"cash":2,"verify":2,"congratulations":2,"offer":1,"limited":1,"now":1,"account":1
}
THRESHOLD=4
USE_LEET=False
LEET=str.maketrans("13450@$","ieasoas")
PUNCTUATION=".,!?:;\"'()"
def clean_word(word):
    word=word.lower()
    if USE_LEET:
        word=word.translate(LEET)
    return word.strip(PUNCTUATION)

def tokenize(message):
    word=[]
    for word in message.split():
        cleaned=clean_word(word)
        if cleaned:
            word.append(cleaned)
    return word

def spam_score(message):
    score=0
    for word in tokenize(message):
        score+=SPAM_WORDS.get(word, 0)
    return score

def classify(message):
    if spam_score(message)>=THRESHOLD:
        return "SPAM"
    return "SAFE"

TEST_MESSAGES=[
    ("Congratulations! You WON a free iPhone. Click now to claim", "SPAM"),
    ("URGENT: verify your account or it will be blocked", "SPAM"),
    ("Claim your cash prize before midnight", "SPAM"),
    ("Hey, are we still meeting at 5?", "SAFE"),
    ("Your free coding class starts at 5 PM today", "SAFE"),
    ("Mom says dinner is ready, come down now", "SAFE"),
    ("WINNER!!! click here for your prize", "SPAM"),
    ("Limited offer: free cash for new users, claim now", "SPAM"),
    ("Click the link in the class group to join the free quiz now", "SAFE"),
    ("Your bank account statement for March is ready", "SAFE"),
]

def run_tests():
    correct=false_positivies=false_negatives=0
    for message,expected in TEST_MESSAGES:
        result=classify(message)
        if result==expected:
            correct+=1
            mark="OK"
        elif result=="SPAM":
            false_positivies+=1
            mark="FP"
        else:
            false_negatives+=1
            mark="FN"
        print(f"{mark}  {result}    Score={spam_score(message)::2}  (message)")
    print(f"\nAccuracy: {correct}/{len(TEST_MESSAGES)}")
    print(f"False positives (safe messages blocked): {false_positivies}")
    print(f"False negatives (spam messages through): {false_negatives}")
if __name__=="__main__":
    run_tests()
    print("\nType a message to cheak it or quit to stop.")
    while True:
        messags=input("\n>")
        if messags.strip().lower()=="quit":
            break
        print(f"{classify(message)} | score: {spam_score(message)} | flagged:{explain(message)}")