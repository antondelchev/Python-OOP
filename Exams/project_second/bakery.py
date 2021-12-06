from project_second.baked_food.bread import Bread
from project_second.baked_food.cake import Cake
from project_second.drink.tea import Tea
from project_second.drink.water import Water
from project_second.table.inside_table import InsideTable
from project_second.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "".strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        for element in self.food_menu:
            if element.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")

        if food_type == "Bread":
            food = Bread(name, price)
            self.food_menu.append(food)

        elif food_type == "Cake":
            food = Cake(name, price)
            self.food_menu.append(food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        for element in self.drinks_menu:
            if element.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")

        if drink_type == "Tea":
            drink = Tea(name, portion, brand)
            self.drinks_menu.append(drink)

        elif drink_type == "Water":
            drink = Water(name, portion, brand)
            self.drinks_menu.append(drink)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        for element in self.tables_repository:
            if element.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
            self.tables_repository.append(table)

        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)
            self.tables_repository.append(table)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.is_reserved = True
                table.number_of_people = number_of_people
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        all_orders = [x for x in args]
        search_table_num = [x for x in self.tables_repository if x.table_number == table_number]
        if not search_table_num:
            return f"Could not find table {table_number}"

        orders_available = []

        for food in self.food_menu:
            if food.name in all_orders:
                orders_available.append(food)
                all_orders.remove(food.name)

        orders_not_available = all_orders

        search_table_num[0].food_orders = orders_available

        result = ""
        if orders_available:
            result = f"Table {table_number} ordered:\n"
            result += "\n".join([str(x) for x in orders_available]) + "\n"
        result += f"{self.name} does not have in the menu:\n"
        result += "\n".join([str(x) for x in orders_not_available])

        return result.strip()

    def order_drink(self, table_number: int, *args):
        all_orders = [x for x in args]
        search_table_num = [x for x in self.tables_repository if x.table_number == table_number]
        if not search_table_num:
            return f"Could not find table {table_number}"

        orders_available = []

        for drink in self.drinks_menu:
            if drink.name in all_orders:
                orders_available.append(drink)
                all_orders.remove(drink.name)

        orders_not_available = all_orders

        search_table_num[0].drink_orders = orders_available

        result = ""
        if orders_available:
            result = f"Table {table_number} ordered:\n"
            result += "\n".join([str(x) for x in orders_available]) + "\n"
        result += f"{self.name} does not have in the menu:\n"
        result += "\n".join([str(x) for x in orders_not_available])

        return result.strip()

    def leave_table(self, table_number: int):
        result = f"Table: {table_number}\n"
        for table in self.tables_repository:
            if table.table_number == table_number:
                result += f"{table.get_bill():.2f}"
                self.total_income += table.get_bill()
                table.clear()
                break
        return result

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            if not table.is_reserved:
                result.append(table.free_table_info())
        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
