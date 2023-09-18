import json
from ansible.module_utils.basic import AnsibleModule
import sys
import socket
def main():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required=True, type='str'),
            age  = dict(required=True, type='str'),
        )
    )

    name = module.params['name']
    age = module.params['age']
    hostname = socket.gethostname()
    print(hostname)

    data = dict(
        output="hostname is {} : your data has stored successfully :-) ".format(hostname),
    )
    try:
       # file = open("/var/lib/awx/projects/_36__rayank_git_project/userdata.txt","r")
        print(name,age)
       # file.write(name+ "," + age + "\n")
        module.exit_json(changed=True, success=data,msg=data)
    except Exception as e:
        module.fail_json(msg='something went wrong. :-(')


if __name__ == '__main__':
    main()
