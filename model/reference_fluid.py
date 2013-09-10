

class ReferenceFluid(object):
    """Defines the Fluid that will be running through the pipe"""
    def __init__(self, name, sg, viscosity, tempC):
        self.name = name
        self.sg = sg  # Specific Gravity
        self.viscosity = viscosity  # Centipoise
        self.tempC = tempC  # Celsius

    @property
    def tempC(self):
        return self._tempC

    @property
    def tempF(self):
        return self._tempF

    @tempC.setter
    def tempC(self, value):
        self._tempC = value
        self._tempF = value * (9.0/5.0) + 32.0

    @tempF.setter
    def tempF(self, value):
        self._tempF = value
        self._tempC = (value - 32.0) * (5.0/9.0)
