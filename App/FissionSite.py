from dataclasses import dataclass

@dataclass
class FissionSite():
  position: list[float]
  physicalElementTag: int