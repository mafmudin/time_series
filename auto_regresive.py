import numpy as np
from statsmodels.tsa.ar_model import AutoReg

if __name__ == '__main__':

    # Data: Monthly sales of a product over 12 months
    sales_data = np.array([30, 32, 29, 35, 33, 36, 38, 40, 37, 39, 41, 43])

    # Fit an AR(1) model using AutoReg
    model = AutoReg(sales_data, lags=1).fit()

    # Display the parameter phi
    phi = model.params[1]  # phi is the coefficient of Y_t-1
    print(phi)