"""
Created on Fri Jul 26 16:07:41 2024

@author: user288 (JS)
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams["figure.autolayout"] = True
columns = ["Wmass", "Chi2"]
df = pd.read_csv("/home/user312/FutureWMassAnalysis/outputChi2_test_pseudo_and_semilep_others_semilep_leptonPt.csv", usecols=columns)

mass = df.Wmass.str[:7]
x = mass.astype(float)
y = df.Chi2
#x = df.W_mass
def parabola(x, a, b, c):
    return a*x**2 + b*x + c

parameters, covariance = curve_fit(parabola, x, y)

fit_A = parameters[0]
fit_B = parameters[1]
fit_C = parameters[2]


z = np.linspace(x[0], x[np.argmax(x)], 100)

fit_y = parabola(z, fit_A, fit_B, fit_C)

mw = - (fit_B)/(2*fit_A)

perr = np.sqrt(np.diag(covariance))

A_err = perr[0]
print("A err", A_err)
B_err = perr[1]
print("B_err", B_err)
C_err = perr[2]
print("C err", C_err)
#unc = (np.sqrt((B_err/(2*fit_A))**2+((fit_B*A_err)/(2*fit_A**2))**2)-((fit_B*A_err*B_err)/(2*fit_A**3))*covariance[0][1])
unc = (np.sqrt((B_err/(2*fit_A))**2+((fit_B*A_err)/(2*fit_A**2))**2-(fit_B*covariance[0][1])/(2*fit_A**3)))

print(unc)

print(parameters)
print(perr)

print("Covariance:", covariance)
print("Cov ab", covariance[0][1])

print(mw)

mw_up = mw + unc
mw_lo = mw - unc

plt.vlines(mw, 0, 60, 'k', '--', label=mw)
plt.vlines(mw_up, 0, 60, 'r', '--', label=unc)
plt.vlines(mw_lo, 0, 60, 'r', '--')

plt.plot(x, y, 'o', label='Data')
plt.plot(z, fit_y, '-', label='Fit')
plt.legend()