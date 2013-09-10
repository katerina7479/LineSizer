import unittest
from model.reference_pipe import ReferencePipe


class RefPipeTest(unittest.TestCase):
    # First define a class variable that determines
    # if setUp was ever run
    ClassIsSetup = False

    def setUp(self):
        # If it was not setup yet, do it
        if not self.ClassIsSetup:
            print "Running Reference Pipe Tests"
            # run the real setup
            self.setupClass()
            # remember that it was setup already
            self.__class__.ClassIsSetup = True

    def setupClass(self):
        # Do the real setup
        unittest.TestCase.setUp(self)
        # you want to have persistent things to test
        self.__class__.refpipe = ReferencePipe("1 inch Tube", "tubing", 1.0, 0.87)
        # (you can call this later with self.myclass)

    def testName(self):
        result = self.refpipe.name
        self.assertEqual(result, "1 inch Tube")

    def testQuality(self):
        result = self.refpipe.quality
        self.assertEqual(result, "tubing")

    def testDnomInch(self):
        result = self.refpipe.dnom_in
        self.assertEqual(result, 1.0)

    def testDnom_mm(self):
        result = self.refpipe.dnom_mm
        self.assertEqual(result, 25.4)

    def testDactInch(self):
        result = self.refpipe.dact_in
        self.assertEqual(result, 0.87)

    def testDact_mm(self):
        result = self.refpipe.dact_mm
        self.assertEqual(result, 22.1)