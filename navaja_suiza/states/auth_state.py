import reflex as rx


class AuthState(rx.State):
    users: dict[str, str] = {
        "admin@reflex.com": "password123"
    }
    in_session: bool = True

    @rx.event
    def sign_up(self, form_data: dict[str, str]):
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "")
        if not email or not password:
            yield rx.toast(
                "Correo electrónico y contraseña son requeridos.",
                duration=3000,
            )
            return
        if email in self.users:
            yield rx.toast(
                "Este correo electrónico ya está en uso.",
                duration=3000,
            )
        else:
            self.users[email] = password
            self.in_session = True
            yield rx.toast(
                "¡Cuenta creada exitosamente!",
                duration=3000,
            )
            return rx.redirect("/")

    @rx.event
    def sign_in(self, form_data: dict[str, str]):
        email = form_data.get("email", "").strip()
        password = form_data.get("password", "")
        if not email or not password:
            yield rx.toast(
                "Correo electrónico y contraseña son requeridos.",
                duration=3000,
            )
            return
        if (
            email in self.users
            and self.users[email] == password
        ):
            self.in_session = True
            yield rx.toast(
                "¡Inicio de sesión exitoso!", duration=3000
            )
            return rx.redirect("/")
        else:
            self.in_session = False
            yield rx.toast(
                "Correo electrónico o contraseña inválidos.",
                duration=3000,
            )

    @rx.event
    def sign_out(self):
        self.in_session = False
        yield rx.toast("Sesión cerrada.", duration=3000)
        return rx.redirect("/sign-in")

    @rx.event
    def check_session(self):
        if not self.in_session:
            return rx.redirect("/sign-in")
        return