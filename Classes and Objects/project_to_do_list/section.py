from project_to_do_list.task import Task


class Section:
    def __init__(self, name):
        self.name = name

    def add_task(self, new_task: Task):
        pass

    def complete_task(self, task_name: str):
        pass

    def clean_section(self):
        pass

    def view_section(self):
        pass
