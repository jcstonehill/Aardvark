from Materials.MaterialBase import MaterialBase
from Materials.MaterialBase import Nuclide

class Hydrogen(MaterialBase):
  
  nuclides: list[Nuclide] = [
    Nuclide("H1", 1)
  ]

  def AtomDensity(self, T: float) -> float:
    return 0.005004