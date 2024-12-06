import pandas as pd
import os

REPORT_PATH = "./reports/test_report.csv"

def write_to_csv(page_url, testcase, status, comment):
    if not os.path.exists(REPORT_PATH):
        df = pd.DataFrame(columns=["page_url", "testcase", "passed/fail", "comments"])
        df.to_csv(REPORT_PATH, index=False)

    df = pd.read_csv(REPORT_PATH)
    df.loc[len(df)] = [page_url, testcase, status, comment]
    df.to_csv(REPORT_PATH, index=False)
