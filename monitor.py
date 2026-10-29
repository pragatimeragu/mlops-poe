
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

# Reference data: original data
reference_data = pd.DataFrame({
    "feature": [10, 12, 11, 13, 12, 10, 11, 12]
})

# Current data: simulated new data
current_data = pd.DataFrame({
    "feature": [20, 22, 21, 25, 24, 23, 22, 26]
})

# Generate data drift report
report = Report([
    DataDriftPreset()
])

result = report.run(
    reference_data=reference_data,
    current_data=current_data
)

result.save_html("evidently_report.html")

print("Evidently monitoring report generated successfully!")
