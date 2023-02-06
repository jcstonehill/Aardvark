from Materials.MaterialBase import MaterialBase


# STEEL
class TH_TEST1:
    def k(self, T):
        return 1

    def Cp(self, T):
        return 420

    def Rho(self, T):
        return 7850