# Copyright 2018 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from unittest import mock

from nuclio import Context, Event


def handler(context, event):
    return 'Hi ' + event.body + '. How are you?'


def test_handler():
    context, event = Context(), Event(body='Dave')
    context.logger.info_with('some information', x=1, y=2)
    out = handler(context, event)
    assert out == 'Hi Dave. How are you?'


def test_inject_context():
    with mock.patch('IPython.get_ipython') as ipy:
        ipy.side_effect = 'ipykernel.zmqshell.ZMQInteractiveShell'
        context  # noqa - Make sure it's there
