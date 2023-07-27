# tmdb-ten
## Description

tmdb-ten is a Python ETL (Extract, Transform, Load) script that fetches data for ten movies from the TMDB (The Movie Database) API, performs data transformation, and exports the results to CSV files. The script retrieves movie details such as title, overview, release date, IMDb ID, runtime, budget, revenue, vote count, vote average, popularity, and genres. It then cleans and organizes the data to make it more accessible and exports it into three CSV files: `tmdb_ten_movies.csv`, `tmdb_ten_genres.csv`, and `tmdb_ten_datetimes.csv`.

### TL;DR

ETL pipeline for ten movies from TMDB API.

Extract: Get ten movies data from TMDB API with non-recurring pull.

Transform: Structure, format, and selection of essential data. We format data from JSON responses to pandas dataframes.

Load: Export them as CSV ready to be loaded to an external application.

## Getting Started

To use this script and retrieve movie data from TMDB, you'll need to install the necessary dependencies listed in the `requirements.txt` file. Make sure you have Python installed on your system.

## Installation

1. Clone this repository to your local machine or download the `tmdb-ten.py` file.

2. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Ensure you have obtained an API key from TMDB. If you don't have one, you can create an account at https://www.themoviedb.org/ and request an API key.

2. Open the `tmdb-ten.py` file and replace `'YOUR_API_KEY'` in the `config` module with your actual TMDB API key:

```python
# Replace 'YOUR_API_KEY' with your TMDB API key
API_KEY = 'YOUR_API_KEY'
```

3. Execute the script using Python:

```bash
python tmdb-ten.py
```

4. The script will fetch the movie data for the ten specified movies from TMDB, perform data transformation, and export the cleaned data into three CSV files in the same directory:

- `tmdb_ten_movies.csv`: Contains essential movie details like title, overview, IMDb ID, runtime, budget, revenue, vote count, vote average, popularity, and genre columns.

- `tmdb_ten_genres.csv`: Contains a list of unique genres extracted from the movie data.

- `tmdb_ten_datetimes.csv`: Contains additional information about movie release dates, including the day, month, year, and day of the week.

## Note

This script provides a simple demonstration of ETL operations with TMDB API data. Depending on your use case, you can further customize the script to fetch more movies or additional data attributes.

Please remember to comply with TMDB's terms of service and API usage guidelines while using this script.

Feel free to reach out if you have any questions or need further assistance! Happy coding!

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to unit tests as needed.

## License

This project is licensed under an [MIT license](https://github.com/pizofreude/tmdb-ten/blob/main/LICENSE).