pipeline {
    agent { 
        docker { 
            image 'python:latest'
            args '-u root'
        }
    }
    stages {
        stage('build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('unit tests'){
            steps {
                sh 'python -m unittest test_volume_cuboid.py'
            }
        }
    }
}
