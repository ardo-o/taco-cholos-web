# Cholos Tacos Project

Welcome to the Cholos Tacos Project GitHub repository! This project is a collaborative effort aimed at creating a relational database system and utilizing it in real-world applications. The code provided here demonstrates the implementation of a simple system for managing orders and menus for a fictitious restaurant called "Cholos Tacos."

## Overview

The project utilizes several technologies and concepts:

- **Streamlit**: A framework used for building interactive web applications with Python.
- **MySQL Connector**: A Python driver for MySQL databases, facilitating interaction with the database.
- **Pandas**: A powerful data manipulation library, used for handling data in tabular format.
- **Regular Expressions**: Employed for data validation, particularly for phone number formatting.
- **Decimal and Datetime**: Used for accurate handling of monetary values and date manipulation.
- **HTML and CSS**: Leveraged for customizing the appearance of the web application.

## Prerequisites

To run the application, ensure you have the following:

- Python installed on your system.
- MySQL database set up with appropriate permissions.
- Necessary Python packages installed (Streamlit, Pandas, mysql-connector-python, Pillow).

## Setup

1. Clone the repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Ensure your MySQL server is running.
4. Set up environment variables, particularly the `DBPass` variable, containing the database password.

## Running the Application

1. Navigate to the project directory in your terminal.
2. Run the Streamlit application using `streamlit run app.py`.
3. Access the application through your web browser (typically at `http://localhost:8501`).

## Functionality

The application provides three main tabs:

1. **Home Tab**: Displays an introductory section with images representing the restaurant.
2. **Order Tab**: Allows users to place orders by selecting items from the menu and providing necessary contact details. It calculates the subtotal, tax, and total automatically.
3. **Menu Tab**: Shows the menu items available at Cholos Tacos.

## Usage Notes

- Ensure all required fields are filled in the Order tab before submitting an order.
- Validations are in place for fields such as first name, last name, email, and phone number.
- Database interactions are handled securely, with parameters properly sanitized to prevent SQL injection attacks.

## Additional Information

- For further queries or assistance, contact the project team.
- This application is a prototype and can be extended with additional features and refinements.


---


This is for educational purposes only.
