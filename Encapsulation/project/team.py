from project.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = int(rating)
        self.__players = []

    def add_player(self, player: Player):
        for member in self.__players:
            if member.name == player.name:
                return f"Player {member.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        for member in self.__players:
            if member.name == player_name:
                result = member.__str__()
                self.__players.remove(member)
                return result

        return f"Player {player_name} not found"
