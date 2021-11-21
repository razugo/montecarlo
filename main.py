from lib.simulation import Simulation
from lib.configuration import START_DATE, END_DATE


simulation = Simulation(START_DATE, END_DATE)
simulation.run_simulation()
simulation.sort_simulation()
print(simulation.results)

simulation.save_as_csv()
simulation.visualize_data()
