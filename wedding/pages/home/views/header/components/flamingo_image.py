import reflex as rx

import wedding.utils as utils
from wedding import icon


def flamingo_header() -> rx.Component:
    return rx.box(
        rx.image(
            src=icon.ICON_BOTH_FLAMINGOS.value,
            opacity="0.5",
            height="100%",
            width="100%",
            position="relative",
            alt=utils.alt_flamingo_right,
        ),
        display="flex",
        flex_direction="row",
        position="relative",
        width="82%",
    )
