
from pkgs.config import *
import yaml
import pprint
import subprocess

class TennisClub:

    def __init__(self, tennis_club, yaml_file=YAML_FILE):
        self.yaml = self._load_yaml(yaml_file).get(tennis_club)

        if self.yaml is None:
            raise(RuntimeError())

    def _load_yaml(self, yaml_file):
        with open(yaml_file, 'r') as fd:
            return yaml.load(fd, Loader=yaml.FullLoader)

    def display(self, msgs):
        pprint.pprint(msgs)

    def notify_to_console(self, msgs):
        subprocess.run(['notify-send', '--expire-time=20000', 'トーナメント申し込み状況', '\n'.join(msgs)])
