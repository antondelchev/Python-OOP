class Task:
    comments = []
    completed = False

    def __init__(self, date, due_date):
        self.date = date
        self.due_date = due_date
        self.tasks = []

    def change_name(self, new_name: str):
        pass

    def change_due_date(self, new_date: str):
        pass

    def add_comment(self, comment: str):
        pass

    def edit_comment(self, comment_number: int, new_comment: str):
        pass

    def details(self):
        pass
