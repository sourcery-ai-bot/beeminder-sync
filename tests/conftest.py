"""
    Common configuration for all the tests
"""

from configparser import ConfigParser
import pathlib
import pytest
from beeminder_sync.beeminder import Beeminder


BASE_DIR = pathlib.Path.cwd()


@pytest.fixture(scope="module")
def config():
    """ Configuration settings for all the apis """
    fpath = BASE_DIR / "config.ini"
    config = ConfigParser()
    with open(fpath, 'r') as fid:
        config.read_file(fid)
    return config


@pytest.fixture
def beeminder_config(config):
    """ The configuration for the beeminder api """
    assert 'beeminder' in config.keys()
    data = dict(config['beeminder'])
    data['required_fields'] = ["api", "username", "auth_token"]
    return data


@pytest.fixture
def beeminder_interface(beeminder_config):
    """ The `Beeminder` instance to communicate with the api """
    base_url = beeminder_config["api"]
    username = beeminder_config["username"]
    auth_token = beeminder_config["auth_token"]
    interface = Beeminder(base_url, username, auth_token)
    return interface
