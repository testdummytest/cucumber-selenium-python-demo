from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from bs4 import BeautifulSoup
from datetime import datetime
from smtplib import SMTP
import shutil

def send_mail(send_from, send_to, cc_list, subject, body_message, server, port, isTls=True):
    print("In send mail function")

    # Parse HTML file to extract test execution statistics
    with open('report/report.html', 'r') as file:
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
        pass_percentage=round(new_list["pass"]/new_list["total"]*100, 2),
        fail_percentage=round(new_list["fail"]/new_list["total"]*100, 2),
        tags="testhere",
        env="test",
        date=date_time_str
    )

    # Add the table to the body of the message
    body_message += table_data

    # Create email message
    msg = MIMEMultipart()
    body_part = MIMEText(body_message, 'html')  # Use 'html' to include HTML formatted content
    msg['Subject'] = subject
    msg.attach(body_part)
    
    # shutil.make_archive("screenshots", 'zip', "screenshots")
    # Attach report and log files
    with open("report/report.html", 'rb') as file:
        msg.attach(MIMEApplication(file.read(), Name="report.html"))
        
    # Attach screenshots.zip file
    with open("screenshot.zip", 'rb') as file:
        msg.attach(MIMEApplication(file.read(), Name="screenshot.zip"))
        

    msg["From"] = send_from
    msg["To"] = ", ".join(send_to)
    msg["Cc"] = ", ".join(cc_list)
    try:
        server = SMTP("smtp.gmail.com", 587)
        # outlook = client.Dispatch("Outlook.Application")
        server.starttls()
        server.login(msg["From"], "wscbinclchnuewxn")
        server.sendmail(msg["From"], "yogesh@primeqasolutions.com", msg.as_string())
        server.quit()
        print("Mail Sent successfully")
    except Exception as e_mail:
        print("Mail sending Failed")
        print(e_mail)

# Get current date and time
now = datetime.now()
date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

send_to = ["yogesh@primeqasolutions.com"]
cc_list = ["yogesh@primeqasolutions.com"]

send_mail("automationreport477@gmail.com", send_to, cc_list, "Automation execution report: ","\n", "smtp.gmail.com", port=587)
