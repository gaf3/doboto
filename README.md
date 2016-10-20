# doboto

BOTO like interface for DigitalOcean

## Usage

```python
from doboto.DO import DO

do = DO(url="https://api.digitalocean.com/v2/",token="secret")

ssh_keys = do.ssh_key.list(name="My Sample Key")
droplet = do.droplet.create(name="example.com", region="nyc3", size="512mb", image="ubuntu-14-04-x64", ssh_keys=ssh_keys)

do.droplet.destroy(id=droplet['id'])
```