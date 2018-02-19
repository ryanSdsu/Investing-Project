companyList = "/Users/RJ/PycharmProjects/Investing-Project/FindCompaniesROIC/CompanyList.txt"
import os
import webbrowser
import time
from pathlib import Path

from FindCompaniesROIC.ROICsorter import ROIC

with open(companyList,'r') as tickerFile:
    tickerFile = tickerFile.readlines()
    for idx,ticker in enumerate(tickerFile):
        ajaxFail = "false"
        webLink = "http://financials.morningstar.com/ajax/exportKR2CSV.html?t="
        webLink += ticker

        webbrowser.open(webLink)

        analysisLink = "/Users/RJ/Downloads/"
        analysisLink += ticker
        analysisLink += " Key Ratios.csv.html"
        analysisLink = analysisLink.replace("\n","")

        #Check if ajax was successful sent for 5 seconds
        timeout = time.time() + 5
        my_file = Path(analysisLink)
        while my_file.exists() == False:
            print("Currently on {}, {} of {} to go!".format(ticker,len(tickerFile) - idx,len(tickerFile)))
            #print("Checking if {} ajax completed, time left: {}".format(ticker, timeout - time.time()))
            #print(time.time())
            if time.time() >= timeout:
                os.system("killall Safari")
                ajaxFail = "True"
                break
            my_file = Path(analysisLink)

        if ajaxFail == "True":
            ajaxFail = "False"
            continue

        print("Entering ROIC sorter...")
        roicList = ROIC(analysisLink, ticker)
        print("exiting ROICsorter, {}".format(ticker))
        my_file = Path(analysisLink)
        print(my_file.exists())
        print(analysisLink)

        while my_file.exists():
            os.remove(my_file)
            #print(my_file)
            #print("Searching for file: " + analysisLink)

        print(roicList)
        if not roicList:
            print("Not in list")
            continue

        if roicList[0] >= 40:
            if roicList[1] >= 40:
                with open("40%ROIC.txt", 'a') as FortyPercentCompanies:
                    FortyPercentCompanies.write(ticker.replace("\n", ""))
                    FortyPercentCompanies.write(" {}, {}".format(roicList[0], roicList[1]))
                    FortyPercentCompanies.write("\n")
        elif roicList[0] >= 30:
            if roicList[1] >= 30:
                with open("30%ROIC.txt", 'a') as ThirtyPercentCompanies:
                    ThirtyPercentCompanies.write(ticker.replace("\n", ""))
                    ThirtyPercentCompanies.write(" {}, {}".format(roicList[0], roicList[1]))
                    ThirtyPercentCompanies.write("\n")
        elif roicList[0] >= 20:
            if roicList[1] >= 20:
                with open("20%ROIC.txt", 'a') as TwentyPercentCompanies:
                    TwentyPercentCompanies.write(ticker.replace("\n", ""))
                    TwentyPercentCompanies.write(" {}, {}".format(roicList[0], roicList[1]))
                    TwentyPercentCompanies.write("\n")
        elif roicList[0] >= 10:
            if roicList[1] >= 10:
                with open("10%ROIC.txt", 'a') as TenPercentCompanies:
                    TenPercentCompanies.write(ticker.replace("\n", ""))
                    TenPercentCompanies.write(" {}, {}".format(roicList[0], roicList[1]))
                    TenPercentCompanies.write("\n")

        print("Going to the next ticker...")
print("Stock analysis complete!")