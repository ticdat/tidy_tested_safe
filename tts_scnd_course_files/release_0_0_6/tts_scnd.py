from ticdat import TicDatFactory

input_schema = TicDatFactory(plants=[["Name"],[]],
                             warehouses=[["Name"], ["Max Assignment Capacity", "Fixed Cost"]],
                             customers=[["Name"], []],
                             products=[["Name"], ["Warehouse Volume"]],
                             demand=[["Customer", "Product"], ["Demand"]],
                             supply=[["Plant", "Product"], ["Supply"]],
                             plant_to_warehouse_costs=[["Plant", "Warehouse", "Product"], ["Cost"]],
                             warehouse_to_customer_costs=[["Warehouse", "Customer", "Product"], ["Cost"]],
                             warehouse_to_customer_distances=[["Warehouse", "Customer"], ["Distance"]],
                             parameters=[["Parameter"], ["Value"]])

input_schema.add_parameter("Number of Warehouses", default_value=4, inclusive_min=False, inclusive_max=False, min=0,
                            max=float("inf"), must_be_int=True)
input_schema.add_parameter("High Service Distance", default_value=0, inclusive_min=True, inclusive_max=True, min=0,
                            max=float("inf"), must_be_int=False)
input_schema.add_parameter("Maximum Average Service Distance", default_value=float("inf"), inclusive_min=True,
                           inclusive_max=True, min=0, max=float("inf"), must_be_int=False)
input_schema.add_parameter("Minimum Percent High Service Demand", default_value=0, inclusive_min=True,
                           inclusive_max=True, min=0, max=100, must_be_int=False)
input_schema.add_parameter("Maximum Individual Service Distance", default_value=float("inf"), inclusive_min=False,
                           inclusive_max=True, min=0, max=float("inf"), must_be_int=False)
input_schema.add_parameter("Maximum Total Cost", default_value=float("inf"), inclusive_min=True,
                           inclusive_max=True, min=0, max=float("inf"), must_be_int=False)
input_schema.add_parameter("Objective", "Minimize Average Service Distance",
    strings_allowed=["Minimize Average Service Distance", "Maximize Percent High Service Demand", "Minimize Total Cost"],
    number_allowed=False)
input_schema.set_data_type("warehouses", "Fixed Cost", min=0, max=float("inf"), inclusive_min=True, inclusive_max=False)
input_schema.set_data_type("warehouses", "Max Assignment Capacity", min=0, max=float("inf"),
                           inclusive_min=True, inclusive_max=True)
input_schema.set_default_value("warehouses", "Max Assignment Capacity", float("inf"))
input_schema.set_data_type("products", "Warehouse Volume", min=0, max=float("inf"),
                           inclusive_min=False, inclusive_max=False)
input_schema.set_default_value("products", "Warehouse Volume", 1)
input_schema.set_data_type("demand", "Demand", min=0, max=float("inf"), inclusive_min=True, inclusive_max=False)
input_schema.set_data_type("supply", "Supply", min=0, max=float("inf"), inclusive_min=True, inclusive_max=True)
input_schema.set_default_value("supply", "Supply", float("inf"))
input_schema.set_data_type("plant_to_warehouse_costs", "Cost", min=0, max=float("inf"), inclusive_min=True,
                           inclusive_max=False)
input_schema.set_data_type("warehouse_to_customer_costs", "Cost", min=0, max=float("inf"), inclusive_min=True,
                           inclusive_max=False)
input_schema.set_data_type("warehouse_to_customer_distances", "Distance", min=0, max=float("inf"), inclusive_min=True,
                           inclusive_max=False)
input_schema.add_foreign_key("demand", "customers", ["Customer", "Name"])
input_schema.add_foreign_key("demand", "products", ["Product", "Name"])
input_schema.add_foreign_key("supply", "plants", ["Plant", "Name"])
input_schema.add_foreign_key("supply", "products", ["Product", "Name"])
input_schema.add_foreign_key("plant_to_warehouse_costs", "plants", ["Plant", "Name"])
input_schema.add_foreign_key("plant_to_warehouse_costs", "warehouses", ["Warehouse", "Name"])
input_schema.add_foreign_key("plant_to_warehouse_costs", "products", ["Product", "Name"])
input_schema.add_foreign_key("warehouse_to_customer_distances", "customers", ["Customer", "Name"])
input_schema.add_foreign_key("warehouse_to_customer_distances", "warehouses", ["Warehouse", "Name"])
input_schema.add_foreign_key("warehouse_to_customer_costs", "products", ["Product", "Name"])
input_schema.add_foreign_key("warehouse_to_customer_costs", "warehouse_to_customer_distances",
                             [["Warehouse", "Warehouse"], ["Customer", "Customer"]])

solution_schema = TicDatFactory(warehouses_opened=[['Warehouse'], ["Fixed Cost", "Assignment Volume"]],
                                plant_to_warehouse_shipments=[["Plant", "Warehouse", "Product"],
                                                              ["Units Shipped", "Shipment Cost"]],
                                warehouse_to_customer_shipments=[["Warehouse", "Customer", "Product"],
                                                                 ["Units Shipped", "Shipment Cost"]],
                                production=[["Plant", "Product"], ["Units Produced"]],
                                parameters=[["Parameter"], ["Value"]])