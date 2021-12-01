from .configuration import Configuration


def create_config_list(lst_config):
    lst_obj_config = []
    for config in lst_config:
        split_path = config.split("\\")
        name = split_path[-1].replace(".txt", "")
        new_config = Configuration(name, config)
        lst_obj_config.append(new_config)
    return lst_obj_config
