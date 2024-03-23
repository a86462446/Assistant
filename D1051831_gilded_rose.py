# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            double= 0
            if item.sell_in== 0:
                double= 2
            else:
                double= 1

            if item.quality<= 50:
                if item.name== "Aged Brie" or item.name== "Sulfuras, Hand of Ragnaros" or item.name== "Backstage passes to a TAFKAL80ETC concert":
                    item.quality+= 1
                    if item.name== "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in<= 5:
                            item.quality+= 2
                        elif item.sell_in<= 10:
                            item.quality+= 1
                        elif item.sell_in== 0:
                            item.quality= 0

                        if item.quality> 50:
                            item.quality= 50
                else:
                    if item.name== "Conjured Mana Cake":
                        item.quality-= (2* double)
                    else:
                        item.quality-= (1* double)

            if item.name!= "Sulfuras, Hand of Ragnaros":
                item.sell_in-= 1
            


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
