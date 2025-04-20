pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                bat 'C:\\Users\\ADM\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe install pandas scikit-learn flask'
            }
        }
        
        stage('Train model') {
            steps {
                bat 'C:\\Users\\ADM\\AppData\\Local\\Programs\\Python\\Python313\\python.exe main.py'
            }
            post {
                success {
                    archiveArtifacts artifacts: 'model.pkl,metrics.txt', fingerprint: true
                }
            }
        }
    }
    
    post {
        always {
            script {
                if (fileExists('metrics.txt')) {
                    def metrics = readFile 'metrics.txt'
                    echo "Model metrics:\n${metrics}"
                } else {
                    echo "Metrics file not found - training probably failed"
                }
            }
        }
    }
}