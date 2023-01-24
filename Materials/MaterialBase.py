from Materials.IsotopeData import IsotopeData
from abc import abstractmethod
import os

class Nuclide:
  name: str
  atomicFraction: float
  xs: IsotopeData
  molarMass: float
  isFissionable: bool

  def __init__(self, name: str, atomicFraction: float):
    self.name = name
    self.atomicFraction = atomicFraction
    self.xs = IsotopeData(name)
    self.isFissionable = self.xs.isFissionable

    molarMassFilePath = os.getcwd() + '\\Materials\\NuclideData\\' + name + '\\molarmass.txt'
    file = open(molarMassFilePath)
    self.molarMass = float(file.readline())
    file.close()

class MaterialBase():
  
  nuclides: list[Nuclide]

  @abstractmethod
  def k(self, T):
      pass

  @abstractmethod
  def Cp(self, T):
      pass

  @abstractmethod
  def Rho(self, T):
      pass

  @abstractmethod
  def AtomDensity(self, T: float) -> float:
    pass

  def ScatteringMicroXS(self, E: float, T: float) -> float:
    microXS = 0
    for nuclide in self.nuclides:
      microXS = microXS + (nuclide.atomicFraction * nuclide.xs.scatteringInterp(E))

    return microXS

  def AbsorptionMicroXS(self, E: float, T: float) -> float:
    return self.TotalMicroXS(E, T) - self.ScatteringMicroXS(E, T)

  def CaptureMicroXS(self, E: float, T: float) -> float:
    microXS = 0
    for nuclide in self.nuclides:
      microXS = microXS + (nuclide.atomicFraction * (nuclide.xs.totalInterp(E) - nuclide.xs.scatteringInterp(E) - nuclide.xs.fissionInterp(E)))

    return microXS

  def FissionMicroXS(self, E: float, T: float) -> float:
    microXS = 0
    for nuclide in self.nuclides:
      if(nuclide.isFissionable):
        microXS = microXS + (nuclide.atomicFraction * nuclide.xs.fissionInterp(E))
      else:
        microXS = microXS + 0

    return microXS

  def TotalMicroXS(self, E: float, T: float):
    microXS = 0
    for nuclide in self.nuclides:
      microXS = microXS + (nuclide.atomicFraction * nuclide.xs.totalInterp(E))

    return microXS

  def AbsorptionXS(self, E: float, T: float) -> float:
    return self.AbsorptionMicroXS(E, T) * self.AtomDensity(T)

  def ScatteringXS(self, E: float, T: float) -> float:
    return self.ScatteringMicroXS(E, T) * self.AtomDensity(T)

  def FissionXS(self, E: float, T: float) -> float:
    return self.FissionMicroXS(E, T) * self.AtomDensity(T)

  def TotalXS(self, E: float, T: float):
    return  self.TotalMicroXS(E, T) * self.AtomDensity(T)