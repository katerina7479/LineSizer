import unittest
from model.reference_fluid import ReferenceFluid


class FluidTest(unittest.TestCase):
    # First define a class variable that determines
    # if setUp was ever run
    ClassIsSetup = False

    def setUp(self):
        # If it was not setup yet, do it
        if not self.ClassIsSetup:
            print "Running ReferenceFluid Tests"
            # run the real setup
            self.setupClass()
            # remember that it was setup already
            self.__class__.ClassIsSetup = True

    def setupClass(self):
        # Do the real setup
        unittest.TestCase.setUp(self)
        # you want to have persistent things to test
        self.__class__.fluid = ReferenceFluid("Water", 1.0, 1.0, 20)
        # (you can call this later with self.myclass)

    def testName(self):
        result = self.fluid.name
        self.assertEqual(result, "Water")

    def testSG(self):
        result = self.fluid.sg
        self.assertEqual(result, 1.0)

    def testViscosity(self):
        result = self.fluid.viscosity
        self.assertEqual(result, 1.0)

    def testTempC(self):
        result = self.fluid.tempC
        self.assertEqual(result, 20)

    def testTempF(self):
        result = self.fluid.tempF
        self.assertEqual(result, 68.0)
