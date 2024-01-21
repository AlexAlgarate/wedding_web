from enum import Enum


def icon_route(filename: str, png: bool = False) -> str:
    if png:
        return f"/icons/{filename}.png"
    else:
        return f"/icons/{filename}.svg"


class Route(Enum):
    INDEX = "/"
    CONTACT = "/contact"


class FileRoutes(Enum):
    JS_COUNTDOWN = "/js/countdown.js"
    IMAGE_HEADER_ONE = "/images/vicky_bici_copia.png"
    IMAGE_HEADER_TWO = "/images/vicky_bota_copia.png"
    AGRIPINA = "/images/agripina.jpg"


class IconRoutes(Enum):
    ICON_BUS = icon_route("bus")
    ICON_CAMERA = icon_route("camera")
    ICON_CELEBRATION = icon_route("wedding")
    ICON_CONFIRMATION = icon_route("confirmation")
    ICON_UBICATION = icon_route("localization", png=True)
