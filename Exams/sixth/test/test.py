from sixth.project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("TeamName")

    def test_init_creates_all_attributes(self):
        self.assertEqual("TeamName", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_with_non_letter_characters_raises(self):
        with self.assertRaises(ValueError) as msg:
            self.team = Team("#!123 Name")
        self.assertEqual("Team Name can contain only letters!", str(msg.exception))

    def test_add_members_with_no_duplicates(self):
        result = self.team.add_member(name=23, name2=25)
        self.assertEqual(f"Successfully added: name, name2", result)
        self.assertEqual({"name": 23, "name2": 25}, self.team.members)

    def test_remove_member_removing_existing_member(self):
        self.team.add_member(name=23, name2=25)
        self.assertEqual({"name": 23, "name2": 25}, self.team.members)
        result = self.team.remove_member("name")
        self.assertEqual("Member name removed", result)
        self.assertEqual({"name2": 25}, self.team.members)

    def test_remove_member_removing_nonexistent_member(self):
        self.team.add_member(name=23, name2=25)
        self.assertEqual({"name": 23, "name2": 25}, self.team.members)
        result = self.team.remove_member("name3")
        self.assertEqual("Member with name name3 does not exist", result)
        self.assertEqual({"name": 23, "name2": 25}, self.team.members)

    def test_greater_than_returns_true(self):
        self.team.add_member(name=23, name2=25)
        self.assertEqual({"name": 23, "name2": 25}, self.team.members)

        another_team = Team("AnotherTeam")
        another_team.add_member(name=20)
        self.assertEqual({"name": 20}, another_team.members)

        self.assertEqual(True, self.team > another_team)

    def test_greater_than_returns_false(self):
        self.team.add_member(name=23)
        self.assertEqual({"name": 23}, self.team.members)

        another_team = Team("AnotherTeam")
        another_team.add_member(name=20, name2=25)
        self.assertEqual({"name": 20, "name2": 25}, another_team.members)
        self.assertEqual(False, self.team > another_team)

    def test_len_returning_correct_value(self):
        self.team.add_member(name=23)
        self.assertEqual({"name": 23}, self.team.members)
        self.assertEqual(1, len(self.team))

    def test_add_method_returns_combined_team_name_and_members(self):
        self.team.add_member(name=23)
        self.assertEqual({"name": 23}, self.team.members)

        another_team = Team("AnotherTeam")
        another_team.add_member(name2=20, name3=25)
        self.assertEqual({"name2": 20, "name3": 25}, another_team.members)

        result = self.team + another_team
        self.assertEqual("TeamNameAnotherTeam", result.name)

        self.assertEqual({"name": 23, "name2": 20, "name3": 25}, result.members)

    def test_str_returns_sorted_team(self):
        self.team.add_member(name=28, name2=25, name3=32)
        self.assertEqual({"name": 28, "name2": 25, "name3": 32}, self.team.members)
        result = str(self.team)
        expected = f"Team name: TeamName\nMember: name3 - 32-years old" \
                   f"\nMember: name - 28-years old\nMember: name2 - 25-years old"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
