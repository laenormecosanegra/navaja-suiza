import reflex as rx
from navaja_suiza.states.main_state import MainState
from navaja_suiza.components.sidebar import sidebar
from navaja_suiza.components.mobile_header import mobile_header
from navaja_suiza.components.books_page import books_page
from navaja_suiza.components.agenda_page import agenda_page
from navaja_suiza.components.calendar_page import calendar_page
from navaja_suiza.components.chat_page import chat_page


def protected_page() -> rx.Component:
    return rx.el.div(
        sidebar(),
        rx.cond(
            MainState.is_mobile_menu_open,
            rx.el.div(
                class_name="fixed inset-0 bg-black/60 z-40 md:hidden",
                on_click=MainState.close_mobile_menu,
            ),
        ),
        rx.el.div(
            mobile_header(),
            rx.el.main(
                rx.match(
                    MainState.current_page,
                    ("books", books_page()),
                    ("agenda", agenda_page()),
                    ("calendar", calendar_page()),
                    ("chat", chat_page()),
                    rx.el.p(
                        "Página no encontrada",
                        class_name="text-red-500 text-xl p-8",
                    ),
                ),
                class_name="flex-grow h-full overflow-y-auto bg-gray-900",
            ),
            class_name="md:pl-64 flex flex-col w-full h-screen",
        ),
        class_name="flex min-h-screen bg-gray-900 font-['Inter']",
    )