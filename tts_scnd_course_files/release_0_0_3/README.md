Files provided.

* `LargeScale3Location.json` - - data file for 200 cities, in list-of-lists json format. Some city pairs are repeated
twice in the distance table, and some aren't, but there is a valid distance for all pairs. Your `solve` routine will 
need to look up the distances with this in mind.

Your repository for this release.

* Extend the `solve` function to actually solve the problem, using `gurobipy` or equivalent.
  * Solve tests that use `MIP_for_9_City_Example`.
    * The optimal solution when solving  should have a total cost within 0.1% of
  552775000.
    * The total cost is the same even after removing the "Atlanta" to "Charlotte" record from the 
  `dat` object and re-solving.
    * If you remove both the "Atlanta" to "Charlotte" record and the "Charlotte" to "Atlanta" record
  and re-solve, then the total cost should be larger than  `1.01*552775000`.
  *  The total cost when solving from `LargeScale3Location.json` should be within 0.1% of 591087305.
* Don't lose the tests from the second release.
* Tag and `__version__` to be "0.0.3".   