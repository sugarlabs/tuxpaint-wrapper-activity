import os
import subprocess

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import GLib
from gi.repository import Gtk

from sugar3.activity.activity import Activity


class TuxPaintLauncher(Activity):

    def __init__(self, handle):
        # Initialize the parent
        Activity.__init__(self, handle)

        self.max_participants = 1

        hbox = Gtk.HBox()
        self.set_canvas(hbox)
        self.show_all()
        options = ['tuxpaint', '--nolockfile', '--fullscreen=native', '--noprint']
        doc_path = self.get_documents_path()
        if doc_path is not None:
            options.extend(('--savedir', doc_path))
        proc = subprocess.Popen(options)

        # Stay alive with a blank window mapped for at least 60 seconds
        # so that the shell knows that we launched
        GLib.timeout_add_seconds(60, Gtk.main_quit)
        # but get rid of that window if the child exits beforehand
        GLib.child_watch_add(proc.pid, Gtk.main_quit)

    def get_documents_path(self):
        """Gets the path of the DOCUMENTS folder

        If xdg-user-dir can not find the DOCUMENTS folder it returns
        $HOME, which we omit. xdg-user-dir handles localization
        (i.e. translation) of the filenames.

        Returns: Path to $HOME/DOCUMENTS or None if an error occurs

        Code from src/jarabe/journal/model.py
        """
        try:
            pipe = subprocess.Popen(['xdg-user-dir', 'DOCUMENTS'],
                                    stdout=subprocess.PIPE)
            documents_path = os.path.normpath(pipe.communicate()[0].strip())
            if os.path.exists(documents_path) and \
                    os.environ.get('HOME') != documents_path:
                return documents_path
        except OSError, exception:
            if exception.errno != errno.ENOENT:
                logging.exception('Could not run xdg-user-dir')
        return None

