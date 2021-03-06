from project_guild_system.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:
            if player.guild == self.name:
                return f"Player {player.name} is already in the guild."
            else:
                return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name in self.players:
            player_name.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = [el.player_info() for el in self.players]
        return f"Guild: {self.name}\n" + "\n".join(result)


player_one = Player("George", 50, 100)
print(player_one.add_skill("Shield Break", 20))
print(player_one.player_info())
guild = Guild("UGT")
print(guild.assign_player(player_one))
print(guild.guild_info())
