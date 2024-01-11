# NYC Top Bikers Data Visualization Project

Welcome to the **NYC Top Bikers Data Visualization Project** GitHub repository! This project focuses on the top bikers in New York City who use Strava. I will be using Strava API (acess via Postman and Python), web scraping with Beautiful Soup, Python for some data retival and EDL, and HTML to run MapBox for presentation purposes.

![image](https://github.com/djara1214/NycStravaHighlights/assets/44910053/d6cd5628-71d9-44dd-aec8-41d468b4bcbd)



⚠️This project is a work in progress⚠️
## ⚠️Currently in phase 2⚠️

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

2. **Data Visualization**: Once the data is collected, I will also leverage Python's data visualization libraries (e.g., Matplotlib, Plotly) to create informative and engaging visualizations that showcase the top bikers and their achievements on the identified segments. In addition to python, I will use MAPBOX GL-JS to plot all biking segments in NYC. All Segment data will be shown **at** **once** and showcase their top riders. Something hard to do on Stravas own website.

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

This project will present Top bikers in a given area. I will present NYC, but with placing coordinates in any area where Strava data is recorded; you can then see it in that area.

## Data Collection

Contact Stava API to find all segments in given area
Scrape Stravas site to get all athlete info

## Data Visualization

MapBox GL-JS
Using this service I will plot converted Strava API data to geo json and present **all** segments at one time. Making each segment clickable with data presentation at hovering and clicking. 


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
