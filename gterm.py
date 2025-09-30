import os
import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Vte", "2.91")
from gi.repository import Gtk, Vte, GLib, Pango, Gdk


class TerminalWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="gTerm")
        self.set_default_size(1200, 500)

        self.terminal = Vte.Terminal()
        self.add(self.terminal)

        # Set font
        fontdesc = Pango.FontDescription("Monospace 16")
        self.terminal.set_font(fontdesc)

        # Quit app when child (bash) exits
        self.terminal.connect("child-exited", self.on_child_exited)
        # Get the user's home directory
        home_dir = os.path.expanduser("~")

        # Spawn shell
        self.terminal.spawn_async(
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

    def on_key_pressed(self, widget, event):
        state = event.state
        keyval = event.keyval

        # Ctrl+Shift+C for copy
        if (state & Gdk.ModifierType.CONTROL_MASK) and \
           (state & Gdk.ModifierType.SHIFT_MASK) and \
           keyval == ord('C'):
            self.terminal.copy_clipboard()
            return True

        # Ctrl+Shift+V for paste
        if (state & Gdk.ModifierType.CONTROL_MASK) and \
           (state & Gdk.ModifierType.SHIFT_MASK) and \
           keyval == ord('V'):
            self.terminal.paste_clipboard()
            return True

        return False

    def on_child_exited(self, terminal, status):
        """Callback when the shell process exits"""
        Gtk.main_quit()


if __name__ == "__main__":
    win = TerminalWindow()
    win.connect("destroy", Gtk.main_quit)  # window close button
    win.show_all()
    Gtk.main()
