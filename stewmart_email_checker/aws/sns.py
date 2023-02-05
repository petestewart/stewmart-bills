import boto3
import json
from botocore import client


class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""

    def __init__(self, sns_resource):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """
        self.sns_resource = sns_resource

    def publish_to_topic(self, message):
        sns_client = self.sns_resource.meta.client
        response = sns_client.publish(
            TopicArn='arn:aws:sns:us-east-2:628624869667:splitwise_parser',
            Message=json.dumps({'default': json.dumps(message)}),
            Subject='hello there',
            MessageStructure='JSON',
            # MessageAttributes={
            #     'string': {
            #         'DataType': 'string',
            #         'StringValue': 'string',
            #         'BinaryValue': b'bytes'
            #     }
            # },
            # MessageDeduplicationId='string',
            # MessageGroupId='string'
        )
        return response


# def demo():
#     sns_wrapper = SnsWrapper(boto3.resource('sns'))
#     res = sns_wrapper.publish_to_topic()
#     print(res)



if __name__ == '__main__':
    demo()
