from trame_datagrid.widgets.datagrid import *


def initialize(server):
    from trame_datagrid.module import datagrid

    server.enable_module(datagrid)
