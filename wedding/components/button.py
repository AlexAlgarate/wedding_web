import reflex as rx

from wedding.styles import Color, Size


def button(button_name: str, url: str, **args) -> rx.Component:
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
            background=Color.TITLE.value,
            border_radius="5px",
            border="2px solid #4F1F7E",
            text_align="center",
            margin_bottom=Size.DEFAULT.value,
            _hover={
                "background": "rgba(80, 69, 135, 0.91)",
            },
        ),
        href=url,
        is_external=True,
    )
