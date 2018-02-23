from YearAfterYearGrowthSorter.YearOverYearGrowthCheck import *

with open("/Users/RJ/PycharmProjects/Investing-Project/YearAfterYearGrowthSorter/ROIC>=10%List", 'r') as ROIClist:
    ROIClist = ROIClist.read().split('\n')
    for idx,ticker in enumerate(ROIClist):
        YearOverYearGrowthCheck(ticker)
        print("{} of {} to go!".format(idx, len(ROIClist)))
        print("Sorting Complete!")