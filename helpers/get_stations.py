import httpx
import logging
import sys

from config import WAQI_API_TOKEN, WAQI_API_URL


def get_stations(
    latitude1: float,
    longitude1: float,
    latitude2: float,
    longitude2: float,
):
    params = {
        "latlng": f"{latitude1},{longitude1},{latitude2},{longitude2}",
        "token": WAQI_API_TOKEN,
    }
    url = f"{WAQI_API_URL}/v2/map/bounds"
    logging.info(
        f"fetching stations in the bound {latitude1},{longitude1},{latitude2},{longitude2}"
    )

    try:
        data = httpx.get(url, params=params).raise_for_status().json()
        logging.info("stations fetched successfully")
        return data.get("data", [])
    except httpx.HTTPError as e:
        logging.error(f"failed to fetch stations: {e}")
        sys.exit(1)


__all__ = ["get_stations"]
