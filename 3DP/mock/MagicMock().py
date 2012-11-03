import mock
import os
import pgpass


my_mock = mock.MagicMock()
with mock.patch('__builtin__.open', my_mock):
    manager = my_mock.return_value.__enter__.return_value
    manager.read.return_value = 'some data'
    with open('foo') as h:
        print h.read()
    my_mock.assert_called_once_with('foo')