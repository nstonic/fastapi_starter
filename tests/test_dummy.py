import pytest


@pytest.mark.anyio()
async def test_dummy() -> None:
    assert True
