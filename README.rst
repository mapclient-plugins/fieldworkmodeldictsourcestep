Fieldwork Model Dict Source Step
================================

MAP Client plugin to read in a list of named fieldwork models and output a dictionary of fieldwork models.

Require
-------

-  GIAS2 : https://bitbucket.org/jangle/gias2

Inputs
------

None

Output
------

* **ju#fieldworkmodeldict** : A dictionary of model names (str) mapping to fieldwork model instances

Configuration
-------------

*  **identifier** : Unique name for the step.
*  **Config File** : The file path of an .ini configuration file containing the names and file paths of the fieldwork models to be loaded.

Usage
-----
This step is used to read in a set of Fieldwork models at once. It currently relies on reading an INI file containing the filenames of the fieldwork models to be read. An example INI file can be found in the same directory as this readme. Each entry in the INI file should be::

    [model_name]
    geof=/path/to/geof_file.geof
    ens=/path/to/ens_file.ens
    mesh=/path/to/mesh_file.mesh