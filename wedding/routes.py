from enum import Enum


def icon_route(filename: str) -> str:
    return f"/icons/{filename}.png"


class Route(Enum):
    INDEX = "/"
    CONTACT = "/contact"


class FileRoutes(Enum):
    JS_COUNTDOWN = "/js/countdown.js"
    IMAGE_HEADER_ONE = "/images/vicky_bici_copia.png"
    IMAGE_HEADER_TWO = "/images/vicky_bota_copia.png"


class IconRoutes(Enum):
    ICON_FLAMINGO_RIGHT = icon_route("flamingo_right")
    ICON_FLAMINGO_LEFT = icon_route("flamingo_left")
    ICON_IMAGE_HOME = icon_route("hogar")
    ICON_BUS = icon_route("bus")
    ICON_CAMERA = icon_route("camera")
    ICON_CELEBRATION = icon_route("celebration")
    ICON_CONFIRMATION = icon_route("confirmation")
    ICON_MENU = icon_route("menu_icon")
    ICON_GIFT = icon_route("gift")
    ICON_UBICATION = icon_route("ubication")
