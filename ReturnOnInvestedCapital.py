def ROIC(FN, ticker):
    import statistics
    import os

    from pathlib import Path

    my_file = Path(FN)
    while my_file.exists() == False:
        my_file = Path(FN)

    with open(FN, 'r') as x:
        x = x.readlines()
        for idx,row in enumerate(x):
            if "Return on Invested Capital" in row:
                ROIC = x[idx]

        ROIC = ROIC.replace("\n","")
        print("Ticker: " + ticker.replace("\n",""))

        for idx, char in enumerate(ROIC):
            if char.isdigit():
                start = idx
                break

        ROIC = ROIC[start:].replace("\n","")
        ROIC = ROIC.split(",")

        if len(ROIC) >= 6:
            ROIC = [float(i) for i in ROIC]
            print("The TTM ROIC: {}".format(ROIC[-1]))
            print("The 5 Year average ROIC: {}".format(statistics.mean(ROIC[-6:-1])))


        #Get Book Value per share
        for idx,row in enumerate(x):
            if "Book Value Per Share" in row:
                BookValuePerShare = x[idx]
        BookValuePerShare = BookValuePerShare.replace("\n","")
        print("Book Value Per Share")
        for idx, char in enumerate(BookValuePerShare):
            if char.isdigit():
                start = idx
                break
        BookValuePerShare = BookValuePerShare[start:].replace("\n","")
        BookValuePerShare = BookValuePerShare.split(",")
        BookValuePerShare = BookValuePerShare[:-1]
        print(BookValuePerShare)


        #Get EPS
        for idx,row in enumerate(x):
            if "Earnings Per Share" in row:
                EPS = x[idx]
        EPS = EPS.replace("\n","")
        print("Earnings Per Share")
        for idx, char in enumerate(EPS):
            if char.isdigit():
                start = idx
                break
        EPS = EPS[start:].replace("\n","")
        EPS = EPS.split(",")
        EPS = EPS[:-1]
        print(EPS)

        #Get Net Income
        for idx,row in enumerate(x):
            if "Net Income USD" in row:
                NetIncome = x[idx]
        NetIncome = NetIncome.replace("\n","")
        print("Net Income USD")
        for idx, char in enumerate(NetIncome):
            if char.isdigit():
                start = idx
                break
        if NetIncome[start-1] == "\"":
            NetIncomeMod = "[\""
        else:
            NetIncomeMod = "["
        NetIncomeMod += NetIncome[start:].replace("\n","")

        stopLast = []
        for idx, char in enumerate(NetIncomeMod):
            if char == ",":
                stopLast.append(idx)

        checkQuote = NetIncomeMod[stopLast[-1]:]
        if "\"" in checkQuote:
            NetIncomeMod = NetIncomeMod[:stopLast[-2]]
        else:
            NetIncomeMod = NetIncomeMod[:stopLast[-1]]

        if NetIncomeMod.count("\"") % 2 == 1:
            NetIncomeMod += "\"]"
        else:
            NetIncomeMod += "]"

        print(NetIncomeMod)
        print('\n')

    return

