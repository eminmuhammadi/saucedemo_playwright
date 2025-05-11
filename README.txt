$ python -m venv .venv

$ source ./.venv/Scripts/activate

$ pip install pytest pytest-html playwright pytest-playwright pytest_tagging

$ playwright install

$ pytest ui_test.py -v --tags auth --browser=chromium --slowmo 500 --headed --html=report.html --tracing on

[-v]                                - Verbose
[--tags name]                       - Run specific tags
[--browser chromium|firefox|webkit] - Specific browser
[--slowmo 500]                      - Waits for each command
[--headed]                          - Hide browser
[--html=report.html]                - Generates report.html
[--tracing on]                      - Enables tracing

$ playwright show-trace ./test-results/XXXX/trace.zip