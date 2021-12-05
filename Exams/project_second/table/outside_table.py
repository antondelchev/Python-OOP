from project_second.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if 51 <= value <= 100:
            self.__table_number = value
        else:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
