import reflex as rx

import wedding.utils as utils
from wedding.routes import IconRoutes as icon


def flamingo_header() -> rx.Component:
    return rx.box(
        rx.image(
            src=icon.ICON_FLAMINGO_RIGHT.value,
            opacity="0.5",
            height="50%",
            width="50%",
            position="relative",
            alt=utils.alt_flamingo_right,
        ),
        rx.image(
            src=icon.ICON_FLAMINGO_LEFT.value,
            opacity="0.5",
            height="50%",
            width="50%",
            position="relative",
            left="-1.5em",
            alt=utils.alt_flamingo_left,
        ),
        display="flex",
        flex_direction="row",
        position="relative",
        width="85%",
    )