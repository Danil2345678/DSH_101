list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
count_players_on_team = len(list_players) // 2
team_1 = list_players[:count_players_on_team]
team_2 = list_players[count_players_on_team:]

print(team_1, team_2, sep="\n")
