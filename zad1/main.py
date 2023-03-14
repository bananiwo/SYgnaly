import numpy as np
import matplotlib.pyplot as plt

def get_input():
    time_start = int(input('Podaj czas początkowy:'))
    duration = int(input('Podaj czas trwania sygnału:'))
    time_to_end = time_start + duration
    amplitude = float(input('Podaj amplitude sygnału:'))
    sampling_rate = int(input('Podaj częstotliwość próbkowania:'))

    return time_start, time_to_end, amplitude, sampling_rate

def draw_graph(name, time_start, time_to_end, amplitude, sampling_rate, values_y):

    # Create a time axis for the signal
    t = np.linspace(time_start, time_to_end, sampling_rate * time_to_end)

    plt.plot(t, values_y)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(name)
    plt.show()


def constant_noise():
    time_start, time_to_end, amplitude, sampling_rate = get_input()

    # Set the sampling rate and duration of the signal
    values_y = np.random.uniform(-amplitude/2, amplitude/2, sampling_rate * time_to_end)

    draw_graph("Constant noise", time_start, time_to_end, amplitude, sampling_rate, values_y)




constant_noise()

