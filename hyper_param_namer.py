import os


def get_experiment_name(hyperparameters_dict: dict, prefix_length: int = -1) -> str:
    """
    Entry point of the string creator that iterates over the dictionary of values
    :param hyperparameters_dict: dict
    :param prefix_length: int
    :return: str of concatenated key/values with unique prefixes
    """
    experiment_name = ''
    keys = {}

    try:
        # Validate types of incoming params
        if type(hyperparameters_dict) is not dict or type(prefix_length) is not int:
            raise Exception("Hyper parameters must be of type dict and prefix length of type integer")

        # Show whole key if prefix is too short
        if prefix_length <= 0:
            prefix_length = None

        # Build new map to hold original values / old names, and start creating new keys that adhere to the length
        for key, val in hyperparameters_dict.items():
            key = key.replace('_', '')  # Remove underscores from key names-- it's used as a separator in string concat
            truncated_key = key[0:prefix_length]  # Getting truncated key

            # Discovered a duplicate key; need to discover common prefix
            if truncated_key in keys:
                # Find new unique length
                unique_keys = get_unique_prefixes([key, keys[truncated_key]['orig']])
                keys[unique_keys[0]] = keys.pop(truncated_key)
                truncated_key = unique_keys[1]

            keys[truncated_key] = {
                "orig": key,
                "val": val
            }

        for key, val in keys.items():
            experiment_name += f"{str(key)}_{str(val['val'])}_"

        return experiment_name[:-1]
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return ''


def get_unique_prefixes(arr: []) -> []:
    """
    Finds the common prefix and adds 1 character to be unique
    :param arr: []
    :return: []
    """
    result = []
    prefix = os.path.commonprefix(arr)
    result.append(prefix + arr[0][len(prefix)])
    result.append(prefix + arr[1][len(prefix)])
    return result


H = {
    "learning_rate": 0.1,
    "dropout_in": 0.5,
    "dropout_out": 0.3,
    "use_cutout": True,
    "use_skip": False,
    "momentum": 0.9
}

print(get_experiment_name(H, 4))
