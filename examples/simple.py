"""pip install Faker"""

from trame.app import get_server
from trame.widgets import vuetify3, datagrid
from trame.ui.vuetify3 import SinglePageLayout

from faker import Faker

FAKE_DATA = Faker()
PROFILE_KEEP = {"name", "residence", "job", "company", "sex", "mail", "ssn"}


def fake_profile(id):
    profile = FAKE_DATA.profile()
    return {"id": id, **{k: profile[k] for k in PROFILE_KEEP}}


ROWS = [fake_profile(i) for i in range(100)]
COLUMNS = [
    {
        "name": "Name",
        "prop": "name",
        "autoSize": True,
        "sortable": True,
        "order": "asc",
        "pin": "colPinStart",
    },
    {"name": "Address", "prop": "residence"},
    {
        "name": "Title",
        "prop": "job",
    },
    {
        "name": "Company",
        "prop": "company",
    },
    {
        "name": "Sex",
        "prop": "sex",
        "sortable": True,
        "order": "asc",
        # "columnType": "select",
        # "labelKey": "label",
        # "valueKey": "value",
        # "source": [
        #     {"label": "Male", "value": "M"},
        #     {"label": "Female", "value": "F"},
        # ],
    },
    {
        "name": "E-Mail",
        "prop": "mail",
    },
]


class SpreadSheetExample:
    def __init__(self, server=None):
        self.server = get_server(server, client_type="vue3")
        self.ui = self._build_ui()

    @property
    def state(self):
        return self.server.state

    def on_event(self, type, event):
        # print("event", event)
        if type == "edit":
            row = self.state.rows[event.get("rowIndex")]
            row[event.get("prop")] = event.get("val")
            # self.state.dirty("rows")

        if type == "sort":
            pass
            # sort_key = event.get("column").get("prop")
            # self.state.rows.sort(reverse= event.get("order") == "desc", key= lambda x: x[sort_key])
            # self.state.dirty("rows")
            # print(self.state.rows)

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
                            columns=("columns", COLUMNS),
                            # events
                            # before_sorting=(self.on_event, "['sort', $event.preventDefault() || $event.detail]"),
                            after_edit=(self.on_event, "['edit', $event.detail]"),
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
