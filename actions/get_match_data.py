import requests



def get_match_history(puuid):
    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=3"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": "RGAPI-ac7cc32a-168f-4e60-97f8-bc93e826b277"
}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        first_game_id = response.json()[0]
        second_game_id = response.json()[1]
        third_game_id = response.json()[2]
        return first_game_id,second_game_id,third_game_id




def get_match_data(match_id,puuid):
    url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}"
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
        game_mode = data['info']['gameMode']
        
        game_duration_from_api = data['info']['gameDuration']
        from actions.game_time_convertor import convert_game_time
        game_duration = convert_game_time(game_duration_from_api)
        
        game_end_timestamp = data['info']['gameEndTimestamp']
        from actions.timestamp_difference import get_time_difference
        time_from_game = get_time_difference(game_end_timestamp)
        
        all_players = data['info']['participants']
        for player in all_players:
            if player['puuid'] == puuid:
                player_kills = player['kills']
                player_deaths = player['deaths']
                player_assists = player['assists']
                player_kda = f"{round(int(player_kills)+int(player_assists)/int(player_deaths),1)}:1 KDA"
                player_item1 = player['item0']
                player_item2 = player['item1']
                player_item3 = player['item2']
                player_item4 = player['item3']
                player_item5 = player['item4']
                player_item6 = player['item5']
                player_item7 = player['item6']
                player_items = [player_item1,player_item2,player_item3,player_item4,player_item5,player_item6,player_item7]
                player_gold = player['goldEarned']
                champion_name = player['championName']
                player_summoner_spell_1 = player['summoner1Id']
                player_summoner_spell_2 = player['summoner2Id']
                
                rune_id_1 = player['perks']['styles'][0]['style']
                rune_id_2 = player['perks']['styles'][1]['style']
                
                nexus_lost = player['nexusLost']
                
                
                
        return game_mode, game_duration, player_kills, player_deaths,player_assists, player_items, player_gold, champion_name, time_from_game, player_kda, player_summoner_spell_1, player_summoner_spell_2,rune_id_1,rune_id_2,nexus_lost
