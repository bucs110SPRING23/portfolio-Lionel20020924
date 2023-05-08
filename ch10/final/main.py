from Proxy.Jikansearch import Jikansearch as search
from Proxy.Animequote import Animequote

def main():
    answer = input("Want the Japanese name and synopsis about an anime?\n")
    search(answer).get()    

    want_quotes = input("Radnom Anime Quote of the day? Y/N\n").upper()
    if want_quotes == "Y":  # user wants a random quote
        quote = Animequote().get()  # quote returned by Animequote
        print(quote)    
    else:
        print("I guess not") # The user typed in N

main()