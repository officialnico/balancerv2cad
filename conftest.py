from model.pools.stable.StableMath import StableMath
import pytest

@pytest.fixture()
def stablemath_test() -> None:
    yield StableMath
