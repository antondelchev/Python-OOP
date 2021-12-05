from project_second.table.table import Table


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if 1 <= value <= 50:
            self.__table_number = value
        else:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")
