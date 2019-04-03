
# -*- coding: utf-8 -*-
"""The graphical part of a Cassandra step"""

import molssi_workflow
from molssi_workflow import ureg, Q_, units_class  # nopep8
import molssi_util.molssi_widgets as mw
import cassandra_step
import Pmw
import pprint  # nopep8
import tkinter as tk
import tkinter.ttk as ttk


class TkCassandra(molssi_workflow.TkNode):
    """The graphical part of a Cassandra step in a MolSSI flowchart.

    """

    def __init__(self, tk_workflow=None, node=None, canvas=None,
                 x=None, y=None, w=None, h=None):
        '''Initialize a node

        Keyword arguments:
        '''
        self.dialog = None

        super().__init__(tk_workflow=tk_workflow, node=node,
                         canvas=canvas, x=None, y=None, w=200, h=50)

    def create_dialog(self):
        """Create the dialog!"""

        self.dialog = Pmw.Dialog(
            self.toplevel,
            buttons=('OK', 'Help', 'Cancel'),
            defaultbutton='OK',
            master=self.toplevel,
            title='Edit Cassandra step',
            command=self.handle_dialog)

        self.dialog.withdraw()

        nb = Pmw.NoteBook(self.dialog.interior())
        p1 = nb.add('Page 1')

        nb.pack(padx=5, pady=5, fill=tk.BOTH, expand=1)

        # tk.Button(p1, text='This is text on page 1', fg='blue').pack(pady=40)
        # c = tk.Canvas(p2, bg='gray30')
        # w = c.winfo_reqwidth()
        # h = c.winfo_reqheight()
        # c.create_oval(10, 10, w - 10, h - 10, fill='DeepSkyBlue1')
        # c.create_text(w / 2, h / 2, text='This is text on a canvas', fill='white',
        #               font=('Verdana', 14, 'bold'))
        # c.pack(fill=tk.BOTH, expand=1)

        # self.dialog = Pmw.Dialog(
        #     self.toplevel,
        #     buttons=('OK', 'Help', 'Cancel'),
        #     defaultbutton='OK',
        #     master=self.toplevel,
        #     title='Edit Cassandra step',
        #     command=self.handle_dialog)
        # self.dialog.withdraw()

        #         # The information about widgets is held in self['xxxx'], i.e. this
        #         # class is in part a dictionary of widgets. This makes accessing
        #         # the widgets easier and allows loops, etc.

        #         # Create a frame to hold everything. This is always called 'frame'.
        #         self['frame'] = ttk.Frame(self.dialog.interior())
        #         self['frame'].pack(expand=tk.YES, fill=tk.BOTH)
        #         # Shortcut for parameters
        #         P = self.node.parameters

        # # *********************************

        #     # Frame to isolate widgets
        #         self['thermo_state'] = ttk.LabelFrame(
        #             self['frame'], borderwidth=4, relief='sunken',
        #             text='Thermodynamic state', labelanchor='n', padding=10
        #         )

        #         self['thermo_state'].pack(expand=tk.YES, fill=tk.BOTH)

        # # *********************************

        #         # Frame to isolate widgets
        #         self['general_info'] = ttk.LabelFrame(
        #             self['frame'], borderwidth=4, relief='sunken',
        #             text='General simulation information', labelanchor='n', padding=10
        #         )
        #         self['general_info'].pack(expand=tk.YES, fill=tk.BOTH)

        # # *********************************

        #         self['temperature'] = P['temperature'].widget(self['thermo_state'])
        #         self['num_mols'] = P['num_mols'].widget(self['thermo_state'])

        #         row = 0
        #         self['temperature'].grid(row=row, column=0, sticky=tk.W)
        #         row += 1
        #         self['num_mols'].grid(row=row, column=0, sticky=tk.W)

        # # *********************************

        #         self['run_name'] = P['run_name'].widget(self['general_info'])
        #         self['run_type'] = P['run_type'].widget(self['general_info'])

        #         row = 0
        #         self['run_name'].grid(row=row, column=0, sticky=tk.W)
        #         row += 1
        #         self['run_type'].grid(row=row, column=0, sticky=tk.W)

        # # *********************************

        #         mw.align_labels(
        #             (self['temperature'],
        #              self['num_mols'],
        #              self['run_name'],
        #              self['run_type']
        #              )
        #         )

        #         # The create the widgets
        #         # for key in P:
        #         #     self[key] = P[key].widget(self['frame'])

        #         # and lay them out
        #         self.reset_dialog()

    def reset_dialog(self, widget=None):
        """Layout the widgets in the dialog

        This initial function simply lays them out row by rows with
        aligned labels. You may wish a more complicated layout that
        is controlled by values of some of the control parameters.
        """

        # Remove any widgets previously packed
        # frame = self['frame']
        # for slave in frame.grid_slaves():
        #     slave.grid_forget()

        # # Shortcut for parameters
        # P = self.node.parameters

        # # keep track of the row in a variable, so that the layout is flexible
        # # if e.g. rows are skipped to control such as 'method' here
        # row = 0
        # widgets = []
        # for key in P:
        #     self[key].grid(row=row, column=0, sticky=tk.EW)
        #     widgets.append(self[key])
        #     row += 1

        # # Align the labels
        # mw.align_labels(widgets)
        pass

    def right_click(self, event):
        """Probably need to add our dialog...
        """

        super().right_click(event)
        self.popup_menu.add_command(label="Edit..", command=self.edit)

        self.popup_menu.tk_popup(event.x_root, event.y_root, 0)

    def edit(self):
        """Present a dialog for editing the Cassandra input
        """
        if self.dialog is None:
            self.create_dialog()

        self.dialog.activate(geometry='centerscreenfirst')

    def handle_dialog(self, result):
        """Handle the closing of the edit dialog

        What to do depends on the button used to close the dialog. If
        the user closes it by clicking the 'x' of the dialog window,
        None is returned, which we take as equivalent to cancel.
        """
        if result is None or result == 'Cancel':
            self.dialog.deactivate(result)
            return

        if result == 'Help':
            # display help!!!
            return

        if result != "OK":
            self.dialog.deactivate(result)
            raise RuntimeError(
                "Don't recognize dialog result '{}'".format(result))

        self.dialog.deactivate(result)
        # Shortcut for parameters
        P = self.node.parameters

        # Get the values for all the widgets. This may be overkill, but
        # it is easy! You can sort out what it all means later, or
        # be a bit more selective.
        for key in P:
            P[key].set_from_widget()

    def handle_help(self):
        """Not implemented yet ... you'll need to fill this out!"""
        print('Help not implemented yet for Cassandra!')
