export DEVICE_TYPE=android
export HUB_URL=http://localhost:4723/wd/hub
python -m pytest -k endtoend -p no:cacheprovider --alluredir=./test_results
allure serve ./test_results
