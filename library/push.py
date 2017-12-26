#!/usr/bin/python

import  json
from ansible.module_utils.basic import AnsibleModule
import requests

def main():
    module = AnsibleModule(argument_spec= dict( API = dict(required=True, type='str'), text = dict(required=True, type='str')))
    API = module.params['API']
    text = module.params['text']
    slack_data = {"text": "{0}".format(text)}
    try:                       
        response = requests.post(
            API, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )
        print (json.dumps({
        "message: " : "text sent"
    }))
    except Exception as em:
        print (json.dumps({
        "EXCEPTION: " : str(em)
        }))
    module.exit_json(changed=True, keyword=value)
    module.exit_json(changed=False, msg='error message', keyword=value)

if __name__ == '__main__':
    main()
