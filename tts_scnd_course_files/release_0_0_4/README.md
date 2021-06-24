Files provided.

* `tts_scnd.py` - Only provides the new `input_schema`, which is the same as the 0.0.3 `input_schema`, 
  except with 5 new parameters.
* `tts_scnd_pd.py`  -  Same as `tts_scnd.py`, except using `PanDatFactory`.

Your repository for this release.

* Extend the `solve` function so that the solution reports on two KPIs in the `parameters` solution table.
  * "Percent High Service Demand" - the percentage of demand thats fulfilled with high service.
  * "Average Service Distance" - the average service distance (weighted by demand).
* Extend the `solve` function to implement the 5 new parameters. (Don't use true equality checking below, only check
4 most significant digits).
* Extend the unit tests to test this new functionality.
  * Test "Maximum Individual Service Distance" like this.
    * Solve the "MIP_for_9_City_Example.json" data set.
    * Validate that the "Average Service Distance" of this solution is 36.57.
    * Find the largest distance used in that solution. Call this `max_used`.
    * Re-solve the  "MIP_for_9_City_Example.json" data set, except applying a "Maximum Individual Service Distance"
    of `0.999*max_used`.
    * The "Average Service Distance" for this second solution should be 83.42.
    * The largest distance used in this second solution should be no bigger than `0.999*max_used`.
  * Test "Objective" and "High Service Distance" like this. 
    * Solve the "LargeScale3Location.json" data set with a "High Service Distance" of 250.
    * Validate that the "Average Service Distance" of this solution is 239.8.
    * Validate that the "Percent High Service Demand" is below 60.
    * Re-solve, except with the "Objective" set to "Maximize Percent High Service Demand".
    * Validate that the "Average Service Distance" is now larger than 260.
    * Validate that the "Percent High Service Demand" is now 61.50. 
  * Test "Minimum Percent High Service Demand" and "Maximize Percent High Service Demand" like this.
     * Create a solution from "LargeScale3Location.json" with "High Service Distance" of 250, 
       "Objective" of "Minimize Average Service Distance", and "Minimum Percent High Service Demand" of 61.15.
     * Create a second solution from "LargeScale3Location.json" with "High Service Distance" of 250, 
       "Objective" of "Maximize Percent High Service Demand", and "Maximum Average Service Distance" of 256.6.
     * Validate that both of these solutions have 'Percent High Service Demand' of 61.15 and 
       "Average Service Distance" of 256.5.
* Don't lose the tests from the previous release. However, be aware that the new `solve` will, by default
be minimizng the average service distance and not the total sku-miles. Therefore, numbers like 
552775000 and 591087305 need to be scaled by the total demand of the `dat` object being solved.
* Tag and `__version__` to be "0.0.4". 
