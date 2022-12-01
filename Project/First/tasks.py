from task import Task


class Tasks:
    def __init__(self):
        self._tasks = []

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        self._tasks = tasks

    def add_task(self, machine, time):
        self._tasks.append(Task(machine, time))

    def __str__(self):
        output = 'Tasks: \n [\n'
        for task in self._tasks:
            output += ' ' + task.__str__() + '\n'

        return output + ']'
