from PySide.QtGui import QGridLayout, QLabel, QFrame


class LabelGrid(QGridLayout):
    def __init__(self, headerlist, resultslist):
        super(LabelGrid, self).__init__()
        self.setContentsMargins(20, 20, 20, 20)
        self.setSpacing(10)
        self.maxcols = len(headerlist)
        self.headerlist = headerlist
        self.resultslist = resultslist
        self.r = 0
        self.c = 0
        self.labellist = []
        self.setHorizontalSpacing(0)

    def build(self):
        for name in self.headerlist:
            label = QLabel('<b><font align="center">%s</font></b>' % name)
            self.labellist.append(label)
            label.setMargin(2)
            label.setFrameStyle(QFrame.Box | QFrame.Plain)
            label.setLineWidth(1)
            self.addWidget(label, self.r, self.c)
            self.c += 1

        self.c = 0
        self.r += 1

        for row in self.resultslist:
            for name in row:
                label = QLabel('<font align="center">%s</font>' % name)
                self.labellist.append(label)
                label.setMargin(2)
                label.setFrameStyle(QFrame.Box | QFrame.Plain)
                label.setLineWidth(1)
                self.addWidget(label, self.r, self.c)
                if self.c == self.maxcols - 1:
                    self.c = 0
                    self.r += 1
                else:
                    self.c += 1

    def clearall(self):
        for label in self.labellist:
            label.setParent(None)
        del self.labellist
        self.labellist = []
        self.r = 0
        self.c = 0

    def Update(self, headerlist, resultslist):
        self.clearall()
        self.headerlist = headerlist
        self.resultslist = resultslist
        self.build()
