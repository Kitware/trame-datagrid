from pathlib import Path

serve_path = str(Path(__file__).with_name("serve").resolve())
serve = {"__trame_datagrid": serve_path}
scripts = ["__trame_datagrid/trame_datagrid.umd.js"]
vue_use = ["trame_datagrid"]
