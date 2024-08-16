
# Tumbnail Generator

The design consists of 2 lambda functions, one to process new files, and another to notify the Web Application that the resized file was written and the path to download it for the user.

The lambda is triggered by the S3 notification of a new file written in the input path.
The file get's resized and stored in an output bucket, the notification from this file triggers the second lambda that notifies the Web App.

Strength:
- It's a simple design that can be quickly deployed to iterate and test.

Weakness:
- This is a simple design it does not scale if the Web App has a lot's of requests.
- It does not have any error handler to notify the user if something went wrong.
- It does not handle files that have the same file name.
- It does not enalbe the user to choose the size that they want.
- The size of the image that can processed is limited by the lambda's RAM configuration.
- It does not have a vpc configured to make the request go in a private network.
- The lambda functions are missing the Iam Role with the permissions to read and write to S3.
- The code does not have the ci pipeline to deploy the stack to AWS.

Proposal:
- Change the lambda with a ECS resource so it can handle images with sizes over the lambda's limits.
- Deploy the code with Docker images stored in a Container Registry.
- Send all the requests to an Event Bridge that trigger the ECS's processes.
