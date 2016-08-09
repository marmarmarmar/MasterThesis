# Main function which we will approximate
def main_function(x):
    return x**4 - x**3 - 3 * x**2 + 4 * x - 5

import matplotlib.pyplot as plt
import numpy

arguments = numpy.arange(-2, 2, 0.1)
main_values = main_function(arguments)

def sample_from_training_set(arguments, size):
    permutation = numpy.arange(arguments.shape[0])
    numpy.random.shuffle(permutation)
    return arguments[permutation[0:size]]

def generate_random_polynomial(arguments, degree, size):
    training_set = sample_from_training_set(arguments, size)
    training_values = main_function(training_set) + numpy.random.normal(0, 1, size)
    return numpy.polyfit(training_set, training_values, degree)

def plot_polynomial_variance_with_percnetile(arguments, degree, size, number_of_samples, percentile):

    polynomials = numpy.zeros((number_of_samples, degree + 1))

    for i in range(number_of_samples):
        polynomials[i,:] = generate_random_polynomial(arguments, degree, size)

    results = numpy.zeros((number_of_samples, arguments.shape[0]))

    for i in range(number_of_samples):
        results[i,:] = numpy.polyval(polynomials[i,:], arguments)
        print results[i,:]

    for i in range(number_of_samples):
        plt.plot(arguments[3:37], results[i,3:37])
        plt.ylim((-12, -2))
        plt.title("Aproksymacja wielomianowa stopnia " + str(degree))

plt.figure(1)
plt.subplot(221)
plt.plot(arguments[3:37], main_values[3:37])
plt.title("Oryginalna funkcja")
plt.ylim((-12, -2))
plt.subplot(222)
plot_polynomial_variance_with_percnetile(arguments, 1, 40, 20, 0.3)
plt.subplot(223)
plot_polynomial_variance_with_percnetile(arguments, 4, 40, 20, 0.3)
plt.subplot(224)
plot_polynomial_variance_with_percnetile(arguments, 16, 40, 20, 0.3)
plt.show()







