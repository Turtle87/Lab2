"""
Description:
Creates a numbered menu string from a menuList and returns it.
"""
__author__ = "Joshua DeNio"


def createMenu(optionList):
    tmp = ""
    ct = 1
    for item in optionList:
        tmp += str(ct)+". " +item +"\n"
        ct+=1
    return tmp
