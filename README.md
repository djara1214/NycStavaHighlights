# NYC's Fastest Strava Bikers 

Welcome to my project! This is all about the speed demons tearing up NYC's streets on two wheels, courtesy of Strava. Here, I'm shining a spotlight on the fastest riders and the segments they dominate, giving you a bird's-eye view of NYC's cycling hotspots. My toolkit? Python for snagging data from Strava's API and doing a bit of web scraping, plus Bokeh for slick data visualizations. Oh, and HTML comes into play for sprucing up my presentation with MapBox GL JS. Come on in and let's dive into the world of NYC's cycling scene together!

![hippo](https://github.com/djara1214/NycStravaHighlights/blob/b6d179f9fcf2d143186aac4d9596999eef97fb12/DataVis/MapMoving.gif)

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Data Collection](#data-collection)
- [Data Visualization](#data-visualization)
- [Contributing](#contributing)


## Project Overview

The primary goal of this project is to showcase the best riders in New York City and assist those aiming for sub-25 leader board rankings.

- Discover which riders hold the most sub-25 positions and how they compare to other top riders.
- Identify segments with the closest top times, enabling riders to avoid the most challenging segments. Since they'll be competing for extremely similar times to others therefore possibly not making the sub-25 leader board even with stellar times. 
- Explore the months in which these sub-25 times were achieved.
- Gain a comprehensive overview of **all** biking segments in NYC.
    - Unlike on their own site, where segments are often fragmented or selectively displayed, here you can view them all at once. Some of their map issues can seen as:
        - Some segments appear briefly and then vanish.
        - Some segments just simply remain hidden.
        - Only the most popular segments in an area are typically shown.

Over the years, I've found this fragmentation of segments on Strava's map to be a significant inconvenience. So, I decided to create my own solution.

- **Data Collection**: Leveraging the Strava API, we gather segment numbers representing biking routes across New York City. Initially, we define arbitrary coordinates encompassing NYC, which are then divided into smaller n boxes. These box coordinates serve as inputs for the Strava API to retrieve the top 10 segments in each area. This process is iterated numerous times with varying n values to ensure comprehensive segment coverage. Subsequently, employing web scraping techniques with Beautiful Soup, we extract leader board data for these segments. The scraping is conducted using my personal Strava account, which includes a paid subscription, granting access to the desired leader boards. This data acquisition returns:
		
	    - User names
	    - User ID numbers
	    - Completion times
	    - Rankings 
	    - Average Speeds
2. **Data Visualization**: Once the data is collected, I will also leverage Python's data visualization libraries (e.g., Matplotlib, Plotly) to create informative and engaging visualizations that showcase the top bikers and their achievements on the identified segments. In addition to python, I will use MAPBOX GL-JS to plot all biking segments in NYC. All Segment data will be shown **at** **once** and showcase their top riders. Something hard to do on Stravas own website.



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

