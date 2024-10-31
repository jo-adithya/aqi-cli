import httpx
import logging

from config import WAQI_API_TOKEN, WAQI_API_URL


async def get_aqi_data(
    client: httpx.AsyncClient, latitude: float, longitude: float
) -> float | None:
    try:
        params = {"token": WAQI_API_TOKEN}
        url = f"{WAQI_API_URL}/feed/geo:{latitude};{longitude}"
        response = (await client.get(url, params=params)).raise_for_status().json()
        aqi = response.get("data", {}).get("iaqi", {}).get("pm25", {}).get("v", None)
        return aqi
    except httpx.HTTPError as e:
        logging.error(f"failed to fetch AQI for {latitude}, {longitude}: {e}")


__all__ = ["get_aqi_data"]
