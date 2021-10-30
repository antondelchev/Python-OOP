from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        for task in self.tasks:
            if task.name == new_task.name:
                return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task Name: {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                return f"Completed task {task_name}"

        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        counter = 0
        not_completed = []

        for task in self.tasks:
            if task.completed:
                counter += 1
            else:
                not_completed.append(task)

        self.tasks = not_completed
        return f"Cleared {counter} tasks."

    def view_section(self):
        result = f"Section {self.name}:"

        for task in self.tasks:
            result += "\n"
            result += task.details()

        return result