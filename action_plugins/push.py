from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase



class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        if task_vars is None:
            task_vars = dict()
        result = super(ActionModule, self).run(tmp, task_vars)
        API = self._task.args.get('API', None)
        text = self._task.args.get('text', None)       
        new_module_args = dict()
        new_module_args.update(
            dict(
                API=API,
                text=text,               
            ),
        )
        result.update(
            self._execute_module(
                module_name='push',
                module_args=new_module_args,
            )
        )
        return result
