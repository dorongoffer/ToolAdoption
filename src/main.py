import json

from model.world import World
from logic.simulator import Simulator
from util import global_config
from deepmerge import always_merger

if __name__ == '__main__':
    config_file_path = 'configurations/my_first_simulation.json'
    with open(config_file_path, 'r') as f:
        config = json.load(f)
        world = World.from_config(config['world'])
        always_merger.merge(global_config.config, config)
        simulator = Simulator(world, generational_events=['migration'])
        print("Running simulation with config {}: {}"
              .format(config_file_path, json.dumps(global_config.get_vars(), indent=2)))
        # print("Initial state of world: %s" % world)
        simulator.run()
        # print("Final state of world: %s" % world)
