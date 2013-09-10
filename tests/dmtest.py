import unittest
from kglobals import DM


class DMTest(unittest.TestCase):

    ClassIsSetup = False
    ClassIsTornDown = False

    def setUp(self):
        # If it was not setup yet, do it
        if not self.ClassIsSetup:
            print "Running Database Manager Tests"
            # run the real setup
            self.setupClass()
            # remember that it was setup already
            self.__class__.ClassIsSetup = True

    def setupClass(self):
        # Do the real setup
        unittest.TestCase.setUp(self)
        # you want to have persistent things to test
        self.__class__.DM = DM
        # (you can call this later with self.myclass)

    def testTableList(self):
        result = self.DM.GetTableList()
        self.assertEqual(result[0][0], "ReferenceFluid")

    def testColumns(self):
        result = self.DM.GetColumns("ReferenceFluid")
        self.assertEqual(result[0], "id")

    def testAddUpdateDelete(self):
        self.myid = self.DM.Add("ReferenceFluid", {"name": "TestFluid"})
        self.DM.Update("ReferenceFluid", self.myid, {"sg": 1.23})
        result = self.DM.Query("ReferenceFluid", row=self.myid)
        self.assertEqual(result["sg"], 1.23)
        self.DM.Delete("ReferenceFluid", self.myid)

    def testQueryAll(self):
        result = self.DM.Query("ReferenceFluid")
        self.assertEqual(result[0]["name"], "AWFI")

    def testQueryRow(self):
        result = self.DM.Query("ReferenceFluid", row=1)
        self.assertEqual(result["viscosity"], 0.7975)

    def testQueryWhere(self):
        result = self.DM.Query("ReferenceFluid", wcol="name", wval="AWFI")
        self.assertEqual(result[0]["id"], 1)
