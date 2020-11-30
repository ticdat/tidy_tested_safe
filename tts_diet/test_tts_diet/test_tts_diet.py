import os
import inspect
import tts_diet
import unittest

def _this_directory() :
    return os.path.dirname(os.path.realpath(os.path.abspath(inspect.getsourcefile(_this_directory))))

def get_test_data(filename):
    path = os.path.join(_this_directory(), "data", filename)
    assert os.path.exists(path) and os.path.isfile(path), f"bad filename {filename}"
    # right now assumes testing data is stored as json files
    return tts_diet.input_schema.json.create_tic_dat(path)

def _nearly_same(x, y, epsilon=1e-5):
    if x == y or max(abs(x), abs(y)) < epsilon:
        return True
    if min(abs(x), abs(y)) > epsilon:
        return abs(x-y) /  min(abs(x), abs(y)) < epsilon

def _smaller(x, y, epsilon=1e-5):
    return x < y and not _nearly_same(x, y, epsilon)

class TestDiet(unittest.TestCase):
    # This is a pretty simple test suite - just one data set. But the template should be clear for how you could
    # archive many useful data sets for validating your optimization engine.
    def test_standard_data_set(self):
        dat = get_test_data("standard_data_set.json")
        sln = tts_diet.solve(dat)
        self.assertTrue(_nearly_same(11.82886, sln.parameters["Total Cost"]["Value"], epsilon=1e-4))
        # The test_ subroutine can stop here and still be a good test. The rest of the subroutine
        # demonstrates how you can validate the objective function is being handled by the optimization
        most_eaten = sorted(sln.buy_food, key= lambda f: sln.buy_food[f]["Quantity"], reverse=True)[0]
        dat.foods[most_eaten]["Cost"] *= 10
        sln2 =  tts_diet.solve(dat)
        self.assertTrue(_smaller(11.82886, sln2.parameters["Total Cost"]["Value"]))
        self.assertTrue(most_eaten not in sln2.buy_food or
                        _smaller(sln2.buy_food[most_eaten]["Quantity"], sln.buy_food[most_eaten]["Quantity"]))

# Run the tests via the command line
if __name__ == "__main__":
    unittest.main()