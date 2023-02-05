import re


def piedmont(message: str) -> dict:
    original_email = message.split('---------- Forwarded message ---------')[1]
    detail_start = original_email.index('Bill due date:')
    detail_end = original_email.index('Please click on the following link to log in and access your account.')
    details = original_email[detail_start:detail_end - 1]

    section = original_email.split('Total Current Balance:')[1]

    amount_index = re.search(r"\d", section).start()
    if not amount_index:
        raise Exception("No cost amount found in email")

    section = section[amount_index::]
    amount = section[0:section.index('.') + 3]
    return {
        'biller': 'Piedmont Natural Gas',
        'amount': amount,
        'category': 'Heat/gas',
        'details': details
    }
