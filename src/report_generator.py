from quake_log_parser import parse_log_file, generate_player_ranking

def print_match_reports(games):
    """
    Prints the reports for each match.
    """
    for game_name, game_data in games.items():
        print(f"\nMatch report {game_name}:")
        print(f"  Total kills: {game_data['total_kills']}")
        print(f"  Players: {', '.join(game_data['players'])}")
        print("  Kills per player:")
        for player, kills in game_data["kills"].items():
            print(f"    {player}: {kills}")

        # Print kills by means of death (item 3.3)
        print("  Kills by means of death:")
        for means, count in game_data["kills_by_means"].items():
            print(f"    {means}: {count}")

def print_player_ranking(ranking):
    """
    Prints the player ranking.
    """
    print("\nPlayer ranking:")
    for i, (player, kills) in enumerate(ranking):
        print(f"  {i+1}. {player}: {kills} kills")

if __name__ == "__main__":
    games = parse_log_file("games.log")
    ranking = generate_player_ranking(games)

    print_match_reports(games)
    print_player_ranking(ranking)