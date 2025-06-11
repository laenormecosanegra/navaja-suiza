import reflex as rx
from navaja_suiza.states.main_state import MainState


def mobile_header() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.icon(
                tag="layout-dashboard",
                class_name="h-6 w-6 text-blue-500",
            ),
            rx.el.h2(
                "Navaja Suiza",
                class_name="text-xl font-bold text-gray-100 ml-2",
            ),
            class_name="flex items-center",
        ),
        rx.el.button(
            rx.icon(tag="menu", class_name="h-6 w-6"),
            on_click=MainState.toggle_mobile_menu,
            class_name="p-2 text-gray-300 hover:text-white",
        ),
        class_name="md:hidden flex items-center justify-between p-4 bg-gray-800 border-b border-gray-700 sticky top-0 z-30",
    )