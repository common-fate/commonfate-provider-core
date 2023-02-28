import sys
from os import path

import pytest

from commonfate_provider import namespace


@pytest.fixture(autouse=True)
def fresh_namespace():
    yield
    namespace.clear()


# @pytest.fixture
# def dist_module():
#     old_path = sys.path

#     yield
#     sys.path = old_path


def test_entrypoint_works(dist_module):
    sys.path.append(path.join(path.dirname(__file__)))
    from commonfate_provider.runtime import aws_lambda_entrypoint
