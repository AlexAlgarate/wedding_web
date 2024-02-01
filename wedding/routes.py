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
    IMAGE_HEADER = "/images/almendros_.png"
    IMAGE_AGRIPINA = "/images/agripina.jpg"
    IMAGE_LAVENDER_TOP = "/images/lavender_top.png"
    IMAGE_LAVENDER_BOTTOM = "/images/lavender_bottom.png"
    IMAGE_LEAFS_SECTION = "/images/leafs.svg"


class IconRoutes(Enum):
    ICON_BUS = icon_route("bus")
    ICON_CAMERA = icon_route("camera")
    ICON_CELEBRATION = icon_route("wedding")
    ICON_CONFIRMATION = icon_route("confirmation")
    ICON_UBICATION = icon_route("localization", png=True)
    ICON_GIFT = icon_route("regalo", png=True)
    ICON_WHATSAPP = icon_route("whatsapp")
    ICON_EMAIL = icon_route("email")
    ICON_PHONE = icon_route("phone")
