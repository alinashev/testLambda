pipeline {
    agent any
    stages {
        stage('Submit Stack') {
            steps {
            sh "aws cloudformation create-stack --stack-name a-testLambda --template-body file://template.yml --region 'us-east-2'"
              }
             }
           }
         }