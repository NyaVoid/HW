import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_wal(self):
        runner = Runner('1')
        for i in range(10):
            runner.walk()
        self.assertEqual(50, runner.distance)

    def test_run(self):
        runner = Runner('2')
        for i in range(10):
            runner.run()
        self.assertEqual(100, runner.distance)

    def test_challenge(self):
        runner = Runner('3')
        runner_2 = Runner('4')
        for i in range(10):
            runner.walk()
            runner_2.run()
        self.assertNotEqual(runner.distance, runner_2.distance)
        
if __name__ == '__main__':
    unittest.main()
