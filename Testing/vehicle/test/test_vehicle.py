from unittest import TestCase, main

from vehicle.project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(50.8, 150)

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.vehicle.fuel, 50.8)
        self.assertEqual(self.vehicle.horse_power, 150)
        self.assertEqual(self.vehicle.capacity, 50.8)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_with_enough_fuel(self):
        self.assertEqual(self.vehicle.fuel, 50.8)
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 38.3)

    def test_drive_with_insufficient_fuel(self):
        self.assertEqual(self.vehicle.fuel, 50.8)
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_valid_amount(self):
        self.assertEqual(self.vehicle.fuel, 50.8)
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 38.3)
        self.vehicle.refuel(8)
        self.assertEqual(self.vehicle.fuel, 46.3)

    def test_refuel_with_excess_amount(self):
        self.assertEqual(self.vehicle.fuel, 50.8)
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 38.3)
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str_representation(self):
        self.assertEqual(str(self.vehicle), "The vehicle has 150 horse power with "
                                            "50.8 fuel left and 1.25 fuel consumption")


if __name__ == "__name__":
    main()
