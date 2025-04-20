pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                bat 'C:\\Users\\ADM\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\pip.exe install pandas scikit-learn flask waitress'
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

        stage('Deploy service') {
            steps {
                bat '''
                    echo Запуск Flask-сервиса...
                    start /B C:\\Users\\ADM\\AppData\\Local\\Programs\\Python\\Python313\\python.exe app.py
                    echo Сервис запущен на http://localhost:5000
                '''
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
        success {
            echo 'Flask service deployed successfully!'
            echo 'API endpoint: http://localhost:5000/predict'
        }
    }
}