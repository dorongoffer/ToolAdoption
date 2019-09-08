import json

from model.world import World
from logic.simulator import Simulator
from util import global_config
from deepmerge import always_merger

if __name__ == '__main__':
    config_file_path = 'conf/random_world_simulation.json'
    with open(config_file_path, 'r') as f:
        config = json.load(f)
        always_merger.merge(global_config.config, config)
        config = global_config.config

        world = World.from_config(config['world'])
        events = config["generational_events"]
        simulator = Simulator(world, generational_events=events)
        print("Running simulation with config {}: {}"
              .format(config_file_path, json.dumps(global_config.get_vars(), indent=2)))
        print("Initial world: %s" % world)
        simulator.run()
        print("Final world: %s" % world)
