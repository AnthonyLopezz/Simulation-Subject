from machine import Machine


class Machines:
    def __init__(self):
        self._machines = []

    @property
    def machines(self):
        return self._machines

    @machines.setter
    def id(self, machines):
        self._machines = machines

    def add_machines(self, machines):
        for machine in machines:
            self._machines.append(Machine(machine))

    def get_machine(self, id):
        for machine in self.machines:
            if machine.id == id:
                return machine
        return None

    def is_available(self, machine):
        for m in self._machines:
            if machine.id == m.id and m.available:
                return True
        return False

    def __str__(self):
        output = 'Machines: \n [\n'
        for machine in self._machines:
            output += ' ' + machine.__str__() + '\n'

        return output + ']'
