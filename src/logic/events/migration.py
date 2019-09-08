import random
import numpy as np
from util import global_config


def run(world, generation):
    prob = global_config.get_var('migration.probability')
    for pop in world.populations:
        if np.random.binomial(pop.size, prob) <= 0:
            continue
        destination = randomize_destination(pop, world)
        migrate_tools(pop, destination)
        pass


def migrate_tools(origin, destination):
    tool_adoption_prob = global_config.get_var('migration.tool_adoption_probability')
    max_adopted_tools = global_config.get_var('migration.max_tools')
    adopted_tools_count = min(max_adopted_tools, np.random.binomial(len(origin.tools), tool_adoption_prob))
    adopted_tools = random.sample(list(origin.tools), adopted_tools_count)
    print("Migration occurred from %s to %s, who adopted tools: [%s]" % (origin.id, destination.id, ','.join(adopted_tools)))
    destination.adopt_tools(adopted_tools)


def randomize_destination(pop, world):
    destinations = world.populations.copy()
    destinations.remove(pop)
    return random.sample(destinations, 1)[0]
