import reflex as rx


def flowers_mobile(image: str, margin_type: bool = True) -> rx.Component:
    return rx.mobile_only(
        rx.cond(
            margin_type,
            rx.image(
                src=image,
                width="100%",
                height="100%",
                flex_shrink="0",
                margin_bottom="-150px",
                z_index="990",
            ),
            rx.image(
                src=image,
                width="100%",
                height="100%",
                flex_shrink="0",
                margin_top="-140px",
                z_index="990",
            ),
        )
    )
