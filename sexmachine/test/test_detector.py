# -*- coding: utf-8 -*-
import unittest
import sexmachine.detector as d


class TestDetector(unittest.TestCase):

    def setUp(self):
        self.case = d.Detector()
        self.incase = d.Detector(case_sensitive=False)

    def test_gender(self):
        self.assertEqual(self.case.get_gender("Bob"), "male")
        self.assertEqual(self.case.get_gender("Sally"), "female")
        self.assertEqual(self.case.get_gender("Pauley"), "andy")

    def test_unicode(self):
        self.assertEqual(self.case.get_gender("Álfrún"), "female")
        self.assertEqual(self.case.get_gender("Ayşe"), "female")
        self.assertEqual(self.case.get_gender("Gavriliţă"), "female")
        self.assertEqual(self.case.get_gender("İsmet"), "male")
        self.assertEqual(self.case.get_gender("Snæbjörn"), "male")

    def test_country(self):
        self.assertEqual(self.case.get_gender("Jamie"), "mostly_female")
        self.assertEqual(self.case.get_gender("Jamie", "great_britain"),
                         "mostly_male")

    def test_case(self):
        self.assertEqual(self.incase.get_gender("sally"), "female")
        self.assertEqual(self.incase.get_gender("Sally"), "female")
        self.assertEqual(self.incase.get_gender("aydın"), "male")
        self.assertEqual(self.incase.get_gender("Aydın"), "male")

if __name__ == '__main__':
    unittest.main()
