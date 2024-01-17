import reflex as rx

from wedding.styles import Size


def initials_navbar(initials: str) -> rx.Component:
    return rx.text(
        initials,
        # text_align="center",
        font_size=[
            Size.BIG_TITLES.value,
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
            Size.MEDIUM_BIGGER.value,
        ],
        # font_size=[
        #     FontHeight.MEDIUM.value,
        #     FontHeight.BIG.value,
        #     FontHeight.BIG.value,
        #     FontHeight.BIG.value,
        #     FontHeight.BIG.value,
        # ],
        height="100%",
    )
