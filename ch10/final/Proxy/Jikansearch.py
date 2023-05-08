import requests

class Jikansearch:
    def __init__(self, name):
        """
        initlize the url of the api and the status for status_code
        args: animeName(str)- name of an anime
        return: None
        """
        self.api_url = f"https://api.jikan.moe/v4/anime?q={name}&limit=1"
        self.status = None
    
    def get(self):
        """
        Try to fetch anime information from api. Check status code to confirm if information is fetched correctly. Return information only when status code=200. 
        If not, print out message and exit. Call print_anime_info to print out certain anime information to the screen
        args: Nonemak
        return: None
        """
        try:
            self.status = requests.get(self.api_url, timeout=3)
            if self.status.status_code == 200:
                results = self.status.json()
                if len(results) > 0:
                    self.print_anime_info(anime_dict=results['data'][0])
                else:
                    print(f"No results found for anime selected")
            else:
                print("Something went wrong, please try again")
                exit()
        except:
            print("Cannot obtain information regarding the anime")
            exit()
    
    def print_anime_info(self, anime_dict):
        """
        Go into the given dictionary containing anime information and display certain information on the screen
        args: anime_dict(dict) - a dictionary with the anime information
        return: None
        """
        if 'title_japanese' in anime_dict and 'synopsis' in anime_dict:
            jap_title = anime_dict['title_japanese']
            synopsis = anime_dict['synopsis']
            print(f"Japanese Title: {jap_title}")
            print(f"Synopsis: {synopsis}")
        else:
            print("Error: anime_dict does not have expected informations")
    
    def __str__(self):
        """
        return the descrption of the object
        args: None
        return: self.description(str)
        """
        self.description = 'Animesearch Class Object'
        return self.description









