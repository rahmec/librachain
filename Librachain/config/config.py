import yaml

config = yaml.safe_load(open('configuration.yml', 'r'))
print(config["db_path"])
