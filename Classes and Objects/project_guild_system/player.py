class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if self.skills.get(skill_name):
            return "Skill already added"
        else:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        info = [f"==={k} - {v}" for k, v in self.skills.items()]
        return f"Name: {self.name}\n" + f"Guild: {self.guild}\n" + f"HP: {self.hp}\n" \
               + f"MP: {self.mp}\n" + "\n".join(info)
