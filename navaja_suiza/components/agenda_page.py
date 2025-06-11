import reflex as rx
from navaja_suiza.states.main_state import MainState


def contact_card(contact: dict[str, str]) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                contact["name"],
                class_name="text-lg font-semibold text-gray-100",
            ),
            rx.cond(
                contact["phone"],
                rx.el.p(
                    rx.icon(
                        tag="phone",
                        class_name="h-4 w-4 mr-1 inline text-gray-400",
                    ),
                    contact["phone"],
                    class_name="text-sm text-gray-300",
                ),
            ),
            rx.cond(
                contact["email"],
                rx.el.p(
                    rx.icon(
                        tag="mail",
                        class_name="h-4 w-4 mr-1 inline text-gray-400",
                    ),
                    contact["email"],
                    class_name="text-sm text-gray-300",
                ),
            ),
            class_name="flex-grow",
        ),
        rx.el.button(
            rx.icon(tag="trash-2", class_name="h-4 w-4"),
            on_click=lambda: MainState.remove_contact(
                contact["name"]
            ),
            class_name="text-red-500 hover:text-red-400 p-2 rounded-md",
            title="Eliminar Contacto",
        ),
        class_name="flex items-center p-4 bg-gray-800 border border-gray-700 rounded-lg shadow-sm hover:shadow-md transition-shadow",
    )


def add_contact_form() -> rx.Component:
    return rx.el.dialog(
        rx.el.div(
            rx.el.h2(
                "Añadir Nuevo Contacto",
                class_name="text-xl font-semibold mb-4 text-gray-100",
            ),
            rx.el.form(
                rx.el.label(
                    "Nombre:",
                    class_name="block text-sm font-medium text-gray-300",
                ),
                rx.el.input(
                    name="name",
                    placeholder="Nombre del Contacto",
                    default_value=MainState.new_contact_name,
                    class_name="w-full p-2 border border-gray-600 rounded-md mb-3 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 text-gray-100 placeholder-gray-400",
                ),
                rx.el.label(
                    "Teléfono:",
                    class_name="block text-sm font-medium text-gray-300",
                ),
                rx.el.input(
                    name="phone",
                    type="tel",
                    placeholder="Número de Teléfono",
                    default_value=MainState.new_contact_phone,
                    class_name="w-full p-2 border border-gray-600 rounded-md mb-3 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 text-gray-100 placeholder-gray-400",
                ),
                rx.el.label(
                    "Correo Electrónico:",
                    class_name="block text-sm font-medium text-gray-300",
                ),
                rx.el.input(
                    name="email",
                    type="email",
                    placeholder="Dirección de Correo Electrónico",
                    default_value=MainState.new_contact_email,
                    class_name="w-full p-2 border border-gray-600 rounded-md mb-4 focus:ring-blue-500 focus:border-blue-500 bg-gray-700 text-gray-100 placeholder-gray-400",
                ),
                rx.el.div(
                    rx.el.button(
                        "Cancelar",
                        on_click=MainState.toggle_add_contact_form,
                        class_name="px-4 py-2 bg-gray-600 text-gray-200 rounded-md hover:bg-gray-500 font-medium",
                    ),
                    rx.el.button(
                        "Añadir Contacto",
                        type="submit",
                        class_name="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 font-medium",
                    ),
                    class_name="flex justify-end space-x-2 mt-4",
                ),
                on_submit=MainState.add_contact,
                reset_on_submit=True,
            ),
            class_name="bg-gray-800 p-6 rounded-lg shadow-xl w-full max-w-md",
        ),
        open=MainState.show_add_contact_form,
        class_name="fixed inset-0 open:flex items-center justify-center bg-black bg-opacity-75 z-50 p-4",
    )


def agenda_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Mi Agenda",
                class_name="text-3xl font-bold text-gray-100",
            ),
            rx.el.button(
                rx.icon(
                    tag="circle_plus", class_name="mr-2"
                ),
                "Añadir Contacto",
                on_click=MainState.toggle_add_contact_form,
                class_name="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors font-medium",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        add_contact_form(),
        rx.cond(
            MainState.contacts.length() > 0,
            rx.el.div(
                rx.foreach(
                    MainState.contacts, contact_card
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4",
            ),
            rx.el.p(
                "Aún no hay contactos. ¡Añade algunos!",
                class_name="text-gray-400",
            ),
        ),
        class_name="p-6 md:p-8",
    )