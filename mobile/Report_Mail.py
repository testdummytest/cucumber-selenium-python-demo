# from email.mime.application import MIMEApplication
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders
# from selenium import webdriver
# from pretty_html_table import build_table
# import pandas as pd
# from smtplib import SMTP
# import logging, requests
# import os
# from datetime import datetime
 
# SuccessCount = 0
# FailureCount = 0
# SkippedCount = 0
# Success_List = []
# Failure_Cause = []
# Execution_time = []
# loginNotHappened = []
# noSuchElementFound = []
# timedOutException = []
# assertionError = []
# miscellaneous = []
# clickIntercepted = []
# elementNotInteractable = []
# SENDER_MAIL = "yogesh@primeqasolutions.com"
# SENDER_PWD = "Hey_test@9299"
# Tester = ""
# cc = os.environ.get(
#     "EMAIL_CC", ""
# )
# cc = "shahyogesh0902@gmail.com"
# Recipents = cc.split(",") + [Tester]
 
 
# # def getReportLink():
# #     data = (
# #         "https://git.panasonic.aero/pac/tools/marketplace-ground-pim-server-test/-/jobs/"
# #         + os.environ.get("CI_JOB_ID")
# #         + "/artifacts/browse"
# #     )
# #     api_url = "http://tinyurl.com/api-create.php"
 
# #     response = requests.get(api_url, params={"url": data})
 
# #     if response.status_code == 200:
# #         tiny_url = response.text
# #         logging.info("Shortened URL:", tiny_url)
# #         return tiny_url
# #     else:
# #         logging.info("Error shortening URL.")
# #         return data
 
 
# def Success_List_Append(testID, description, results):
#     global SuccessCount, FailureCount
#     Success_List.append([testID, description, results])
#     if results == "Pass":
#         SuccessCount += 1
#         # print(testID)
#         logging.info("Success Count = " + str(SuccessCount))
 
 
# def Failure_Cause_Append(testID, description, failureCause):
#     global SuccessCount, FailureCount
#     Failure_Cause.append([testID, description, failureCause])
#     FailureCount += 1
#     logging.info("Failure Count = " + str(FailureCount))
#     if ("pimcore_logout" in str(failureCause)) or ("pimcore_loading" in str(failureCause)) or ("Login Elements not found" in str(failureCause)):
#         loginNotHappened.append([testID])
#         logging.info("Append to loginNotHappened")
#     elif "no such element" in str(failureCause):
#         noSuchElementFound.append([testID])
#         logging.info("Append to noSuchElementFound")
#     elif "Message: \nStacktrace:" in str(failureCause):
#         timedOutException.append([testID])
#         logging.info("Append to timedOutException")
#     elif "assert" in str(failureCause):
#         assertionError.append([testID])
#         logging.info("Append to assertionError")
#     elif "element click intercepted" in str(failureCause):
#         clickIntercepted.append([testID])
#         logging.info("Append to clickIntercepted")
#     elif "element not interactable" in str(failureCause):
#         elementNotInteractable.append([testID])
#         logging.info("Append to elementNotInteractable")
#     else:
#         miscellaneous.append([testID])
#         logging.info("Append to miscellaneous")    
 
# # dependent on if-else in Failure_Cause_Append
# def Error_Table_Generation():
#     global Error_Report_Table
 
#     print("Entered into Error_Table_Generation()")
#     Error_Report = [
#         ["loginNotHappened", len(loginNotHappened)],
#         ["noSuchElementFound", len(noSuchElementFound)],
#         ["timedOutException", len(timedOutException)],
#         ["assertionError", len(assertionError)],
#         ["clickIntercepted", len(clickIntercepted)],
#         ["elementNotInteractable", len(elementNotInteractable)],
#         ["miscellaneous", len(miscellaneous)]
#     ]
#     Error_Report_DF = pd.DataFrame(Error_Report, columns=("Error Type", "Count"))
#     Error_Report_Table = build_table(Error_Report_DF, "red_dark", text_align="justify")
#     Error_Report_CSV = [
#         ["loginNotHappened", loginNotHappened],
#         ["noSuchElementFound", noSuchElementFound],
#         ["timedOutException", timedOutException],
#         ["assertionError", assertionError],
#         ["clickIntercepted", clickIntercepted],
#         ["elementNotInteractable", elementNotInteractable],
#         ["miscellaneous", miscellaneous]
#     ]
#     Error_Report_CSV_DF = pd.DataFrame(Error_Report_CSV, columns=("Error Type", "List"))
#     max_len = max(Error_Report_CSV_DF['List'].apply(len))
#     for i in range(max_len):
#         Error_Report_CSV_DF[i+1] = Error_Report_CSV_DF['List'].apply(lambda x: x[i] if i < len(x) else "")
#     Error_Report_CSV_DF.drop(columns = ['List'], inplace=True)
#     Error_Report_CSV_DF.to_csv('Results.csv')
#     print("Exiting from Error_Table_Generation()")
 
# def TestReport_Generation():
#     global Test_Report_Table
#     # driver = webdriver.Chrome()
#     options = webdriver.ChromeOptions()
#     driver = webdriver.Remote(
#         command_executor="http://selenium__standalone-chrome:4444/wd/hub",
#         options=options,
#     )
 
#     print("Entered into TestReport_Generation()")
#     Test_Report = [
#         ["Project Name", "I-PAYOUT"],
#         ["Test Type", "Automation"],
#         ["Browser Used", "Chrome"],
#         ["Browser Version", driver.capabilities["browserVersion"]],
#         ["Test Pass", SuccessCount],
#         ["Test Fail", FailureCount],
#         ["Total Test Cases", int(SuccessCount + FailureCount)],
#     ]
#     Test_Report_DF = pd.DataFrame(Test_Report, columns=("Summary", "Details"))
#     Test_Report_Table = build_table(Test_Report_DF, "blue_dark", text_align="justify")
#     driver.quit()
#     print("Exiting from TestReport_Generation()")
 
 
# def Summary_Table_Formation():
#     global Summary_Table
#     global Failure_Cause_Table
#     Summary_table_DF = pd.DataFrame(
#         Success_List, columns=["TestCase No.", "TestCases Summary", "Results"]
#     )
#     Summary_Table = build_table(Summary_table_DF, "green_dark", text_align="justify")
#     if FailureCount != 0:
#         Failure_Cause_Table_DF = pd.DataFrame(
#             Failure_Cause,
#             columns=["TestCase No.", "TestCases Summary", "Failure Cause"],
#         )
#         Failure_Cause_Table = build_table(
#             Failure_Cause_Table_DF, "red_dark", text_align="justify"
#         )
 
 
# def Send_Mail():
#     print("Sending Mail...........")
#     message = MIMEMultipart()
#     message["Subject"] = "Automation report - PAC execution on " + str(
#         datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#     )
#     message["From"] = SENDER_MAIL
#     message["To"] = Tester
#     message["Cc"] = cc
#     # style='height: 500px; overflow: auto; width: fit-content'
#     if FailureCount != 0:
#         empanelled = "<p>Failure Cause Table</p><div>" + Failure_Cause_Table + "</div>"
#         errorTable = "<p>Exception Table</p><div>" + Error_Report_Table + "</div>"
#     else:
#         empanelled = "<p>No Failure Observed.</p>"
#         errorTable = "<p></p>"
#     html = (
#         """\
#         <html>
#         <head></head>
#         <body>
#         <p>Hi,<br>
#                         Please find below Report for Automation Testing
#         </p>
#         <p>Test Report/Details
#         </p>
#         <div>"""
#                 + Test_Report_Table
#                 + """
#         </div>
#         <p>"""
#                 + errorTable
#                 + """</p>
#         <p>Summary Table
#         </p>
#         <div >"""
#                 + Summary_Table
#                 + """
#         </div>
#         <p>"""
#                 + empanelled
#                 + """</p>
#         <p>THIS IS SYSTEM GENERATED MAIL.</p>
#         <p></p>
#         </body>
#         </html>
#                 """
#     )
 
#     part2 = MIMEText(html, "html")
#     message.attach(part2)
#     filename = os.path.join(os.getcwd(), "pytest.log")
#     attachment = open(filename, "rb")
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(attachment.read())
#     encoders.encode_base64(part)
#     part.add_header("Content-Disposition", "attachment; filename= Logs")
#     message.attach(part)
#     if FailureCount != 0:
#         with open('Results.csv', 'rb') as file:
#             # Attach the file with filename to the email
#             message.attach(MIMEApplication(file.read(), Name="Failure_List.csv"))        

 
#     msg_body = message.as_string()
#     try:
#         server = SMTP("smtp.gmail.com", 587)
#         # outlook = client.Dispatch("Outlook.Application")
#         server.starttls()
#         server.login(message["From"], SENDER_PWD)
#         server.sendmail(message["From"], Recipents, msg_body)
#         server.quit()
#         print("Mail Sent successfully")
#     except Exception as e_mail:
#         print("Mail sending Failed")
#         print(e_mail)