Spotify Project
Aubrey Beltran, Jennifer Shtaway, and Raymond Tiu
Useful links
Github -      Spotify API -        Billboard API - 
Gracenote API  -   Last.fm API -    Songkick API -
What Data Sources?
Team 7 will be using web-scraping to gather current Billboard Top 100 lists and Last.fm top lists, along with utilizing RESTful APIs to access historical Billboard data. Loading this data into the MongoDB we’ve established we’ll be appending Gracenote (or Apple or Discocogs) genre data to help classify the ‘type’ of each top track’s artist and plotting the trends over time on D3.js visualizations. Songkick will then let us delve into a more fun question about a single artist’s international presence which will be plotted on Leaftlet to show the accuracy of ‘Mr. Worldwide’.

Once upon a time,music didn’t all sound the same, what happened and when will it end?!? 
What questions are we trying to ask?
How have trends in the top 100 songs in America, as noted by Billboard and Last.fm, changed over time?
Have the top hits come from more or fewer genres (and, if time, artists)

What do the top songs each year and each decade show for trends in the popularity of certain genres and artists?

How much does the self-given title of an artist (ex. Pitbull as “Mr. Worldwide” or Beyonce as “Queen Bee”) truly play out in international trends?
Is Pitbull truly “Mr. Worldwide”? 

Inspirations 💡
# 1 Why Songs of the Summer Sound the Same (by The New York Times) 
https://www.nytimes.com/interactive/2018/08/09/opinion/do-songs-of-the-summer-sound-the-same.html




T7 Rendition :
Visualize each year by a decade’s genre make-up (10 circles per spider graph)
Uses Billboard and the genre info to plot on a 5-10 axis graph the number of songs in each genre per year thus giving each circle it’s shape on the Spider
Color of the decade clusters will reflect the winning genre’s ‘color’ (color from cluster graph)







# 2  100,000 Kickstarter Projects, by City and Category 
Visualize each kickstarter project as a genre type and funding success based on number of backers and amount earned
Color related to genre and size to number of backers
Plotted per city
http://polygraph.cool/kickstarter/


T7 Rendition :
Visualize each year in a decade’s genre make-up (10 circles per spider graph)
Uses Billboard and the genre info to plot on a 5-10 axis graph EACH year
This is more refined than the general decade trends
Color will reflect the winning genre’s ‘color’ (color from cluster graph)



# 3 Songs in 3,000 cities (by Pudding.cool) 
Visualize presence of the artist in question across the globe
Link the song to a youtube video when you select the city on the map



T7 Rendition :
Use songkick to pull all past events, it has location & popularity as well as time. 
Visualize each concert of Pitbull’s around the world
Map those locations on a leaflet.js with a marker size according to popularity, and draw a roadmap line to connect all those events based on time series.
Also show how many continents he’s hit?
