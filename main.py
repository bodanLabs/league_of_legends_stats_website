


from flask import Flask, render_template, request, session, redirect, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key for session management

# Function to get summoner data from the provided URL using summoner's name

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        full_name = request.form['name']
        name = full_name.split("#")[0]
        tag = full_name.split("#")[1]
        
        # Store fetched data in session
        session['game_tag'] = full_name
        
        from actions.get_summoner_data import get_puuid, get_summoner_general_data
        puuid = get_puuid(name,tag)
        session['puuid'] = puuid
        
        summoner_general_data = get_summoner_general_data(puuid)
        session['summoner_id'] = summoner_general_data[0]
        session['account_id'] = summoner_general_data[1]
        session['profile_icon_id'] = summoner_general_data[2]
        session['summoner_level'] = summoner_general_data[3]
        
        
        from actions.get_summoner_data import get_summoner_ranked
        summoner_ranked = get_summoner_ranked(session['summoner_id'])
        session['solo_rank_tier'] = summoner_ranked[0]
        session['solo_rank'] = summoner_ranked[1]
        session['solo_league_points'] = summoner_ranked[2]
        session['solo_wins'] = summoner_ranked[3]
        session['solo_losses'] = summoner_ranked[4]
        session['flex_rank_tier'] = summoner_ranked[5]
        session['flex_rank'] = summoner_ranked[6]
        session['flex_league_points'] = summoner_ranked[7]
        session['flex_wins'] = summoner_ranked[8]
        session['flex_losses'] = summoner_ranked[9]
        
        
        from actions.get_match_data import get_match_history
        match_history = get_match_history(puuid)
        session['first_game_id'] = match_history[0]
        session['second_game_id'] = match_history[1]
        session['third_game_id'] = match_history[2]
        
        
        from actions.get_match_data import get_match_data
        first_game_id = session['first_game_id']
        puuid = session.get('puuid', '')
        match_data = get_match_data(first_game_id,puuid)
        
        
        session['game_mode'] = match_data[0]
        session['game_duration'] = match_data[1]
        session['player_kills'] = match_data[2]
        session['player_deaths'] = match_data[3]
        session['player_assists'] = match_data[4]
        session['player_items'] = match_data[5]
        session['player_gold'] = match_data[6]
        session['champion_name'] = match_data[7]
        session['time_from_game'] = match_data[8]
        session['player_kda'] = match_data[9]
        session['player_summoner_spell_1'] = match_data[10]
        session['player_summoner_spell_2'] = match_data[11]
        session['player_rune_1'] = match_data[12]
        session['player_rune_2'] = match_data[13]
        session['nexus_lost'] = match_data[14]
        
        
        from actions.get_summoner_spell import get_summoner_spell_path
        summoner_spell_1_id = session.get('player_summoner_spell_1', '')
        summoner_spell_2_id = session.get('player_summoner_spell_2', '')
        summoner_spell_paths = get_summoner_spell_path(summoner_spell_1_id,summoner_spell_2_id)
        
        session['summoner_spell_1_path'] = summoner_spell_paths[0]
        session['summoner_spell_2_path'] = summoner_spell_paths[1]
        
        
        from actions.get_player_runes import get_player_rune_path
        player_rune_id_1= session.get('player_rune_1', '')
        player_rune_id_2= session.get('player_rune_2', '')
        player_rune_paths = get_player_rune_path(player_rune_id_1,player_rune_id_2)
        
        session['player_rune_1_path'] = player_rune_paths[0]
        session['player_rune_2_path'] = player_rune_paths[1]
        
        
        from actions.get_items_description import get_items_data   
        item_1_name = get_items_data(match_data[5][0])[0]
        item_1_description = get_items_data(match_data[5][0])
        item_1_cost = get_items_data(match_data[5][0])
        session['item_1_name'] = item_1_name
        session['item_1_description'] = item_1_description
        session['item_1_cost'] = item_1_cost
        
        
        return redirect(url_for('user'))
    return render_template('home.html')

@app.route('/user')
def user():
    # Retrieve data from session to pass to the template
    summoner_name = session.get('game_tag', '')
    puuid = session.get('puuid', '')
    summoner_level = session.get('summoner_level', '')
    profile_icon_id = session.get('profile_icon_id', '')
    profile_icon_id_path = f"img/profileicon/{profile_icon_id}.png"
    
    solo_rank_tier = session.get('solo_rank_tier', '')
    solo_rank = session.get('solo_rank', '')
    solo_league_points = session.get('solo_league_points', '')
    solo_wins = session.get('solo_wins', '')
    solo_losses = session.get('solo_losses', '')
    solo_rank_logo_path = f"/img/rank/logos/{solo_rank_tier}.png"
    
    flex_rank_tier = session.get('flex_rank_tier', '')
    flex_rank = session.get('flex_rank', '')
    flex_league_points = session.get('flex_league_points', '')
    flex_wins = session.get('flex_wins', '')
    flex_losses = session.get('flex_losses', '')
    flex_rank_logo_path = f"/img/rank/logos/{flex_rank_tier}.png"
    
    
    game_mode = session.get('game_mode', '')
    game_duration = session.get('game_duration', '')
    player_kills = session.get('player_kills', '')
    player_deaths = session.get('player_deaths','')
    player_assists = session.get('player_assists','')
    
    player_items = session.get('player_items','')
    player_item_1_url = f"/img/item/{player_items[0]}.png"
    player_item_2_url = f"/img/item/{player_items[1]}.png"
    player_item_3_url = f"/img/item/{player_items[2]}.png"
    player_item_4_url = f"/img/item/{player_items[3]}.png"
    player_item_5_url = f"/img/item/{player_items[4]}.png"
    player_item_6_url = f"/img/item/{player_items[5]}.png"
    
    player_gold = session.get('player_gold','')
    
    champion_name = session.get('champion_name','')
    champion_played_path = f"/img/champion/{champion_name}.png"
    
    
    time_from_game = session.get('time_from_game','')
    
    player_kda = session.get('player_kda','')
    
    
    summoner_spell_1_path = session.get('summoner_spell_1_path','')
    summoner_spell_2_path = session.get('summoner_spell_2_path','')
    
    player_rune_path_1 = session.get('player_rune_1_path','')
    player_rune_path_2 = session.get('player_rune_2_path','')
    
    nexus_lost = session.get('nexus_lost','')
    if str(nexus_lost) == str(0):
        card_color = "#14a620" 
    else:
        card_color = "#ff1919"
        
    item_1_name = session.get('item_1_name','')
    item_1_description = session.get('item_1_description','')
    item_1_cost = session.get('item_1_cost','')
    
    
    
    return render_template('user.html', profile_icon_id_path = profile_icon_id_path,summoner_name=summoner_name,puuid=puuid, summoner_level=summoner_level,
                           solo_rank_tier=solo_rank_tier, solo_rank=solo_rank, solo_league_points=solo_league_points,
                           solo_wins=solo_wins, solo_losses=solo_losses, flex_rank_tier=flex_rank_tier, flex_rank=flex_rank,
                           flex_league_points=flex_league_points, flex_wins=flex_wins, flex_losses=flex_losses,
                           solo_rank_logo_path=solo_rank_logo_path,flex_rank_logo_path=flex_rank_logo_path, 
                           game_mode=game_mode, game_duration=game_duration, player_kills=player_kills,
                           player_deaths=player_deaths, player_assists=player_assists,
                           player_gold=player_gold, champion_name=champion_name,
                           player_item_1_url=player_item_1_url, player_item_2_url=player_item_2_url,
                           player_item_3_url=player_item_3_url, player_item_4_url=player_item_4_url,
                           player_item_5_url=player_item_5_url, player_item_6_url=player_item_6_url,
                           champion_played_path=champion_played_path,time_from_game=time_from_game,
                           player_kda=player_kda, summoner_spell_1_path=summoner_spell_1_path,
                           summoner_spell_2_path=summoner_spell_2_path, player_rune_path_1=player_rune_path_1,
                           player_rune_path_2=player_rune_path_2, card_color=card_color,item_1_name=item_1_name)

if __name__ == '__main__':
    app.run(debug=True)
