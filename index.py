def lambda_handler(event, context):
    for i in range(10):
        print(i)
    print("Test lambda_handler ")
    return "Successfully completed"
