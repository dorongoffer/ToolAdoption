# Just a way of keeping the configuration variables global and accessible from everywhere
# Populate this with default values, and override them in your config json file

config = {
    "world": {
        "tools_count": 5,
        "populations_count": 7,
        "min_pop_size": 20,
        "max_pop_size": 100,
    },
    "generational_events": [
        "migration",
        "tool_development",
        "tool_abandonment"
    ],
    "variables": {
        "sc_func": "math.exp(-10 * x)",
        "simulation_length": 3,
        "migration": {
          "probability": 0.1,
          "max_tools": 2,
          "tool_adoption_probability": 0.2
        },
        "tool_development": {
            "probability": 0.1,
            "max_tools": 1,
        },
        "tool_abandonment": {
            "probability": 0.005
        }
    }
}


def get_vars():
    return config['variables']


def get_var(name, default=None):
    return _get_var_rec(name.split('.'), config['variables'], default)


def _get_var_rec(path, variables, default=None):
    name = path[0]
    if name not in variables:
        return default
    if len(path) == 1:
        return variables[name]
    del path[0]
    return _get_var_rec(path, variables[name], default)

