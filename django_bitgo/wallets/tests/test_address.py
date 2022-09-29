from django_bitgo.wallets.address import Address
from django_bitgo.exceptions import BitGoException
from django_bitgo.client import BitGoClient
import pytest


def test_address_initialize_module_without_access_token():

    with pytest.raises(BitGoClient) as exc:
        bitgo_client = BitGoClient()

    assert str(exc.value) == "Access token is required to create a BitGoClient"
    # address = Address(client=bitgo_client, wallet_id="foobar")

    # assert address.client == bitgo_client
