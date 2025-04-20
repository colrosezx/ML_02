pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/colrosezx/ML_02.git'
            }
        }
        
        stage('Install dependencies') {
            steps {
                sh 'pip install pandas scikit-learn'
            }
        }
        
        stage('Train model') {
            steps {
                sh 'python main.py'
            }
        }
        
        stage('Archive artifacts') {
            steps {
                archiveArtifacts artifacts: 'model.pkl', fingerprint: true
                archiveArtifacts artifacts: 'metrics.txt', fingerprint: true
            }
        }
    }
    
    post {
        always {
            script {
                def metrics = readFile 'metrics.txt'
                echo "Model metrics:\n${metrics}"
            }
        }
    }
}