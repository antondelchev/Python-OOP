from project_to_do_list.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task.name in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task Name: {new_task.name} - Due Date: {new_task.due_date} is added to the section"

    def complete_task(self, task_name: str):
        if task_name in self.tasks:
            task_name.completed = True
            return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        counter = 0
        for index in range(len(self.tasks)):
            if self.tasks[index].completed and counter == 0:
                self.tasks.pop(index)
                counter += 1
            elif self.tasks[index - 1].completed and counter > 0:
                self.tasks.pop(index - 1)
                counter += 1
        return f"Cleared {counter} tasks."

    def view_section(self):
        details = [f"Name: {el.name} - Due Date: {el.due_date}" for el in self.tasks]
        return f"Section {self.name}:\n" + "\n".join(details)


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())
