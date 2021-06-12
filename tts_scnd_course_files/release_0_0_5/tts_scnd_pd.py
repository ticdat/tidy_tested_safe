from ticdat import PanDatFactory
input_schema = PanDatFactory(cities=[["Name"],["Demand", "Max Assignment Capacity"]],
                             distances=[["Source", "Destination"], ["Distance"]],
                             parameters=[["Parameter"], ["Value"]])

input_schema.add_parameter("Number of Centroids", default_value=4, inclusive_min=False, inclusive_max=False, min=0,
                            max=float("inf"), must_be_int=True)
input_schema.add_parameter("High Service Distance", default_value=0, inclusive_min=True, inclusive_max=True, min=0,
                            max=float("inf"), must_be_int=False)
input_schema.add_parameter("Maximum Average Service Distance", default_value=float("inf"), inclusive_min=True,
                           inclusive_max=True, min=0, max=float("inf"), must_be_int=False)
input_schema.add_parameter("Minimum Percent High Service Demand", default_value=0, inclusive_min=True,
                           inclusive_max=True, min=0, max=100, must_be_int=False)
input_schema.add_parameter("Maximum Individual Service Distance", default_value=float("inf"), inclusive_min=False,
                           inclusive_max=True, min=0, max=float("inf"), must_be_int=False)
input_schema.add_parameter("Objective", "Minimize Average Service Distance",
    strings_allowed=["Minimize Average Service Distance", "Maximize Percent High Service Demand"],
    number_allowed=False)
input_schema.set_data_type("cities", "Demand", min=0, max=float("inf"), inclusive_min=True, inclusive_max=False)
input_schema.set_data_type("cities", "Max Assignment Capacity", min=0, max=float("inf"),
                           inclusive_min=True, inclusive_max=True)
input_schema.set_default_value("cities", "Max Assignment Capacity", float("inf"))
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