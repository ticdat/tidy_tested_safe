Files provided.

* `LargeScale3Location.json` - - data file for 200 cities, in list-of-lists json format. Some city pairs are repeated
twice in the distance table, and some aren't, but there is a valid distance for all pairs. Your `solve` routine will 
need to look up the distances with this in mind.

Your repository for this release.

* Extend the `solve` function to actually solve the problem, using `gurobipy` or equivalent. 
  * The solution parameters table should report on the solution objective value, in addition to reporting 
  on the actual assignments and sites opened.
  * Solve tests that use `MIP_for_9_City_Example`.
    * The optimal solution when solving  should have a objective value within 0.1% of
  5.5277e8. This solution should open "New York", "Detroit", "Charlotte" and "Chicago". "Atlanta"
  should be assigned to "Charlotte".
    * The objective value is the same even after removing the "Atlanta" to "Charlotte" record from the 
  `dat` object and re-solving.
    * If you remove both the "Atlanta" to "Charlotte" record and the "Charlotte" to "Atlanta" record
  and re-solve, then the objective value should be larger than  `1.01*5.5277e8`.
  *  The objective value when solving from `LargeScale3Location.json` should be within 0.1% of 5.9109e8. Note
  that you're `solve` function will need to reference the distances table bi-directionally, as 
  `LargeScale3Location.json` does not repeat every distance twice.
* Don't lose the tests from the second release.
* Tag and `__version__` to be "0.0.3".   