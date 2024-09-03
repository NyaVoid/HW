import unittest


class Runner:

    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
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
        while len(finishers) < len(self.participants):
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance and participant not in finishers.values():
                    finishers[len(finishers) + 1] = participant
            if len(finishers) == len(self.participants):
                break
        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.results = []

    @classmethod
    def setUp(cls):
        cls.runner_1 = Runner('Усэйн', 10)
        cls.runner_2 = Runner('Андрей', 9)
        cls.runner_3 = Runner('Ник', 3)

    def test_cup1(self):
        cup = Tournament(90, self.runner_1, self.runner_3)
        results = cup.start()
        formatted_results = {place: str(participant) for place, participant in results.items()}
        TournamentTest.results.append(formatted_results)

    def test_cup2(self):
        cup = Tournament(90, self.runner_2, self.runner_3)
        results = cup.start()
        formatted_results = {place: str(participant) for place, participant in results.items()}
        TournamentTest.results.append(formatted_results)

    def test_cup3(self):
        cup = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        results = cup.start()
        formatted_results = {place: str(participant) for place, participant in results.items()}
        TournamentTest.results.append(formatted_results)

    @classmethod
    def tearDownClass(cls):
        for result in cls.results:
            print(result)


if __name__ == '__main__':
    unittest.main()
