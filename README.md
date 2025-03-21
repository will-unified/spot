# Spotify API Client

This package contains all the functions necessary for connecting to Spotify's Developer API. It provides a set of tools to interact with the API and retrieve data related to music catalogs.

## Getting Started

To run files in this package, use the following command:

````zsh
python -m scripts.get_artist

## Features

- Connect to Spotify's Developer API
- Example scripts for common tasks

## Requirements

- Python 3.x
- Necessary dependencies (listed in `requirements.txt`)

## Installation

1. Clone the repository:
   ```zsh
   git clone https://github.com/will-unified/spotify_api.git
````

2. Navigate to the project directory:
   ```zsh
   cd spotify_api
   ```
3. Install the required dependencies:
   ```zsh
   pip install -r requirements.txt
   ```

## Usage

To use the functions provided by this package, import the necessary module classes in your Python scripts and call their methods as needed.

Example:

```python
from spotify_api.api import FUGAClient
from fuga.products import FUGAProduct

# Initialize the client
api = SpotifyApi(client_id="xxx", client_secret="yyy")
token_data = api.login()

# Initialize SpotifyArtist
artist_api = SpotifyArtist(api)

# Get Artist
artist_data = artist_api.get("<artist_id>")
```

## Acknowledgments

- Spotify for providing the API
