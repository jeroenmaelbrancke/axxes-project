pipeline {
    agent {
        label 'docker'
    }
    stages {
        stage('build') {
            agent {
                docker {
                    image 'python:3.5.1'
                }
            }
            steps {
                sh 'python --version'
            }
        }
    }
}
