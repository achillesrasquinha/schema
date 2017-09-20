# imports - standard imports
import os, shutil

# imports - third-party imports
import pytest

# imports - module imports
from schema      import Cache
from schema.util import get_uuid_str

def test_cache():
    with pytest.raises(TypeError):
        Cache(12345, 'foo')
        Cache('bar', 12345)

def test_create():
    cache   = Cache()
    cache.create()
    
    defloc  = os.path.expanduser('~')
    defdir  = '.schema'
    defpath = os.path.join(defloc, defdir)
    assert os.path.exists(defpath)  == True

    temploc = get_uuid_str(strip = True)
    tempdir = get_uuid_str(strip = True)
    tempath = os.path.join(temploc, tempdir)
    cache   = Cache(location = temploc, dirname = tempdir)
    cache.create()
    assert os.path.exists(tempath) == True

    shutil.rmtree(temploc)