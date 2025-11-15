import yaml

class ServerConfig:
    def __init__(self, port):
        self.port = port

class Config:
    def __init__(self, server):
        self.server = server

def load_config(file_path):
    with open(file_path, "r") as f:
        data = yaml.safe_load(f)
    server_cfg = ServerConfig(port=data["server"]["port"])
    return Config(server=server_cfg)
