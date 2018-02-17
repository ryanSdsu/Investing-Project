def getPeRatio(ticker):
    print("Current PE/ 5 Year High PE/ 5 Year Low PE")
    import requests

    url = "https://www.msn.com/en-us/money/stockdetails/analysis/fi-126.1."
    url += ticker
    url = url.replace("\n", "")
    url += ".NAS"
    r = requests.get(url)

    html = r.text.split('\n')

    peList = []
    for idx,line in enumerate(html):
        if "Current P/E Ratio" in line:
            startPE = idx
        if "P/E Ratio 5-Year High" in line:
            middleFirst = idx
        if "P/E Ratio 5-Year Low" in line:
            middleSecond = idx
        if "Price/Sales Ratio" in line:
            stopPE = idx

    currentPE = html[startPE:middleFirst]
    currentPE = currentPE[4].split("\'")

    #Current PE ratio
    peList.append(float(currentPE[3]))

    fiveYearHighPE = html[middleFirst:middleSecond]
    fiveYearHighPE = fiveYearHighPE[4].split("\'")

    #Five Year High PE ratio
    peList.append(float(fiveYearHighPE[3]))

    fiveYearLowPE = html[middleSecond:stopPE]
    fiveYearLowPE = fiveYearLowPE[4].split("\'")

    #Five Year Low PE ratio
    peList.append(float(fiveYearLowPE[3]))

    print(peList)

    return peList

