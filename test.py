#!/usr/bin/python
from doboto.DO import DO

do = DO(url="https://api.digitalocean.com/v2/",token="e3cc092ee48e428e54067b5ebda86b0d7592a242fd43886d4ba5cc06f603eda2")

ssh_keys = do.ssh_key.list()

print ssh_keys
