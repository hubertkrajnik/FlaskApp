pipeline {
    agent any

    parameters {
        choice(
            name: 'REMOTE_USER',
            choices: ['root', 'hubert', 'julian'],
            description: 'Wybierz użytkownika do połączenia SSH'
        )
        choice(
            name: 'REMOTE_HOST_IP',
            choices: ['10.10.10.10', '10.10.10.20', '192.168.206.140'],
            description: 'Wybierz IP serwera, z którym chcesz się połączyć'
        )
    }

    stages {
        stage('Check SSH Connection') {
            steps {
                script {
                    sshagent (credentials: ['my-ssh-fedora']) {
                        sh """
                            echo "Łączę się z hostem..."
                            ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST_IP} echo "Połączenie udane!"
                        """
                    }
                }
            }
        }
        stage('ls -la on the remote host') {
            steps {
                script {
                    sshagent (credentials: ['my-ssh-fedora']) {
                        sh 'ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST_IP} ls -la /home/hubert'
                    }   
                }
            }
        }
        stage('Operating System show') {
            steps {
                script {
                    sshagent (credentials: ['my-ssh-fedora']) {
                        sh 'ssh -o StrictHostKeyChecking=no ${REMOTE_USER}@${REMOTE_HOST_IP} hostnamectl'
                    }   
                }
            }
        }
    }
}