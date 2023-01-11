def call (Map config = [:]){
	sh "sed -i 's/web_server_ip_address/$config.web_server_ip_address/g' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/web_server.yaml"
	ansiblePlaybook become: true, disableHostKeyChecking: true, installation: 'Ansible', inventory: 'Ansible_for_Jenkins/hosts', playbook: 'Ansible_for_Jenkins/InstallLifeRay.yml'
}
