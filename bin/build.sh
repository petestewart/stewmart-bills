mkdir -p /var/task/build/lib
pipenv run python3 setup.py build
make gen_reqs
pipenv run pip install -r requirements.txt -t /var/task/build/lib
cd /var/task/build/lib
touch __init__.py
rm -rf /var/task/build/lib/boto*
zip -r ../stewmart_email_checker.zip .
cd /var/task