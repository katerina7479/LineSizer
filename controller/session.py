from kglobals import database_manager

from model.pipe import Pipe
from model.reference_fluid import ReferenceFluid
from model.reference_pipe import ReferencePipe


class Session(object):

    def __init__(self):
        self.pipelength = None
        self.flowrate = None
        self._setLists()

    def _setLists(self):
        self.setfluidlist()
        self.setpipelists()
        self.qualitylist = [(1, "Hygienic Tubing"), (
            2, "Sch40 Stainless"), (3, "Carbon Steel")]

    def setfluidlist(self):
        self._fluidlist = database_manager.query("ReferenceFluid",
                                                 cols=["id", "name"])

    def setpipelists(self):
        self._tubinglist = database_manager.query("ReferencePipe",
                                                  cols=["id", "name"],
                                                  wcol="quality",
                                                  wval="tubing")
        self._stainlesslist = database_manager.query("ReferencePipe",
                                                     cols=["id", "name"],
                                                     wcol="quality",
                                                     wval="stainless")
        self._carbonlist = database_manager.query("ReferencePipe",
                                                  cols=["id", "name"],
                                                  wcol="quality",
                                                  wval="carbon")

    @property
    def quality(self):
        return self._quality

    @property
    def fluidlist(self):
        return self._fluidlist

    @property
    def fluid(self):
        return self._fluid

    @property
    def pipelist(self):
        return self._pipelist

    @property
    def pipewidgetlist(self):
        return self._pipewidgetlist

    @fluid.setter
    def fluid(self, value):
        self._fluid_id = value
        answerlist = database_manager.query("ReferenceFluid",
                                            wcol="id", wval=value)
        ans = answerlist[0]
        self._fluid = ReferenceFluid(ans["name"],
                                     ans["sg"],
                                     ans["viscosity"],
                                     ans["tempC"])

    @quality.setter
    def quality(self, myid):
        self._quality = self.qualitylist[myid-1][1]

        if self._quality == "Hygienic Tubing":
            self._pipelist = self._tubinglist
        elif self._quality == "Sch40 Stainless":
            self._pipelist = self._stainlesslist
        elif self._quality == "Carbon Steel":
            self._pipelist = self._carbonlist
        self._setPipeWidgetList()

    def _setPipeWidgetList(self):
        self._pipewidgetlist = []
        for item in self.pipelist:
            a = database_manager.query("ReferencePipe",
                                       cols=["name", "quality",
                                       "dnom_in", "dact_in"],
                                       wcol="id",
                                       wval=item[0])
            ans = a[0]
            self._pipewidgetlist.append(ReferencePipe(
                ans[0], ans[1], ans[2], ans[3]))

    def calculate(self):
        self.pipe = Pipe(self.flowrate, self.pipelength,
                         self.fluid, self.quality, self.pipewidgetlist)
        self.answers = self.pipe.calculate()
        i = 0
        for ans in self.answers:
            if ans["ideal"] is True:
                ideal = i
            else:
                pass
            i += 1

        self.shortanswer = [self.answers[ideal - 2],
                            self.answers[ideal - 1],
                            self.answers[ideal],
                            self.answers[ideal + 1],
                            self.answers[ideal + 2]]

    def getResults(self):
        resultslist = []
        for row in self.shortanswer:
            rowlist = [row["ideal"],
                       row["dnom"],
                       int(row["ReynoldsNumber"]),
                       row["Flowregion"],
                       round(row["dP100"], 2),
                       round(row["velocity"], 2)]
            resultslist.append(rowlist)
        return resultslist

    def getHeaders(self):
        headerlist = ["Ideal?", "Nominal Diameter (in)", "Reynold's Number",
                      "Flow Region", "dP / 100 feet", "Velocity (ft/s)"]
        return headerlist
