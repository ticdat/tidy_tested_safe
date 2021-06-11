Files provided.

* `tts_scnd.py` - same as `first_release\tts_scnd.py`, except bi-directional row predicate 
check added.
* `tts_scnd_pd.py`  - same as `first_release\tts_scnd_pd.py`, except bi-directional row predicate 
check added.

Your repository for this release.

* Extend the unit tests to validate that bi-directional safety is enforced. 
  * Create
`dat` from `MIP_for_9_City_Example.json`.
  * Edit `dat.distances` so that there is a city pair that looks up two different distances depending on which city is the source. 
  * Check that this `dat` object will throw the `"data row check"` exception on `solve`. This requires using `try\except`.
    Be careful to write the check in such a way that the unit test validates that the exception
    is thrown, and also that the thrown exception is the `"data row check"`. It's fine 
    to convert the exception to a string after you capture it ... everything in Python can be converted
    to a string.
* Don't lose the test from the first release.
* Tag and `__version__` to be "0.0.2". 
