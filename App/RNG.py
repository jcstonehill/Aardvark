from numpy import random

def RandomFromRange(lowerLim: float, upperLim: float):
  return (upperLim - lowerLim)*random.random() + lowerLim