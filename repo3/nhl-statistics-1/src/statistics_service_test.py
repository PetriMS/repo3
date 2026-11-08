import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
        
    def test_search_finds_player(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        
    def test_pelaajaa_ei_loydy(self):
        player = self.stats.search("Uotila")

        self.assertIsNone(player)
    
    def test_team_loytaa(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)
        
    def test_maalitykki(self):
        maalitykki = self.stats.top(0)

        self.assertEqual(maalitykki[0].name, "Gretzky")
        