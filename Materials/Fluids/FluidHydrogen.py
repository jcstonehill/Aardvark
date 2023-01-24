from Materials.Fluids.FluidBase import FluidBase

class FluidHydrogen(FluidBase):
    def mu(self):
        return 8.9e-4

    def Cp(self):
        return 100

    def k(self):
        return 0.598