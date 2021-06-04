'''
MAP Client Plugin Step
'''
import json

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint
from mapclientplugins.fieldworkmodeldictsourcestep.configuredialog import ConfigureDialog

import os
import configobj
from gias2.fieldwork.field import geometric_field


class FieldworkModelDictSourceStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be a helpful starting point
    for new steps.
    '''

    def __init__(self, location):
        super(FieldworkModelDictSourceStep, self).__init__('Fieldwork Model Dict Source', location)
        self._configured = False  # A step cannot be executed until it has been configured.
        self._category = 'Source'
        # Add any other initialisation code here:
        # Ports:
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'ju#fieldworkmodeldict'))
        # Config:
        self._config = {}
        self._config['identifier'] = ''
        self._config['Config File'] = '.ini'

        self._modelPathDict = None
        self._modelDict = None  # ju#fieldworkmodeldict

    def execute(self):
        '''
        Add your code here that will kick off the execution of the step.
        Make sure you call the _doneExecution() method when finished.  This method
        may be connected up to a button in a widget for example.
        '''
        # Put your execute step code here before calling the '_doneExecution' method.
        self._parseConfig()
        self._loadModels()
        self._doneExecution()

    def getPortData(self, index):
        '''
        Add your code here that will return the appropriate objects for this step.
        The index is the index of the port in the port list.  If there is only one
        provides port for this step then the index can be ignored.
        '''
        return self._modelDict  # ju#fieldworkmodeldict

    def configure(self):
        '''
        This function will be called when the configure icon on the step is
        clicked.  It is appropriate to display a configuration dialog at this
        time.  If the conditions for the configuration of this step are complete
        then set:
            self._configured = True
        '''
        dlg = ConfigureDialog(self._main_window)
        dlg.setWorkflowLocation(self._location)
        dlg.identifierOccursCount = self._identifierOccursCount
        dlg.setConfig(self._config)
        dlg.validate()
        dlg.setModal(True)

        if dlg.exec_():
            self._config = dlg.getConfig()

        self._configured = dlg.validate()
        self._configuredObserver()

    def getIdentifier(self):
        '''
        The identifier is a string that must be unique within a workflow.
        '''
        return self._config['identifier']

    def setIdentifier(self, identifier):
        '''
        The framework will set the identifier for this step when it is loaded.
        '''
        self._config['identifier'] = identifier

    def serialize(self):
        '''
        Add code to serialize this step to string.  This method should
        implement the opposite of 'deserialize'.
        '''
        return json.dumps(self._config, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def deserialize(self, string):
        '''
        Add code to deserialize this step from string.  This method should
        implement the opposite of 'serialize'.
        '''
        self._config.update(json.loads(string))

        d = ConfigureDialog()
        d.setWorkflowLocation(self._location)
        d.identifierOccursCount = self._identifierOccursCount
        d.setConfig(self._config)
        self._configured = d.validate()

    def _parseConfig(self):
        """
        Read in the ini file
        """

        modelPathCfgPath = os.path.join(
            self._location,
            self._config['Config File'],
        )
        print('config files: {}'.format(modelPathCfgPath))
        if (modelPathCfgPath is None) or (len(modelPathCfgPath) == 0):
            raise RuntimeError('Config File must be defined')

        self._modelPathDict = configobj.ConfigObj(
            infile=modelPathCfgPath,
            raise_errors=True,
            unrepr=False
        )

        if (self._modelPathDict is None) or (len(self._modelPathDict) == 0):
            raise RuntimeError('No model file paths defined')

        print('model paths: {}'.format(self._modelPathDict))

    def _loadModels(self):
        self._modelDict = {}
        for modelName in self._modelPathDict:

            gpath = os.path.join(self._location, self._modelPathDict[modelName].get('geof'))
            epath = os.path.join(self._location, self._modelPathDict[modelName].get('ens'))
            mpath = os.path.join(self._location, self._modelPathDict[modelName].get('mesh'))

            print('loading {} from:'.format(modelName))
            print('{}\n{}\n{}\n'.format(gpath, epath, mpath))

            if (gpath is None) or (epath is None) or (mpath is None):
                raise RuntimeError('Invalid config file format')

            model = geometric_field.load_geometric_field(gpath, epath, mpath)
            self._modelDict[modelName] = model
