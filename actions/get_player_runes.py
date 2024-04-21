import requests


def get_player_rune_path(rune_id_1,rune_id_2):
    url = f"https://ddragon.leagueoflegends.com/cdn/14.4.1/data/en_US/runesReforged.json"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "riot_token"
}
    response = requests.get(url, headers=headers)
    data = response.json()
    for item in data:
        if str(item['id']) == str(rune_id_1):
            rune_path_1 = f"/img/runes/{item['key']}.png"
        else:
            continue
    
    for item in data:
        if str(item['id']) == str(rune_id_2):
            rune_path_2 = f"/img/runes/{item['key']}.png"
        else:
            continue
        
    return rune_path_1, rune_path_2






