from reportlab.pdfgen import canvas
from datetime import datetime


class Reporter(object):
    def __init__(self, path):
        print path
        filename = self._generatename()
        c = canvas.Canvas(path + "\\reports\\%s.pdf" % filename)
        c.drawString(100, 100, "Hello World")
        c.showPage()
        c.save()

    def _generatename(self):
        d = datetime.now()
        cleandate = "%s%s_%s%s%s" % (d.month, d.day, d.hour, d.minute, d.second)
        name = "LineSizer_%s" % cleandate
        return name

    def addTitle(self):
        pass

    def addInputs(self, fluid, pipe):
        pass

    def addGrid(self, header, results):
        pass

    def make(self):
        pass


if __name__ == "__main__":
    R = Reporter()
