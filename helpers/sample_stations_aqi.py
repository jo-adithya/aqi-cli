import httpx
import asyncio
import logging

from . import get_aqi_data

from typing import Any, Dict, List


async def sample_stations_aqi(
    client: httpx.AsyncClient, stations: List[Dict[str, Any]]
) -> List[float | None]:
    # Iterate over the stations and fetch the AQI asynchronously
    logging.info("fetching AQI data for all stations")
    tasks = [
        get_aqi_data(client, station["lat"], station["lon"]) for station in stations
    ]
    return await asyncio.gather(*tasks)


__all__ = ["sample_stations_aqi"]
