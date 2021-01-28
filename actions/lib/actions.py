import pytesla

from st2common.runners.base_action import Action

from .parsers import ResultSets


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.connection = pytesla.Connection(config['tesla_username'],
                                             config['tesla_password'])
        self.formatter = ResultSets()
