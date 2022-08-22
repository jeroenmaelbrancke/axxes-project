pipeline {
    agent { 
        docker { 
            image 'python:latest'
            args '-u root --entrypoint='
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
