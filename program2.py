import numpy as np


# Unit Step Function
def unitStep(v):
    if v >= 0:
        return 1
    else:
        return 0


# Perceptron Model
def perceptronModel(x, w, b):
    v = np.dot(w, x) + b
    y = unitStep(v)
    return y


# NOT Logic Function
def Not_logicFunction(x):
    wNot = -1
    bNot = 0.5
    return perceptronModel(x, wNot, bNot)


# AND Logic Function
def AND_logicFunction(x):
    w = np.array([1, 1])
    bAND = -1.5
    return perceptronModel(x, w, bAND)


# OR Logic Function
def OR_logicFunction(x):
    w = np.array([1, 1])
    bOR = -0.5
    return perceptronModel(x, w, bOR)


# XOR Logic Function
def XOR_logicFunction(x):
    y1 = OR_logicFunction(x)
    y2 = AND_logicFunction(x)

    # XOR = OR AND NOT(AND)
    y2 = Not_logicFunction(y2)

    final = AND_logicFunction(np.array([y1, y2]))

    return final


# XNOR Logic Function
def XNOR_logicFunction(x):
    # XNOR = NOT(XOR)
    y = XOR_logicFunction(x)

    final = Not_logicFunction(y)

    return final


# Testing XNOR
test1 = np.array([0, 0])
test2 = np.array([0, 1])
test3 = np.array([1, 0])
test4 = np.array([1, 1])


print("XNOR({}, {}) = {}".format(0, 0, XNOR_logicFunction(test1)))
print("XNOR({}, {}) = {}".format(0, 1, XNOR_logicFunction(test2)))
print("XNOR({}, {}) = {}".format(1, 0, XNOR_logicFunction(test3)))
print("XNOR({}, {}) = {}".format(1, 1, XNOR_logicFunction(test4)))