from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_s3 as _s3,
    aws_s3_notifications,
    RemovalPolicy,
)

from constructs import Construct


class ThumbnailGeneratorStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        layer = _lambda.LayerVersion(
            self,
            "pillow_layer",
            code=_lambda.Code.from_asset("layer"),
            description="Common helper utility",
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_10],
            removal_policy=RemovalPolicy.DESTROY,
        )

        image_function = _lambda.Function(
            self,
            "ImgProcessingFunction",
            runtime=[
                _lambda.Runtime.PYTHON_3_10,
            ],
            code=_lambda.Code.from_asset("./lambda"),
            handler="image_function.handler",
            layers=[layer],
        )

        file_processed_notification_function = _lambda.Function(
            self,
            "FileProcessedNotificationFunction",
            runtime=[
                _lambda.Runtime.PYTHON_3_10,
            ],
            code=_lambda.Code.from_asset("./lambda"),
            handler="notification_function.handler",
        )

        # create s3 bucket
        input_images_s3 = _s3.Bucket(self, "input_images_bucket")
        output_images_s3 = _s3.Bucket(self, "output_images_bucket")

        # create s3 notification for lambda function I
        input_notification = aws_s3_notifications.LambdaDestination(image_function)
        output_notification = aws_s3_notifications.LambdaDestination(
            file_processed_notification_function
        )

        # assign notification for the s3. event type (ex: OBJECT_CREATED)
        input_images_s3.add_event_notification(
            _s3.EventType.OBJECT_CREATED, input_notification
        )
        output_images_s3.add_event_notification(
            _s3.EventType.OBJECT_CREATED, output_notification
        )
