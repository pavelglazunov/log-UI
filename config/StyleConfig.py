from dataclasses import dataclass
import yaml

THEME = {
    "white": {
        "back_ground": "#808080",
        "window_color": "#FFFFFF",
        "text_color": "#000000",
        "button_color": "#C6C6C6",
        "border_color": "#000000"
    },
    "dark": {
        "back_ground": "#404040",
        "window_color": "#303030",
        "text_color": "#FFFFFF",
        "button_color": "#FA5539",
        "border_color": "#FA5539"
    },
    "green": {
        "back_ground": "#212121",
        "window_color": "#000000",
        "text_color": "#31FF1E",
        "button_color": "#808080",
        "border_color": "#31FF1E"
    },
    "blue": {
        "back_ground": "#2B647F",
        "window_color": "#0E4A7F",
        "text_color": "#FFFFFF",
        "button_color": "#F600FF",
        "border_color": "#F600FF"
    }
}
with open('./config/AppSettings.yaml') as fh:
    cfg = yaml.safe_load(fh)

with open(f"./config/themes/{cfg['active_theme']}.yaml") as th:
    theme = yaml.safe_load(th)


class Style:
    font_size = cfg.get("size")
    font_style = cfg.get("font")
    text_color = theme.get("text_color")
    border_radius = cfg.get("border_radius")

    logs_word_colors = cfg.get("log_text_colors")

    bg = f"background-color: {theme['back_ground']}"
    window = f"background-color: {theme['window_color']}; " \
             f"border: {theme['border_color']}; " \
             f"border-radius: {border_radius}px;" \
             f"font-size: {font_style}px;" \
             f"color: {theme['text_color']}"
    window_color = f"background-color: {theme['window_color']}; " \
                   f"border: {theme['border_color']}; " \
                   f"border: 1px solid {theme['border_color']};" \
                   f"border-radius: {border_radius - 5}px;" \
                   f"font-size: {font_size}px"

    check_box = "QCheckBox {" \
                f"color: {theme['text_color']};" \
                "}" \
                "QCheckBox::indicator {" \
                f"border: 1px solid {theme['border_color']};" \
                f"background-color: {theme['back_ground']};" \
                "}" \
                "QCheckBox::indicator:checked {" \
                f"background-color: {theme['border_color']};" \
                f"border-radius: 12px" \
                "}"

    menu_btn = "QPushButton {color: " \
               f"{theme['text_color']};" \
               " border:  none} QPushButton::hover {background-color : " \
               f"{theme['button_color']};" \
               " border:  none}"
    add_menu_btn = "QPushButton {color: " \
                   f"{theme['text_color']};" \
                   f"border: 1px solid {theme['border_color']};" \
                   f"border-radius: {border_radius - 5}px;" \
                   "} QPushButton::hover {background-color : " \
                   f"{theme['button_color']};" \
                   f"border-radius: {border_radius - 5}px;" \
                   " border:  none}"

    warning_btn = "QPushButton {color: " \
                  f"{theme['text_color']};" \
                  f"border: 1px solid {theme['warning_color']};" \
                  f"border-radius: {border_radius - 5}px;" \
                  "} QPushButton::hover {background-color : " \
                  f"{theme['warning_color']};" \
                  f"border-radius: {border_radius - 5}px;" \
                  " border:  none}"

    line = f"background-color: {theme['border_color']};"
    border = f"border: 1px solid {theme['border_color']};"
    input_line = f"background-color: {theme['window_color']}; " \
                 f"border: 1px solid {theme['border_color']};" \
                 f"font-size: {font_style}px;" \
                 f"border-radius: {border_radius - 5}px;" \
                 f"color: {theme['text_color']};" \
                 f""

    window_width = cfg["width"]
    window_height = cfg["height"]

    def update(self):
        Style.logs_word_colors = cfg.get("log_text_colors")


class Config:
    last_opened_files = cfg.get("last_open_file")


def edit_style_config(param, value, key=None):
    if type(cfg[param]) == dict:

        if key[0] == "-":
            cfg[param].pop(key[1:])
        else:
            cfg[param][key] = value

    with open('./config/AppSettings.yaml', "w") as f:
        yaml.dump(cfg, f)
