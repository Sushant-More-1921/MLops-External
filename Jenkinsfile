pipeline {
    agent any

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
                            if not exist venv (
                                python -m venv venv
                            )
                            call venv\\Scripts\\activate.bat
                            python -m pip install --upgrade pip
                            pip install -r requirements.txt
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
                            pytest -v --junitxml=reports/pytest-results.xml
                        '''
                    } else {
                        bat '''
                            call venv\\Scripts\\activate.bat
                            pytest -v --junitxml=reports/pytest-results.xml
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
