import reflex as rx

from wedding import urls as url
from wedding import utils
from wedding.components import button, icon_section, text_section, title_section
from wedding.routes import IconRoutes as icon
from wedding.styles.fonts import Font


def wedding_google_photos() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                title_section(title=utils.title_photo),
                icon_section(icon=icon.ICON_CAMERA.value),
                button(button_name=utils.button_google_photo, url=url.GOOGLE_FOTOS_URL),
                text_section(text=utils.photo_section),
            ),
            width="100%",
            font_family=Font.DEFAULT.value,
        )
    )
