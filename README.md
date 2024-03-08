# Demo Data Generator

The **Demo Data Generator** is a Python script that generates demo data in JSON format for testing or demonstration purposes. This script creates synthetic data with random values for various fields such as names, IDs, dates, prices, and more.

## Installation

To use the **Demo Data Generator**, you need to have Python installed on your system. Additionally, you'll need to install the Faker library, which is used to generate fake data.

You can install Faker using pip, the Python package installer. Run the following command in your command prompt or terminal:


## Usage

To generate demo data, run the `demo_data_generator.py` script. You can customize the number of lines of data generated and the output file path.

### Running the Script

Navigate to the directory containing the `demo_data_generator.py` script in your command prompt or terminal.

Run the script using the following command:


### Customizing Data Generation

You can customize the data generation by modifying the parameters inside the `demo_data_generator.py` script. For example, you can change the number of lines of data generated or customize the fields and their types.

## Data Format

The generated demo data is stored in JSON format. Each JSON object represents a single data entry with various fields such as:

- First name
- Last name
- ID
- Start date
- End date
- Price
- Paid (Yes/No)
- Complete (Yes/No)
- City
- State
- Birthdate

## Output

By default, the generated demo data is saved in a JSON file named `demo_data.json` in the same directory as the script. You can specify a different output directory or file name by modifying the script.

## Example

Here's an example of generated demo data:

```json
[
    {
        "Fname": "John",
        "Lname": "Doe",
        "ID": "12345678",
        "StartDate": "2023-03-03",
        "EndDate": "2023-03-22",
        "Price": 589.45,
        "Paid": "Yes",
        "Complete": "No",
        "City": "New York",
        "State": "NY",
        "Birthdate": "1985-08-12"
    },
    {
        "Fname": "Jane",
        "Lname": "Smith",
        "ID": "87654321",
        "StartDate": "2022-11-25",
        "EndDate": "2022-12-14",
        "Price": 278.73,
        "Paid": "No",
        "Complete": "Yes",
        "City": "Los Angeles",
        "State": "CA",
        "Birthdate": "1992-05-28"
    },
    ...
]
