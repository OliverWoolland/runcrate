# Copyright 2022-2024 CRS4.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path

import pytest


THIS_DIR = Path(__file__).absolute().parent
DATA_DIR_NAME = 'data'


# pytest's tmpdir returns a py.path object
@pytest.fixture
def tmpdir(tmpdir):
    return Path(tmpdir)


@pytest.fixture
def data_dir(tmpdir):
    return THIS_DIR / DATA_DIR_NAME
