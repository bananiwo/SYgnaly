import numpy as np
import matplotlib.pyplot as plt

def constant_noise():
    # Set the sampling rate and duration of the signal
    t1 = input('Podaj czas początkowy:')
    d = input('Podaj czas trwania sygnału:')



    sampling_rate = 1000  # samples per second
    duration = 1  # in seconds

    # Create a time axis for the signal
    t = np.linspace(0, duration, sampling_rate*duration, endpoint=False)

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

