Files provided.

* `MIP_for_9_City_Example.json` - data file for 9 cities. The list-of-lists format used here can be ingested
   by both `PanDatFactory` and `TicDatFactory`.
* `tts_scnd.py` - core file for `tts_scnd` package, using `TicDatFactory`. Does nothing
beyond validating input data.
* `tts_scnd_pd.py` - Same as `tts_scnd.py`, except using `PanDatFactory`.

Your repository for this release. (Look [here](https://github.com/ticdat/tts_diet), 
[here](https://github.com/ticdat/tts_netflow_a) and [here](https://github.com/ticdat/tts_netflow_b) for examples).

* `tts_scnd` repository that implements `tts_scnd` package.
* Your `test_tts_scnd` directory implements unit tests for `tts_scnd`.
* Your single unit test validates that `tts_scnd.solve`, when run with the data in 
`MIP_for_9_City_Example.json`, doesn't throw any asserts. Since you can assume your unit 
tests are being run with asserts enabled, all you need to do is call `tts_scnd.solve(dat)`, 
where `dat` is created from `MIP_for_9_City_Example.json`.
* Your `notebooks` directory includes a notebook that converts `MIP_for_9_City_Example.json` to an
Excel file or a directory of csv files. This is so a user can interact more naturally with your sample data.
* Don't forget the `.gitignore` file and the `setup.py` file. 
* Tag and `__version__` to be "0.0.1".