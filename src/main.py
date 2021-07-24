# main.py
#
# Copyright 2021 Amit Prakash Ambasta
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, GLib, Adw

from .window import KontolWindow
from .settings import KontolSettings

class Kontol(Gtk.Application):

    def __init__(self, version):
        super().__init__(application_id='io.github.ambasta.kontol',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.__version = version
        GLib.set_application_name('kontol')

    def __on_show_about(self):
        about = Gtk.AboutDialog()
        about.set_transient_for(self.props.active_window)
        about.set_modal(True)
        about.set_version(self.__version)
        about.set_program_name("Kontol")
        about.set_logo_icon_name("io.github.ambasta.kontol")
        about.set_authors(["Amit Prakash Ambasta"])
        about.set_comments("Simple volume control")
        about.set_wrap_license(True)
        about.set_license_type(Gtk.License.GPL_3_0)
        about.set_copyright(_("Copyright 2021 Amit Prakash Ambasta"))
        about.set_website_label(_("GitHub"))
        about.set_website("https://github.com/ambasta/kontol")
        about.present()

    def __setup_actions(self):
        actions = [('show-about', self.__on_show_about, None)]

        for action, callback, parameter_type in actions:
            simple_action = Gio.SimpleAction.new(action, parameter_type)
            simple_action.connect('activate', callback)
            self.add_action(simple_action)

    def do_startup(self):
        Gtk.Application.do_startup(self)
        self.settings = KontolSettings()
        self.__setup_actions()

    def do_activate(self):
        window = self.props.active_window

        if not window:
            window = KontolWindow(application=self)
        window.present()


def main(version):
    app = Kontol("1.0.0")
    return app.run(sys.argv)
