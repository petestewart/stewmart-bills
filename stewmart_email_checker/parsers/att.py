import re


def att(message: str) -> dict:
    original_email = message.split('---------- Forwarded message ---------')[1]

    detail_start = original_email.index('Service:')
    detail_end = original_email.index('Bill total:')
    details = original_email[detail_start:detail_end - 1]

    section = original_email.split('Bill total:')[1]

    amount_index = re.search(r"\d", section).start()
    if not amount_index:
        raise Exception("No cost amount found in email")

    section = section[amount_index::]
    amount = section[0:section.index('.') + 3]
    return {
        'biller': 'AT&T',
        'amount': amount,
        'category': 'TV/Phone/Internet',
        'details': details
    }
