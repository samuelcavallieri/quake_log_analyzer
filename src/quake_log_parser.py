import re

def parse_log_file(log_file):
    """
    Reads the log file and groups the information by match.
    """
    games = {}
    current_game = None

    with open(log_file, 'r') as f:
        for line in f:
            if "InitGame:" in line:
                current_game = f"game-{len(games) + 1}"
                games[current_game] = {
                    "total_kills": 0,
                    "players": set(),
                    "kills": {},
                    "kills_by_means": {}  # For item 3.3 (Plus)
                }
            elif "Kill:" in line:
                match = re.match(r".*Kill: (\d+) (\d+) (\d+): (.+) killed (.+) by (.+)", line)
                if match:
                    killer, killed, means_of_death = match.group(4), match.group(5), match.group(6)

                    # Update total kills
                    games[current_game]["total_kills"] += 1

                    # Add players
                    if killer != "<world>":
                        games[current_game]["players"].add(killer)
                        games[current_game]["kills"].setdefault(killer, 0)
                        games[current_game]["kills"][killer] += 1
                    else:
                        games[current_game]["kills"].setdefault(killed, 0)
                        games[current_game]["kills"][killed] -= 1

                    # Update kills by means of death (item 3.3)
                    games[current_game]["kills_by_means"].setdefault(means_of_death, 0)
                    games[current_game]["kills_by_means"][means_of_death] += 1

    # Convert the set of players to a list
    for game in games.values():
        game["players"] = list(game["players"])

    return 

def generate_player_ranking(games):
    """
    Generates a player ranking based on the total number of kills in all matches.
    """
    player_kills = {}
    for game in games.values():
        for player, kills in game["kills"].items():
            player_kills.setdefault(player, 0)
            player_kills[player] += kills

    ranking = sorted(player_kills.items(), key=lambda x: x[1], reverse=True)
    return ranking
