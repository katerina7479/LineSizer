

class ReferencePipe(object):
    """Reference Pipe or Tube"""
    def __init__(self, name, quality, dnom, dact):
        self.name = name
        self.quality = quality
        self.dnom_in = dnom  # Nominal Diameter (inches)
        self.dact_in = dact  # Actual Diameter (inches)

    @property
    def dnom_in(self):
        return self._dnom_in

    @property
    def dnom_mm(self):
        return self._dnom_mm

    @dnom_in.setter
    def dnom_in(self, value):
        self._dnom_in = round(value, 3)
        self._dnom_mm = round(value * 25.4, 3)

    @dnom_mm.setter
    def dnom_mm(self, value):
        self._dnom_in = round(value / 25.4, 3)
        self._dnom_mm = round(value, 1)

    @property
    def dact_in(self):
        return self._dact_in

    @property
    def dact_mm(self):
        return self._dact_mm

    @dact_in.setter
    def dact_in(self, value):
        self._dact_in = round(value, 3)
        self._dact_mm = round(value * 25.4, 1)

    @dact_mm.setter
    def dact_mm(self, value):
        self._dact_in = round(value / 25.4, 3)
        self._dact_mm = round(value, 1)
