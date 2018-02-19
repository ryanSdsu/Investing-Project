def ROIC(FN, ticker):
    import statistics
    from pathlib import Path

    start = 0
    roicList = []
    my_file = Path(FN)
    while my_file.exists() == False:
        my_file = Path(FN)

    with open(FN, 'r') as x:
        x = x.read()
        #Return empty list if there is no ROIC
        if "Return on Invested Capital" not in x:
            return roicList
        x = x.split("\n")
        for idx,row in enumerate(x):
            if "Return on Invested Capital" in row:
                ROIC = x[idx]

        ROIC = ROIC.replace("\n","")

        for idx, char in enumerate(ROIC):
            if char.isdigit():
                start = idx
                break

        ROIC = ROIC[start:].replace("\n","")
        ROIC = ROIC.split(",")
        for idx,i in enumerate(ROIC):
            if i == "":
                ROIC[idx] = float(0)

        if ROIC[0] == "Return on Invested Capital %":
            ROIC[0] = float(0)

        print(ROIC)


        if len(ROIC) >= 6:
            ROIC = [float(i) for i in ROIC]
            print("Ticker: " + ticker.replace("\n","") + ", {} {}".format(ROIC[-1], statistics.mean(ROIC[-6:-1])))
            roicList.append(ROIC[-1])
            roicList.append(statistics.mean(ROIC[-6:-1]))

    return roicList