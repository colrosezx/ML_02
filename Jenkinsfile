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
                    echo Запуск сервиса предсказания выживания на Титанике...
                    start /B C:\\Users\\ADM\\AppData\\Local\\Programs\\Python\\Python313\\python.exe app.py
                    echo Сервис запущен на http://localhost:5000
                    echo Для проверки используйте: curl -X POST http://localhost:5000/predict -H "Content-Type: application/json" -d "{\\"Pclass\\":1,\\"Name\\":\\"Ann\\", \\"Sex\\":\\"male\\", \\"Age\\":30, \\"SibSp\\":0, \\"Parch\\":0, \\"Fare\\":71.2833, \\"Embarked\\":\\"S\\"}"
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
                }
            }
        }
    }
}
В\