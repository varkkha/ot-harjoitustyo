from tkinter import ttk, StringVar, constants
from services.counter_service import counter_service, InvalidCredentialsError

#UI was developed with reference to the sample repository "todo-app".

class LoginView:

    def __init__(self, root, handle_show_create_user_view, handle_login_success):
        self._root = root
        self._handle_show_create_user_view = handle_show_create_user_view
        self._handle_login_success = handle_login_success
        self._frame = None

        self._username_entry = None
        self._password_entry = None
        self._error_variable = StringVar()
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _login_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            #poista
            print(f"Yritetään kirjautua sisään käyttäjällä: {username}, salasanalla: {password}")
            #poista

            user = counter_service.login(username, password)

            #poista
            if user:
                print(f"Kirjautunut käyttäjä: {user.username}")
            #poista

            self._handle_login_success()
        except InvalidCredentialsError:
            self._show_error("Virheellinen käyttäjätunnus tai salasana.")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_username_field(self):
        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")

        self._username_entry = ttk.Entry(master=self._frame)

        username_label.grid(padx=5, pady=5, sticky=constants.W)
        self._username_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize_password_field(self):
        password_label = ttk.Label(master=self._frame, text="Salasana")

        self._password_entry = ttk.Entry(master=self._frame, show="*")

        password_label.grid(padx=5, pady=5, sticky=constants.W)
        self._password_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._error_variable = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._initialize_username_field()
        self._initialize_password_field()

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._login_handler
        )

        create_user_info_label = ttk.Label(
            master=self._frame,
            text="Eikö sinulla ole vielä käyttäjätunnusta? Luo tunnus tästä:"
        )

        create_user_button = ttk.Button(
            master=self._frame,
            text="Luo uusi käyttäjä",
            command=self._handle_show_create_user_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        login_button.grid(padx=5, pady=5, sticky=constants.EW)
        create_user_info_label.grid(padx=5, pady=(15, 5), sticky=constants.W)
        create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()