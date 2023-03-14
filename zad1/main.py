import numpy as np
import matplotlib.pyplot as plt

def constant_noise():
    # Set the sampling rate and duration of the signal
    time_start = int(input('Podaj czas początkowy:'))
    time_to_end = int(input('Podaj czas trwania sygnału:'))
    duration = time_start + time_to_end

    sampling_rate = 1000  # samples per second

    # Create a time axis for the signal
    t = np.linspace(time_start, duration, sampling_rate*duration)

    # Generate the constant signal of amplitude 2
    constant_signal = 2*np.ones_like(t)

    # Plot the signal
    plt.plot(t, constant_signal)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Constant signal of amplitude 2')
    plt.show()

constant_noise()

# Prompt the user to enter a value and store it in a variable
value = input("Enter a value: ")

# Print the entered value
print("You entered:", value)

