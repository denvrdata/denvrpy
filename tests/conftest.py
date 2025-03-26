import pytest
import requests

from denvr.config import Config


@pytest.fixture(scope="session")
def mock_config():
    # Populate the lcoal mock server with our test spec
    # Assumes you've run `docker run -d --rm -p 1080:1080 mockserver/mockserver`
    resp = requests.put(
        "http://localhost:1080/mockserver/openapi",
        json={"specUrlOrPayload": "https://api.cloud.denvrdata.com/swagger/v1/swagger.json"},
    )
    resp.raise_for_status()

    # NOTE: We set Auth to None because our mock server doesn't support the auth endpoint.
    return Config(defaults={"server": "http://localhost:1080"}, auth=None)
