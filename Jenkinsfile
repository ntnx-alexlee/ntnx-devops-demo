pipeline {
  agent {
    node {
      label 'master'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'Build using Nutanix CALM blueprint'
        sh '''cd /tmp/jenkins
rm -rf scripts
git clone https://github.com/ntnx-alexlee/ntnx-devops-demo.git scripts
python /tmp/jenkins/scripts/launch_blueprint.py'''
      }
    }
  }
}