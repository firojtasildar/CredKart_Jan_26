pytest -v -s  --html=Html_reports\my_headless_report_31st_jan_2026.html --browser headless  --alluredir=AllureReports
pytest --html=Html_reports\my_chromereport_31st_jan_2026.html --browser chrome --alluredir=AllureReports
pytest --html=Html_reports\my_firefoxreport_31st_jan_2026.html --browser firefox  --alluredir=AllureReports
pytest --html=Html_reports\my_edgereport_31st_jan_2026.html --browser edge  --alluredir=AllureReports