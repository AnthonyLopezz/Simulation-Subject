from machines import Machines
from machine import Machine
from works import Works
from time import sleep


class Simulator:
    def __init__(self):
        self._machines = None
        self._works = []
        self._clock = 0

    @property
    def machines(self):
        return self._machines

    @machines.setter
    def machines(self, machines):
        return self._machines == machines

    @property
    def works(self):
        return self._works

    @works.setter
    def works(self, works):
        return self._works == works

    @property
    def clock(self):
        return self._clock

    @clock.setter
    def clock(self, clock):
        return self._clock == clock

    def update_clock(self):
        self._clock += 1
        sleep(1)
        print(f"\nSimulation clock: {self.clock}")

    def load_works(self):
        self._works = Works()
        self._works.add_works(
            [
                {'A1': 30, 'A2': 50},  # W1
                {'A1': 0, 'A2': 40},   # W2
                {'A1': 20, 'A2': 70},  # W3
                {'A1': 30, 'A2': 0},  # W4
                {'A1': 50, 'A2': 20},  # W5
            ],
            self._machines
        )

    def load_machines(self):
        self._machines = Machines()
        self._machines.add_machines(
            ['A1', 'A2']
        )

    def assign_works(self):
        for machine in self._machines:
            return self._machines.get_machine(machine)
                            

    def update_count_down(self):
        pass

    def show_machine_status(self):
        pass

    def run(self):
        self.load_machines()
        self.load_works()
        self.assign_works()