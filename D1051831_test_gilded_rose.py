# -*- coding: utf-8 -*-
import unittest

from D1051831_gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
                Item(name="Aged Brie", sell_in=2, quality=0),
                Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
                Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
                Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
                Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
                ]
        
        days = 2
        import sys
        if len(sys.argv) > 1:
            days = int(sys.argv[1]) + 1

        for day in range(days):
            print("-------- day %s --------" % day)
            print("name, sellIn, quality")
            for item in items:
                print(item)
            print("")
            GildedRose(items).update_quality()

        self.assertEqual("+5 Dexterity Vest", items[0].name)
        self.assertEqual(18, items[0].quality)
        self.assertEqual(8, items[0].sell_in)

        self.assertEqual("Aged Brie", items[1].name)
        self.assertEqual(2, items[1].quality)
        self.assertEqual(0, items[1].sell_in)

        self.assertEqual("Elixir of the Mongoose", items[2].name)
        self.assertEqual(5, items[2].quality)
        self.assertEqual(3, items[2].sell_in)

        self.assertEqual("Sulfuras, Hand of Ragnaros", items[3].name)
        self.assertEqual(80, items[3].quality)
        self.assertEqual(0, items[3].sell_in)

        self.assertEqual("Sulfuras, Hand of Ragnaros", items[4].name)
        self.assertEqual(80, items[4].quality)
        self.assertEqual(-1, items[4].sell_in)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[5].name)
        self.assertEqual(22, items[5].quality)
        self.assertEqual(13, items[5].sell_in)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[6].name)
        self.assertEqual(50, items[6].quality)
        self.assertEqual(8, items[6].sell_in)

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[7].name)
        self.assertEqual(50, items[7].quality)
        self.assertEqual(3, items[7].sell_in)

        self.assertEqual("Conjured Mana Cake", items[8].name)
        self.assertEqual(2, items[8].quality)
        self.assertEqual(1, items[8].sell_in)

if __name__ == '__main__':
    unittest.main()
