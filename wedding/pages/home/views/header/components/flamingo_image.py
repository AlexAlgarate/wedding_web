import reflex as rx


def flamingo_header() -> rx.Component:
    return rx.box(
        rx.image(
            src="/icons/old_icons/both_flamingos_2.png",
            opacity="0.5",
            height="100%",
            width="100%",
            position="relative",
            # alt=utils.alt_flamingo_right,  # Eliminado
        ),
        display="flex",
        flex_direction="row",
        position="relative",
        width="82%",
    )
