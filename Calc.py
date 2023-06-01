class Сalculator():
    def __init__(self):
        self.larchesHeight = None
        self.larchesArea = None
        self.larchesSum = None
        self.larchesGirth = None
        self.larchesCount = None
        self.pineSum = None
        self.pineArea = None
        self.pineHeight = None
        self.pineGirth = None
        self.pineCount = None
        self.sum = 0
        self.k = 3.14
        self.pineStake = 150.84
        self.larchesStake = 120.78

    def addPine(self, count, height, girth):
        self.pineCount = count
        self.pineHeight = height
        self.pineGirth = girth
        self.pineArea = girth / 3.14 * count * height
        self.pineSum = self.pineStake * self.pineArea

    def addLarches(self, count, height, girth):
        self.larchesCount = count
        self.larchesHeight = height
        self.larchesGirth = girth
        self.larchesArea = girth / 3.14 * count * height
        self.larchesSum = self.larchesArea * self.larchesStake

    def addSpruce(self,count, height, girth):
        self.spruceCount = count
        self.spuceHeight = height
