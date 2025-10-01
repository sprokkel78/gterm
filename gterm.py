import os
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Vte", "2.91")
from gi.repository import Gtk, Vte, GLib, Pango, Gdk

# CREATE THE GTK APPLICATION
class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.sprokkel78.gterm")
        GLib.set_application_name("gTerm")

    def do_activate(self):
        global win
        win = Gtk.ApplicationWindow(application=self, title="gterm")

        win.set_default_size(1200, 500)

        terminal = Vte.Terminal()
        win.add(terminal)

        # Set font
        fontdesc = Pango.FontDescription("Monospace 16")
        terminal.set_font(fontdesc)

        # Quit app when child (bash) exits
        terminal.connect("child-exited", on_child_exited)

        # Get the user's home directory
        home_dir = os.path.expanduser("~")

        # Spawn shell
        terminal.spawn_async(
            Vte.PtyFlags.DEFAULT,
            home_dir,
            ["/bin/bash"],
            None,
            GLib.SpawnFlags.DEFAULT,
            None,
            None,
            -1,
            None,
            None,
            None
        )

        app = terminal.get_toplevel().get_application()
        win.connect("destroy", app.quit) # window close button
        win.show_all()

def on_child_exited(terminal, status):
   app = terminal.get_toplevel().get_application()
   if app:
       app.quit()

# START THE APPLICATION
def main():
    app = MyApplication()
    app.run(None)

if __name__ == "__main__":
    main()
