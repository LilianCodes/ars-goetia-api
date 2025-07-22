# **Ars Goetia API**
Hello and welcome to the Ars Goetia API! This REST API was created using information from The Lesser Key of Solomon as well as [Demons and Demonolatry](https://demonsanddemonolatry.com). It is **consumption only**. Built with FastAPI.

# **Live Link**
[Ars-Goetia-API](https://ars-goetia-api.onrender.com)

# **Overview**
The Ars Goetia API serves JSON data about the 72 Goetic Demons. This includes: Names, Ranks, Ruling Days, and more. Works wonderful for those occultists and/or developers that want this information at a faster rate than Google.

# **Features**
- Full data on all Goetics.
- Query by ID, name, alternate names, etc.
- Includes `/docs` and `/redoc` via Swagger UI for testing.

# **Endpoints**
- GET /goetia   # Get all Goetics
- GET /goetia/id    # Get all Goetic ID numbers
- GET /goetia/id/{num}  # Get Goetic by specific ID number
- GET /goetia/name  # Get all Goetics by name
- GET /goetia/name/{name}   # Get Goetic by specific name
- GET /goetia/alt-names # Get all Goetics by alternate names
- GET /goetia/alt-names/{name}  # Get Goetic by specific alternate name
- GET /goetia/ruling-days/month/{month} # Get Goetic by Ruling Month
- GET /goetia/ruling-days/sign/{sign}   # Get Goetic by Ruling Astrological Sign
- GET /goetia/ruling-days/day-night/{cycle} # Get Goetic by Day or Night
- GET /geetia/color/{color} # Get Goetic by Ruling Color
- GET /goetia/rank-name/{rank_name}  # Get Goetic by Ruling Rank
- GET /goetia/incense/{incense} # Goetic by Rank Incense
- GET /goetia/metal/{metal} # Get Goetic by Rank Metal
- GET /goetia/celestial/{celestial} # Get Goetic by Celestial Body
- GET /goetia/random    # Get a random Goetic


# **Local Setup**
Local setup is as simple as:

- git clone https://github.com/LilianCodes/ars-api
- cd ars-api
- pip install -r requirements.txt
- uvicorn main:app
- Open http://localhost:8000/docs to interact with the API.

Or you could alternatively download from the Code dropdown, install requirements and start the API.

# **The Stack**
- Python 3.12+
- FastAPI
- Uvicorn
- JSON dataset

# **License**
MIT. Please feel free to fork, remix, or do whatever you desire!

# **Credits**
Built by LilianCodes (xnarisa).

Enjoy the project? Feel free to:
- Donate to my [Ko-Fi](https://ko-fi.com/wispydealings).
- Spread the word with #goetiaapi
