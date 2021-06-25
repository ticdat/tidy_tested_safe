Files provided.

 * `tts_scnd.py` - Only providing the new `input_schema` and `solution_schema`.  You will build `solve`.
 * `tts_scnd_pd.py` - Same as `tts_scnd.py`, except using `PanDatFactory`.
 
 Your repository for this release. 
 
 * Implement the new `solve` function.
   * The solution parameters table should report on three KPIs - "Percent High Service Demand",
   "Total Cost" and "Average Service Distance".
   * More details in chapter 10.
 * Forward convert the testing data. 
   * Details on the forward conversion logic farther down.
   * Both `LargeScale3Location.json` and `MIP_for_9_City_Example.json` should forward convert.
 * Edit the `test_tts_scnd.py` appropriately.
   * The `try/except` test you added in release 0.0.2 is no longer relevant, as the lane tables aren't
   bi-directionally safe.
   * **Don't** retain the test that the `MIP_for_9_City_Example` total cost solution is the 
   same even after removing "Atlanta" to "Charlotte". It's no longer relevant since there the warehouse 
   to customer tables aren't bi-directionally safe.
   * All the other tests carry forward in a straightforward way.
     * The test you added in release 0.0.3 that involved removing both "Atlanta" to "Charlotte" and 
     "Charlotte" to "Atlanta" for `MIP_for_9_City_Example` is still relevant. If there is no way
     for the Atlanta customer to be assigned to the Charlotte warehouse, nor vice-versa, then the solution 
      average service distance should be larger than `1.01*5.5277e8` divided by the total demand.
   * Add the sequence of tests involving the `100_big_cities.json` file detailed below.
   
### Forward conversion of testing data 

The two input schema changes significantly between 0.0.5 and 0.0.6. Technically, 0.0.5 `solve`
doesn't fully reduce to the 0.0.6 `solve`, because 0.0.5 can support bi-direction shipment information
and 0.0.6 can't. That said, we can bear this in mind to make sure both of the 0.0.5 data sets
forward convert accurately. 

Here is a summary of the 0.0.5->0.0.6 forward conversion logic.
* The "Number of Centroids" parameter in 0.0.5 data is a "Number of Warehouses" parameter for 0.0.6.
* The 0.0.6 `dat` object gets a single product record. 
  * For simplicity, lets assume this is product `"P"`.
  * Product `"P"` needs a Warehouse Volume of 1.
* For each record of the 0.0.5 cities table...
   * Create a plant with the same name.
     * Create a supply record for the plant you just created and product `"P"` with a supply of 
     infinity.
   * Create a warehouse with the same name, a Fixed Cost of zero, and the same Max Assignment Capacity.
   * Create a customer with the same name.
     * Create a demand record for the customer you just created and product `"P"` with a demand the
   same as the cities record.
 * For each record of the distances table.
   * Create matching record in the `warehouse_to_customer_distances` table with the same source, 
   destination and distance.
   * Create a record in `warehouse_to_customer_costs` table with the same source and destination, 
   with the product `"P"`, and with cost of zero.
   * Because the 0.0.5 `solve` enforced bi-directionally on the distances table, and the
   0.0.6 `solve` does no such thing, we need to create the same two new records again for 
   `warehouse_to_customer_distances` and `warehouse_to_customer_costs`, except with source and 
   destination reversed. 
 * For each pair of cities, create a `plant_to_warehouse_costs` record with cost of zero.
 * This was all fairly involved, so don't forget to look for 0.0.6 foreign key failures, 
 data type failures, and data row failures before overwriting. 
 
### Full sequence of  100_big_cities.json tests
* Solution from the original data set.
  * The total cost should be within 0.1% of 7.834e5.
  * Both Carmel and Wilmington should be among the warehouses opened.
* Edit the original data set so that Carmel and Wilmington both have Max Assignment Capacity
of 40000 and re-solve.
  * The total cost should now be within 0.1% of 8.0591e5.
  * Carmel should be among the warehouses opened with an Assignment Volume larger than 39900.
* Retaining the previous edits, set the supply of Trenton for each product to be 20000 and
re-solve.
  * The total cost should now be within 0.1% of 8.1226e5.
  * The average service distance should be greater than 375.
  * Carmel should be among the warehouses opened with an Assignment Volume larger than 39900.
  * Trent should produce between  19000 and 20000 units for every product.
* Retaining the previous edits, set the Maximum Average Service Distance parameter to be 375 and re-solve.
  * The total cost should now be within 0.1% of 8.1346e5.
  * The average service distance should be no greater than 375.
  * Carmel should be among the warehouses opened with an Assignment Volume smaller than 39900.
* Retaining the previous edits, set the Warehouse Volume of p1 to be 10 and re-solve.
  * The total cost should now be within 0.1% of 8.4463e5.
  * Carmel should be among the warehouses opened with an Assignment Volume larger than 39900.
 * All these edits should be in memory, as part of the `test` subroutine. You should only have one copy
 of the `100_big_cities.json ` file in the repository.
   
`