def YearOverYearGrowthCheck(ticker):
    print("Total Revneue, Net Income, EPS: " + ticker)

    url = "https://www.msn.com/en-us/money/stockdetails/financials/fi-126.1."
    urlCSLAnys = url + ticker[:ticker.find(".")]
    url += ticker
    url = url.replace("\n", "")
    urlNAS = url + ".NAS"
    urlNYS = url + ".NYS"
    urlCSLAnys += "%7CSLA%7CA.NYS."
    urlCSLAnys += ticker

    htmlAsList = attemptToOpenUrl(urlNAS)
    indexList = attemptToGetIndexList(htmlAsList)

    if len(indexList) == 0:
        htmlAsList = attemptToOpenUrl(urlNYS)
        indexList = attemptToGetIndexList(htmlAsList)

    if len(indexList) == 0:
        print("checking url: " + urlCSLAnys)
        htmlAsList = attemptToOpenUrl(urlCSLAnys)
        indexList = attemptToGetIndexList(htmlAsList)

    print(indexList)

    totalRevenue = htmlAsList[indexList[0]:indexList[1]]
    netIncome = htmlAsList[indexList[2]:indexList[3]]
    basicEps = htmlAsList[indexList[4]:indexList[5]]

    totalRevenueList = findYearOverYearValues(totalRevenue)
    netIncomeList = findYearOverYearValues(netIncome)
    basicEpsList = findYearOverYearValues(basicEps)

    print(totalRevenueList)
    print(netIncomeList)
    print(basicEpsList)

    if totalRevenueList[0] > totalRevenueList[1]:
        if netIncomeList[0] > netIncomeList[1]:
            if basicEpsList[0] > basicEpsList[1]:
                with open("1YearOverYearGrowth.txt", 'a') as oneYear:
                    oneYear.write(ticker)
                    oneYear.write('\n')
            if totalRevenueList[1] > totalRevenueList[2]:
                    if netIncomeList[1] > netIncomeList[2]:
                        if basicEpsList[1] > basicEpsList[2]:
                            with open("2YearOverYearGrowth.txt", 'a') as twoYear:
                                twoYear.write(ticker)
                                twoYear.write('\n')
                        if totalRevenueList[2] > totalRevenueList[3]:
                                if netIncomeList[2] > netIncomeList[3]:
                                    if basicEpsList[2] > basicEpsList[3]:
                                        with open("3YearOverYearGrowth.txt", 'a') as threeYear:
                                            threeYear.write(ticker)
                                            threeYear.write('\n')

    return

def findYearOverYearValues(webLinkList):
    YearOverYearList = []


    current = webLinkList[20].split("\'")
    current = current[3]
    current = current.replace(",","")
    current = current.replace("-","0")
    YearOverYearList.append(float(current))

    oneYearAgo = webLinkList[15].split("\'")
    oneYearAgo = oneYearAgo[3]
    oneYearAgo = oneYearAgo.replace(",","")
    oneYearAgo = oneYearAgo.replace("-","0")
    YearOverYearList.append(float(oneYearAgo))

    twoYearsAgo = webLinkList[10].split("\'")
    twoYearsAgo = twoYearsAgo[3]
    twoYearsAgo = twoYearsAgo.replace(",","")
    twoYearsAgo = twoYearsAgo.replace("-","0")
    YearOverYearList.append(float(twoYearsAgo))

    threeYearsAgo = webLinkList[5].split("\'")
    threeYearsAgo = threeYearsAgo[3]
    threeYearsAgo = threeYearsAgo.replace(",","")
    threeYearsAgo = threeYearsAgo.replace("-","0")
    YearOverYearList.append(float(threeYearsAgo))

    return YearOverYearList

def attemptToOpenUrl(url):
    import requests

    r = requests.get(url)
    html = r.text.split('\n')

    return html

def attemptToGetIndexList(htmlAsList):
    indexList = []
    checkEps = False
    checkWAS = False

    for idx,line in enumerate(htmlAsList):
        if ">Total Revenue<" in line:
            indexList.append(idx)
        if ">Cost of Revenue<" in line:
            indexList.append(idx)
        if ">Net Income<" in line:
            indexList.append(idx)
        if ">Dividend Per Share<" in line:
            indexList.append(idx)
        if ">Basic EPS<" in line and checkEps == False:
            indexList.append(idx)
            checkEps = True
        if ">Basic Weighted Average Shares<" in line and checkWAS == False:
            indexList.append(idx)
            checkWAS = True

    return indexList