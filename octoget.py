import datetime, time, requests
from bs4 import BeautifulSoup
import pytz

#Octoget by Paige Spellman
#v1.0
#https://github.com/sp3lllz/octoget
#Use permitted under the MIT Licence


#Enter Your Name here 
USER_NAME = " "

# Replace with your Octopus Energy API credentials and your electricity meter ID, you can get your api key from https://octopus.energy/dashboard/developer/
API_KEY = " "

# Get the current date and time please do not edit this 
uk_timezone = pytz.timezone('UTC')
current_datetime = datetime.datetime.now(uk_timezone)

# Extract individual components
current_day = str(current_datetime.day).zfill(2)
current_month = str(current_datetime.month).zfill(2)
current_year = current_datetime.year
current_hour = str(current_datetime.hour).zfill(2)
current_minute = str(current_datetime.minute).zfill(2)

# Check the current minute and set the minute variables accordingly
current_minute = current_datetime.minute
if current_minute < 30:
    start_minute = 0
    end_minute = 29
else:
    start_minute = 30
    end_minute = 59
    
zero_minute = str(start_minute).zfill(2)


# Octopus Energy API endpoint for Agile Octopus rates
AGILE_URL_ELE = f"https://api.octopus.energy/v1/products/AGILE-FLEX-22-11-25/electricity-tariffs/E-1R-AGILE-FLEX-22-11-25-E/standard-unit-rates/?period_from={current_year}-{current_month}-{current_day}T{current_hour}:{zero_minute}Z&period_to={current_year}-{current_month}-{current_day}T{current_hour}:{end_minute}Z"


# Send the GET request
response = requests.get(AGILE_URL_ELE)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract the value_inc_vat value
    value_inc_vat = data['results'][0]['value_inc_vat']

    # Read the HTML file
    with open('/var/www/html/index.html', 'r') as html_file:
        html_content = html_file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the HTML element where you want to display the value_inc_vat
    target_element = soup.find('div', id='value_inc_vat')

    # Update the element's content with the value_inc_vat
    target_element.string = f"The current rate is:  {value_inc_vat} p/kWh"

    # Write the updated HTML content back to the file
    with open('/var/www/html/index.html', 'w') as html_file:
        html_file.write(str(soup))
    # Print the extracted value
    print(f"Hello {USER_NAME}, The current rate is: {value_inc_vat} p/kWh")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")