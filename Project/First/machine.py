from mimetypes import init


class Machine:
    def __init__(self, id):
        self._id = id
        self._available = True
        self._current_work = None
        self._count_down = 0

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, available):
        self._available = available

    @property
    def current_work(self):
        return self._current_work

    @current_work.setter
    def current_work(self, current_work):
        self._current_work = current_work

    @property
    def count_down(self):
        return self._count_down

    @count_down.setter
    def count_down(self, count_down):
        self._count_down = count_down

    def __str__(self):
        return f'Machine: [Id: {self._id}, ' +\
            f'Available: {self._available} ' +\
            f'Current work: {self._current_work} ' +\
            f'Count down: {self._count_down} ]'
