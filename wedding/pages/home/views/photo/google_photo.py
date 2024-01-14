import reflex as rx

from wedding import urls as url
from wedding import utils
from wedding.components import button, icon_section, main_text, title_section
from wedding.routes import IconRoutes as icon
from wedding.styles.fonts import Font


def wedding_google_photos() -> rx.Component:
    return rx.box(
        rx.center(
            rx.vstack(
                title_section("Álbum de fotos"),
                icon_section(icon=icon.ICON_CAMERA.value),
                button(button_name="Abrir álbum", url=url.GOOGLE_FOTOS_URL),
                main_text(text=utils.photo_section),
            ),
            width="100%",
            text_align="center",
            font_family=Font.DEFAULT.value,
        )
    )


# def wedding_google_photos() -> rx.Component:
#     return rx.vstack(
#         title_section("Álbum de fotos"),
#         icon_section(icon=icon.ICON_CAMERA.value),
#         button(button_name="Abrir álbum", url=url.GOOGLE_FOTOS_URL),
#         main_text(text=utils.photo_section),
#     )
