import aws_cdk as core
import aws_cdk.assertions as assertions

from stori.stori_stack import StoriStack


# example tests. To run these tests, uncomment this file along with the example
# resource in stori/stori_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = StoriStack(app, "stori")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
