from random import choice
from numpy import array, dot, random
import matplotlib.pyplot as plt
# from matplotlib.pyplot.ylim import ylim

unit_step = lambda x: 0 if x < 0 else 1
# xor truth table for Non Linear
training_data = [
    (array([0,0,1]), 1),
    (array([0,1,1]), 0),
    (array([1,0,1]), 0),
    (array([1,1,1]), 1),
]

w = random.rand(3)
errors = []
eta = 0.02
n = 100

for i in range(n):
    x, expected = choice(training_data)
    result = dot(w, x)
    error = expected - unit_step(result)
    errors.append(error)
    w += eta * error * x

for x, _ in training_data:
    result = dot(x, w)
    print("{}: {} -> {}".format(x[:2], result, unit_step(result)))


plt.ylim(-1,1)
plt.plot(errors)
plt.show()
