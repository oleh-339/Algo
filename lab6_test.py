import unittest
from lab6 import find_unreachable_cities


class TestGasSupply(unittest.TestCase):
    def test_all_cities_reachable(self):
        cities = ["Львів", "Стрий", "Долина"]
        storages = ["Сховище_1"]
        pipes = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
            ["Стрий", "Долина"],
        ]
        self.assertEqual(find_unreachable_cities(cities, storages, pipes), [])

    def test_unreachable_city(self):
        cities = ["Львів", "Стрий", "Долина"]
        storages = ["Сховище_1"]
        pipes = [
            ["Сховище_1", "Львів"],
            ["Львів", "Стрий"],
        ]
        expected = ["Сховище_1", ["Долина"]]
        self.assertEqual(find_unreachable_cities(cities, storages, pipes), expected)

    def test_transit_delivery(self):
        cities = ["Київ", "Одеса", "Харків"]
        storages = ["Сховище_А"]
        pipes = [
            ["Сховище_А", "Київ"],
            ["Київ", "Одеса"],
        ]
        expected = ["Сховище_А", ["Харків"]]
        self.assertEqual(find_unreachable_cities(cities, storages, pipes), expected)

    def test_multiple_storages_one_fails(self):
        cities = ["Місто_1"]
        storages = ["Сховище_1", "Сховище_2"]
        pipes = [
            ["Сховище_1", "Місто_1"],
        ]
        expected = ["Сховище_2", ["Місто_1"]]
        self.assertEqual(find_unreachable_cities(cities, storages, pipes), expected)


if __name__ == "__main__":
    unittest.main()