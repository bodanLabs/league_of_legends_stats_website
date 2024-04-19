import requests

def get_puuid(name,tag):
    url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}"
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-ac7cc32a-168f-4e60-97f8-bc93e826b277"
}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        puuid = data['puuid']
        return puuid
    else:
        print("Request failed with status code:", response.status_code)
        
        
def get_summoner_general_data(puuid):
    url = f"https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-ac7cc32a-168f-4e60-97f8-bc93e826b277"
}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        summoner_id = data['id']
        account_id = data['accountId']
        profile_icon_id = data['profileIconId']
        summoner_level = data['summonerLevel']
        return summoner_id, account_id, profile_icon_id, summoner_level
    else:
        print("Request failed with status code:", response.status_code)

def get_summoner_ranked(summoner_id):
    url = f"https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-ac7cc32a-168f-4e60-97f8-bc93e826b277"
}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        try:
            solo_rank_tier = data[1]['tier']
            solo_rank_ = data[1]['rank']
            solo_league_points = f"{data[1]['leaguePoints']} LP"
            solo_wins = f"{data[1]['wins']} W"
            solo_losses = f"{data[1]['losses']} L"
        except:
            solo_rank_tier = "UNRANKED"
            solo_rank_ = ""
            solo_league_points = ""
            solo_wins = ""
            solo_losses = ""
        
        
        try:
            flex_rank_tier = data[0]['tier']
            flex_rank_ = data[0]['rank']
            flex_league_points = f"{data[0]['leaguePoints']} LP"
            flex_wins = f"{data[0]['wins']} W"
            flex_losses = f"{data[0]['losses']} L"
        except:
            flex_rank_tier = "UNRANKED"
            flex_rank_ = ""
            flex_league_points = ""
            flex_wins = ""
            flex_losses = ""
        return solo_rank_tier, solo_rank_, solo_league_points, solo_wins, solo_losses, flex_rank_tier, flex_rank_, flex_league_points, flex_wins, flex_losses
        
        
        


