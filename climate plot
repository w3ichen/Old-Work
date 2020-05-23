# pandas is used for making tables
import pandas as pd
# requests is for retriving the data
import requests
# plots is used to graph the data
from matplotlib import pyplot as plt

# annual temperature/precipitation points data
t_p_x = [] ; a_temp_y = [] ; a_prec_y = [] ; m_temp_y = {}
year_ranges = {
	1920:1939 , 1940:1959 , 1960:1979 , 1980:1999 , 2020:2039
}
months = ['Jan','\nFeb','Mar','\nApr','May','\nJun','Jul','\nAug','Sept','\nOct','Nov','\nDec']
# country Codes
countryCodes = {'Afghanistan': 'AFG', 'Aland Islands': 'ALA', 'Albania': 'ALB', 'Algeria': 'DZA', 'American Samoa': 'ASM', 'Andorra': 'AND', 'Angola': 'AGO', 'Anguilla': 'AIA', 'Antarctica': 'ATA', 'Antigua and Barbuda': 'ATG', 'Argentina': 'ARG', 'Armenia': 'ARM', 'Aruba': 'ABW', 'Australia': 'AUS', 'Austria': 'AUT', 'Azerbaijan': 'AZE', 'Bahamas': 'BHS', 'Bahrain': 'BHR', 'Bangladesh': 'BGD', 'Barbados': 'BRB', 'Belarus': 'BLR', 'Belgium': 'BEL', 'Belize': 'BLZ', 'Benin': 'BEN', 'Bermuda': 'BMU', 'Bhutan': 'BTN', 'Bolivia': 'BOL', 'Bosnia and Herzegovina': 'BIH', 'Botswana': 'BWA', 'Bouvet Island': 'BVT', 'Brazil': 'BRA', 'British Virgin Islands': 'VGB', 'British Indian Ocean Territory': 'IOT', 'Brunei Darussalam': 'BRN', 'Bulgaria': 'BGR', 'Burkina Faso': 'BFA', 'Burundi': 'BDI', 'Cambodia': 'KHM', 'Cameroon': 'CMR', 'Canada': 'CAN', 'Cape Verde': 'CPV', 'Cayman Islands': 'CYM', 'Central African Republic': 'CAF', 'Chad': 'TCD', 'Chile': 'CHL', 'China': 'CHN', 'Hong Kong': 'HKG', 'Macao': 'MAC', 'Christmas Island': 'CXR', 'Cocos Islands': 'CCK', 'Colombia': 'COL', 'Comoros': 'COM', 'Congo': 'COG', 'Congo': 'COD', 'Cook Islands': 'COK', 'Costa Rica': 'CRI', "Cote d'Ivoire": 'CIV', 'Croatia': 'HRV', 'Cuba': 'CUB', 'Cyprus': 'CYP', 'Czech Republic': 'CZE', 'Denmark': 'DNK', 'Djibouti': 'DJI', 'Dominica': 'DMA', 'Dominican Republic': 'DOM', 'Ecuador': 'ECU', 'Egypt': 'EGY', 'El Salvador': 'SLV', 'Equatorial Guinea': 'GNQ', 'Eritrea': 'ERI', 'Estonia': 'EST', 'Ethiopia': 'ETH', 'Falkland Islands': 'FLK', 'Faroe Islands': 'FRO', 'Fiji': 'FJI', 'Finland': 'FIN', 'France': 'FRA', 'French Guiana': 'GUF', 'French Polynesia': 'PYF', 'French Southern Territories': 'ATF', 'Gabon': 'GAB', 'Gambia': 'GMB', 'Georgia': 'GEO', 'Germany': 'DEU', 'Ghana': 'GHA', 'Gibraltar': 'GIB', 'Greece': 'GRC', 'Greenland': 'GRL', 'Grenada': 'GRD', 'Guadeloupe': 'GLP', 'Guam': 'GUM', 'Guatemala': 'GTM', 'Guernsey': 'GGY', 'Guinea': 'GIN', 'Guinea-Bissau': 'GNB', 'Guyana': 'GUY', 'Haiti': 'HTI', 'Heard Island and Mcdonald Islands': 'HMD', 'Vatican': 'VAT', 'Honduras': 'HND', 'Hungary': 'HUN', 'Iceland': 'ISL', 'India': 'IND', 'Indonesia': 'IDN', 'Iran': 'IRN', 'Iraq': 'IRQ', 'Ireland': 'IRL', 'Isle of Man': 'IMN', 'Israel': 'ISR', 'Italy': 'ITA', 'Jamaica': 'JAM', 'Japan': 'JPN', 'Jersey': 'JEY', 'Jordan': 'JOR', 'Kazakhstan': 'KAZ', 'Kenya': 'KEN', 'Kiribati': 'KIR', "North Korea": 'PRK', 'South Korea': 'KOR', 'Kuwait': 'KWT', 'Kyrgyzstan': 'KGZ', 'Lao PDR': 'LAO', 'Latvia': 'LVA', 'Lebanon': 'LBN', 'Lesotho': 'LSO', 'Liberia': 'LBR', 'Libya': 'LBY', 'Liechtenstein': 'LIE', 'Lithuania': 'LTU', 'Luxembourg': 'LUX', 'Macedonia': 'MKD', 'Madagascar': 'MDG', 'Malawi': 'MWI', 'Malaysia': 'MYS', 'Maldives': 'MDV', 'Mali': 'MLI', 'Malta': 'MLT', 'Marshall Islands': 'MHL', 'Martinique': 'MTQ', 'Mauritania': 'MRT', 'Mauritius': 'MUS', 'Mayotte': 'MYT', 'Mexico': 'MEX', 'Micronesia, Federated States of': 'FSM', 'Moldova': 'MDA', 'Monaco': 'MCO', 'Mongolia': 'MNG', 'Montenegro': 'MNE', 'Montserrat': 'MSR', 'Morocco': 'MAR', 'Mozambique': 'MOZ', 'Myanmar': 'MMR', 'Namibia': 'NAM', 'Nauru': 'NRU', 'Nepal': 'NPL', 'Netherlands': 'NLD', 'Netherlands Antilles': 'ANT', 'New Caledonia': 'NCL', 'New Zealand': 'NZL', 'Nicaragua': 'NIC', 'Niger': 'NER', 'Nigeria': 'NGA', 'Niue': 'NIU', 'Norfolk Island': 'NFK', 'Northern Mariana Islands': 'MNP', 'Norway': 'NOR', 'Oman': 'OMN', 'Pakistan': 'PAK', 'Palau': 'PLW', 'Palestinian Territory, Occupied': 'PSE', 'Panama': 'PAN', 'Papua New Guinea': 'PNG', 'Paraguay': 'PRY', 'Peru': 'PER', 'Philippines': 'PHL', 'Pitcairn': 'PCN', 'Poland': 'POL', 'Portugal': 'PRT', 'Puerto Rico': 'PRI', 'Qatar': 'QAT', 'Reunion': 'REU', 'Romania': 'ROU', 'Russian Federation': 'RUS', 'Rwanda': 'RWA', 'Saint-Barthelemy': 'BLM', 'Saint Helena': 'SHN', 'Saint Kitts and Nevis': 'KNA', 'Saint Lucia': 'LCA', 'Saint-Martin': 'MAF', 'Saint Pierre and Miquelon': 'SPM', 'Saint Vincent and Grenadines': 'VCT', 'Samoa': 'WSM', 'San Marino': 'SMR', 'Sao Tome and Principe': 'STP', 'Saudi Arabia': 'SAU', 'Senegal': 'SEN', 'Serbia': 'SRB', 'Seychelles': 'SYC', 'Sierra Leone': 'SLE', 'Singapore': 'SGP', 'Slovakia': 'SVK', 'Slovenia': 'SVN', 'Solomon Islands': 'SLB', 'Somalia': 'SOM', 'South Africa': 'ZAF', 'South Georgia and the South Sandwich Islands': 'SGS', 'South Sudan': 'SSD', 'Spain': 'ESP', 'Sri Lanka': 'LKA', 'Sudan': 'SDN', 'Suriname': 'SUR', 'Svalbard and Jan Mayen Islands': 'SJM', 'Swaziland': 'SWZ', 'Sweden': 'SWE', 'Switzerland': 'CHE', 'Syria': 'SYR', 'Taiwan': 'TWN', 'Tajikistan': 'TJK', 'Tanzania': 'TZA', 'Thailand': 'THA', 'Timor-Leste': 'TLS', 'Togo': 'TGO', 'Tokelau': 'TKL', 'Tonga': 'TON', 'Trinidad and Tobago': 'TTO', 'Tunisia': 'TUN', 'Turkey': 'TUR', 'Turkmenistan': 'TKM', 'Turks and Caicos Islands': 'TCA', 'Tuvalu': 'TUV', 'Uganda': 'UGA', 'Ukraine': 'UKR', 'United Arab Emirates': 'ARE', 'United Kingdom': 'GBR', 'United States': 'USA', 'United States Minor Outlying Islands': 'UMI', 'Uruguay': 'URY', 'Uzbekistan': 'UZB', 'Vanuatu': 'VUT', 'Venezuela': 'VEN', 'Viet Nam': 'VNM', 'Virgin Islands, US': 'VIR', 'Wallis and Futuna Islands': 'WLF', 'Western Sahara': 'ESH', 'Yemen': 'YEM', 'Zambia': 'ZMB', 'Zimbabwe': 'ZWE'}

print("Graphing Climate Change Data by Country")
print("Enter Country Name or 3-Digit Country Code to Analyze: ")
country = input(" ")
try:
	countryDecoded = countryCodes[country.lower().title()]
except:
	# if not found in dictionary, assume user entered the country code
	countryDecoded = country.upper()

print("Getting and Analyzing Data...")
for startYear in year_ranges:
	annual_temperature_data = requests.get('http://climatedataapi.worldbank.org/climateweb/rest/v1/country/annualavg/tas/'+ str(startYear) +'/'+ str(year_ranges[startYear]) +'/'+ countryDecoded +'.json')
	annual_precipitation_data = requests.get('http://climatedataapi.worldbank.org/climateweb/rest/v1/country/annualavg/pr/'+ str(startYear) +'/'+ str(year_ranges[startYear]) +'/'+ countryDecoded +'.json')
	monthly_temperature_data = requests.get('http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/'+ str(startYear) +'/'+ str(year_ranges[startYear]) +'/'+ countryDecoded +'.json')

	annual_temperature_table = pd.read_json(annual_temperature_data.text)
	annual_precipitation_table = pd.read_json(annual_precipitation_data.text)
	monthly_temperature_table = pd.read_json(monthly_temperature_data.text)

	a_temp_y.append( annual_temperature_table['annualData'][0][0] )
	a_prec_y.append( annual_precipitation_table['annualData'][0][0] )
	m_temp_y[startYear] = monthly_temperature_table['monthVals'][0]
	t_p_x.append(str(startYear)+'\n'+str(year_ranges[startYear]))

print("Graphing Data...")

# graphs
plt.subplot(212)
plt.title("Annual Temperature")
plt.xlabel("Years")
plt.ylabel("Temperature in celsius")
plt.tight_layout()
plt.plot(t_p_x,a_temp_y)

plt.subplot(221)
plt.title("Annual Precipitation")
plt.xlabel("Years")
plt.ylabel("Precipitation in mm")
plt.tight_layout()
plt.plot(t_p_x,a_prec_y)

plt.subplot(222)
plt.title("Monthly Temperature")
plt.xlabel("Months")
plt.ylabel("Temperature in celsius")


for years in year_ranges:
	plt.plot(months, m_temp_y[years])
plt.tight_layout()
plt.show()

print("Data retrieved from WorldBank Climate Data")
print("Data is derived from Global Circulation Models")
