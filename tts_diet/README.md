### Diet example rendered in Tidy, Tested, Safe format

Example project of how to make a Tidy, Tested, Safe diet example. Although this code is small enough
to be a one file engine, we are demonstrating a simple package format for educational purposes.

This example requires `gurobipy` to solve, but the schemas can still be examined even if `gurobipy` is not
installed.   

We also include a very simple `setup.py` file, so that the `tts_diet` package can be distributed as a 
.whl file.

* **tidy** The engine is organized as a package, or is one single file. The code is organized into public 
           and private sections (this example is too small to have the latter). 
* **tested** There is a testing section for the engine that uses `unittest` (or something similar, like 
             `pytest`) to validate the behavior of the engine. Using a tool like `coverage` with the testing
             section will create a report demonstrating that the testing code exercises close to 100% of the 
             production code.
* **safe** The `solve` function fully validates the input data for data integrity problems. This is not to say 
           that infeasibile models are always pre-diagnosed (analyzing feasibility is mathematically the same
           as analyzing optimality) but all mathematically trivial data issues are discovered prior to 
           perfoming true optimization.
           

### Contents
* `tts_diet` The subdirectory that defines the `tts_diet` package.
* `test_tts_diet` The subdirectory that contains data and code required for testing `tts_diet`.
* `setup.py` Standard file for distributing `tts_diet`. Note that `gurobipy` is **not** specified as a requirement,
             as `tts_diet` can still provide partial functionality in its absence.


