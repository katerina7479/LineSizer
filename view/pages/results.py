from PySide import QtGui
from pages import Page
from view.widgets.labelgrid import LabelGrid
from kglobals import SS


class ResultsPage(Page):
    # I use this as a "dashboard", to quickly make an initial selection, like opening
    # an existing project.
    def __init__(self, parent, name):
        self.SS = SS
        super(ResultsPage, self).__init__(parent, name)

    def _setup(self):
        self.headerlist = self.SS.getHeaders()
        self.resultslist = self.SS.getResults()

        self.input1text = 'Fluid = %s, Pipe = %s' % (self.SS.fluid.name, self.SS.pipe.quality)
        self.input2text = 'Flowrate = %s, PipeLength = %s' % (self.SS.flowrate, self.SS.pipe.length)

    def _header(self):
        label = QtGui.QLabel(
            '<font size=16 align="center">Results: </font>')
        label.indent = 20
        self.layout.addWidget(label)

        self.inputs1 = QtGui.QLabel(self.input1text)
        self.inputs1.indent = 40
        self.layout.addWidget(self.inputs1)

        self.inputs2 = QtGui.QLabel(self.input2text)
        self.inputs2.indent = 40
        self.layout.addWidget(self.inputs2)

    def _center(self):
        self.grid = LabelGrid(self.headerlist, self.resultslist)
        self.grid.build()
        self.layout.addLayout(self.grid)

    def _footer(self):
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)

        okbut = QtGui.QPushButton("Generate Report", self)
        okbut.released.connect(self.on_report)
        hbox.addWidget(okbut)

        clearbut = QtGui.QPushButton("Exit", self)
        clearbut.released.connect(self.on_exit)
        hbox.addWidget(clearbut)

        hbox.addStretch(1)  # Moves boxes to the center, delete to right justify

        self.layout.addLayout(hbox)
        self.layout.addStretch(1)

    def refresh(self):
        self.grid.clearall()
        self._setup()
        self.inputs1.setText(self.input1text)
        self.inputs2.setText(self.input2text)
        self.grid.Update(self.headerlist, self.resultslist)
        self.show()

    def on_open_page(self, pageid):
        if pageid is 0:
            self.PM.ThisPage("FormPage")
        else:
            self.PM.ThisPage("TableBoxPage")

    def on_report(self):
        print "Generating Report"
        self.SS.MakeReport()

    def on_exit(self):
        self.PM.Quit()
