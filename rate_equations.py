import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sys

class SolidStateLaserSimulator:
    """
    Numerical solver for 4-level Solid-State Laser Rate Equations.
    Tracks Population Inversion (N2) and Photon Density (Phi).
    """
    def __init__(self, tau_f=230e-6, tau_c=10e-9, sigma=2.8e-19, c=3e10, beta=1e-6):
        self.tau_f = tau_f    
        self.tau_c = tau_c    
        self.sigma = sigma    
        self.c = c            
        self.beta = beta      

    def equations(self, y, t, Rp):
        N2, Phi = y
        # Rate of change for Population Inversion
        dn2_dt = Rp - (self.sigma * self.c * Phi * N2) - (N2 / self.tau_f)
        # Rate of change for Photon Density
        dphi_dt = (self.sigma * self.c * Phi * N2) - (Phi / self.tau_c) + (self.beta * N2 / self.tau_f)
        return [dn2_dt, dphi_dt]

    def run_simulation(self, Rp, t_max=0.0005, points=10000):
        t = np.linspace(0, t_max, points)
        y0 = [0, 0]  # Initial conditions
        solution = odeint(self.equations, y0, t, args=(Rp,))
        return t, solution

def main():
    try:
        sim = SolidStateLaserSimulator()
        pumping_rate = 1.5e22 
        
        print("Simulating laser dynamics... Close the plot window to exit.")
        time, sol = sim.run_simulation(Rp=pumping_rate)
        N2, Phi = sol[:, 0], sol[:, 1]

        # Plotting
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

        ax1.plot(time * 1e6, Phi, color='tab:red', label='Photon Density')
        ax1.set_ylabel(r'Photon Density $\Phi$ ($cm^{-3}$)')
        ax1.set_title('Laser Relaxation Oscillations', fontsize=14)
        ax1.grid(True, alpha=0.4)

        ax2.plot(time * 1e6, N2, color='tab:blue', label='Inversion')
        ax2.set_xlabel(r'Time ($\mu s$)')
        ax2.set_ylabel(r'Inversion $N_2$ ($cm^{-3}$)')
        ax2.grid(True, alpha=0.4)

        plt.tight_layout()
        
        # Phase Space Portrait
        plt.figure(figsize=(7, 6))
        plt.plot(N2, Phi, color='darkviolet')
        plt.xlabel(r'Population Inversion ($N_2$)')
        plt.ylabel(r'Photon Density ($\Phi$)')
        plt.title('Phase Space Analysis')
        plt.grid(True, alpha=0.4)
        
        plt.show()

    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()