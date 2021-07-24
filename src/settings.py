from gi.repository  import Gio, GObject

class KontolSettings(Gio.Settings):

    enable_tray = GObject.Property(type=bool, default=False)

    def __init__(self,):
        super().__init__('io.github.ambasta.kontol')
        self.bind('enable_tray', self, 'enable_tray', Gio.SettingsBindFlags.DEFAULT)

    def get_is_tray_enabled(self):
        return self.get_boolean('enable_tray')
