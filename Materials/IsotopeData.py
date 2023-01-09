import json
from scipy.interpolate import interp1d
import os

class IsotopeData:
  scatteringInterp: interp1d
  fissionInterp: interp1d
  totalInterp: interp1d
  isFissionable: bool

  def __init__(self, isotopeName: str):
    scatteringXSFilePath = os.getcwd() + '\\Materials\\NuclideData\\' + isotopeName + '\\scattering.txt'
    fissionXSFilePath = os.getcwd() + '\\Materials\\NuclideData\\' + isotopeName + '\\fission.txt'
    totalXSFilePath = os.getcwd() + '\\Materials\\NuclideData\\' + isotopeName + '\\total.txt'

    file = open(scatteringXSFilePath)
    test = json.load(file)
    E = []
    xs = []
    for i in test['datasets']:
      for j in i['pts']:
        E.append(j['E'])
        xs.append(j['Sig'])
    self.scatteringInterp = interp1d(E, xs)
    file.close()
  
    if(os.path.exists(fissionXSFilePath)):
      self.isFissionable = True

      file = open(fissionXSFilePath)
      test = json.load(file)
      E = []
      xs = []
      for i in test['datasets']:
        for j in i['pts']:
          E.append(j['E'])
          xs.append(j['Sig'])
      self.fissionInterp = interp1d(E, xs)
      file.close()
    else:
      self.isFissionable = False

    file = open(totalXSFilePath)
    test = json.load(file)
    E = []
    xs = []
    for i in test['datasets']:
      for j in i['pts']:
        E.append(j['E'])
        xs.append(j['Sig'])
    self.totalInterp = interp1d(E, xs)
    file.close()