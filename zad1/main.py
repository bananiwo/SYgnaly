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

def jump():
    time_start, time_to_end, amplitude, sampling_rate = get_input()
    basic_period = float(input('Podaj okres podstawowy sygnału:'))

    nr_of_samplings = sampling_rate * (time_to_end - time_start)
    values_y = np.zeros(nr_of_samplings)
    for x in range(0, nr_of_samplings):
        values_y[x] = amplitude * math.sin(2.0 * math.pi * (x - time_start) / basic_period)

    draw_graph("Constant noise", time_start, time_to_end, amplitude, nr_of_samplings, values_y)

def rectangular_signal(): #6
    time_start, time_to_end, amplitude, sampling_rate = get_input()
    # time_start, time_to_end, amplitude, sampling_rate = 0, 10, 10, 100
    basic_period = float(input('Podaj okres podstawowy sygnału:'))
    fill_value = float(input('Podaj współczynnik wypełnienia sygnału:'))
    # basic_period = 2
    # fill_value = 0.5


    nr_of_samplings = sampling_rate * (time_to_end - time_start)
    values_y = np.zeros(nr_of_samplings)

    for x in range(time_start, time_to_end, basic_period):
        for i in range(int(basic_period * fill_value * sampling_rate)):
            values_y[x * sampling_rate + i] = amplitude

    draw_graph("Rectangular signal", time_start, time_to_end, amplitude, nr_of_samplings, values_y)

def rectangular_symmetrical_signal(): #7
    time_start, time_to_end, amplitude, sampling_rate = get_input()
    # time_start, time_to_end, amplitude, sampling_rate = 0, 10, 10, 1000
    basic_period = float(input('Podaj okres podstawowy sygnału:'))
    fill_value = float(input('Podaj współczynnik wypełnienia sygnału:'))
    # basic_period = 2
    # fill_value = 0.5

    nr_of_samplings = sampling_rate * (time_to_end - time_start)
    values_y = np.zeros(nr_of_samplings)
    for x in range(nr_of_samplings):
        values_y[x] = -amplitude

    for x in range(time_start, time_to_end, basic_period):
        for i in range(int(basic_period * fill_value * sampling_rate)):
            values_y[x * sampling_rate + i] = amplitude

    # for x in range(time_start * sampling_rate, time_to_end * sampling_rate, basic_period * sampling_rate):
    #     for i in range(int(basic_period * fill_value * sampling_rate)):
    #         values_y[x + i] = amplitude

    draw_graph("Rectangular symmetrical signal", time_start, time_to_end, amplitude, nr_of_samplings, values_y)

def jump_signal(): #9
    time_start, time_to_end, amplitude, sampling_rate = get_input()
    ts = int(input('Podaj czas skoku:'))

    nr_of_samplings = sampling_rate * (time_to_end - time_start)
    values_y = np.zeros(nr_of_samplings)

    for y in range(time_start, time_to_end):
        for x in range(0, sampling_rate):
            t = y * sampling_rate + x
            if time_start < 0:
                if t > ts * sampling_rate:
                    values_y[t - time_start * sampling_rate] = amplitude
                elif t == ts * sampling_rate:
                    values_y[t - time_start * sampling_rate] = amplitude / 2
                else:
                    values_y[t - time_start * sampling_rate] = 0
            if time_start >= 0:
                if t > ts * sampling_rate:
                    values_y[t - time_start * sampling_rate] = amplitude
                elif t == ts * sampling_rate:
                    values_y[t - time_start * sampling_rate] = amplitude / 2
                else:
                    values_y[t - time_start * sampling_rate] = 0

    draw_graph("Jump signal", time_start, time_to_end, amplitude, nr_of_samplings, values_y)



def sinus_half_straight_signal():
    time_start, time_to_end, amplitude, sampling_rate = get_input()
    basic_period = float(input('Podaj okres podstawowy sygnału:'))

    nr_of_samplings = sampling_rate * (time_to_end - time_start)
    values_y = np.zeros(nr_of_samplings)
    for x in range(0, nr_of_samplings):
        values_y[x] = 0.5 * amplitude * ((math.sin(2.0 * math.pi * (x - time_start) / basic_period)) + abs(math.sin(2.0 * math.pi * (x - time_start) / basic_period)))

    draw_graph("Constant noise", time_start, time_to_end, amplitude, nr_of_samplings, values_y)

def sinus_double_half_straight_signal():
    time_start, time_to_end, amplitude, sampling_rate = get_input()
    # nie dziala dla basic_period = 1, 2
    basic_period = float(input('Podaj okres podstawowy sygnału:'))

    nr_of_samplings = sampling_rate * (time_to_end - time_start)
    values_y = np.zeros(nr_of_samplings)
    for x in range(0, nr_of_samplings):
        values_y[x] = amplitude * abs(
                math.sin(2.0 * math.pi * (x - time_start) / basic_period))

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
# sinus_half_straight_signal()
# sinus_double_half_straight_signal()
rectangular_signal()
# rectangular_symmetrical_signal()
# jump_signal()