import numpy as np
import matplotlib.pyplot as plt
import math

def get_input():
    time_start = int(input('Podaj czas początkowy:'))
    duration = int(input('Podaj czas trwania sygnału:'))
    time_to_end = time_start + duration
    amplitude = float(input('Podaj amplitude sygnału:'))
    sampling_rate = int(input('Podaj częstotliwość próbkowania:'))

    return time_start, time_to_end, amplitude, sampling_rate

def draw_graph(name, time_start, time_to_end, amplitude, sampling_rate, values_y):

    # Create a time axis for the signal
    t = np.linspace(time_start, time_to_end, sampling_rate)

    plt.plot(t, values_y)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(name)
    plt.show()

def sinus_signal():
    time_start, time_to_end, amplitude, sampling_rate = get_input()
    basic_period = float(input('Podaj okres podstawowy sygnału:'))

    nr_of_samplings = sampling_rate * (time_to_end - time_start)
    values_y = np.zeros(nr_of_samplings)
    for x in range(0, nr_of_samplings):
        values_y[x] = amplitude * math.sin(2.0 * math.pi * (x - time_start) / basic_period)

    draw_graph("Constant noise", time_start, time_to_end, amplitude, nr_of_samplings, values_y)

def sinus_straight_signal():
    time_start, time_to_end, amplitude, sampling_rate = get_input()
    basic_period = float(input('Podaj okres podstawowy sygnału:'))

    nr_of_samplings = sampling_rate * (time_to_end - time_start)
    values_y = np.zeros(nr_of_samplings)
    for x in range(0, nr_of_samplings):
        values_y[x] = 0.5 * amplitude * ((math.sin(2.0 * math.pi * (x - time_start) / basic_period)) + abs(math.sin(2.0 * math.pi * (x - time_start) / basic_period)))

    draw_graph("Constant noise", time_start, time_to_end, amplitude, nr_of_samplings, values_y)



def constant_noise():
    time_start, time_to_end, amplitude, sampling_rate = get_input()

    nr_of_samplings = sampling_rate * (time_to_end - time_start)

    # Set the sampling rate and duration of the signal
    values_y = np.random.uniform(-amplitude/2, amplitude/2, nr_of_samplings)

    draw_graph("Constant noise", time_start, time_to_end, amplitude, nr_of_samplings, values_y)

def gaussian_noise():
    time_start, time_to_end, amplitude, sampling_rate = get_input()

    nr_of_samplings = sampling_rate * (time_to_end - time_start)

    # Set the sampling rate and duration of the signal
    values_y = np.random.normal(0, amplitude/2, nr_of_samplings)

    draw_graph("Gaussian noise", time_start, time_to_end, amplitude, nr_of_samplings, values_y)

# sinus_signal()
# gaussian_noise()
# constant_noise()
sinus_straight_signal()