import numpy as np
import matplotlib.pyplot as plt

def constant_noise():
    # Set the sampling rate and duration of the signal
    time_start = int(input('Podaj czas początkowy:'))
    time_to_end = int(input('Podaj czas trwania sygnału:'))
    duration = time_start + time_to_end
    amplitude = float(input('Podaj amplitude sygnału:'))
    sampling_rate = int(input('Podaj częstotliwość próbkowania:'))

    random_Y = np.random.uniform(-amplitude/2, amplitude/2, sampling_rate * duration)

    # Create a time axis for the signal
    t = np.linspace(time_start, duration, sampling_rate*duration)


    # Plot the signal
    plt.plot(t, random_Y)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    title_str = 'Constant noise of amplitude ' + str(amplitude)
    plt.title(title_str)
    plt.show()

constant_noise()

