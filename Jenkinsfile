pipeline {
    agent any
    stages {
        stage('Submit Stack') {
            steps {
                withCredentials([aws(accessKeyVariable:'AWS_ACCESS_KEY_ID', credentialsId:'aws-cresds1', secretKeyVariable:'AWS_SECRET_ACCESS_KEY')])
                {
                sh '''
                    aws cloudformation create-stack \
                      --stack-name a-testLambda \
                      --template-body file://template.yml --region 'us-east-2' \
                      --capabilities CAPABILITY_NAMED_IAM \
                      --parameters ParameterKey=FunctionName, ParameterValue=A-test-02
                    '''
                }
              }
             }
           }
         }