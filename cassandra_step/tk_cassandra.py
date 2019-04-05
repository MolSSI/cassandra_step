
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

        sections = {'general_info': 'General information', 'thermo_state': 'Thermodynamic state', 'energy_calc': 'Energy calculation', 'probability': 'Probabilities', 'initial_config': 'Initial configuration', 'output_prop': 'Output properties', 'other': 'Other'}

        """Create the dialog!"""
        self.dialog = Pmw.Dialog(
            self.toplevel,
            buttons=('OK', 'Help', 'Cancel'),
            master=self.toplevel,
            title='Edit Energy step',
            command=self.handle_dialog)
        self.dialog.withdraw()
        P = self.node.parameters

        # The tabbed notebook
        notebook = ttk.Notebook(self.dialog.interior())
        notebook.pack(side='top', fill=tk.BOTH, expand=1)
        self._widget['notebook'] = notebook

        # Main frame holding the widgets
        frame = ttk.Frame(notebook)
        notebook.add(frame, text='General information', sticky=tk.NW)

        run_type_label = ttk.Label(frame, text='Run type: ')
        run_type = ttk.Combobox(
            frame,
            state='readonly',
            values=P["run_type"]["enumeration"])
        run_type_label.grid(row=0, column=0, columnspan=2, sticky=tk.E)
        run_type.grid(row=0, column=2, sticky=tk.W)

        sim_length_label = ttk.Label(frame, text='Simulation length: ')
        sim_length = ttk.Entry(frame, width=15)
        sim_length_units = ttk.Combobox(
            frame,
            state='readonly',
            values=P["sim_length_units"]["enumeration"])
        sim_length_label.grid(row=2, column=0, columnspan=2, sticky=tk.E)
        sim_length.grid(row=2, column=2, sticky=tk.W)
        sim_length_units.grid(row=2, column=3, columnspan=2, sticky=tk.E)

        seeds_label = ttk.Label(frame, text='Random seeds: ')
        seeds_label_one = ttk.Entry(frame, width=15)
        seeds_label_two = ttk.Entry(frame, width=15)
        seeds_label.grid(row=3, column=0, columnspan=2, sticky=tk.E)
        seeds_label_one.grid(row=3, column=2, sticky=tk.W)
        seeds_label_two.grid(row=3, column=3, columnspan=2, sticky=tk.E)

        freq_xyz_label = ttk.Label(frame, text='Coordinate output frequency: ')
        freq_xyz = ttk.Entry(frame, width=15)
        freq_xyz_label.grid(row=4, column=0, columnspan=2, sticky=tk.E)
        freq_xyz.grid(row=4, column=2, sticky=tk.W)

        freq_thermo_label = ttk.Label(frame, text='Property output frequency: ')
        freq_thermo = ttk.Entry(frame, width=15)
        freq_thermo_label.grid(row=5, column=0, columnspan=2, sticky=tk.E)
        freq_thermo.grid(row=5, column=2, sticky=tk.W)

        frame = ttk.Frame(notebook)
        notebook.add(frame, text='Thermodynamic state', sticky=tk.NW)
        frame = ttk.Frame(notebook)
        notebook.add(frame, text='Initial configuration', sticky=tk.NW)
        frame = ttk.Frame(notebook)
        notebook.add(frame, text='Energy calculation', sticky=tk.NW)
        frame = ttk.Frame(notebook)
        notebook.add(frame, text='Probabilities', sticky=tk.NW)
        frame = ttk.Frame(notebook)
        notebook.add(frame, text='Outputs', sticky=tk.NW)
        frame = ttk.Frame(notebook)
        notebook.add(frame, text='Other', sticky=tk.NW)

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
