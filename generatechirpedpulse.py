import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Constants
c = 3e8  # Speed of light (m/s)
fs = 1e-15  # Femtosecond (s)
nm = 1e-9  # Nanometer (m)
Fs = 2.35e16  # Sampling frequency (Hz)
Ts = 1 / Fs  # Sampling interval (s)
carrier_freq = 2.35e15  # Carrier frequency (Hz)

# Create a figure and axis for the plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

# Sampling time instants
t = np.arange(-0.8e-13, 0.8e-13, Ts)

# Initial values for variables
initial_t0 = 0
initial_tau = 40
initial_carrier_freq = 2.35e15

# Generate the chirp pulse function
def generate_chirp_pulse(t0, tau, carrier_freq):
    chirp_pulse = np.exp(-2 * np.log(2) * ((t - t0) / tau) ** 2) * np.cos(2 * np.pi * (carrier_freq * t + (t - t0) ** 2 / (2 * tau ** 2)))
    return chirp_pulse

chirp_pulse = generate_chirp_pulse(initial_t0, initial_tau, initial_carrier_freq)
line, = plt.plot(t, chirp_pulse)

# Create sliders for variable values
axcolor = 'lightgoldenrodyellow'
ax_t0 = plt.axes([0.15, 0.01, 0.65, 0.03], facecolor=axcolor)
ax_tau = plt.axes([0.15, 0.06, 0.65, 0.03], facecolor=axcolor)
ax_carrier_freq = plt.axes([0.15, 0.11, 0.65, 0.03], facecolor=axcolor)

s_t0 = Slider(ax_t0, 't0 (s)', -1e-13, 1e-13, valinit=initial_t0)
s_tau = Slider(ax_tau, 'tau (s)', 1e-15, 100e-15, valinit=initial_tau)
s_carrier_freq = Slider(ax_carrier_freq, 'Carrier Freq (Hz)', 2e15, 3e15, valinit=initial_carrier_freq)

# Function to update the chirp pulse
def update(val):
    t0 = s_t0.val
    tau = s_tau.val
    carrier_freq = s_carrier_freq.val
    chirp_pulse = generate_chirp_pulse(t0, tau, carrier_freq)
    line.set_ydata(chirp_pulse)
    fig.canvas.draw_idle()

s_t0.on_changed(update)
s_tau.on_changed(update)
s_carrier_freq.on_changed(update)

plt.show()
