"""Sovelluksen käyttöliittymästä vastaava luokka."""

from ui.login_view import LoginView
from ui.counter_view import CounterView
from ui.create_user_view import CreateUserView
from services.counter_service import counter_service

#UI was developed with reference to the sample repository "todo-app".

class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka."""

    def __init__(self, root):
        """Luokan konstruktori. Luo uuden käyttöliittymästä vastaavan luokan.

        Args:
            root:
            TKinter-elementti, jonka sisään näkymä alustetaan.
        """
        self._root = root
        self._root.geometry("700x700")
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän."""
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_create_user_view,
            self._show_counter_view
        )

        self._current_view.pack()

    def _show_counter_view(self):
        self._hide_current_view()

        user = counter_service.get_user()

        self._current_view = CounterView(self._root, self._show_login_view, user)
        self._current_view.pack()

    def _show_create_user_view(self):

        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._show_counter_view,
            self._show_login_view
        )

        self._current_view.pack()