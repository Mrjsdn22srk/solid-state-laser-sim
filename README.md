# solid-state-laser-sim
Numerical simulation of 4-level solid-state laser dynamics using coupled rate equations. Features relaxation oscillations and phase space analysis.
# Solid-State Laser Rate Equation Simulator

This repository contains a Python implementation for simulating the dynamics of a **4-level solid-state laser** (e.g., Nd:YAG). The project uses coupled Ordinary Differential Equations (ODEs) to model the interaction between population inversion and photon density.

## 🔗 Repository
Check out the source code here: [Mrjsdn22srk/solid-state-laser-sim](https://github.com/Mrjsdn22srk/solid-state-laser-sim)

## 📖 Overview
The simulation provides insights into how a laser reaches its steady-state through **Relaxation Oscillations**. By solving the rate equations numerically, we can observe the "spiking" behavior of the laser immediately after it is turned on.

### Key Features:
- **Numerical Solver:** Uses `SciPy`'s `odeint` for high-accuracy integration.
- **Temporal Analysis:** Visualizes the time-evolution of Photon Density ($\Phi$) and Population Inversion ($N_2$).
- **Phase Space Analysis:** Provides a phase portrait to show the system's stability and convergence.

## 📊 Simulation Results

### 1. Laser Dynamics (Relaxation Oscillations)
The plot below shows the initial spikes in photon density before the system settles into a stable Continuous Wave (CW) output.
![Laser Dynamics](results.png)

### 2. Phase Space Portrait
This spiral graph demonstrates the relationship between the number of excited atoms and the number of photons, showing how the system evolves towards a stable equilibrium point.
![Phase Space Analysis](phase_portrait.png)

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Mrjsdn22srk/solid-state-laser-sim.git](https://github.com/Mrjsdn22srk/solid-state-laser-sim.git)
