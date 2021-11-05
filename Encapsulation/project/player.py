class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = int(sprint)
        self.__dribble = int(dribble)
        self.__passing = int(passing)
        self.__shooting = int(shooting)

    @property
    def name(self):
        return self.__name

    def __str__(self):
        result = {"Player": self.__name,
                  "Sprint": self.__sprint,
                  "Dribble": self.__dribble,
                  "Passing": self.__passing,
                  "Shooting": self.__shooting
                  }

        return "\n".join([f"{k}: {v}" for k, v in result.items()])
