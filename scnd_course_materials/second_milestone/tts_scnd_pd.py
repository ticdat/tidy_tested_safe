from ticdat import PanDatFactory
input_schema = PanDatFactory(cities=[["Name"],["Demand"]],
                             distances=[["Source", "Destination"], ["Distance"]],
                             parameters=[["Parameter"], ["Value"]])

input_schema.add_parameter("Number of Centroids", default_value=3, inclusive_min=False, inclusive_max=False, min=0,
                            max=float("inf"), must_be_int=True)
input_schema.set_data_type("cities", "Demand", min=0, max=float("inf"), inclusive_min=True, inclusive_max=False)
input_schema.set_data_type("distances", "Distance", min=0, max=float("inf"), inclusive_min=True, inclusive_max=False)
input_schema.add_foreign_key("distances", "cities", ['Source', 'Name'])
input_schema.add_foreign_key("distances", "cities", ['Destination', 'Name'])

# The distance matrix is bi-directionally safe. I.e. if the same source/dest and dest/source exist then the
# distances must match. If only one is present, it can fall back to the other in the code.
def _distance_matrix(dat):
    return {"distance_matrix": {tuple(row[:2]): row[2] for row in dat.distances.itertuples(index=False)}}
input_schema.add_data_row_predicate("distances", predicate_name="Check Bi-Directionally Safe",
    predicate=lambda row, distance_matrix: ((row["Destination"], row["Source"]) not in distance_matrix) or
                                            (row["Distance"] == distance_matrix[row["Destination"], row["Source"]]),
    predicate_kwargs_maker=_distance_matrix)

solution_schema = PanDatFactory(openings=[['City'],[]], assignments=[['City', 'Assigned To'],[]],
                                parameters=[["Parameter"], ["Value"]])

def solve(dat):
    assert input_schema.good_pan_dat_object(dat), "bad dat check"
    assert not input_schema.find_duplicates(dat), "duplicate row check"
    assert not input_schema.find_foreign_key_failures(dat), "foreign key check"
    assert not input_schema.find_data_type_failures(dat), "data type value check"
    assert not input_schema.find_data_row_failures(dat), "data row check"
