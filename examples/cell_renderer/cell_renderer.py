from pathlib import Path
from trame.app import get_server
from trame.widgets import vuetify3, datagrid
from trame.ui.vuetify3 import SinglePageLayout
from trame.decorators import TrameApp, trigger

from trame_client.utils.defaults import TrameDefault


def create_entry(id):
    return {
        "id": id,
        "name": f"name {id}",
        "custom1": f"custom1 {id}",
        "check": not (id % 2),
    }


ROWS = [create_entry(i) for i in range(10)]
COLUMNS = [
    {
        "name": "Name",
        "prop": "name",
    },
    {
        "name": "Red",
        "prop": "custom1",
        "cellTemplate": "trame.utils.datagrid.renderers.red",
    },
    {
        "name": "Checkbox",
        "prop": "check",
        "cellTemplate": "trame.utils.datagrid.renderers.checkbox",
    },
]


def load_my_js(server):
    # must run before server start
    js_file = Path(__file__).with_name("renderers.js").resolve()
    server.enable_module(
        dict(
            # Path to serve under /my_code
            serve={"my_code": str(js_file.parent)},
            # JS file(s) to load
            scripts=[f"my_code/{js_file.name}"],
        )
    )


@TrameApp()
class SpreadSheetExample:
    def __init__(self, server=None):
        self.server = get_server(server, client_type="vue3")
        load_my_js(self.server)
        self.ui = self._build_ui()

    @property
    def state(self):
        return self.server.state

    @trigger("toggle_grid_checkbox")
    def _toggle_checkbox(self, row_index, new_value):
        print("Update checkbox value on server side", row_index, new_value)
        self.state.rows[row_index]["check"] = new_value
        # self.state.dirty("rows") # Don't do it of you don't want to force a refresh client side

    def _build_ui(self):
        with SinglePageLayout(self.server, full_height=True) as layout:
            with layout.toolbar.clear() as toolbar:
                toolbar.density = "compact"
                toolbar.title = "Spreadsheet Example"

            with layout.content:
                with vuetify3.VContainer(fluid=True, classes="fill-height pa-0 ma-0"):
                    print(
                        datagrid.VGrid(
                            classes="fill-height",
                            theme="compact",
                            resize=True,
                            auto_size_column=(
                                "auto_conf",
                                dict(mode="autoSizeOnTextOverlap", allColumns=True),
                            ),
                            # readonly=True,
                            source=("rows", ROWS),
                            columns=(
                                "trame.utils.datagrid.decorator(columns)",
                                TrameDefault(columns=COLUMNS),
                            ),
                        )
                    )

            return layout


# -----------------------------------------------------------------------------
# Standalone execution
# -----------------------------------------------------------------------------
def main():
    app = SpreadSheetExample()
    app.server.start()


if __name__ == "__main__":
    main()
