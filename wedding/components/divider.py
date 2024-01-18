import reflex as rx

from wedding.styles.colors import Color

# def divider(section=True,width: str = "65%") -> rx.Component:
#     return rx.divider(
#         orientation="horizontal",
#         variant="solid",
#         border_color=Color.TEXT_DEFAULT.value,
#         width=width,
#         padding_top="1.25em",
#     )


def divider(width: str = "65%") -> rx.Component:
    return rx.divider(
        orientation="horizontal",
        variant="solid",
        border_color=Color.TEXT_DEFAULT.value,
        width=width,
    )
