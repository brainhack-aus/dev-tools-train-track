import os
import shutil
from pathlib import Path
# from tempfile import mkdtemp
import pytest


# @pytest.fixture
# def work_dir():
#     tmp_dir = tempfile.mkdtemp()
#     yield tmp_dir
#     shutil.rmtree(tmp_dir)

# For debugging in IDE's don't catch raised exceptions and let the IDE
# break at it
if os.getenv('_PYTEST_RAISE', "0") != "0":

    @pytest.hookimpl(tryfirst=True)
    def pytest_exception_interact(call):
        raise call.excinfo.value

    @pytest.hookimpl(tryfirst=True)
    def pytest_internalerror(excinfo):
        raise excinfo.value