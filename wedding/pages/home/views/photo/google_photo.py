import reflex as rx

from wedding import urls as url
from wedding import utils
from wedding.components.icon_section import icon_section
from wedding.components.main_text import main_text
from wedding.components.title_section import title_section
from wedding.routes import IconRoutes as icon
from wedding.styles import Size
from wedding.styles.colors import Color


def wedding_google_photos() -> rx.Component:
    return rx.vstack(
        title_section("Álbum de fotos"),
        icon_section(icon=icon.ICON_CAMERA.value),
        button_date(button_name="Abrir álbum", url=url.GOOGLE_FOTOS_URL),
        main_text(text=utils.photo_section),
    )


def button_date(button_name: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            button_name,
            width="100%",
            font_size=[
                Size.DEFAULT.value,
                Size.DEFAULT.value,
                Size.DEFAULT.value,
                Size.LARGE.value,
                Size.LARGE.value,
            ],
            padding=Size.DEFAULT.value,
            color=Color.BACKGROUND.value,
            background=Color.TEXT_DEFAULT.value,
            border_radius=Size.VERY_BIG.value,
            text_align="center",
            margin_bottom=Size.DEFAULT.value,
            box_shadow=f"3px 2.5px 7px 1px {Color.DEFAULT_OPACITY.value}",
            _hover={
                "background": "",
            },
        ),
        href=url,
        is_external=True,
        # width="100%",
        height="100%",
    )
