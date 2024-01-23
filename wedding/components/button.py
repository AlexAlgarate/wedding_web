import reflex as rx

from wedding.styles import Color, Size


def button(button_name: str, url: str, **args) -> rx.Component:
    """
    Create a button link component.

    Parameters:
    - button_name (str): The text to display on the button.
    - url (str): The URL to which the button links.
    - **args: Additional keyword arguments for customizing the button's appearance.

    Returns:
    - rx.Component: A Reflex component representing the button link.
    """

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
                "background": "rgba(80, 69, 135, 0.81)",
                "box_shadow": "2px 1.5px 3px 1px rgba(80, 69, 135, 0.91)",
            },
        ),
        href=url,
        is_external=True,
    )
