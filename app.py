import aws_cdk as cdk

from cdk.thumbnail_stack import ThumbnailGeneratorStack


app = cdk.App()
ThumbnailGeneratorStack(app, "ThumbnailGeneratorStack")

app.synth()
