# -*- coding: UTF-8 -*-
#
# Copyright 2015-2023 Flavio Garcia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import click
import taskio


@taskio.command(short_help="Generates an uuid4 string")
@click.argument("path", required=False, type=click.Path(resolve_path=True))
def uuid():
    """Initializes a repository."""
    print("booo")


@taskio.group(name="g1", short_help="A group level 1")
def group1():
    pass
