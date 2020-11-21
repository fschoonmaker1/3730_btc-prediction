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
import seaborn as sns
import matplotlib.pyplot as plt

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
    price = "PriceUSD"
    date = "date"
    y = data[price].fillna(0)
    # X = data.iloc[:, data.columns == date]
    X = pd.DataFrame(range(1, (y.size+1)))
    # uprt(X)

    #split dataset
    xtrain, xtest, ytrain, ytest = split(X, y)
    #print split data sets
    # uprt("\nytrain:", ytrain)
    # uprt("\nxtrain:", xtrain)
    # uprt("\nxtest:", xtest)
    # uprt("\nytest:", ytest)
    
    regression = LinearRegression(fit_intercept=False)
    regression.fit(X,y)
    uprt(regression.intercept_)

    # coefs = {"y-intercept": format(regression.intercept_, ".2f"),
    #         "B1": format(regression.coef_[0], ".2f")}
    #         # "B2": format(regression.coef_[1], ".2f")}

    # for key, val in coefs.items(): 
    #     uprt(key,": ", val)

if __name__ == "__main__":
    main()