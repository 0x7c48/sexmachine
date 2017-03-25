# -*- coding: utf-8 -*-
import unittest
import sexmachine.mapping as m


class TestMapping(unittest.TestCase):

    def test_map_name(self):
        self.assertEqual(m.map_name("Ay<s,>e"), "Ayşe")
        self.assertEqual(m.map_name("<ß>ahri"), "ẞahri")
        self.assertEqual(m.map_name("<Ö>mer"), "Őmer")
        self.assertEqual(m.map_name("<SCH>vet"), "Švet")

if __name__ == '__main__':
    unittest.main()
