pipeline {
    agent { 
        docker { 
            image 'python:latest'
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip --version'
            }
        }
    }
}
