import reflex as rx
from navaja_suiza.states.auth_state import AuthState


def sign_up_card():
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Crear una Cuenta",
                class_name="font-semibold tracking-tight text-2xl text-gray-100",
            ),
            rx.el.p(
                "Ingresa tu correo electrónico para crear tu cuenta.",
                class_name="text-sm text-gray-400 font-medium",
            ),
            class_name="flex flex-col text-center mb-6",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.label(
                    "Correo Electrónico",
                    class_name="text-sm font-medium leading-none text-gray-300 mb-1",
                ),
                rx.el.input(
                    type="email",
                    placeholder="usuario@ejemplo.com",
                    name="email",
                    required=True,
                    class_name="flex h-10 w-full rounded-md border border-gray-600 bg-gray-700 px-3 py-2 text-sm text-gray-100 placeholder-gray-400 shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:border-blue-500",
                ),
                class_name="flex flex-col gap-1.5 mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Contraseña",
                    class_name="text-sm font-medium leading-none text-gray-300 mb-1",
                ),
                rx.el.input(
                    type="password",
                    name="password",
                    required=True,
                    class_name="flex h-10 w-full rounded-md border border-gray-600 bg-gray-700 px-3 py-2 text-sm text-gray-100 placeholder-gray-400 shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:border-blue-500",
                ),
                class_name="flex flex-col gap-1.5 mb-6",
            ),
            rx.el.button(
                "Crear Cuenta",
                type="submit",
                class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors text-white shadow bg-blue-600 hover:bg-blue-700 h-10 px-4 py-2 w-full",
            ),
            rx.el.div(
                rx.el.span(
                    "¿Ya tienes una cuenta?",
                    class_name="text-sm text-gray-400 font-medium",
                ),
                rx.el.a(
                    "Iniciar Sesión",
                    href="/sign-in",
                    class_name="text-sm text-blue-400 font-medium underline hover:text-blue-300 transition-colors",
                ),
                class_name="flex flex-row gap-2 mt-4 justify-center",
            ),
            class_name="flex flex-col gap-4",
            on_submit=AuthState.sign_up,
        ),
        class_name="p-8 rounded-xl bg-gray-800 flex flex-col gap-6 shadow-xl border border-gray-700 text-gray-100 w-full max-w-md",
    )