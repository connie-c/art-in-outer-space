Projects = [
    {
        "project_title": "NASA: Reach for the Stars with will.i.am",
        "artist_name": "will.i.am", 
        "description": "http://collectSPACE.com — For the first time in history, a recorded song has been beamed back to Earth from another planet. Students, special guests and news media gathered at NASA's Jet Propulsion Laboratory (JPL) in Pasadena, Calif., on Tuesday, Aug. 28, 2012, to hear Reach for the Stars by musician will.i.am after it was transmitted from the surface of Mars by the Curiosity rover. ",
        "url": "https://www.youtube.com/watch?v=6WZGxg0oPKc&t=34s",
        "img": "https://www.nasa.gov/images/content/682008main_william20120828b-full_full.jpg",
        "project_id": "001"
    },
    {
        "project_title": "Tesla roadster's 'Starman' on space journey after SpaceX launch",
        "artist_name": "Elon Musk, SpaceX", 
        "description": "SpaceX launched the world's most powerful rocket Tuesday to thunderous applause and cheers.  The Falcon Heavy sent a cherry-red Tesla roadster into space as well.",
        "url": "https://www.youtube.com/watch?v=q_WQ-Ds8ZvE",
        "img": "https://upload.wikimedia.org/wikipedia/commons/1/1a/Elon_Musk%27s_Tesla_Roadster_%2840110297852%29.jpg",
        "project_id": "002"

    },
    {
        "project_title": "EXOBIOTANICA (2014)",
        "artist_name": "Azuma Makoto", 
        "description": "More than four decades after van Hoeydonck’s project, Japanese artist Makoto Azuma took his floral art practice into outer space in 2014, when he launched a 50-year-old white pine bonsai tree and an bouquet of flowers nearly 100,000 feet into the stratosphere. Dubbed EXOBIOTANICA, the botanical specimens were propelled into space from Black Rock Desert in Nevada through a specially designed balloon and frame made by JP Aerospace, a DIY space operation.Though the project’s time in space lasted just over two hours (100 minutes to reach its peak height and 40 minutes of earthbound descent), six mounted cameras captured stunning stills of the many phases of the project’s trajectory, falling in line with the artist’s goal to see “what kind of beauty shall be born… by giving up the [plant’s] links to life—roots[,] soil[,] and gravity.”",
        "url": "https://news.artnet.com/art-world/art-outer-space-1462288",
        "img": "https://news.artnet.com/app/news-upload/2014/07/07-23-14-azuma-makoto-space-bonsai-1-e1406111998600.jpg",
        "project_id": "003"

    },
    {
        "project_title": "Fallen Astronaut (1971)",
        "artist_name": "Paul Van Hoeydonck", 
        "description": "Without confirmation that the Moon Museum is, in fact, on the moon, the first artwork in space may actually be Fallen Astronaut, a small aluminum sculpture of a collapsed astronaut in a spacesuit made in 1971 by Belgian artist Paul van Hoeydonck. The result of an agreement between the artist and American astronaut David Scott, the three-inch tall sculpture was transported to the surface of the moon by the crew of the Apollo 15 space mission in 1971. Installed next to a plaque listing the names of the fourteen American and Soviet astronauts who had died during the age of space exploration, the sculpture serves as a monument to early cosmic pioneers.",
        "url": "https://news.artnet.com/art-world/art-outer-space-1462288",
        "img": "https://news.artnet.com/app/news-upload/2019/02/Fallen-Astronaut-1024x1021.jpg",
        "project_id": "004"

    },
    {
        "project_title": "Orbital Reflector (2018)",
        "artist_name": "Trevor Paglen", 
        "description": "Trevor Paglen’s Orbital Reflector, one of the most recent projects to make it to space, is also perhaps the most ambitious. Co-produced by the Nevada Museum of Art, the 100-foot-long, 5-foot-wide sculptural balloon (made of material similar to Mylar) is housed in a brick-shaped container. It was launched into space aboard a Space X rocket this past December as part of the largest-ever satellite launch into space in US history.The nonfunctional satellite, which Paglen hopes will “help to change the way we see our place in the world,” is installed about 350 miles away from earth. Because Paglen needed FCC approval for the work, the proper installation of the $1.5 million project was delayed when the longest US government shutdown in history unfolded throughout December and January. The producers are also dependent on CSpOC, a branch of the United States Air Force, to “properly identify each satellite so that they can be tracked as they orbit the earth”, according to a statement released by the Nevada Museum last month. Given the large number of satellites that launched at the same time as Orbital Reflector, this task is still a work in progress.",
        "url": "https://news.artnet.com/art-world/art-outer-space-1462288",
        "img": "https://news.artnet.com/app/news-upload/2018/08/space-steam.png",
        "project_id": "005"

    }


]

# import requests
# from bs4 import BeautifulSoup

# # page = requests.get('https://news.artnet.com/art-world/art-outer-space-1462288')
# page = requests.get('https://www.media.mit.edu/posts/sojourner-2020/')

# soup = BeautifulSoup(page.content, 'html.parser')

# # artproject = soup.find(id='href')
# artproject = soup.find(id='global-footer')
# artproject_items = soup.find_all(class='main-content')

# for artproject in artproject_items:
#     print(f"{artproject.find(class_='main-copy').get_text()}")