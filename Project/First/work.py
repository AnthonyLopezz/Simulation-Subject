
class Work:
    def __init__(self, id, tasks):
        self._id = id
        self._tasks = tasks
        self._completed = False

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def tasks(self):
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        self._tasks = tasks

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, completed):
        self._completed = completed


    def __str__(self):
        return f'Work: [Id: {self._id} ' +\
            f'{self._tasks} ' +\
            f'Completed: {self._completed}]'
