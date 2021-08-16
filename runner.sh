export DEVICE_TYPE="android"

python -m pytest -k endtoend -p no:cacheprovider --alluredir=./test_results
#allure serve ./test_results
