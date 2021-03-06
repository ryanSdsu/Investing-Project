import webbrowser
import os

from pathlib import Path
from ReturnOnInvestedCapital import ROIC
from PEratio import getPeRatio

with open("/Users/RJ/PycharmProjects/Investing-Project/List of company ticker",'r') as tickerFile:
    tickerFile = tickerFile.readlines()
    for ticker in tickerFile:

        webLink = "http://financials.morningstar.com/ajax/exportKR2CSV.html?t="
        webLink += ticker
        webbrowser.open(webLink)

        analysisLink = "/Users/RJ/Downloads/"
        analysisLink += ticker
        analysisLink += " Key Ratios.csv.html"
        analysisLink = analysisLink.replace("\n","")

        ttmEPS = ROIC(analysisLink, ticker)

        #/Users/RJ/Downloads/AAPL Key Ratios.csv.html
        my_file = Path(analysisLink)
        while my_file.exists() == False:
            my_file = Path(analysisLink)
        while my_file.exists():
            os.remove(analysisLink)

        getPeRatio(ticker)
        print("TTM EPS: {}".format(ttmEPS))
        print('\n')


print("Stock analysis complete!")