
import json
import random
import string
import os
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

def generate_demo_data(num_lines):
    data = []
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Columbus', 'Fort Worth', 'Indianapolis', 'Charlotte', 'Seattle', 'Denver', 'Washington', 'Boston', 'El Paso', 'Detroit', 'Nashville', 'Portland', 'Memphis', 'Oklahoma City', 'Las Vegas', 'Louisville', 'Baltimore', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno', 'Mesa', 'Sacramento', 'Atlanta', 'Kansas City', 'Colorado Springs', 'Miami', 'Raleigh', 'Omaha', 'Long Beach', 'Virginia Beach', 'Oakland', 'Minneapolis', 'Tulsa', 'Arlington', 'Tampa', 'New Orleans', 'Wichita', 'Cleveland', 'Bakersfield', 'Aurora', 'Anaheim', 'Honolulu', 'Santa Ana', 'Riverside', 'Corpus Christi', 'Lexington', 'Stockton', 'St. Louis', 'Saint Paul', 'Henderson', 'Pittsburgh', 'Cincinnati', 'Anchorage', 'Greensboro', 'Plano', 'Newark', 'Lincoln', 'Toledo', 'Orlando', 'Chula Vista', 'Irvine', 'Fort Wayne', 'Jersey City', 'Durham', 'St. Petersburg', 'Laredo', 'Buffalo', 'Madison', 'Lubbock', 'Chandler', 'Scottsdale', 'Glendale', 'Reno', 'Norfolk', 'Winston-Salem', 'North Las Vegas', 'Irving', 'Chesapeake', 'Gilbert', 'Hialeah', 'Garland', 'Fremont', 'Baton Rouge', 'Richmond', 'Boise', 'San Bernardino', 'Spokane', 'Birmingham', 'Modesto', 'Des Moines', 'Rochester', 'Tacoma', 'Fontana', 'Oxnard', 'Moreno Valley', 'Fayetteville', 'Aurora', 'Glendale', 'Yonkers', 'Huntington Beach', 'Montgomery', 'Amarillo', 'Little Rock', 'Akron', 'Grand Rapids', 'Augusta', 'Mobile', 'Salt Lake City', 'Huntsville', 'Tallahassee', 'Grand Prairie', 'Overland Park', 'Knoxville', 'Worcester', 'Brownsville', 'Newport News', 'Santa Clarita', 'Port St. Lucie', 'Providence', 'Fort Lauderdale', 'Chattanooga', 'Tempe', 'Oceanside', 'Garden Grove', 'Rancho Cucamonga', 'Cape Coral', 'Santa Rosa', 'Vancouver', 'Sioux Falls', 'Peoria', 'Ontario', 'Jackson', 'Elk Grove', 'Springfield', 'Pembroke Pines', 'Salem', 'Corona', 'Eugene', 'McKinney', 'Fort Collins', 'Lancaster', 'Cary', 'Palmdale', 'Hayward', 'Salinas', 'Alexandria', 'Lakewood', 'Springfield', 'Pasadena', 'Sunnyvale', 'Macon', 'Pomona', 'Hollywood', 'Kansas City', 'Escondido', 'Clarksville', 'Joliet', 'Rockford', 'Torrance', 'Naperville', 'Savannah', 'Paterson', 'Bridgeport', 'Mesquite', 'Killeen', 'Syracuse', 'McAllen', 'Pasadena', 'Bellevue', 'Fullerton', 'Orange', 'Dayton', 'Miramar', 'Thornton', 'West Valley City', 'Olathe', 'Hampton', 'Warren', 'Midland', 'Waco', 'Charleston', 'Denton', 'Carrollton', 'Surprise', 'Roseville', 'Sterling Heights', 'Murfreesboro', 'Gainesville', 'Cedar Rapids', 'Visalia', 'Coral Springs', 'New Haven', 'Stamford', 'Thousand Oaks', 'Concord', 'Elizabeth', 'Lafayette', 'Kent', 'Santa Clara', 'Simi Valley', 'Topeka', 'Athens', 'Round Rock', 'Hartford', 'Norman', 'Victorville', 'Fargo', 'Berkeley', 'Allentown', 'Evansville', 'Abilene', 'Provo', 'Independence', 'Ann Arbor', 'Peoria', 'El Monte', 'Lansing', 'Frisco', 'Columbia', 'Downey', 'Costa Mesa', 'Wilmington', 'Arvada', 'Inglewood', 'Miami Gardens', 'Carlsbad', 'Westminster', 'Rochester', 'Odessa', 'Manchester', 'Elgin', 'West Jordan', 'Round Rock', 'Clearwater', 'Waterbury', 'Gresham', 'Fairfield', 'Billings', 'Lowell', 'San Buenaventura (Ventura)', 'Pueblo', 'High Point', 'West Covina', 'Richmond', 'Murrieta', 'Cambridge', 'Antioch', 'Temecula', 'Norwalk', 'Centennial', 'Everett', 'Palm Bay', 'Wichita Falls', 'Green Bay', 'Daly City', 'Burbank', 'Richardson', 'Pompano Beach', 'North Charleston', 'Broken Arrow', 'Boulder', 'West Palm Beach', 'Santa Maria', 'El Cajon', 'Davenport', 'Rialto', 'Las Cruces', 'San Mateo', 'Lewisville', 'South Bend', 'Lakeland', 'Erie', 'Tyler', 'Pearland', 'College Station', 'Kenosha', 'Sandy Springs', 'Clovis', 'Flint', 'Roanoke', 'Albany', 'Jurupa Valley', 'Compton', 'San Angelo', 'Hillsboro', 'Lawton', 'Renton', 'Vista', 'Davie', 'Greeley', 'Mission Viejo', 'Portsmouth', 'Dearborn', 'South Gate', 'Tuscaloosa', 'Livonia', 'New Bedford', 'Vacaville', 'Brockton', 'Roswell', 'Beaverton', 'Quincy', 'Sparks', 'Yakima', 'Lee\'s Summit', 'Federal Way', 'Carson', 'Santa Monica', 'Hesperia', 'Allen', 'Rio Rancho', 'Yuma', 'Westminster', 'Orem', 'Lynn', 'Redding', 'Spokane Valley', 'Miami Beach', 'League City', 'Lawrence', 'Santa Barbara', 'Plantation', 'Sandy', 'Sunrise', 'Macon-Bibb County', 'Fishers', 'Edmond', 'Bend', 'Gastonia', 'St. Joseph', 'Temple', 'Woodbridge', 'Pawtucket', 'San Leandro', 'New Britain', 'Yorba Linda', 'Kennewick', 'Redwood City', 'Oshkosh', 'Boca Raton', 'Baytown', 'Lauderhill', 'Waltham', 'St. George', 'Auburn', 'Lake Forest', 'Duluth', 'Federal Way', 'Westland', 'Pharr', 'Missoula', 'East Orange', 'Anderson', 'Wilmington', 'Folsom', 'Lawrence', 'Kirkland', 'Taylorsville', 'East Los Angeles', 'Aloha', 'Chino', 'Bismarck', 'New Rochelle', 'Union City', 'Mount Vernon', 'South Suffolk', 'Blaine', 'Tallahassee', 'Montebello', 'Freeport', 'Apple Valley', 'Passaic', 'Redondo Beach', 'Conway', 'La Mesa', 'Yorba Linda', 'Middletown', 'Davis', 'Smyrna', 'Sarasota', 'Santa Cruz', 'Edinburg', 'Gilroy', 'Cathedral City', 'Royal Oak', 'Lakeville', 'Cedar Park', 'Boise City', 'Malden', 'Redlands', 'Oshkosh', 'Palatine', 'Missouri City', 'Eastvale', 'Rock Hill', 'North Miami', 'Maple Grove', 'Tulare', 'Cheyenne', 'Charleston', 'Gulfport', 'Iowa City', 'Lauderhill', 'Great Falls', 'Bremerton', 'West Haven', 'Cupertino', 'Wausau', 'Rancho Cordova', 'Bradenton', 'South Jordan', 'San Marcos', 'Hattiesburg', 'Arlington Heights', 'Castle Rock', 'La Quinta', 'Prescott Valley', 'Olympia', 'Attleboro', 'Rancho Santa Margarita', 'Hackensack', 'Tigard', 'Hendersonville', 'Ankeny', 'Grand Forks', 'Parker', 'Glen Burnie', 'Maricopa', 'Palm Desert', 'Bullhead City', 'North Port', 'Hamilton', 'Farmington', 'Cary', 'Hickory', 'Riverview', 'Richland', 'Westfield', 'Sanford', 'Kettering', 'Lakewood', 'Town ']
    for _ in range(num_lines):
        row = {
            'Fname': fake.first_name(),
            'Lname': fake.last_name(),
            'ID': ''.join(random.choices(string.digits, k=8)),
            'StartDate': (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d'),
            'EndDate': (datetime.now() + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d'),
            'Price': round(random.uniform(10, 1000), 2),
            'Paid': round(random.uniform(10, 1000), 2),
            'Complete':  random.choice([1, 2]),
            'City': random.choice(cities),
            'USState': random.choice(states),
            'Birthdate': (datetime.now() - timedelta(days=random.randint(365*18, 365*80))).strftime('%Y-%m-%d')
        }
        data.append(row)
    return data

def main():
    num_lines = 500
    output_file = 'demo_data.json'

    # Specify the output directory path
    output_directory = r'C:\Users\Owner\OneDrive\Documents\DemoData'
    # Specify the full output file path
    output_file_path = os.path.join(output_directory, output_file)

    all_data = generate_demo_data(num_lines)

    with open(output_file_path, 'w') as f:
        json.dump(all_data, f, indent=4)

    print("Demo data generated and saved to '{}'.".format(output_file_path))

if __name__ == "__main__":
    main()
