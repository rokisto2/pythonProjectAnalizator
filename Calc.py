class Сalculator:
    def __init__(self):
        self.sum = 0
        self.sosnaStake = 150.84  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ сосен
        self.larchesStake = 120.78  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ лиственниц
        self.pixtStake = 136.44  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ елей и пихт
        self.dubStake = 566.82  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ дубов, ясеней и клёнов
        self.bukStake = 1100  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ буков
        self.berezStake = 75.78  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ берёз
        self.lipStake = 45  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ ольхи черной, грабов, вязов и лип
        self.topolStake = 14.4  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ ольхи белой и тополей выше
        self.otherTrees25Stake = 10782  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ остальных деревьев (включая краснокнижные виды) выше 2,5
        self.otherTrees125Stake = 3212  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ остальных деревьев (включая краснокнижные виды) выше от 1 до 1.25
        self.otherTreesStake = 808  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ остальных деревьев (включая краснокнижные виды) до 1
        self.lichenStake = 22500  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ мест произрастания лишайниковых форм растений
        self.treeStake = 75000  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ мест произрастания древесных форм растений
        self.soilStake = 4700  # СТАВКА ЗА 1 ПЛОТНЫЙ М³ нарушеной земели

    # рассчет сумм сосен
    def addSosna(self, count, height, girth):
        self.sosnaCount = count
        self.sosnaHeight = height
        self.sosnaGirth = girth
        self.sosnaArea = girth / 3.14 * count * height  # расчет обьема
        self.sosnaSum = self.sosnaStake * self.sosnaArea  # расчет ценны

    # рассчет сумм лиственниц
    def addLarches(self, count, height, girth):
        self.larchesCount = count
        self.larchesHeight = height
        self.larchesGirth = girth
        self.larchesArea = girth / 3.14 * count * height  # расчет обьема
        self.larchesSum = self.larchesArea * self.larchesStake  # расчет ценны

    # рассчет сумм елей и пихт
    def addPixt(self, count, height, girth):
        self.pixtCount = count
        self.pixtHeight = height
        self.pixtGirth = girth
        self.pixtArea = girth / 3.14 * count * height  # расчет обьема
        self.pixtSum = self.pixtArea * self.pixtStake  # расчет ценны

    # рассчет сумм дубов, ясеней и клёнов
    def addDub(self, count, height, girth):
        self.dubCount = count
        self.dubHeight = height
        self.dubGirth = girth
        self.dubArea = girth / 3.14 * count * height  # расчет обьема
        self.dubSum = self.dubArea * self.dubStake  # расчет ценны

    # рассчет сумм буков
    def addBuk(self, count, height, girth):
        self.bukCount = count
        self.bukHeight = height
        self.bukGirth = girth
        self.bukArea = girth / 3.14 * count * height  # расчет обьема
        self.bukSum = self.bukArea * self.bukStake  # расчет ценны

    # рассчет сумм берёз
    def addBerez(self, count, height, girth):
        self.berezCount = count
        self.berezHeight = height
        self.berezGirth = girth
        self.berezArea = girth / 3.14 * count * height  # расчет обьема
        self.berezSum = self.berezArea * self.berezStake  # расчет ценны

    # рассчет сумм ольхи черной, грабов, вязов и лип
    def addLip(self, count, height, girth):
        self.lipCount = count
        self.lipHeight = height
        self.lipGirth = girth
        self.lipArea = girth / 3.14 * count * height  # расчет обьема
        self.lipSum = self.lipArea * self.lipStake  # расчет ценны

    # рассчет сумм ольхи белой и тополей
    def addTopol(self, count, height, girth):
        self.topolCount = count
        self.topolHeight = height
        self.topolGirth = girth
        self.topolArea = girth / 3.14 * count * height  # расчет обьема
        self.topolSum = self.topolArea * self.topolStake  # расчет ценны

    # рассчет сумм остальных деревьев (включая краснокнижные виды) выше 2,5
    def addOtherTrees25(self, count):
        self.otherTreesCount25 = count
        self.otherTreesSum25 = count * self.otherTrees25Stake  # расчет ценны

    # рассчет сумм остальных деревьев (включая краснокнижные виды) выше от 1 до 1.25
    def addOtherTrees125(self, count):
        self.otherTreesCount125 = count
        self.otherTreesSum125 = count * self.otherTrees125Stake  # расчет ценны

    # рассчет сумм #СТАВКА ЗА 1 ПЛОТНЫЙ М³ остальных деревьев (включая краснокнижные виды) до 1
    def addOtherTrees(self, count):
        self.otherTreesCount = count
        self.otherTreesSum = count * self.otherTreesStake  # расчет ценны

    # рассчет сумм мест произрастания лишайниковых форм растений
    def addLichen(self, area):
        self.lichenArea = area
        self.lichenSum = self.lichenArea * self.lichenStake  # расчет ценны

    # рассчет мест произрастания древесных форм растений
    def addTree(self, area):
        self.treeArea = area
        self.treeSum = self.treeArea * self.treeStake / 10000  # расчет ценны

    # рассчет сумм нарушеной земели
    def addSoil(self, area):
        self.soilArea = area
        self.soilSum = self.soilArea * self.soilStake  # расчет ценны

    def calculate(self):  # рассчет всех сумм для вывода
        self.sum = self.sosnaSum + self.lichenSum + self.spruceSum + self.dubSum + self.bukSum + self.berezSum + self.lipSum + self.topolSum + self.otherTrees25Stake + self.otherTreesSum125 + self.otherTreesSum + self.lichenSum + self.treeSum + self.soilSum
        self.sumTree = self.treeSum + self.sosnaSum + self.lichenSum + self.spruceSum + self.dubSum + self.bukSum + self.berezSum + self.lipSum + self.topolSum + self.otherTrees25Stake + self.otherTreesSum125 + self.otherTreesSum
        self.sumTree125 = self.otherTreesSum125
        self.sumTree1 = self.otherTreesSum
        self.recovery = self.treeSum * self.treeArea
        self.recoveryLichen = self.lichenSum
        self.recoverySoil = self.soilSum

    def get_project(self):
        return [self.sum, self.sumTree, self.sumTree125, self.sumTree1, self.recovery, self.recoveryLichen,
                self.recoverySoil]
