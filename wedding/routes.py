from enum import Enum


def icon_route(filename: str, png: bool = False) -> str:
    if png:
        return f"/icons/{filename}.png"
    else:
        return f"/icons/{filename}.svg"


def image_route(filename: str, svg: bool = False) -> str:
    if svg:
        return f"/images/{filename}.svg"
    else:
        return f"/images/{filename}.webp"


class Route(Enum):
    INDEX = "/"
    CONTACT = "/contact"


class FileRoutes(Enum):
    JS_COUNTDOWN = "/js/countdown.js"
    IMAGE_HEADER = image_route("almendros_")
    IMAGE_AGRIPINA = image_route("agripina")
    IMAGE_LAVENDER_TOP = image_route("lavender_top")
    IMAGE_LAVENDER_BOTTOM = image_route("lavender_bottom")
    IMAGE_LEAFS_SECTION = image_route("leafs", svg=True)


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
