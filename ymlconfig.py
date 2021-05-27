import yaml


class YMLConfig:

    def __init__(self):
        with open(r'config.yml') as file:
            try:
                self.config = yaml.load(file, Loader=yaml.FullLoader)
            except Exception:
                print("cant read config file")
