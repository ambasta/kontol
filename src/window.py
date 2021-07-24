# window.py
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

from gi.repository import Gtk, GObject

from .settings import KontolSettings

@Gtk.Template(resource_path='/io/github/ambasta/kontol/ui/window.ui')
class KontolWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'KontolWindow'

    label = Gtk.Template.Child()
    settings = GObject.Property(type=KontolSettings)

    def __init__(self, settings, **kwargs):
        super().__init__(**kwargs)
        self.settings = settings
        self.__setup_actions()

    def __setup_actions(self):
        builder = Gtk.Builder.new_from_resource('/io/github/ambasta/kontol/ui/help_overlay.ui')
        help_overlay = builder.get_object('help_overlay')
        self.set_help_overlay(help_overlay)

        settings_actions = [
            'enable_systray'
        ]

        for action in settings_actions:
            settings_action = self.settings.create_action(action)
            self.add_action(settings_action)

    
