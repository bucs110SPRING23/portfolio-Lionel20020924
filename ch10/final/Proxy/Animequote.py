import requests

class Animequote:
    def __init__(self):
        """
        initialize the api url
        args: None
        return: None
        """
        self.api_url = f'https://animechan.vercel.app/api/random'

    def get(self):
        """
        Fetching random anime quote from the api. Check the status code and return anime quote when status_code = 200. Otherwise, print out an error message and exit
        args: None
        return: anime_quote(str)- anime quote in the format of anime - character - quote
        """
        try:
            self.status = requests.get(self.api_url, timeout=2)

        except:
            print("Something went wrong, no Anime quotes for you~")
            exit()

        else:
            if self.status.status_code == 200:
                info = self.status.json()
                character = info['character']
                anime = info['anime']
                quote = info['quote']
                anime_quote = f"Character: {character}  \nAnime: {anime}\n" \
                             f"Quote: {quote}"
                return anime_quote

            else:
                print("Something is wrong")
                exit()

    def __str__(self):
        """
        return the descrption of the object
        args: None
        return: self.description(str)
        """
        self.description = 'Class Object for Anime Quotes'
        return self.description





