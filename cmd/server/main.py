from flask import Flask
import yaml

def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def create_server(cfg):
    app = Flask(__name__)
    return app

def main():
    cfg = load_config("configs/config.yaml")
    app = create_server(cfg)
    app.run(host=cfg["server"]["address"].split(":")[0], port=int(cfg["server"]["address"].split(":")[1]))

if __name__ == "__main__":
    main()
