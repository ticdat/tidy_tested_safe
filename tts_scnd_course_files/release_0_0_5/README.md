Files provided.

* `tts_scnd.py` - Only provides the new `input_schema`, which is the same as the 0.0.3 `input_schema`
except adding the "Max Assignment Capacity" field to the cities table. 
  * Note how we set data type and default value for this new field. If you're using 
  `TicDatFactory`, then the default value makes it easier to forward convert the data due to 
  default dict functionality like [this](https://github.com/ticdat/ticdat/wiki/ticdat-defaultdict-enhancements)
* `tts_scnd_pd.py`  -  Same as `tts_scnd.py`, except using `PanDatFactory`.

Your repository for this release.

* Extend the `solve` function to implement the Max Assignment Capacity constraint for each city.
  * Specifically, if cities *a*, *b*, and *c* are assigned to city *d*, then the sum total demand 
  of *a*, *b* and *c* can't exceed the Max Assignment Capacity of *d*. 
* Forward convert the testing data. 
  * That is to say, the data sets archived for the 0.0.4 release don't have the "Max Assignment Capacity"
  field as part of the cities table. Add this field to the cities table for all of the archived data 
  sets. Populate this new field with `float(inf)`, since the tests associated with these 
  data sets all assume no restriction on assignment capacity.
  * If you need a demonstration of how to forward convert testing data, please study the 
  [tts_netflow_a](https://github.com/ticdat/tts_netflow_a) and 
  [tts_netflow_b](https://github.com/ticdat/tts_netflow_b) repos.
  * Your repo needs to include the code you used to forward convert the testing data. This can be a notebook
  in a `notebooks` directory (as demonstrated in the `tts_netflow_` repos referenced above) or as code
  somewhere in the `test_tts_scnd` directory.
* Extend the unit tests to test the new functionality.
  * Solve the "LargeScale3Location.json" file, except with every city having a Max Assignment Capacity
  of 823400. 
  * Validate that the resulting solution has an Average Service Distance that is larger than 
  242 and smaller than 242.2.  
* Don't lose the tests from the previous release. So long as your forward conversion worked, 
* Tag and `__version__` to be "0.0.5". 
