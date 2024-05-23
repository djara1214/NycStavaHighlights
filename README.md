# NYC's Fastest Strava Bikers 

Welcome to my project! This is all about the speed demons tearing up NYC's streets on two wheels, courtesy of Strava. Here, I'm shining a spotlight on the fastest riders and the segments they dominate, giving you a bird's-eye view of NYC's cycling hotspots. My toolkit? Python for snagging data from Strava's API and doing a bit of web scraping, plus Bokeh for slick data visualizations. Oh, and HTML comes into play for sprucing up my presentation with MapBox GL JS. Come on in and let's dive into the world of NYC's cycling scene together!

![hippo](https://github.com/djara1214/NycStravaHighlights/blob/b6d179f9fcf2d143186aac4d9596999eef97fb12/DataVis/MapMoving.gif)

## Table of Contents

- [Project Overview](#project-overview)
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
## Data Collection
Leveraging the Strava API, we gather segment numbers representing biking routes across New York City. Initially, we define arbitrary coordinates encompassing NYC, which are then divided into smaller n boxes. These box coordinates serve as inputs for the Strava API to retrieve the top 10 segments in each area. This process is iterated numerous times with varying n values to ensure comprehensive segment coverage. Subsequently, employing web scraping techniques with Beautiful Soup, we extract leader board data for these segments. The scraping is conducted using my personal Strava account, which includes a paid subscription, granting access to the desired leader boards. This data acquisition returns:
		
	    - User names
	    - User ID numbers
	    - Completion times
	    - Rankings 
	    - Average Speeds
## Data Visualization
Once the data was collected, I began the ETL process. After un-decoding all location data, the segment data was plotted with Mapbox Gl JS. Segments are shown as clickable lines on the map. Hovering over each segment shows you quick information - **Segment name, and its leader with their respective time.** Then when clicking, the hovering data disappears and a panel pans from the right with the full **top 25 leader board**. This allows all users to clearly see all available segments throughout NYC, without the need to hover over a new location to load in more data. 
 
When initially loading in the left panel pans over, presented in this panel is a welcome message and some data insights. All data shown in explained in the [Project Overview](#project-overview)
 Pandas data frames were used for all data manipulation.
 Segment and user data were stored locally on `CSV` files. Here files were easily combined into larger normalized data sets *(which is not presented in this repo)*. Bokeh was then used for chart creation, due to its ease of use and relatively overall good looking charts.



## Contributing
This has been a random idea floating in my head, I plan to add more in the future i.e. Search bar , starting and ending markers, and more.. 
So if anyone wants to add more or play with this, let me know!!
create an issue to let me know or simply:
1.  Fork this repository to your GitHub account.
2.  Create a new branch with a killer name.
3.  Make your changes and improvements.
4.  Test it! *I could hand a helping hand if you need*
5.  Submit a pull request, with the changes you have made.


Thanks for visiting my repo and hopefully this has made you want to rip up the mean streets of New York,
just dont forget your helmet!
