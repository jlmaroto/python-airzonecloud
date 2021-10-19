import asyncio
import pytest

from airzonecloud.AirzoneInstallation import AirzoneInstallation, AirzoneCloudConnector
from unittest.mock import MagicMock

def test_if_provided_connection_uses_that_connection():
    conn = object()
    installation = AirzoneInstallation("1",conn=conn, email="j@j.com",password="1234")
    assert conn == installation._conn
    
def test_if_not_connexion_create_one():
    installation = AirzoneInstallation("1",email="j@j.com",password="1234")
    assert isinstance(installation._conn,AirzoneCloudConnector)

@pytest.mark.asyncio
async def test_installation_start_get_installation_info(mocker):
    get_installation_patch = mocker.patch('airzonecloud.AirzoneCloudConnector.AirzoneCloudConnector.get_installation', return_value=[])
    installation = AirzoneInstallation("1",email="j@j.com",password="1234")
    a = await installation.start()
    assert get_installation_patch.called_once()


@pytest.mark.asyncio
async def test_installation_start_create_installation_devices(mocker):
    get_installation_patch = mocker.patch('airzonecloud.AirzoneCloudConnector.AirzoneCloudConnector.get_installation', return_value={"groups":[{"devices":[{"id":1},{"id":2}]}]})
    get_device_patch = mocker.patch('airzonecloud.AirzoneDevice.AirzoneDevice.get_device', return_value=[])
    installation = AirzoneInstallation("1",email="j@j.com",password="1234")
    a = await installation.start()
    assert get_installation_patch.called_once()
    assert get_device_patch.call_count ==2


        
