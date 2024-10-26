import numpy as np
import matplotlib.pyplot as plt
import pint


ureg = pint.UnitRegistry()
ureg.default_system = 'cgs'


c = 3e5                             # km/s
b = np.array([1,2,3,5,10])          # km/s

def plot_eqwidth(N,f,wavelength,gamma):
    for j in range(len(b)):
        W_list = []
        tau_list = []

        for i in range(len(N)):
            tau_0 = 0.7580 * (N[i]/1e13) * (f/0.4164) * (wavelength/1215.7) * (10/b[j])
            # print(tau_0)
            tau_list += [tau_0]

            if tau_0 < 1.25393:
                W = np.sqrt(np.pi) * b[j]/c * (tau_0/(1 + tau_0/(2*np.sqrt(2))))
                W_list += [W*wavelength]
            elif tau_0 > 1.25393:
                W = np.sqrt((2*b[j]/c)**2 * np.log(tau_0/np.log(2)) + b[j]/c * gamma*wavelength*1e-13/c * (tau_0-1.25393)/np.sqrt(np.pi))
                W_list += [W*wavelength]

        # print(np.max(tau_list))
        plt.plot(np.log10(N),np.log10(W_list),label=f'b={b[j]}')
    plt.legend()
    plt.show()

#Three blocks of code below based on which c.o.g. you want to plot
#uncomment the plot you want and comment out the other two

# Fe II 2832: 

N_Fe = np.linspace(1e12,1e17,100000)    # cm^-2
wl_Fe = 2382.7642
f_Fe = 0.320
gamma_Fe = 3.13e8

plt.xlabel(r"log($N_{FeII}$)")
plt.ylabel(r"log($W_{\lambda}$)")
plt.title(r"Curve of Growth for Fe II 2383")
plt.axhline(y = np.log10(0.051), color = 'k', linestyle = '-') 
plot_eqwidth(N=N_Fe,f=f_Fe,wavelength=wl_Fe,gamma=gamma_Fe)



# Fe II 2249:  

# N_Fe = np.linspace(1e12,1e16,100000)    # cm^-2
# wl_Fe = 2249.8768
# f_Fe = 0.00182
# gamma_Fe = 3.31e8

# plt.xlabel(r"log($N_{FeII}$)")
# plt.ylabel(r"log($W_{\lambda}$)")
# plt.title(r"Curve of Growth for Fe II 2250")
# plt.axhline(y=np.log10(0.0047), color='k', linestyle ='-')
# plot_eqwidth(N=N_Fe,f=f_Fe,wavelength=wl_Fe,gamma=gamma_Fe)



# C II 1334

# N_C = np.linspace(1e13,1e17,50000)      # cm^-2
# wl_C = 1334.5323
# f_C = 0.12780
# gamma_C = 2.880e8

# plt.xlabel(r"log($N_{CII}$)")
# plt.ylabel(r"log($W_{\lambda}$)")
# plt.title(r"Curve of Growth for C II 1335")
# plt.axhline(y=np.log10(0.06), color='k', linestyle ='-')
# plot_eqwidth(N=N_C,f=f_C,wavelength=wl_C,gamma=gamma_C)