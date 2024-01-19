import reflex as rx

from wedding.styles import Color, Size


def button(button_name: str, url: str) -> rx.Component:
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
            box_shadow=f"2px 1.5px 3px 1px {Color.DEFAULT_OPACITY.value}",
            _hover={
                "background": "rgba(125, 69, 135, 0.91)",
            },
        ),
        href=url,
        is_external=True,
    )
