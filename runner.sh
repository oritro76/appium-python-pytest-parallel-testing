export DEVICE_TYPE=$1
export HUB_URL=$2
python -m pytest -k $3 -p no:cacheprovider --alluredir=./test_results
# allure serve ./test_results
