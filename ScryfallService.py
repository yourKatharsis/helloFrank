import requests as req

class ScryfallService:
    base_url: str = 'https://api.scryfall.com'

    def get_card_by_fuzzy(self, fuzzy: str):
        url = self.base_url + '/cards/named?fuzzy=' + fuzzy
        response = req.get(url=url)
        return response
