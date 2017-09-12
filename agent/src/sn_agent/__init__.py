import os
import uuid
from abc import ABC
from pathlib import Path

from urllib3.util import Url, parse_url


class Required:
    def __init__(self, v_type=None):
        self.v_type = v_type


class SettingsBase(ABC):
    """
    Any setting defined here can be overridden by:

    Settings the appropriate environment variable, eg. to override FOOBAR, `export APP_FOOBAR="whatever"`.
    This is useful in production for secrets you do not wish to save in code and
    also plays nicely with docker(-compose). Settings will attempt to convert environment variables to match the
    type of the value here. See also activate.settings.sh.

    Or, passing the custom setting as a keyword argument when initialising settings (useful when testing)
    """

    _ENV_PREFIX = None

    def __init__(self, **custom_settings):
        """
        :param custom_settings: Custom settings to override defaults, only attributes already defined can be set.
        """

        self._custom_settings = custom_settings
        self.substitute_environ()
        for name, value in custom_settings.items():
            if not hasattr(self, name):
                raise TypeError('{} is not a valid setting name'.format(name))
            setattr(self, name, value)

    def substitute_environ(self):
        """
        Substitute environment variables into settings.
        """
        for attr_name in dir(self):

            # Remove anything starts with an underscore
            if attr_name.startswith('_') or attr_name.upper() != attr_name:
                continue

            orig_value = getattr(self, attr_name)

            # If the setting is of type Required
            is_required = isinstance(orig_value, Required)

            orig_type = orig_value.v_type if is_required else type(orig_value)

            if self._ENV_PREFIX is None:
                raise RuntimeError('You must set the value of _ENV_PREFIX')

            env_var_name = "%s%s" % (self._ENV_PREFIX, attr_name)

            env_var = os.getenv(env_var_name, None)

            try:
                if env_var is not None:

                    if issubclass(orig_type, bool):
                        # Convert possible values to uppercase
                        env_var = env_var.upper() in ('1', 'TRUE', 'YES', 'ON')

                    elif issubclass(orig_type, int):
                        env_var = int(env_var)

                    elif issubclass(orig_type, Path):
                        env_var = Path(env_var)

                    elif issubclass(orig_type, bytes):
                        env_var = env_var.encode()

                    elif issubclass(orig_type, Url):
                        env_var = parse_url(env_var).url

                    elif issubclass(orig_type, uuid.UUID):
                        env_var = uuid.UUID(env_var)

                    # could do floats here and lists etc via json
                    setattr(self, attr_name, env_var)

                # If we got here, the value was not found or is None - check to see if it is required and raise an error
                elif is_required and attr_name not in self._custom_settings:
                    msg = """The required environment variable "{0}" is currently not set
you'll need to run `source activate.settings.sh`
or you can set that single environment variable with `export {0}="<value>"`
"""
                    raise RuntimeError(msg.format(env_var_name))
            except TypeError:
                msg = "There was a problem with %s : %s (%s)" % (env_var_name, env_var, orig_type)
                raise RuntimeError(msg.format(env_var_name))
