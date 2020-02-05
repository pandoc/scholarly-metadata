#!/usr/bin/env python3
import json
import sys
import yaml

filename = sys.argv[1]

with open(filename) as yaml_in:
    yaml_object = yaml.safe_load(yaml_in)
    json.dump(yaml_object, sys.stdout)
