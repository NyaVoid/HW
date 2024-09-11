import logging
import unittest
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='runner_test.log', encoding='UTF-8', filemode='w')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class runner_test(unittest.TestCase):
    def test_walk(self):
        try:
            first = Runner('Nya', -12)
            logger.info(msg='test_walk выполнен успешно')
        except ValueError:
            logger.warning(msg='Неверная скорость для Runner')
    
    def test_run(self):
        try:
            second = Runner(123, 123)
            logger.info(msg='test_run выполнен успешно')
        except TypeError:
            logger.warning(msg='Неверное имя для Runner')

            
if __name__ == '__main__':
    unittest.main()