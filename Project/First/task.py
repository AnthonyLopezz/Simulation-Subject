from mimetypes import init


class Task:
    def __init__(self, machine, task_time):
        self._machine = machine
        self._task_time = task_time
        self._count_down = task_time
        self._completed = task_time == 0

    @property
    def machine(self):
        return self._machine

    @machine.setter
    def machine(self, machine):
        self._machine = machine

    @property
    def task_time(self):
        return self._task_time

    @task_time.setter
    def task_time(self, task_time):
        self._task_time = task_time

    @property
    def count_down(self):
        return self._count_down

    @count_down.setter
    def count_down(self, count_down):
        self._count_down = count_down

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, completed):
        self._completed = completed

    def __str__(self):
        return f'Task: [{self._machine}, ' +\
            f'Time: {self._task_time} ' +\
            f'Count down: {self._count_down} ' +\
            f'Completed: {self._completed} ]'
