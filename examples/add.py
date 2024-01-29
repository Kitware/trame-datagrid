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


CHAR_WIDTH = 7
ROWS = [fake_profile(i) for i in range(5)]
COLUMNS = [
    {
        "name": "Name",
        "prop": "name",
        "autoSize": True,
        "pin": "colPinStart",
        "width": 4 * CHAR_WIDTH,
        "sortable": True,
        "order": "asc",
    },
    {
        "name": "Address",
        "prop": "residence",
        "width": 7 * CHAR_WIDTH,
    },
    {
        "name": "Title",
        "prop": "job",
        "width": 5 * CHAR_WIDTH,
    },
    {
        "name": "Company",
        "prop": "company",
        "width": 7 * CHAR_WIDTH,
    },
    {
        "name": "Sex",
        "prop": "sex",
        "width": 3 * CHAR_WIDTH,
    },
    {
        "name": "E-Mail",
        "prop": "mail",
        "width": 6 * CHAR_WIDTH,
    },
]


class SpreadSheetExample:
    def __init__(self, server=None):
        self.server = get_server(server, client_type="vue3")
        self.ui = self._build_ui()

    @property
    def state(self):
        return self.server.state

    def update_entry(self, event):
        row_id = event.get("model").get("id")
        edit_prop = event.get("prop")
        edit_value = event.get("val")
        new_rows = []
        for row in self.state.rows:
            if row.get("id") == row_id:
                row_edited = {**row, edit_prop: edit_value}
                new_rows.append(row_edited)
            else:
                new_rows.append(row)

        self.state.rows = new_rows

    def add_entry(self):
        self.state.rows.append(
            dict(
                id=len(self.state.rows),
                name="",
                residence="",
                job="",
                company="",
                sex="",
                mail="",
                ssn="",
            )
        )
        self.state.dirty("rows")

    def dirty_rows(self, event):
        """Just to overcome the dirty bug to client cache"""
        if event.get("order") is None:
            original = self.state.rows
            with self.state:
                self.state.rows = []
            self.state.rows = original

    def _build_ui(self):
        with SinglePageLayout(self.server, full_height=True) as layout:
            with layout.toolbar.clear() as toolbar:
                toolbar.density = "compact"
                toolbar.title = "Spreadsheet Example"
                vuetify3.VSpacer()
                with vuetify3.VBtn(icon=True, click=self.add_entry):
                    vuetify3.VIcon("mdi-plus")

            with layout.content:
                with vuetify3.VContainer(fluid=True, classes="fill-height pa-0 ma-0"):
                    datagrid.VGrid(
                        classes="fill-height",
                        theme="compact",
                        resize=True,
                        source=("rows", ROWS),
                        columns=("columns", COLUMNS),
                        # events
                        after_edit=(self.update_entry, "[$event.detail]"),
                        before_sorting_apply=(self.dirty_rows, "[$event.detail]"),
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
