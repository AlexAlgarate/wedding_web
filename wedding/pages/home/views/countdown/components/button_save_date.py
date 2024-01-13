import reflex as rx

from wedding.styles import Size
from wedding.styles.colors import Color


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
                "background": "",
            },
        ),
        href=url,
        is_external=True,
    )


# def button_date(url: str) -> rx.Component:
#     return rx.button(
#         rx.html(
#             url,
#             width="100%",
#             font_size=[
#                 Size.DEFAULT.value,
#                 Size.DEFAULT.value,
#                 Size.DEFAULT.value,
#                 Size.LARGE.value,
#                 Size.LARGE.value,
#             ],
#         ),
#         padding=Size.DEFAULT.value,
#         color=Color.BACKGROUND.value,
#         background=Color.TEXT_DEFAULT.value,
#         border_radius=Size.VERY_BIG.value,
#         text_align="center",
#         margin_bottom=Size.DEFAULT.value,
#         box_shadow=f"2px 1.5px 3px 1px {Color.DEFAULT_OPACITY.value}",
#         _hover={
#             "background": "",
#         },
#     )


# def button_date(url: str) -> rx.Component:
#     return rx.button(
#         rx.html(
#             url,
#             width="100%",
#             font_size=[
#                 Size.DEFAULT.value,
#                 Size.DEFAULT.value,
#                 Size.DEFAULT.value,
#                 Size.LARGE.value,
#                 Size.LARGE.value,
#             ],
#         ),
#         padding=Size.DEFAULT.value,
#         background=Color.BUTTON_BG.value,
#         border_radius=Size.MEDIUM_SMALL.value,
#         width="100%",
#         text_align="center",
#         margin_bottom=Size.DEFAULT.value,
#         box_shadow="""
#         inset 0 -3em 3em rgba(0, 0, 0, 0.1),
#         0.3em 0.3em 1em rgba(0, 0, 0, 0.3)
#         """,
#     )
