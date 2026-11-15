pipeline {
    agent any

    environment {
        // Ensure Python and Python Scripts are available in PATH on Windows Jenkins agents
        PATH = "C:\\Users\\Sushant More\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\Sushant More\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking project source code'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            set "PATH=C:\\Users\\Sushant More\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\Sushant More\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;%PATH%"
                            if not exist venv (
                                python -m venv --system-site-packages venv
                            )
                            call venv\\Scripts\\activate.bat
                            python -m pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Run Pytest') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            python -m pytest -v --junitxml=reports/pytest-results.xml
                        '''
                    } else {
                        bat '''
                            set "PATH=C:\\Users\\Sushant More\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\Sushant More\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;%PATH%"
                            call venv\\Scripts\\activate.bat
                            python -m pytest -v --junitxml=reports/pytest-results.xml
                        '''
                    }
                }
            }
        }

        stage('Evidently Monitoring') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            . venv/bin/activate
                            python -m monitoring.evidently_monitor
                        '''
                    } else {
                        bat '''
                            set "PATH=C:\\Users\\Sushant More\\AppData\\Local\\Programs\\Python\\Python313;C:\\Users\\Sushant More\\AppData\\Local\\Programs\\Python\\Python313\\Scripts;%PATH%"
                            call venv\\Scripts\\activate.bat
                            python -m monitoring.evidently_monitor
                        '''
                    }
                }
            }
        }

        stage('Build Completed') {
            steps {
                echo 'Addition API pipeline completed successfully!'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'reports/pytest-results.xml'

            archiveArtifacts artifacts: 'reports/*.html',
                             allowEmptyArchive: true
        }

        success {
            echo 'Pipeline SUCCESS'
        }

        failure {
            echo 'Pipeline FAILED'
        }
    }
}
