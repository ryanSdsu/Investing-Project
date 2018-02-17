import statistics

with open("/Users/RJ/PycharmProjects/Investing-Project/FB Key Ratios.csv.html", 'r') as x:
    x = x.readlines()
    for idx,row in enumerate(x):
        if "Return on Invested Capital" in row:
            ROIC = x[idx]

    print(ROIC)

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

