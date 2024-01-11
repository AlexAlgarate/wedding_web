import reflex as rx
from wedding import utils
from wedding.components.main_text import main_text

from wedding.components.title_section import title_section
from wedding.routes import IconRoutes as icon
from wedding.components.icon_section import icon_section
from wedding import urls as url
from wedding.styles import Size
from wedding.styles.colors import Color, TextColor


def wedding_google_photos() -> rx.Component:
    return rx.vstack(
        title_section("Albúm de fotos"),
        icon_section(icon=icon.ICON_CAMERA.value),
        button_date(button_name="ABRIR ALBÚM", url=url.GOOGLE_FOTOS_URL),
        main_text(text=utils.photo_section),
        button_photo(),
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
            background=TextColor.DEFAULT.value,
            # border_radius=Size.MEDIUM_SMALL.value,
            text_align="center",
            margin_bottom=Size.DEFAULT.value,
            box_shadow="""
                inset 0 -3em 3em rgba(0, 0, 0, 0.1),
                0.3em 0.3em 1em rgba(0, 0, 0, 0.3)
            """,
            class_name="rounded-t-lg",
        ),
        href=url,
        is_external=True,
    )


def button_photo() -> rx.Component:
    return rx.link(
        rx.button(
            "Abrir álbum",
            margin_bottom=Size.DEFAULT.value,
            box_shadow="""
        inset 0 -3em 3em rgba(0, 0, 0, 0.1),
        0.3em 0.3em 1em rgba(0, 0, 0, 0.3)
        """,
        ),
        href=url.GOOGLE_FOTOS_URL,
        is_external=True,
    )
