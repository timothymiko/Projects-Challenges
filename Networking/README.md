Country from IP Lookup
----------------------
Solution: IPLookup.py

Difficulty: 6

Description: Develop an application which can look up the country an IP is from. For instance, if a given IP address is traced to a .ca domain it would tell the user the IP is from a Canadian ISP.

Tips: All users on the Internet have an IP address. They are given this IP address from their service providers who were given a range of IP addresses. This means that using the IP address of a user we can find which ISP was given that address range. Then from that we can find the country. You may need to convert this address into an actual IP number. Then with the number we can ask a database like ip2country for the country.

Added Difficulty: Once the country has been identified, identify the ISP it belongs to and where they are located. You can also go one step further and provide this graphically on a map of the given country much like Google Analytics does for stats tracking.

Fetch Current Weather
---------------------
Solution: Weather.py

Difficulty: 4

Description: Make a program that prompts the user for a city or zip/postal code and returns the current weather information for the area. Have it specify the temperature in both Celsius and Fahrenheit, daily high/low, wind speed and relative humidity.

Tips: First locate a source of weather data that you can pull from. Find out what data that service needs so you know how your program can query the source and get its information. Analyze the format of its response and then create the program to generate the needed data to submit to the service and how to display results back to the user. Look at national weather center APIs. Google currently has an unsupported weather API as well. Just look up “Google Weather API” for articles on the topic. It is an easy way to test your application.

Added Difficulty: Fetch current weather conditions (sunny, rainy, snow, fog) and show an appropriate graphic to represent those conditions. Add one animation somewhere in the project.
