from src import test

def testHandler(event, context):
    print('Starting test')
    test.test()
    print('Completed test')
    return {
        "statusCode": 200,
        "body": "Completed init successfully"
    }
