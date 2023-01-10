def call (Map config = [:]){
	sh "sed 's/db_ip_address/$config.db_ip_address/i' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml"
	sh "sed 's/db_ssh_user/$config.db_ssh_user/i' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml"
	sh "sed 's/db_ssh_pass/$config.db_ssh_pass/i' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml"
	sh "sed 's/db_sudo_pass/$config.db_sudo_pass/i' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml"
	sh "sed 's/pgsql_db_name/$config.pgsql_db_name/i' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml"
	sh "sed 's/pgsql_user_name/$config.pgsql_user_name/i' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml"
	sh "sed 's/pgsql_pass/$config.pgsql_pass/i' ${pwd}/workspace/${JOB_NAME}/Ansible_for_Jenkins/host_vars/db_server.yaml"
}
