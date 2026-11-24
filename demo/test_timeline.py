import unittest
from timeline import Scene, timeline

class TimelineTests(unittest.TestCase):
    def test_contiguous(self):
        self.assertEqual(timeline([Scene("A", 8), Scene("B", 8)]), [{"scene":"A","start":0,"end":8},{"scene":"B","start":8,"end":16}])
    def test_invalid_duration(self):
        for value in [0, -1, 121, True, 2.5]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                timeline([Scene("A", value)])
    def test_empty_name(self):
        with self.assertRaises(ValueError):
            timeline([Scene(" ", 8)])
    def test_empty_timeline(self):
        self.assertEqual(timeline([]), [])

if __name__ == "__main__":
    unittest.main()
