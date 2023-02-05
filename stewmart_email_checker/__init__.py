import logging
from operator import itemgetter

import boto3

from stewmart_email_checker.aws.s3 import upload_to_aws
from stewmart_email_checker.aws.sns import SnsWrapper
from stewmart_email_checker.email_client.email_client import get_emails, mark_read
from stewmart_email_checker.parsers.att import att
from stewmart_email_checker.parsers.nes import nes
from stewmart_email_checker.parsers.msud import msud
from stewmart_email_checker.parsers.piedmont import piedmont

logger = logging.getLogger()
logger.setLevel(logging.INFO)

parsers = {
    'Nashville Electric Service': nes,
    'Madison Suburban Utility District': msud,
    'Your new AT&T bill is available now at myAT&T.': att,
    'AT&T Payment Processed for Account Ending in 7361': att,
    'Piedmont Natural Gas': piedmont
}


def handler(event, context):
    sns_wrapper = SnsWrapper(boto3.resource('sns'))
    emails = get_emails()
    for email in emails:
        message = email.get('message')
        if 'petestew@gmail.com' not in message:
            mark_read(email.get('id'))
            continue  # not a forwarded message
        for trigger, parser in parsers.items():
            if trigger in message:
                data = parser(message)
                logger.info(f'Email {email["id"]} successfully parsed {data}')
                result = sns_wrapper.publish_to_topic(data)
                message_id, metadata = itemgetter('MessageId', 'ResponseMetadata')(result)
                if metadata.get('HTTPStatusCode') == 200:
                    mark_read(email.get('id'))
                    file_url = upload_to_aws(email.get('id'), result)


if __name__ == '__main__':
    # mark_read('5')
    handler()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
