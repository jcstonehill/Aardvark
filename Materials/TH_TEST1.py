from Materials.MaterialBase import MaterialBase


# STEEL
class TH_TEST1:
    def k(self, T):
        return 45

    def Cp(self, T):
        return 420

    def Rho(self, T):
        return 7850