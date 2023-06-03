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
        self.pineStake = 150.84 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ сосен
        self.larchesStake = 120.78 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ лиственниц
        self.spruceStake = 136.44#СТАВКА ЗА 1 ПЛОТНЫЙ М³ елей и пихт
        self.oakStake = 566.82 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ дубов, ясеней и клёнов
        self.beechStake = 1100 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ буков
        self.birchStake = 75.78 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ берёз
        self.alderStake = 45 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ ольхи черной, грабов, вязов и лип
        self.aspenStake = 14.4 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ ольхи белой и тополей выше
        self.otherTrees25Stake = 10782 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ остальных деревьев (включая краснокнижные виды) выше 2,5
        self.otherTrees125Stake = 3212 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ остальных деревьев (включая краснокнижные виды) выше от 1 до 1.25
        self.otherTreesStake = 808 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ остальных деревьев (включая краснокнижные виды) до 1
        self.lichenStake = 22500 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ мест произрастания лишайниковых форм растений
        self.treeStake = 75000 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ мест произрастания древесных форм растений
        self.soilStake  =4700 #СТАВКА ЗА 1 ПЛОТНЫЙ М³ нарушеной земели

    # рассчет сумм сосен
    def addPine(self, count, height, girth):
        self.pineCount = count
        self.pineHeight = height
        self.pineGirth = girth
        self.pineArea = girth / 3.14 * count * height #расчет обьема
        self.pineSum = self.pineStake * self.pineArea #расчет ценны

    # рассчет сумм лиственниц
    def addLarches(self, count, height, girth):
        self.larchesCount = count
        self.larchesHeight = height
        self.larchesGirth = girth
        self.larchesArea = girth / 3.14 * count * height #расчет обьема
        self.larchesSum = self.larchesArea * self.larchesStake  #расчет ценны

    # рассчет сумм елей и пихт
    def addSpruce(self, count, height, girth):
        self.spruceCount = count
        self.spruceHeight = height
        self.spruceGirth = girth
        self.spruceArea = girth / 3.14 * count * height #расчет обьема
        self.spruceSum = self.spruceArea * self.spruceStake  #расчет ценны

    # рассчет сумм дубов, ясеней и клёнов
    def addOak(self, count, height, girth):
        self.oakCount = count
        self.oakHeight = height
        self.oakGirth = girth
        self.oakArea = girth / 3.14 * count * height #расчет обьема
        self.oakSum = self.oakArea * self.oakStake  #расчет ценны

    # рассчет сумм буков
    def addBeeches(self, count, height, girth):
        self.beechCount = count
        self.beechHeight = height
        self.beechGirth = girth
        self.beechArea = girth / 3.14 * count * height #расчет обьема
        self.beechSum = self.beechArea * self.beechStake  #расчет ценны

    # рассчет сумм берёз
    def addBirch(self, count, height, girth):
        self.birchCount = count
        self.birchHeight = height
        self.birchGirth = girth
        self.birchArea = girth / 3.14 * count * height #расчет обьема
        self.birchSum = self.birchArea * self.birchStake  #расчет ценны

    # рассчет сумм ольхи черной, грабов, вязов и лип
    def addAlder(self, count, height, girth):
        self.alderCount = count
        self.alderHeight = height
        self.alderGirth = girth
        self.alderArea = girth / 3.14 * count * height #расчет обьема
        self.alderSum = self.alderArea * self.alderStake  #расчет ценны

    # рассчет сумм ольхи белой и тополей выше
    def addAspen(self, count, height, girth):
        self.aspenCount = count
        self.aspenHeight = height
        self.aspenGirth = girth
        self.aspenArea = girth / 3.14 * count * height #расчет обьема
        self.aspenSum = self.aspenArea * self.aspenStake  #расчет ценны

    # рассчет сумм остальных деревьев (включая краснокнижные виды) выше 2,5
    def addOtherTrees25(self, count):
        self.otherTreesCount25 = count
        self.otherTreesSum25 = self.aspenArea * self.otherTrees25Stake   #расчет ценны

    # рассчет сумм остальных деревьев (включая краснокнижные виды) выше от 1 до 1.25
    def addOtherTrees125(self, count):
        self.otherTreesCount125 = count
        self.otherTreesSum125 = self.aspenArea * self.otherTrees125Stake  #расчет ценны

    # рассчет сумм #СТАВКА ЗА 1 ПЛОТНЫЙ М³ остальных деревьев (включая краснокнижные виды) до 1
    def addOtherTrees(self, count):
        self.otherTreesCount = count
        self.otherTreesSum = self.aspenArea * self.otherTreesStake  #расчет ценны

    # рассчет сумм мест произрастания лишайниковых форм растений
    def addLichen(self, area):
        self.lichenArea = area
        self.lichenSum = self.lichenArea * self.lichenStake  #расчет ценны

    # рассчет мест произрастания древесных форм растений
    def addTree(self, area):
        self.treeArea = area
        self.treeSum = self.treeArea * self.treeStake/10000  #расчет ценны

    # рассчет сумм нарушеной земели
    def addSoil(self, area):
        self.soilArea = area
        self.soilSum = self.soilArea * self.soilStake  #расчет ценны

    def calculate(self):#рассчет всех сумм для вывода
        self.sum = self.pineSum + self.lichenSum+self.spruceSum+self.oakSum+self.beechSum+self.birchSum+self.alderSum+self.aspenSum+self.otherTrees25Stake+self.otherTreesSum125+self.otherTreesSum+self.lichenSum+self.treeSum+self.soilSum
        self.sumTree = self.treeSum + self.pineSum + self.lichenSum+self.spruceSum+self.oakSum+self.beechSum+self.birchSum+self.alderSum+self.aspenSum+self.otherTrees25Stake+self.otherTreesSum125+self.otherTreesSum
        self.sumTree125 = self.otherTreesSum125
        self.sumTree1 = self.otherTreesSum
        self.recovery = self.treeSum * self.treeArea
        self.recoveryLichen = self.lichenSum
        self.recoverySoil = self.soilSum

    def get_project(self):
        return [self.sum, self.sumTree, self.sumTree125, self.sumTree1, self.recovery, self.recoveryLichen, self.recoverySoil]

