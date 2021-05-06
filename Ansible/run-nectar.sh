
# set up deploy instance
. ./CCC-grp-30-openrc.sh; ansible-playbook deploy_instance.yaml

# set up environment 
. ./CCC-grp-30-openrc.sh; ansible-playbook --ask-become-pass set_environment.yaml
