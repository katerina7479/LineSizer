from PySide import QtGui
from pages import Page

from view.widgets.form import Form
from kglobals import SS


class NewPage(Page):

    def __init__(self, parent, name):
        super(NewPage, self).__init__(parent, name)
        self.SS = SS

    def _setup(self):
        self.fluidlist = self.SS.fluidlist
        self.qualitylist = self.SS.qualitylist

        self.formlist = [
            {"column": "fluid_id",
             "label": "Select Fluid: ",
             "type": "combobox",
             "list": self.fluidlist,
             "value": 4
             },
            {"column": "quality_id",
             "label": "Select Quality of Pipe: ",
             "type": "combobox",
             "list": self.qualitylist,
             "value": 1
             }]

    def _header(self):
        label = QtGui.QLabel('<font size=16 align="center">Non-Compressible Fluid Line Sizer</font>')
        label.indent = 20
        self.layout.addWidget(label)

    def _center(self):
        self.form = Form(self.formlist)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(0.5)
        hbox.addLayout(self.form)
        hbox.addStretch(0.5)

        self.layout.addLayout(hbox)
        self.layout.addStretch(1)  # Adds some space between the form and the footer buttons

    def _footer(self):
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)

        okbut = QtGui.QPushButton("Ok", self)
        okbut.released.connect(self.on_ok)
        hbox.addWidget(okbut)

        clearbut = QtGui.QPushButton("Cancel", self)
        clearbut.released.connect(self.on_clear)
        hbox.addWidget(clearbut)

        hbox.addStretch(1)  # Moves boxes to the center, delete to right justify

        self.layout.addLayout(hbox)
        self.layout.addStretch(1)

    def refresh(self):
        self._setup()
        self.form.UpdateComboLists([self.fluidlist, self.qualitylist])
        self.layout.update()

    def on_clear(self):
        self.form.clearForm()

    def on_ok(self):
        formdata = self.form.getData()
        self.SS.quality = formdata["quality_id"]
        self.SS.fluid = formdata["fluid_id"]

        self.PM.ThisPage("Details")
