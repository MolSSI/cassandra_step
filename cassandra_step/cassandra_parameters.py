# -*- coding: utf-8 -*-
"""Control parameters for the Cassandra step in a MolSSI flowchart"""

import logging
import molssi_workflow
import pprint

logger = logging.getLogger(__name__)


class Cassandra_Parameters(molssi_workflow.Parameters):
    """The control parameters for Cassandra

    This is a dictionary of Parameters objects, which themselves are
    dictionaries.  You need to replace the 'time' example below with one or
    more definitions of the control parameters for your plugin and application.

    The fields of each Parameter are:

        default: the default value of the parameter, used to reset it
        kind: one of 'integer', 'float', 'string', 'boolean' or 'enum'
        default_units: the default units, used for reseting the value
        enumeration: a tuple of enumerated values. See below for more.
        format_string: a format string for 'pretty' output
        description: a short string used as a prompt in the GUI
        help_text: a longer string to display as help for the user

    While the 'kind' of a variable might be a numeric value, it may still have
    enumerated values, such as 'normal', 'precise', etc. In addition, any
    parameter can be set to a variable of expression, indicated by having '$'
    as the first character in the field.
    """

    parameters = {
        "run_name": {
            "value": 'Run_name',
            "default": 'my_simulation',
            "kind": "string",
            "format_string": "s",
            "enumeration": tuple(),
            "description": "The simulation run name",
            "help_text": ("Files will be named using this name")
        },

        "sim_length": {
            "default": 5000000,
            "kind": "integer",
            "default_units": None,
            "enumeration": tuple(),
            "format_string": "d",
            "description": "Number of steps:",
            "help_text": ("Total number of Monte Carlo steps in a simulation.")
        },

        "temperature": {
            "default": 450,
            "kind": "float",
            "default_units": "K",
            "enumeration": tuple(),
            "format_string": ".1f",
            "description": "Temperature: ",
            "help_text": ("System temperature")
        },

        "MCF": {
            "value": 'MCF file',
            "default": '/a/b/c/methane.mcf',
            "kind": "string",
            "format_string": "s",
            "enumeration": tuple(),
            "description": "MCF location: ",
            "help_text": ("The file containing a molecule topology")
        },

        "num_mols": {
            "default": 1,
            "kind": "integer",
            "default_units": None,
            "enumeration": tuple(),
            "format_string": "d",
            "description": "Number of molecules: ",
            "help_text": ("Number of molecules")
        },

        "box_shape": {
            "value": 'Cubic',
            "default": 'Cubic',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'Cubic',
                'Orthogonal',
                'Triclinic'
            ),
            "description": "Box shape: ",
            "help_text": ("The shape of the simulation box")
        },

        "vdw": {
            "value": 'LJ',
            "default": 'LJ',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'LJ',
                'Mie',
            ),
            "description": "VDW potential ",
            "help_text": ("The functional form for Van der Waals interaction computation")
        },

        "vdw_truncation": {
            "value": 'Standard tail correction',
            "default": 'Standard tail correction',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'Standard long tail correction',
                'Spline around cut-off',
                'Truncate potential and shift',
                'Truncate',
            ),
            "description": "VDW potential ",
            "help_text": ("The functional form for Van der Waals interaction computation")
        },

        "vdw_cutoff": {
            "value": 16.0,
            "default": 16.0,
            "kind": "float",
            "units": "angstroms",
            "default_units": "angstroms",
            "format_string": ".2f",
            "description": "VDW cutoff: ",
            "help_text": "The cut-off radius for Van der Waals interactions"
        },

        "electrostatics": {
            "value": 'Ewald',
            "default": 'Ewald',
            "kind": "string",
            "format_string": "s",
            "enumeration": (
                'Ewald',
                'Damped shifted force',
                'Truncate',
                'None',
            ),
            "description": "Electrostatics: ",
            "help_text": ("Method to compute electrostatics")
        },

        "electrostatic_cutoff": {
            "value": 16.0,
            "default": 16.0,
            "kind": "float",
            "units": "angstroms",
            "default_units": "angstroms",
            "format_string": ".2f",
            "description": "Electrostatic cutoff: ",
            "help_text": "The cut-off for electrostatic interactions"
        },

        "ewald_accuracy": {
            "value": 0.00001,
            "default": 0.00001,
            "kind": "float",
            "units": "angstroms",
            "default_units": "angstroms",
            "format_string": ".2f",
            "description": "Ewald sum accuracy: ",
            "help_text": "The accuracy of the ewald recipriocal component",
        },

        "dsf_alpha": {
            "value": 0.2,
            "default": 0.2,
            "kind": "float",
            "units": "angstroms",
            "default_units": "angstroms",
            "format_string": ".2f",
            "description": "DSF damping factor: ",
            "help_text": "The damping factor of the DSF method",
        },

        "dim_xx": {
            "value": 40.0,
            "default": 40.0,
            "kind": "float",
            "units": "angstroms",
            "default_units": "angstroms",
            "format_string": ".2f",
            "description": "XX dimension:",
            "help_text": "The XX component of the H matrix"
        },

        "alpha": {
            "value": 10.0,
            "default": 10.0,
            "kind": "float",
            "units": "degrees",
            "default_units": "degrees",
            "format_string": ".2f",
            "description": "Degrees",
            "help_text": "The alpha angle between two basis vectors"
        },

        "translation": {
            "value": 0.5,
            "default": 0.5,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Translation probability",
            "help_text": "Probability of a center-of-mass translation"
        },

        "rotation": {
            "value": 0.5,
            "default": 0.5,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Rotation probability",
            "help_text": "Probability of rotation"
        },

        "angle": {
            "value": 0.5,
            "default": 0.5,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Angle probability",
            "help_text": "Probability of an angle change"
        },

        "dihedral": {
            "value": 0.5,
            "default": 0.5,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Dihedral probability",
            "help_text": "Probability of a dihedral change"
        },

        "regrowth": {
            "value": 0.5,
            "default": 0.5,
            "kind": "float",
            "default_units": None,
            "format_string": ".2f",
            "description": "Regrowth probability",
            "help_text": "Probability of a molecule regrowth"
        },

    }

    def __init__(self, data=parameters):
        """Initialize the instance, by default from the default
        parameters given in the class"""

        logger.debug('Cassandra_Parameters.__init__')

        super().__init__()

        logger.debug("Initializing Cassandra_Parameters object:")
        logger.debug("\n{}\n".format(pprint.pformat(data)))

        self.update(data)
