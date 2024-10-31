
# AQI CLI

Calculate average of air pollutant PM2.5 over n minutes, of all the stations map bound by two pairs of latitudes and longitudes

## Prerequisites

Before cloning the repository, ensure the following are installed on your system:

- **Git**: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- **Python3**: [Install Python3](https://www.python.org/downloads/)


## Cloning the repository

Clone the project and the submodules

```bash
git clone https://github.com/jo-adithya/aqi-cli.git
```

Go to the project directory

```bash
cd aqi-cli
```


## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

| `WAQI_API_TOKEN` |
|---|



## Run Locally

Create a new Python virtual environment and activate it

```bash
python -m venv .venv

# For UNIX environment
source .venv/bin/activate

# For Windows environment (in cmd.exe)
venv\Scripts\activate.bat

# For windows environment (in PowerShell)
venv\Scripts\Activate.ps1
```

Install the required libraries

```bash
pip install -r requirements.txt
```
## Usage/Examples

```bash
usage: python main.py [-h] -lat1 LATITUDE_1 -lng1 LONGITUDE_1 -lat2 LATITUDE_2 -lng2 LONGITUDE_2 [-sp [SAMPLING_PERIOD]] [-sr [SAMPLING_RATE]] [-v]

calculate average of air pollutant PM2.5 over n minutes, of all the stations map bound by two pairs of latitudes and longitudes

options:
  -h, --help            show this help message and exit
  -lat1 LATITUDE_1, --latitude-1 LATITUDE_1
                        latitude of the first point
  -lng1 LONGITUDE_1, --longitude-1 LONGITUDE_1
                        longitude of the first point
  -lat2 LATITUDE_2, --latitude-2 LATITUDE_2
                        latitude of the second point
  -lng2 LONGITUDE_2, --longitude-2 LONGITUDE_2
                        longitude of the second point
  -sp [SAMPLING_PERIOD], --sampling-period [SAMPLING_PERIOD]
                        sampling period in minutes
  -sr [SAMPLING_RATE], --sampling-rate [SAMPLING_RATE]
                        sampling rate in sample(s) / minute
  -v, --verbose         verbose mode
```


## Credits

This project uses the [Air Quality Programmatic APIs](https://aqicn.org/api/) to provide data for retrieving current weather data.

For more information, please refer to their official [documentation](https://aqicn.org/json-api/doc/) and [terms of use](https://aqicn.org/api/tos/).

