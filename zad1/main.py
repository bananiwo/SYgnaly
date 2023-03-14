import numpy as np
import matplotlib.pyplot as plt

def get_input():
    time_start = int(input('Podaj czas początkowy:'))
    duration = int(input('Podaj czas trwania sygnału:'))
    time_to_end = time_start + duration
    amplitude = float(input('Podaj amplitude sygnału:'))
    sampling_rate = int(input('Podaj częstotliwość próbkowania:'))

    return time_start, time_to_end, amplitude, sampling_rate


def constant_noise():
    # Set the sampling rate and duration of the signal
    time_start, time_to_end, amplitude, sampling_rate = get_input()
    random_Y = np.random.uniform(-amplitude/2, amplitude/2, sampling_rate * time_to_end)

    # Create a time axis for the signal
    t = np.linspace(time_start, time_to_end, sampling_rate * time_to_end)


    # Plot the signal
    plt.plot(t, random_Y)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    title_str = 'Constant noise of amplitude ' + str(amplitude)
    plt.title(title_str)
    plt.show()

constant_noise()

