import math


class Pipe(object):
    """Pipe to be calculated"""
    def __init__(self, flowrate, length, fluid, quality, refpipelist):
        self.flowrate = float(flowrate)
        self.length = float(length)  # (Feet)
        self.fluid = fluid
        self.quality = quality
        self.refpipelist = refpipelist
        self.maxpressure = 3
        self.resultlist = []

    @property
    def quality(self):
        return self._quality

    @property
    def rf(self):
        return self._rf  # Roughness Factor

    @quality.setter
    def quality(self, value):
        self._quality = value

        if value == "Hygienic Tubing":
            self._rf = 0.000005
        elif value == "Sch40 Stainless":
            self._rf = 0.00005
        elif value == "Carbon Steel":
            self._rf = 0.00015
        else:
            raise Exception("Value %s must be Hygienic Tubing, Sch40 Stainless, or Carbon Steel")

    def calculate(self):
        i = 0
        for refpipe in self.refpipelist:
            ans = {}
            ans["dnom"] = refpipe.dnom_in

            ans["ReynoldsNumber"] = ((50.6 * self.flowrate * self.fluid.sg) / self.fluid.viscosity) / refpipe.dact_in

            if ans["ReynoldsNumber"] > 2000:
                ans["Flowregion"] = "Turbulent"
                ans["FrictionFactor"] = (-2 * math.log10((7/ans["ReynoldsNumber"])**0.9 + (self.rf / 3.71 * (refpipe.dact_in / 12))))**-2
            else:
                ans["Flowregion"] = "Laminar"
                ans["FrictionFactor"] = 64 / ans["ReynoldsNumber"]

            ans["dP100"] = 0.216 * (ans["FrictionFactor"] * self.fluid.sg * self.flowrate**2) / (refpipe.dact_in**5)

            ans["velocity"] = (self.flowrate * 0.4085) / refpipe.dact_in**2

            if (ans["velocity"] < 7.26 and ans["dP100"] <= self.maxpressure and i < 1):
                ans["ideal"] = True
                i += 1
            else:
                ans["ideal"] = False

            self.resultlist.append(ans)

        return self.resultlist
