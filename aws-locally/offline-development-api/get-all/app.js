const dynamoDb = require('aws-sdk/clients/dynamodb');
exports.lambdaHandler = async (event, context) => {
    try {
        const params = {
            TableName: 'Game',
        };

        const docClient = exports.getDynamoDbDocumentClient();

        const response = await docClient.scan(params).promise();

        return {
            'statusCode': 200,
            'body': JSON.stringify({
                items: response
            })
        };
    } catch (err) {
        console.log(err);
        return {
            'statusCode': 500
        }
    }
};

exports.getDynamoDbDocumentClient = () => {
    console.log(process.env.USE_LOCAL_DYNAMODB);
    if (process.env.USE_LOCAL_DYNAMODB) {
        return new dynamoDb.DocumentClient({'endpoint': 'http://dynamo-local:8000'});
    } else {
        return new dynamoDb.DocumentClient();
    }
}
