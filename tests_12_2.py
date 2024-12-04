from runner_and_tournament import Runner, Tournament
import unittest


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усейн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            #print(i)
            final_result = {}
            for key, value in i.items():
                final_result[key] = value.name  #Runner
            print(final_result)

    def test_run_1(self):
        self.tournament = Tournament(90, self.runner1, self.runner3)
        self.all_results = self.tournament.start()
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")
        TournamentTest.all_results[1] = self.all_results

    def test_run_2(self):
        self.tournament_2 = Tournament(90, self.runner2, self.runner3)
        self.all_results = self.tournament_2.start()
        self.assertTrue(self.all_results[max(self.all_results)] == "Ник")
        TournamentTest.all_results[2] = self.all_results

    def test_run_3(self):
        self.tournament_3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results = self.tournament_3.start()
        self.assertTrue(self.all_results[max(self.all_results)] == 'Ник')
        TournamentTest.all_results[3] = self.all_results
        #print(TournamentTest.all_results.keys())


if __name__ == '__main__':
    unittest.main()
