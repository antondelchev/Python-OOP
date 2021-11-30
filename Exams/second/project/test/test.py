from second.project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("Kingdom")

    def test_init_creates_all_attributes(self):
        self.assertEqual("Kingdom", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_with_quantity_equal_or_less_than_zero(self):
        for quantity in [-5, 0]:
            with self.assertRaises(ValueError) as msg:
                self.pet_shop.add_food("Bread", quantity)
            expected = 'Quantity cannot be equal to or less than 0'
            self.assertEqual(expected, str(msg.exception))

    def test_add_food_adding_food_that_is_not_already_part_of_food_attribute(self):
        self.assertEqual({}, self.pet_shop.food)
        result = self.pet_shop.add_food("Bread", 100)
        self.assertEqual({"Bread": 100}, self.pet_shop.food)
        expected = "Successfully added 100.00 grams of Bread."
        self.assertEqual(expected, result)

    def test_add_food_adding_food_that_is_part_of_food_attribute(self):
        self.assertEqual({}, self.pet_shop.food)
        self.pet_shop.add_food("Bread", 100)
        self.assertEqual({"Bread": 100}, self.pet_shop.food)
        self.pet_shop.add_food("Bread", 100)
        self.assertEqual({"Bread": 200}, self.pet_shop.food)

    def test_add_pet_adding_pet_that_is_not_already_part_of_pet_attribute(self):
        self.assertEqual([], self.pet_shop.pets)
        result = self.pet_shop.add_pet("Tiger Cat")
        self.assertEqual(["Tiger Cat"], self.pet_shop.pets)
        expected = "Successfully added Tiger Cat."
        self.assertEqual(expected, result)

    def test_add_pet_adding_pet_with_same_name(self):
        self.assertEqual([], self.pet_shop.pets)
        self.pet_shop.add_pet("Tiger Cat")
        self.assertEqual(["Tiger Cat"], self.pet_shop.pets)

        with self.assertRaises(Exception) as msg:
            self.pet_shop.add_pet("Tiger Cat")

        expected = "Cannot add a pet with the same name"
        self.assertEqual(expected, str(msg.exception))

    def test_feed_pet_feeding_pet_that_is_not_already_part_of_pet_attribute(self):
        self.assertEqual([], self.pet_shop.pets)
        self.pet_shop.add_food("Bread", 100)
        with self.assertRaises(Exception) as msg:
            self.pet_shop.feed_pet("Bread", "Tiger Cat")
        expected = "Please insert a valid pet name"
        self.assertEqual(expected, str(msg.exception))

    def test_feed_pet_feeding_pet_with_food_that_is_not_already_part_of_food_attribute(self):
        self.assertEqual({}, self.pet_shop.food)
        self.pet_shop.add_pet("Tiger Cat")

        result = self.pet_shop.feed_pet("Bread", "Tiger Cat")
        expected = 'You do not have Bread'
        self.assertEqual(expected, result)

    def test_feed_pet_food_auto_refilling_with_one_thousand_if_quantity_under_one_hundred(self):
        self.pet_shop.add_pet("Tiger Cat")
        self.pet_shop.add_food("Bread", 99)
        result = self.pet_shop.feed_pet("Bread", "Tiger Cat")
        self.assertEqual(1099.00, self.pet_shop.food["Bread"])
        expected = "Adding food..."
        self.assertEqual(expected, result)

    def test_feed_pet_under_normal_circumstances_should_decrease_quantity_by_one_hundred(self):
        self.pet_shop.add_pet("Tiger Cat")
        self.pet_shop.add_food("Bread", 100)
        result = self.pet_shop.feed_pet("Bread", "Tiger Cat")

        expected = "Tiger Cat was successfully fed"
        self.assertEqual({"Bread": 0}, self.pet_shop.food)
        self.assertEqual(expected, result)

    def test_repr_displays_correctly(self):
        expected = f'Shop {self.pet_shop.name}:\nPets: {", ".join(self.pet_shop.pets)}'
        self.assertEqual(expected, str(self.pet_shop))


if __name__ == "__main__":
    main()
