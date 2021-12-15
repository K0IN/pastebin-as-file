from tests.pastebin_api_mock import setup_fake_pastebin_api
import requests_mock
import pastebinfs.os
import requests


def test_os_copy(requests_mock: requests_mock.Mocker):
    setup_fake_pastebin_api(requests_mock)
    res = pastebinfs.os.cp("test.txt", "test_copy.txt",
                           "api_key", "837AD232A4F231AFF")

    