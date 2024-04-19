import requests


def get_items_data(item_id):
    url = f"https://ddragon.leagueoflegends.com/cdn/14.5.1/data/en_US/item.json"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-ac7cc32a-168f-4e60-97f8-bc93e826b277"
}
    response = requests.get(url, headers=headers)
    data = response.json()
    
    for item in data['data']:
        if str(item) == str(item_id):
            item_name = data['data'][item]['name']
            item_description = data['data'][item]['description']
            item_cost = data['data'][item]['gold']['total']
            return item_name, item_description, item_cost