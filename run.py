# import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# import time
# from datetime import datetime, timedelta
# from dateutil.relativedelta import relativedelta
#import csv
# import config
# from helpers.login import login
# from helpers.scroll_page import scroll
# from helpers.datetime_parser import parse_noun_date
# from helpers.revenue_data import all_revenues
# from helpers.icons_details import get_icons
# from openpyxl import Workbook

# Start the driver and navigate to the parks canada site
driver = webdriver.Chrome('/Applications/chromedriver')
driver.get('https://reservation.pc.gc.ca/BrucePeninsula?List')
campingType = Select(driver.find_element_by_id('selResType'))
# print campingType.options
campingType.select_by_value("Campsite")
arrivalMonthInt = Select(driver.find_element_by_id('selArrMth'))
# print [o.text for o in arrivalMonthInt.options] # these are string-s
try:
    arrivalMonthInt.select_by_visible_text('Jul')
except Exception as e:
    print("Usual arrival month error being ignored.")
arrivalDay = Select(driver.find_element_by_id('selArrDay'))
try:
    arrivalDay.select_by_value("Fri Jul 06 2018 00:00:00 GMT-0400 (EDT)")
except Exception as e2:
    print("Ignoring arrival day exception since returns error even when successful.")
nights = Select(driver.find_element_by_id('selNumNights'))
try:
    nights.select_by_value('2')
except Exception as e3:
    print("Ignoring nights exception since returns error even when successful.")

#try:
#available = driver.find_element_by_css_selector('area unavail')
available = driver.find_element_by_css_selector(".area.unavail")
available = driver.find_element_by_css_selector(".area.unavail")
#except Exception as available:
#    print("party time")
# login(driver)       #login to the app using info from config
# get_icons(driver, wb)
# all_revenues(driver, wb)

# #gotta save all that hard work
# wb.save('test.xlsx')

# driver.get('https://thenounproject.com/'+config.noun_project_username+'/activity/')
# the current time, we will need since datetimes are relative to the now
# now = datetime.now()       
# finished_scroll = scroll(driver)      #scrolls icons full page

# ws = wb.create_sheet("Activity", 0)
# ws.append(['Icon ID', 'Username', 'Action', 'DateTime'])


# # read the info we care about from each activity entry
# activities_list = driver.find_element_by_id('activity-list')
# activities = activities_list.find_elements_by_css_selector('li')
# with open(config.csv_file_name, 'wt') as csvfile:

#     for activity in activities:
#         # determine the id of the icon
#         action_user_full = activity.find_elements_by_css_selector('a')[0].get_attribute('href')
#         icon_link = activity.find_elements_by_css_selector('a')[1].get_attribute('href')
#         last_slash = icon_link.rfind('/')
#         last_slash_user = action_user_full.rfind('/')
#         icon_id = icon_link[last_slash + 1:]
#         action_user = action_user_full[last_slash_user + 1:]

#         # the nature of the activity (purchased, downloaded, self-action)
#         activity_type_full = activity.find_element_by_css_selector('span').get_attribute('class')
#         activity_type = 'Download'
#         if activity_type_full == 'action ui_dollar-sign-circle-filled':
#             activity_type = 'Purchase'
#         elif activity_type_full == 'action ui_heart':
#             activity_type = 'Favorite'
#         elif activity_type_full == 'action ui_kit':
#             activity_type = 'Kit'

#         # # calculate the datetime of the activity, best we can
#         # activity_datetime = now.replace(second=0,microsecond=0) #todo implement rounding yourself if you care
#         activity_time = activity.find_element_by_class_name('date-of-action').text
#         activity_datetime = parse_noun_date(activity_time, now)

#         # enter into database the info we've collected
#         ws.append([icon_id, action_user, activity_type, activity_datetime])
    
# #gotta save all that hard work
# wb.save('test.xlsx')
#driver.quit()