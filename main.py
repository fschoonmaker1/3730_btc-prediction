#internal imports
from Util import Util
# from Util import error as uerr
# from Util import print as uprt


#external
import pandas as pd
import numpy as np
import sklearn.linear_model as lin_reg
from sklearn.model_selection import train_test_split as split
from sklearn.linear_model import LinearRegression

def main():
    #setup util functions
    DEBUG = False
    PRINT = True
    util = Util(DEBUG, PRINT)
    #easy access to print funcs
    uprt = util.outPrt
    uerr = util.errPrt

    #read in data from csv
    data = pd.read_csv("./btc.csv")

    #print columns
    # uprt("Columns", data.columns.values.tolist())

    #pull out target column
    y = data["PriceUSD"]
    X = data.loc[:, data.columns != "PriceUSD"]

    #split dataset
    xtrain, xtest, ytrain, ytest = split(X, y)
    #print split data sets
    # uprt("\nytrain:", ytrain)
    # uprt("\nxtrain:", xtrain)
    # uprt("\nxtest:", xtest)
    # uprt("\nytest:", ytest)
    
    # regression = LinearRegression(fit_intercept=False).fit(X, y) 

if __name__ == "__main__":
    main()