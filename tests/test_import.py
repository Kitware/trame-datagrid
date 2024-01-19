def test_import():
    from trame_datagrid.widgets.datagrid import VGrid  # noqa: F401

    # For components only, the CustomWidget is also importable via trame
    from trame.widgets.datagrid import VGrid  # noqa: F401,F811
