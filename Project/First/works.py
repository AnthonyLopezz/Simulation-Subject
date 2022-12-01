from work import Work
from tasks import Tasks


class Works:
    def __init__(self):
        self._works = []

    @property
    def works(self):
        return self._works

    @works.setter
    def works(self, works):
        self._works = works

    def add_works(self, works, machines):
        counter = 1
        for work in works:
            tasks = Tasks()
            for k, v in work.items():
                tasks.add_task(
                    machines.get_machine(k), v
                )
            self._works.append(
                Work(f'W{counter}', tasks)
            )
            counter += 1

    def simulation_end(self):
        for work in self._works:
            if not work._completed:
                return False
            return True

    def __str__(self):
        output = 'Works: \n [\n'
        for work in self._works:
            output += ' ' + work.__str__() + '\n'

        return output + ']'
