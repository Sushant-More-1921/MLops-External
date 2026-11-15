import os
from monitoring.evidently_monitor import generate_report


def test_evidently_report_generation():
    # Run the report generator
    generate_report()

    # Verify report was created
    report_path = os.path.join("reports", "data_quality_report.html")
    assert os.path.exists(report_path)
    assert os.path.getsize(report_path) > 0

