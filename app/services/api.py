# Copyright (C) 2021, Pyronear contributors.

# This program is licensed under the Apache License version 2.
# See LICENSE or go to <https://www.apache.org/licenses/LICENSE-2.0.txt> for full license details.

from pyroclient import Client
import config as cfg


__all__ = ['api_client']


if any(not isinstance(val, str) for val in [cfg.API_DEV_URL, cfg.API_DEV_LOGIN, cfg.API_DEV_PWD]):
    raise ValueError("The following environment variables need to be set: 'API_URL', 'API_DEV_LOGIN', 'API_DEV_PWD'")

api_client = Client(cfg.API_DEV_URL, cfg.API_DEV_LOGIN, cfg.API_DEV_PWD)
