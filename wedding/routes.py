from enum import Enum


class Route(Enum):
    INDEX = "/"
    CONTACT = "/contact"


class FileRoutes(Enum):
    JS_COUNTDOWN = "/js/countdown.js"
    IMAGE_HEADER_ONE = "/images/vicky_bici_copia.png"
    IMAGE_HEADER_TWO = "/images/vicky_bota_copia.png"


class IconRoutes(Enum):
    ICON_FLAMINGO_RIGHT = "/icons/flamingo_right.png"
    ICON_FLAMINGO_LEFT = "/icons/flamingo_left.png"
    ICON_IMAGE_HOME = "/icons/hogar.png"
    ICON_BUS = "/icons/bus.png"
    ICON_CAMERA = "/icons/camera.png"
    ICON_CELEBRATION = "/icons/celebration.png"
    ICON_CONFIRMATION = "/icons/confirmation.png"
    ICON_MENU = "/icons/menu_icon.png"
    ICON_GIFT = "/icons/gift.png"
