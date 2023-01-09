from Materials.MaterialBase import MaterialBase
from Materials.MaterialBase import Nuclide

class HEU(MaterialBase):
  
  nuclides: list[Nuclide] = [
    Nuclide("U234", 0.0102500321),
    Nuclide("U235", 0.9376828725),
    Nuclide("U238", 0.0520670954)
  ]

  def AtomDensity(self, T: float) -> float:
    return 4.7984