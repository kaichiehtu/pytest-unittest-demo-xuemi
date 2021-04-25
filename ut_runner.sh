#! /bin/bash

UT_REPORT_DIR="ut-reports"
COV_REPORT_DIR="cov-reports"

# clear report
rm -r ${COV_REPORT_DIR}


# run tests
pytest -v tests --html-report=${UT_REPORT_DIR} --cov=src/ --cov-report=html:${COV_REPORT_DIR}
