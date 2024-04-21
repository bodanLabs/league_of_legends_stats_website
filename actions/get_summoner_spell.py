import requests


def get_summoner_spell_path(summoner_spell_key_1,summoner_spell_key_2):
    url = f"https://ddragon.leagueoflegends.com/cdn/14.4.1/data/en_US/summoner.json"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "riot_token"
}
    response = requests.get(url, headers=headers)
    data = response.json()
    for item in data['data']:
        if str(data['data'][item]['key']) == str(summoner_spell_key_1):
            summoner_spell_path_1 = f"/img/spell/{data['data'][item]['id']}.png"
        else:
            continue
    
    for item in data['data']:
        if str(data['data'][item]['key']) == str(summoner_spell_key_2):
            summoner_spell_path_2 = f"/img/spell/{data['data'][item]['id']}.png"
        else:
            continue
        
    return summoner_spell_path_1, summoner_spell_path_2

