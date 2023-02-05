import re


def msud(message: str) -> dict:
    original_email = message.split('---------- Forwarded message ---------')[1]
    detail_start = original_email.index('Bill Date:')
    detail_end = original_email.index('Amount Due:')
    details = original_email[detail_start:detail_end - 1]

    amount = original_email.split('Amount Due:')[1]
    amount_index = re.search(r"\d", amount).start()
    if not amount_index:
        raise Exception("No cost amount found in email")

    amount = amount[amount_index::]
    amount = amount[0:amount.index('.') + 3]
    return {
        'biller': 'Madison Suburban Utility District',
        'amount': amount,
        'category': 'Water',
        'details': details
    }
