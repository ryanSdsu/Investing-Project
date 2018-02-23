from YearAfterYearGrowthSorter.YearOverYearGrowthCheck import *

with open("/Users/RJ/PycharmProjects/Investing-Project/YearAfterYearGrowthSorter/ROIC>=10%List", 'r') as ROIClist:
    for ticker in ROIClist:
        YearOverYearGrowthCheck(ticker)
