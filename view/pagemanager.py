from PySide.QtGui import QStackedWidget
from pages.blank import BlankPage
from pages.newpage import NewPage
from pages.details import Details
from pages.results import ResultsPage


class PageManager(QStackedWidget):
    def __init__(self, *args):
        super(PageManager, self).__init__()
        self.widgetdict = {}
        self.pagedict = {"Blank": BlankPage,
                         "NewPage": NewPage,
                         "Details": Details,
                         "Results": ResultsPage
                         }
        self.keylist = []
        self.index = 0
        self._setup()

    def _setup(self):
        self.ThisPage("NewPage")

    def _AddPage(self, key):
        cls = self.pagedict[key]
        self.widgetdict[key] = cls(self, key)
        self.addWidget(self.widgetdict[key])
        self.setCurrentWidget(self.widgetdict[key])

    def _SetPage(self, key):
        if key in self.widgetdict:
            self.PageRefresh(self.widgetdict[key])
            self.setCurrentWidget(self.widgetdict[key])
        else:
            self._AddPage(key)

    def ThisPage(self, key):
        maxindex = len(self.keylist) - 1
        if self.index < maxindex:
            self.keylist = self.keylist[0:(self.index+1)]
        else:
            pass
        self.keylist.append(key)
        self.index = len(self.keylist) - 1
        self._SetPage(key)

    def LastPage(self):
        self.index = self.index - 1
        if self.index < 0:
            self.index = 0
        key = self.keylist[self.index]
        self._SetPage(key)

    def NextPage(self):
        self.index = self.index + 1
        maxindex = len(self.keylist) - 1
        if self.index > maxindex:
            self.index = maxindex
        key = self.keylist[self.index]
        self._SetPage(key)

    def PageRefresh(self, widget):
        widget.refresh()

    def Quit(self):
        parent = self.parent()
        parent.on_quit()
