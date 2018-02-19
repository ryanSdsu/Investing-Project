NYSEcompanyList = "/Users/RJ/PycharmProjects/Investing-Project/FindCompaniesROIC/NYSEcompanyList.txt"
NASDAQcompanyList = "/Users/RJ/PycharmProjects/Investing-Project/FindCompaniesROIC/NASDAQcompanyList.txt"
AMEXcompanyList = "/Users/RJ/PycharmProjects/Investing-Project/FindCompaniesROIC/AMEXcompanyList.txt"

from FindCompaniesROIC.ROICprintToTxt import findCompaniesROIC

findCompaniesROIC(NASDAQcompanyList)
findCompaniesROIC(NYSEcompanyList)
findCompaniesROIC(AMEXcompanyList)
