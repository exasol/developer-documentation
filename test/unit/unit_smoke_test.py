# F401 is used here as this is an import which is not explicitly used. The purpose of
# the unit_smoke_test.py file is to verify that the Python module can be loaded.
import exasol.developer_documentation  # noqa: F401


def test_unit_smoke_test():
    assert True
