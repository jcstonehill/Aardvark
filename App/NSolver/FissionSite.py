from dataclasses import dataclass

@dataclass
class FissionSite():
  position: list[float]
  cellID: int