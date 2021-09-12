import json
import yaml

from github_config.const import APP_NAME_YAML


def dict_to_yaml_convert(in_app_name=False):
    yaml_data = None
    if in_app_name:
        app_data_json = json.dumps(APP_NAME_YAML)
        yaml_data = yaml.dump(yaml.load(app_data_json), default_flow_style=False)
    return yaml_data
