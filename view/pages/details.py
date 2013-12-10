from PySide import QtGui
from pages import Page

from view.widgets.form import Form


class Details(Page):

    def __init__(self, parent, name):
        super(Details, self).__init__(parent, name)

    def _setup(self):
        self.formlist = [
            {"column": "flowrate",
             "label": "Enter Flowrate (GPM) : ",
             "type": "textenter",
             "value": 50
             },
            {"column": "length",
             "label": "Enter Length of Pipe (feet) : ",
             "type": "textenter",
             "value": 100
             },
        ]

    def _header(self):
        label = QtGui.QLabel('<font size=16 align="center">\
                              NCF Line Sizer</font>')
        label.indent = 20
        self.layout.addWidget(label)

    def _center(self):
        self.form = Form(self.formlist)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(0.5)
        hbox.addLayout(self.form)
        hbox.addStretch(0.5)

        self.layout.addLayout(hbox)
        self.layout.addStretch(1)  # Adds some space between the
                                   # form and the footer buttons

    def _footer(self):
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)

        okbut = QtGui.QPushButton("Calculate", self)
        okbut.released.connect(self.on_ok)
        hbox.addWidget(okbut)

        clearbut = QtGui.QPushButton("Cancel", self)
        clearbut.released.connect(self.on_clear)
        hbox.addWidget(clearbut)

        hbox.addStretch(1)  # Moves boxes to the center,
                            # delete to right justify

        self.layout.addLayout(hbox)
        self.layout.addStretch(1)

    def refresh(self):
        self._setup()
        self.form.clearForm()
        self.layout.update()

    def on_clear(self):
        self.form.clearForm()

    def on_ok(self):
        formdata = self.form.getData()
        self.session.flowrate = formdata["flowrate"]
        self.session.pipelength = formdata["length"]
        self.session.calculate()

        self.PM.ThisPage("Results")
