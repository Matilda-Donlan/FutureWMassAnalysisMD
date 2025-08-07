import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

plt.rcParams["figure.autolayout"] = True
columns = ["W_mass", "Chi2"]
df = pd.read_csv("/home/user312/FutureWMassAnalysis/outputChi2_5mil_7mass_and_pseudo_unspec_leptonic_mm_muon2Pt.csv", usecols=columns)

mass = df.W_mass.str[:7]
x = mass.astype(float)
print(x)
y = df.Chi2
#x = df.W_mass
def parabola(x, a, b, c):
    return a*x**2 + b*x + c

parameters, covariance = curve_fit(parabola, x, y)

fit_A = parameters[0]
fit_B = parameters[1]
fit_C = parameters[2]


z = np.linspace(x[np.argmin(x)], x[np.argmax(x)], 100)
print(x[0])
print(x[np.argmax(x)])
fit_y = parabola(z, fit_A, fit_B, fit_C)
print(fit_y)
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

#plt.vlines(mw, 0, plt.ylim(), 'k', '--', label=mw)
#plt.vlines(mw_up, 0, 60, 'r', '--', label=unc)
#plt.vlines(mw_lo, 0, 60, 'r', '--')

plt.plot(x, y, 'o', label='Data')
plt.plot(z, fit_y, '-', label='Fit')

ylim = 0

ylim = plt.ylim()[1]

plt.vlines(mw, 0, ylim, 'k', '--', label=mw)
plt.vlines(mw_up, 0, ylim, 'r', '--', label=unc)
plt.vlines(mw_lo, 0, ylim, 'r', '--')
plt.legend()