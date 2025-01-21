import os
import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from bs4 import BeautifulSoup
from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth

# def get_app_management_details():
#     sauce_username = "petcomobileapp"
#     sauce_access_key = "73f739dc-75f9-42ba-9008-d0e8ee4ce0ca"
#     # Sauce Labs API endpoint for app management
#     url = 'https://api.us-west-1.saucelabs.com/v1/storage/files'

#     response = requests.get(url, auth=HTTPBasicAuth(sauce_username, sauce_access_key), verify=False)
    
#     if response.status_code == 200:
#         app_details = response.json()
#         platform = sys.argv[2].lower()
#         ext = 'debug.apk' if platform == 'android' else '.ipa'

#         for item in app_details["items"]:
#             if ext in item["name"]:
#                 version = item["metadata"].get("short_version", item["metadata"].get("version"))
#                 print(version)
#                 return version
#     else:
#         print(f"Failed to retrieve app details: {response.status_code} - {response.text}")
#         return None


def send_mail(send_from, send_to, cc_list, subject, body_message, server, port, isTls=True):
    print("In send mail function")

    # Parse HTML file to extract test execution statistics
    with open('public/report.html', 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
    
    # Count occurrences 
    total_pass = len(soup.find_all(string="PASSED"))
    total_fail = len(soup.find_all(string="FAILED"))
    total_skip = len(soup.find_all(string="SKIPPED"))
    
    # Assuming total tests include passed and failed only
    total_tc = total_pass + total_fail


    new_list = {
        "total": total_tc,
        "pass": total_pass,
        "fail": total_fail,
        "skip": total_skip,
    }

    # Create a table to include in the body of the message
    table_data = "<html>"\
                    "<body><h2>Test Summary Information</h2><br>"\
                            "<p><b>Date of execution:</b> {date}<br></p>"\
                            "<p><b>Device Platform:</b> {env}<br></p>"\
                            "<p><b>Suite:</b> {tags}<br></p>"\
                            "<b>RESULT STATISTICS:</b><br>"\
                                "<table border='1' style='width: 36%; border-collapse: collapse; height:80px'><br>"\
                                    "<tr style=' background-color: Navy; color: white; text-align: center;'>"\
                                        "<th>Total</th>"\
                                        "<th>Pass</th>"\
                                        "<th>Fail</th>"\
                                        "<th>Skip</th>"\
                                        "<th>Pass %</th>"\
                                        "<th>Fail %</th>"\
                                    "</tr>"\
                                    "<tr style='text-align: center;height:40px'>"\
                                        "<td>{total}</td>"\
                                        "<td style='color: green;'>{passed}</td>"\
                                        "<td style='color: red;'>{fail}</td>"\
                                        "<td style='color: grey;'>{skip}</td>"\
                                        "<td style='color: green;'>{pass_percentage}</td>"\
                                        "<td>{fail_percentage}</td>"\
                                    "</tr>"\
                                "</table>"\
                            "<p>Attached log and report to view the executions.</p>"\
                    "</body>"\
                "</html>"
    
    # Fill in the table with values
    table_data = table_data.format(
        total=new_list["total"],
        passed=new_list["pass"],
        fail=new_list["fail"],
        skip=new_list["skip"],
        pass_percentage=round(new_list["pass"] / new_list["total"] * 100, 2),
        fail_percentage=round(new_list["fail"] / new_list["total"] * 100, 2),
        tags=str(sys.argv[1]),
        env=str(sys.argv[2]),
        date=date_time_str
    )

    # Add the table to the body of the message
    body_message += table_data

    # Create email message
    msg = MIMEMultipart()
    body_part = MIMEText(body_message, 'html')  # Use 'html' to include HTML formatted content
    msg['From'] = send_from
    msg['To'] = ", ".join(send_to)
    msg['CC'] = ", ".join(cc_list)
    msg['Subject'] = subject
    msg.attach(body_part)

    # Attach report and log files
    with open("public/report.html", 'rb') as file:
        msg.attach(MIMEApplication(file.read(), Name="report.html"))

    # Attach any PNG files in the "public" directory
    for file_name in os.listdir("public/"):
        if file_name.endswith(".png"):
            file_path = os.path.join("public/", file_name)
            with open(file_path, 'rb') as file:
                part = MIMEApplication(file.read(), Name=file_name)
                part['Content-Disposition'] = f'attachment; filename="{file_name}"'
                msg.attach(part)

    # Connect to SMTP server and send email
    server = smtplib.SMTP(server, port)
    print("Sending Email")
    server.sendmail(send_from, send_to + cc_list, msg.as_string())
    server.quit()

# Get current date and time
now = datetime.now()
date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

send_to = ["shahyogesh0902@gmail.com"]
cc_list = ["yogesh@primeqasolutions.com"]

send_mail("automationreport477@gmail.com", send_to, cc_list, "Automation execution report - Mobile Native " + " Device: " + sys.argv[2] + " Build: ", "SMTP.petc.com", port=25)
