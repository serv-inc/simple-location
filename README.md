# Simple Location
This package provides a file-based location mechanism.


## Configuration
To configure, simply place two files named `latitude` and `longitude`
to the expected directories `/etc/location/` or `~/.config/location/`.

You can also set the (user) configuration programmatically
(and then copy to `/etc/location`), see below.

If you do not set a location, Greenwich (`51.48, 0`) is used.

## Usage
To use, simply call `location.get()`:

```
import location

location.get()  # returns Config(lat=47.35, lon=8.44, alt=0.0, path=PosixPath('/etc/location'))
```

### Setting the configuration
To set the configuration , use e.g.

```python
import location

mh = location.Config(47.35, 8.44, 0, location.user_dir())
mh.save()
```
