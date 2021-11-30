from unittest import TestCase, main

from third.project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train("Speed", 3)

    def test_init_creates_all_attributes(self):
        self.assertEqual("Speed", self.train.name)
        self.assertEqual(3, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_class_attributes(self):
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_add_passenger_with_full_capacity_raises(self):
        self.train.passengers = ["P1", "P2", "P3"]
        self.assertEqual(["P1", "P2", "P3"], self.train.passengers)
        with self.assertRaises(ValueError) as msg:
            self.train.add("P4")

        self.assertEqual("Train is full", str(msg.exception))
        self.assertEqual(["P1", "P2", "P3"], self.train.passengers)

    def test_add_passenger_who_is_already_on_board_raises(self):
        self.train.passengers = ["P1", "P2"]
        self.assertEqual(["P1", "P2"], self.train.passengers)
        with self.assertRaises(ValueError) as msg:
            self.train.add("P1")

        self.assertEqual("Passenger P1 Exists", str(msg.exception))
        self.assertEqual(["P1", "P2"], self.train.passengers)

    def test_add_passenger_who_is_not_on_board_with_enough_spaces_available(self):
        self.train.passengers = ["P1", "P2"]
        self.assertEqual(["P1", "P2"], self.train.passengers)

        result = self.train.add("P3")

        self.assertEqual("Added passenger P3", result)
        self.assertEqual(["P1", "P2", "P3"], self.train.passengers)

    def test_remove_passenger_who_is_not_on_board(self):
        self.train.passengers = ["P1", "P2"]
        self.assertEqual(["P1", "P2"], self.train.passengers)

        with self.assertRaises(ValueError) as msg:
            self.train.remove("P3")

        self.assertEqual("Passenger Not Found", str(msg.exception))
        self.assertEqual(["P1", "P2"], self.train.passengers)

    def test_remove_passenger_who_is_on_board(self):
        self.train.passengers = ["P1", "P2"]
        self.assertEqual(["P1", "P2"], self.train.passengers)

        result = self.train.remove("P2")

        self.assertEqual("Removed P2", result)
        self.assertEqual(["P1"], self.train.passengers)


if __name__ == "__main__":
    main()
