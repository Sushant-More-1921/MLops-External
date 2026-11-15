
import os
import pandas as pd

from evidently import Report
from evidently.presets import DataSummaryPreset


def generate_report():

    # Sample API input data
    data = pd.DataFrame({
        "num1": [10, 20, 30, 40, 50],
        "num2": [5, 10, 15, 20, 25],
        "result": [15, 30, 45, 60, 75]
    })

    # Create Evidently report
    report = Report([
        DataSummaryPreset()
    ])

    snapshot = report.run(data, None)

    # Create reports directory
    os.makedirs("reports", exist_ok=True)

    # Save HTML report
    snapshot.save_html("reports/data_quality_report.html")

    print("Evidently report generated successfully!")


if __name__ == "__main__":
    generate_report()
