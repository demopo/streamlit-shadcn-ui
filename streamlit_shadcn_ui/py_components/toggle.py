from .utils import declare_component

_component_func = declare_component("toggle")

def toggle(default_checked=False, key=None):
    props = {
        "defaultChecked": default_checked,
    }
    component_value = _component_func(comp="toggle",props=props, key=key, default=default_checked)
    return component_value
