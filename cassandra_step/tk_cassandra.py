# -*- coding: utf-8 -*-

"""The graphical part of a Cassandra step"""

import seamm
from seamm_util import ureg, Q_, units_class  # noqa: F401
import seamm_widgets as sw  # noqa: F401
import pprint  # noqa: F401
import tkinter as tk
import tkinter.ttk as ttk


class TkCassandra(seamm.TkNode):
    """The graphical part of a Cassandra step in a MolSSI flowchart.

    """

    def __init__(
        self,
        tk_flowchart=None,
        node=None,
        canvas=None,
        x=None,
        y=None,
        w=None,
        h=None
    ):
        '''Initialize a node

        Keyword arguments:
        '''
        self.dialog = None

        super().__init__(
            tk_flowchart=tk_flowchart,
            node=node,
            canvas=canvas,
            x=None,
            y=None,
            w=200,
            h=50
        )

    def create_dialog(self):
        """Create the dialog!"""
        frame = super().create_dialog('Edit Cassandra Step')

        # The tabbed notebook
        notebook = ttk.Notebook(frame)
        notebook.pack(side='top', fill=tk.BOTH, expand=1)
        self._widget['notebook'] = notebook

        # # Main frame holding the widgets
        self["general"] = ttk.Frame(notebook)
        notebook.add(self["general"], text='General information', sticky=tk.NW)
        self["thermo_state"] = ttk.Frame(notebook)
        notebook.add(
            self["thermo_state"], text='Thermodynamic state', sticky=tk.NW
        )
        self["initial_config"] = ttk.Frame(notebook)
        notebook.add(
            self["initial_config"], text='Initial configuration', sticky=tk.NW
        )
        self["energy_calc"] = ttk.Frame(notebook)
        notebook.add(
            self["energy_calc"], text='Energy calculation', sticky=tk.NW
        )
        self["probability"] = ttk.Frame(notebook)
        notebook.add(self["probability"], text='Probabilities', sticky=tk.NW)
        self["outputs"] = ttk.Frame(notebook)
        notebook.add(self["outputs"], text='Outputs', sticky=tk.NW)
        self["other"] = ttk.Frame(notebook)
        notebook.add(self["other"], text='Other', sticky=tk.NW)

        row = 0
        P = self.node.parameters
        for k, v in P.items():
            # print(v['group'], k)
            self[k] = P[k].widget(self[v["group"]])
            self[k].grid(row=row, column=0, sticky=tk.W)
            row += 1

            # sw.align_labels(
            #     (self[k])
            # )

        # bindings...

    def right_click(self, event):
        """Probably need to add our dialog...
        """

        super().right_click(event)
        self.popup_menu.add_command(label="Edit..", command=self.edit)

        self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
