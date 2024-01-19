from trame_client.widgets.core import AbstractElement, Template  # noqa
from ..module import datagrid


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(datagrid)


class VGridVueEditor(HtmlElement):
    """ """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-grid-vue-editor", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VGridVueTemplate(HtmlElement):
    """ """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-grid-vue-template", children, **kwargs)
        self._attr_names += []
        self._event_names += []


class VGrid(HtmlElement):
    """
    Spreadsheet like component
    Properties

    :param auto_size_column: Autosize config Enable columns autoSize, for more details check @autoSizeColumn plugin By default disabled, hence operation is not resource efficient true to enable with default params (double header separator click for autosize) or provide config boolean \| { mode?: ColumnAutoSizeMode; allColumns?: boolean; letterBlockSize?: number; preciseSize?: boolean; } false
    :param can_focus: When true cell focus appear. boolean true
    :param col_size: Indicates default column size. number 100
    :param column_types: Types Every type represent multiple column properties Types will be merged but can be replaced with column properties { [name: string]: ColumnType; } {}
    :param columns: Columns - defines an array of grid columns. Can be column or grouped column. (ColumnRegular \| ColumnGrouping)[] []
    :param editors: Custom editors register { [name: string]: EditorCtr; } {}
    :param exporting: Enables export plugin Can be boolean Can be export options boolean false
    :param filter: Enables filter plugin Can be boolean Can be filter collection boolean \| { collection?: Record<ColumnProp, FilterCollectionItem>; include?: string[]; customFilters?: Record<string, CustomFilter>; } false
    :param frame_size: Defines how many rows/columns should be rendered outside visible area. number 1
    :param grouping: Group models by provided properties Define properties to be groped by { props?: ColumnProp[]; expandedAll?: boolean; } undefined
    :param pinned_bottom_source: Pinned bottom Source: {[T in ColumnProp]: any} - defines pinned bottom rows data source. DataType[] []
    :param pinned_top_source: Pinned top Source: {[T in ColumnProp]: any} - defines pinned top rows data source. DataType[] []
    :param plugins: Custom grid plugins Has to be predefined during first grid init Every plugin should be inherited from BasePlugin (typeof Plugin)[] undefined
    :param range: When true, user can range selection. boolean false
    :param readonly: When true, grid in read only mode. boolean false
    :param resize: When true, columns are resizable. boolean false
    :param row_class: Row class property Define this property in rgRow object and this will be mapped as rgRow class string ''
    :param row_definitions: Row properties applied RowDefinition[] []
    :param row_headers: Excel like show rgRow indexe per rgRow RowHeaders \| boolean undefined
    :param row_size: Indicates default rgRow size. By default 0, means theme package size will be applied number 0
    :param source: defines main data source. Can be an Object or 2 dimensional array([][]); Keys/indexes referenced from columns Prop DataType[] []
    :param stretch: Defines stretch strategy for columns with @StretchColumn plugin if there are more space on the right last column size would be increased boolean \| string true
    :param theme: Theme name "compact" \| "darkCompact" \| "darkMaterial" \| "default" \| "material" 'default'
    :param trimmed_rows: Trimmed rows Functionality which allows to hide rows from main data set { [x: number]: boolean; } {}
    :param use_clipboard: use-clipboard When true enable clipboard. boolean true

    Events

    :param auto_size_column: Autosize config Enable columns autoSize, for more details check @autoSizeColumn plugin By default disabled, hence operation is not resource efficient true to enable with default params (double header separator click for autosize) or provide config boolean \| { mode?: ColumnAutoSizeMode; allColumns?: boolean; letterBlockSize?: number; preciseSize?: boolean; } false
    :param can_focus: When true cell focus appear. boolean true
    :param col_size: Indicates default column size. number 100
    :param column_types: Types Every type represent multiple column properties Types will be merged but can be replaced with column properties { [name: string]: ColumnType; } {}
    :param columns: Columns - defines an array of grid columns. Can be column or grouped column. (ColumnRegular \| ColumnGrouping)[] []
    :param editors: Custom editors register { [name: string]: EditorCtr; } {}
    :param exporting: Enables export plugin Can be boolean Can be export options boolean false
    :param filter: Enables filter plugin Can be boolean Can be filter collection boolean \| { collection?: Record<ColumnProp, FilterCollectionItem>; include?: string[]; customFilters?: Record<string, CustomFilter>; } false
    :param frame_size: Defines how many rows/columns should be rendered outside visible area. number 1
    :param grouping: Group models by provided properties Define properties to be groped by { props?: ColumnProp[]; expandedAll?: boolean; } undefined
    :param pinned_bottom_source: Pinned bottom Source: {[T in ColumnProp]: any} - defines pinned bottom rows data source. DataType[] []
    :param pinned_top_source: Pinned top Source: {[T in ColumnProp]: any} - defines pinned top rows data source. DataType[] []
    :param plugins: Custom grid plugins Has to be predefined during first grid init Every plugin should be inherited from BasePlugin (typeof Plugin)[] undefined
    :param range: When true, user can range selection. boolean false
    :param readonly: When true, grid in read only mode. boolean false
    :param resize: When true, columns are resizable. boolean false
    :param row_class: Row class property Define this property in rgRow object and this will be mapped as rgRow class string ''
    :param row_definitions: Row properties applied RowDefinition[] []
    :param row_headers: Excel like show rgRow indexe per rgRow RowHeaders \| boolean undefined
    :param row_size: Indicates default rgRow size. By default 0, means theme package size will be applied number 0
    :param source: defines main data source. Can be an Object or 2 dimensional array([][]); Keys/indexes referenced from columns Prop DataType[] []
    :param stretch: Defines stretch strategy for columns with @StretchColumn plugin if there are more space on the right last column size would be increased boolean \| string true
    :param theme: Theme name "compact" \| "darkCompact" \| "darkMaterial" \| "default" \| "material" 'default'
    :param trimmed_rows: Trimmed rows Functionality which allows to hide rows from main data set { [x: number]: boolean; } {}
    :param use_clipboard: use-clipboard When true enable clipboard. boolean true
    """

    def __init__(self, children=None, **kwargs):
        super().__init__("v-grid", children, **kwargs)
        self._attr_names += [
            "auto_size_column",
            "can_focus",
            "col_size",
            "column_types",
            "columns",
            "editors",
            "exporting",
            "filter",
            "frame_size",
            "grouping",
            "pinned_bottom_source",
            "pinned_top_source",
            "plugins",
            "range",
            "readonly",
            "resize",
            "row_class",
            "row_definitions",
            "row_headers",
            "row_size",
            "source",
            "stretch",
            "theme",
            "trimmed_rows",
            "use_clipboard",
        ]
        self._event_names += [
            ("after_column_resize", "aftercolumnresize"),
            ("after_columns_set", "aftercolumnsset"),
            ("after_edit", "afteredit"),
            ("after_source_set", "aftersourceset"),
            ("after_trimmed", "aftertrimmed"),
            ("before_range", "beforerange"),
            ("before_auto_fill", "beforeautofill"),
            ("before_cell_focus", "beforecellfocus"),
            ("before_column_applied", "beforecolumnapplied"),
            ("before_columns_set", "beforecolumnsset"),
            ("before_edit", "beforeedit"),
            ("before_edit_start", "beforeeditstart"),
            ("before_export", "beforeexport"),
            ("before_filter_apply", "beforefilterapply"),
            ("before_filter_trimmed", "beforefiltertrimmed"),
            ("before_focus_lost", "beforefocuslost"),
            ("before_range_edit", "beforerangeedit"),
            ("before_sorting", "beforesorting"),
            ("before_sorting_apply", "beforesortingapply"),
            ("before_source_set", "beforesourceset"),
            ("before_source_sorting_apply", "beforesourcesortingapply"),
            ("before_trimmed", "beforetrimmed"),
            ("header_click", "headerclick"),
            ("row_drag_start", "rowdragstart"),
            ("row_order_changed", "roworderchanged"),
            ("viewport_scroll", "viewportscroll"),
        ]


__all__ = [
    "VGridVueEditor",
    "VGridVueTemplate",
    "VGrid",
]
