function toJSExpression(v) {
    if ((typeof v === 'string' || v instanceof String) && v.startsWith("trame.utils")) {
        return window.trame.utils.get(v);
    }
    return v;
}

function decorateEntry(input) {
    const output = {};
    for (const [key, value] of Object.entries(input)) {
        output[key] = toJSExpression(value);
    }
    return output;
}

window.trame.utils.datagrid = {
    decorator(entries) {
        return entries.map(decorateEntry)
    },
    renderers: {
        red(createElement, props) {
            console.log("red props", props);
            return createElement('span', {
              style: {
                color: 'red'
              },
            }, props.model[props.prop]);
        },
        checkbox(createElement, props) {
            return createElement('input', {
                type: "checkbox",
                checked: props.model.check,
                onclick: () => {
                    // Change data locally (if the server won't send the updated model with dirty)
                    props.model.check = !props.model.check;
                    // Let the server know about the change
                    window.trame.trigger('toggle_grid_checkbox', [props.rowIndex, props.model.check]);
                },
            });
        },
    },
}