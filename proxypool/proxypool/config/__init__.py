"""
Configuration center.
Use https://www.dynaconf.com/
"""""
import os
import sys
from pathlib import Path

from dynaconf import Dynaconf

_base_dir = Path(__file__).parent.parent
_local_path = _base_dir / '.local'

_setting_files = [
    # All config file will merge.
    Path(__file__).parent / 'setting.yml',  # Load default config.
]

# User configuration. It will be created automatically by the pip installer .
_external_files = [
    Path(sys.prefix, 'etc', 'CREWLERSTACK', 'proxypool', 'setting.yml')
]
# 自定义配置

setting = Dynaconf(
    # Set env `CREWLERSTACK_PROXYPOOL='bar'`，use `setting.FOO` .
    envvar_prefix='CREWLERSTACK_PROXYPOOL',
    setting_files=_setting_files,  # load user configuration.
    # environments=True,  # Enable multi-level configuration，eg: default, development, production
    load_dotenv=True,  # Enable load .env
    # env_switcher='CREWLERSTACK_PROXYPOOL_ENV',
    lowercase_read=False,
    includes=_external_files,
    basedir=_base_dir,
    localpath=_local_path,
)

os.makedirs(_local_path, exist_ok=True)
