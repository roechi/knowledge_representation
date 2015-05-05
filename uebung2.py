#Loesung fuer 2 a.) fertig

import numpy as np

import agents

runs = np.array(range(100))

print "\n+++TrivialVacuumEnvironment+++\n"


for key, value in enumerate(runs):
    reflex_vacuum_agent = agents.ReflexVacuumAgent()
    vacuum_environment = agents.TrivialVacuumEnvironment()
    vacuum_environment.add_thing(reflex_vacuum_agent)
    vacuum_environment.run(10)
    runs[key] = reflex_vacuum_agent.performance

print "\nReflexVacuumAgent:\n"
print runs
print("\n\nAverage: " + str(runs.mean()))

for key, value in enumerate(runs):
    model_vacuum_agent = agents.ModelBasedVacuumAgent()
    vacuum_environment = agents.TrivialVacuumEnvironment()
    vacuum_environment.add_thing(model_vacuum_agent)
    vacuum_environment.run(10)
    runs[key] = model_vacuum_agent.performance

print "\nModelBasedVacuumAgent:\n"
print(runs)
print("\n\nAverage: " + str(runs.mean()))
