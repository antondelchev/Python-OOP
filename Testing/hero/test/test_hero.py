from unittest import TestCase, main

from hero.project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("P1", 10, 100.0, 7.0)
        self.enemy_hero = Hero("P2", 8, 90.0, 5.0)

    def test_creates_all_attributes_on_initialization(self):
        self.assertEqual("P1", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100.0, self.hero.health)
        self.assertEqual(7.0, self.hero.damage)

    def test_hero_and_enemy_same_usernames(self):
        self.enemy_hero.username = "P1"
        with self.assertRaises(Exception) as msg:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight yourself", str(msg.exception))

    def test_hero_health_below_zero(self):
        self.hero.health = -10
        with self.assertRaises(ValueError) as msg:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(msg.exception))

    def test_hero_health_equal_to_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as msg:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(msg.exception))

    def test_enemy_hero_health_below_zero(self):
        self.enemy_hero.health = -10
        with self.assertRaises(ValueError) as msg:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight P2. He needs to rest", str(msg.exception))

    def test_enemy_hero_health_equal_to_zero(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as msg:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight P2. He needs to rest", str(msg.exception))

    def test_outcome_as_draw(self):
        self.hero.damage = 10000
        self.enemy_hero.damage = 10000

        expected_hero_health = self.hero.health - (self.enemy_hero.damage * self.enemy_hero.level)
        expected_enemy_hero_health = self.enemy_hero.health - self.hero.damage * self.hero.level

        self.assertEqual(self.hero.battle(self.enemy_hero), "Draw")

        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_enemy_hero_health, self.enemy_hero.health)

    def test_outcome_as_victory(self):
        self.hero.damage = 10000
        self.enemy_hero.damage = 1
        self.assertEqual(self.hero.battle(self.enemy_hero), "You win")
        self.assertEqual(11, self.hero.level)
        self.assertEqual(97.0, self.hero.health)
        self.assertEqual(10005, self.hero.damage)

    def test_outcome_as_defeat(self):
        self.enemy_hero.damage = 10000
        self.hero.damage = 1
        self.assertEqual(self.hero.battle(self.enemy_hero), "You lose")
        self.assertEqual(9, self.enemy_hero.level)
        self.assertEqual(85.0, self.enemy_hero.health)
        self.assertEqual(10005, self.enemy_hero.damage)

    def test_str_representation(self):
        result = f"Hero P1: 10 lvl\nHealth: 100.0\nDamage: 7.0\n"
        self.assertEqual(result, str(self.hero))


if __name__ == "__main__":
    main()
