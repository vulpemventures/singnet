import base64
import os

import aiohttp_session
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from sn_agent_ui.settings import UISettings


def setup_session(app):
    settings = UISettings()
    secret_key = base64.urlsafe_b64decode(settings.COOKIE_SECRET)
    aiohttp_session.setup(app, EncryptedCookieStorage(secret_key))


def create_session_key():
    return base64.urlsafe_b64encode(os.urandom(32))


if __name__ == "__main__":
    print(create_session_key())
