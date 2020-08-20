# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:57:01 2020

@author: Salman
"""

import csv

lstdata = []
N = 14
closeprices = []

def readStockFile(strfile):
    blnFlag = False
    with open(strfile, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if not blnFlag:
                blnFlag = True
                continue
            else:
                lstdata.append(row)

def SMMA(array, N):
    tmpSMA = array[:]
    for i in range(len(array)-3,-1,-1):
        tmpSMA[i] = (tmpSMA[i+1]*(N-1)+tmpSMA[i])/N
    return tmpSMA

def fillPrice():
    for n in range(0,len(lstdata)):
        closeprice = lstdata[n][5]
        closeprices.append(int(closeprice))

def calcRSI(closeprices, N):
    U = []
    D = []
    for i in range(0, len(closeprices)-1):
        difference = closeprices[i] - closeprices[i+1]
        if difference > 0:
            U.append(difference)
            D.append(0)
        elif difference < 0:
            D.append(-1*difference)
            U.append(0)
        else:
            U.append(0)
            D.append(0)
    RS = SMMA(U,N)[0] / SMMA(D,N)[0]
    RSI = 100 - 100/(1+RS)
    return RSI
                

def main():
    # This program calculates RSI for a stock
    readStockFile("test.csv")
    fillPrice()
    RSI = calcRSI(closeprices, N)
    print("RSI = ", RSI)
    
if __name__ == "__main__":
    main()
