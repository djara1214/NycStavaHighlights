# NYC Top Bikers Data Visualization Project

Welcome to the **NYC Top Bikers Data Visualization Project** GitHub repository! This project focuses on using Python to retrieve and visualize data about the top bikers in New York City using the Strava API, web scraping, and Beautiful Soup.

⚠️This project is a work in progress⚠️
## ⚠️Currently in phase 1⚠️

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Data Collection](#data-collection)
- [Data Visualization](#data-visualization)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The primary goal of this project is to showcase the top bikers in New York City by utilizing data from the Strava API and web scraping techniques. The project involves two main phases:

1. **Data Collection**: Utilizing the Strava API, we retrieve segment numbers that represent popular biking routes in New York City. Then, by employing web scraping techniques with Beautiful Soup, we extract leader board data for these segments.

2. **Data Visualization**: Once the data is collected, we leverage Python's data visualization libraries (e.g., Matplotlib, Plotly) to create informative and engaging visualizations that showcase the top bikers and their achievements on the identified segments.

## Installation

To run this project locally, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/nyc-top-bikers.git
   cd nyc-top-bikers
   2.  Install the required dependencies using pip:
    
    bashCopy code
    
    `pip install -r requirements.txt` 
    
3.  Obtain API keys:
    
    -   You'll need a Strava API key to access segment information.
    -   If any web scraping is required, ensure that you have access to the necessary website and are aware of its terms of use.
4.  Configure your API keys:
    
    -   Create a `.env` file in the project's root directory.
        
    -   Add your API keys in the following format:
        
        plaintextCopy code
        
        `STRAVA_API_KEY=your_strava_api_key_here` 
        
5.  Run the project:
    
    bashCopy code
    
    `python main.py` 
    

## Usage

Explain how to use your project here. Provide examples of commands, input formats, or any other relevant information that users might need to interact with your project effectively.

## Data Collection

Describe how you retrieve data from the Strava API and perform web scraping using Beautiful Soup. Provide an overview of the logic, algorithms, or methods used for data extraction.

## Data Visualization

Explain how the collected data is visualized using Python's data visualization libraries. You can include sample code snippets, descriptions of different visualization techniques used, and any insights that can be gained from the visualizations.

## Contributing

We welcome contributions from the community! If you'd like to contribute to this project, follow these steps:

1.  Fork this repository to your GitHub account.
2.  Create a new branch with a descriptive name.
3.  Make your changes and improvements.
4.  Test thoroughly to ensure everything works as expected.
5.  Submit a pull request, detailing the changes you made.

Please ensure that your contributions align with the project's goals and coding standards.

## License

This project is licensed under the [MIT License](https://chat.openai.com/LICENSE). Feel free to use, modify, and distribute the code as permitted by the license.
