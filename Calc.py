class Сalculator:
    def __init__(self):
        self.recoverySoil = None
        self.recovery = None
        self.recoveryLichen = None
        self.sumTree1 = None
        self.sumTree125 = None
        self.sumTree = 0
        self.treeSum = None
        self.treeArea = None
        self.soilArea = None
        self.soilSum = None
        self.lichenSum = None
        self.lichenArea = None
        self.otherTreesSum125 = None
        self.otherTreesCount125 = None
        self.otherTreesSum25 = None
        self.otherTreesCount25 = None
        self.otherTreesSum = None
        self.otherTreesCount = None
        self.aspenSum = None
        self.aspenArea = None
        self.aspenGirth = None
        self.aspenHeight = None
        self.aspenCount = None
        self.alderSum = None
        self.alderArea = None
        self.alderGirth = None
        self.alderCount = None
        self.alderHeight = None
        self.birchGirth = None
        self.birchSum = None
        self.birchArea = None
        self.birchHeight = None
        self.birchCount = None
        self.beechArea = None
        self.beechSum = None
        self.beechGirth = None
        self.beechHeight = None
        self.beechCount = None
        self.oakArea = None
        self.oakSum = None
        self.oakGirth = None
        self.oakHeight = None
        self.oakCount = None
        self.spruceArea = None
        self.spruceSum = None
        self.spruceHeight = None
        self.spruceGirth = None
        self.spruceCount = None
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
        self.pineStake = 150.84
        self.larchesStake = 120.78
        self.spruceStake = 136.44
        self.oakStake = 566.82
        self.beechStake = 1100
        self.birchStake = 75.78
        self.alderStake = 45
        self.aspenStake = 14.4
        self.otherTrees25Stake = 10782
        self.otherTrees125Stake = 3212
        self.otherTreesStake = 808
        self.lichenStake = 22500
        self.treeStake = 75000
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

    def addSpruce(self, count, height, girth):
        self.spruceCount = count
        self.spruceHeight = height
        self.spruceGirth = girth
        self.spruceArea = girth / 3.14 * count * height
        self.spruceSum = self.spruceArea * self.spruceStake

    def addOak(self, count, height, girth):
        self.oakCount = count
        self.oakHeight = height
        self.oakGirth = girth
        self.oakArea = girth / 3.14 * count * height
        self.oakSum = self.oakArea * self.oakStake

    def addBeeches(self, count, height, girth):
        self.beechCount = count
        self.beechHeight = height
        self.beechGirth = girth
        self.beechArea = girth / 3.14 * count * height
        self.beechSum = self.beechArea * self.beechStake

    def addBirch(self, count, height, girth):
        self.birchCount = count
        self.birchHeight = height
        self.birchGirth = girth
        self.birchArea = girth / 3.14 * count * height
        self.birchSum = self.birchArea * self.birchStake

    def addAlder(self, count, height, girth):
        self.alderCount = count
        self.alderHeight = height
        self.alderGirth = girth
        self.alderArea = girth / 3.14 * count * height
        self.alderSum = self.alderArea * self.alderStake

    def addAspen(self, count, height, girth):
        self.aspenCount = count
        self.aspenHeight = height
        self.aspenGirth = girth
        self.aspenArea = girth / 3.14 * count * height
        self.aspenSum = self.aspenArea * self.aspenStake

    def addOtherTrees25(self, count):
        self.otherTreesCount25 = count
        self.otherTreesSum25 = self.aspenArea * self.otherTrees25Stake

    def addOtherTrees125(self, count):
        self.otherTreesCount125 = count
        self.otherTreesSum125 = self.aspenArea * self.otherTrees125Stake

    def addOtherTrees(self, count):
        self.otherTreesCount = count
        self.otherTreesSum = self.aspenArea * self.otherTreesStake

    def addLichen(self, area):
        self.lichenArea = area
        self.lichenSum = self.lichenArea * self.lichenStake

    def addTree(self, area):
        self.treeArea = area
        self.treeSum = self.treeArea * self.treeStake/10000

    def addSoil(self, area):
        self.soilArea = area
        self.soilSum = self.soilArea * self.soilStake

    def calculate(self):
        self.sum = self.pineSum + self.lichenSum+self.spruceSum+self.oakSum+self.beechSum+self.birchSum+self.alderSum+self.aspenSum+self.otherTrees25Stake+self.otherTreesSum125+self.otherTreesSum+self.lichenSum+self.treeSum+self.soilSum
        self.sumTree = self.treeSum + self.pineSum + self.lichenSum+self.spruceSum+self.oakSum+self.beechSum+self.birchSum+self.alderSum+self.aspenSum+self.otherTrees25Stake+self.otherTreesSum125+self.otherTreesSum
        self.sumTree125 = self.otherTreesSum125
        self.sumTree1 = self.otherTreesSum
        self.recovery = self.treeSum * self.treeArea
        self.recoveryLichen = self.lichenSum
        self.recoverySoil = self.soilSum

