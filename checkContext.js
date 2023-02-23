export const handler = async(event, context) => {
    // TODO implement
    const response = {
        statusCode: 200,
        body: JSON.stringify('Hello from Lambda!'),
    };
    console.log(context.getRemainingTimeInMillis());
    setTimeout(() => {console.log("test")}, 1000);
    console.log(context.getRemainingTimeInMillis());

    console.log("functionName: ", context.functionName);
    console.log("functionVersion: ", context.functionVersion);
    console.log("invokedFunctionArn: ", context.invokedFunctionArn);
    console.log("memoryLimitInMB: ", context.memoryLimitInMB);
    console.log("awsRequestId: ", context.awsRequestId);
    console.log("logGroupName: ", context.logGroupName);
    console.log("logStreamName: ", context.logStreamName);
    console.log("identity: ", context.identity);
    console.log("clientContext: ", context.clientContext);
    console.log("callbackWaitsForEmptyEventLoop: ", context.callbackWaitsForEmptyEventLoop);
    return response;
};
