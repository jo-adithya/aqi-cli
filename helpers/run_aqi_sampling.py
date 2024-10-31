import asyncio
import httpx
import logging
import time

from . import sample_stations_aqi

from typing import Any, Dict, List


async def run_aqi_sampling(
    stations: List[Dict[str, Any]], sampling_period: int, sampling_rate
):
    total_samples = sampling_period * sampling_rate
    time_gap = 60 / sampling_rate
    count_sample, sum_aqi = 0, 0
    async with httpx.AsyncClient(timeout=None) as client:
        start_sampling_time = time.time()
        for i in range(total_samples):
            start_time = time.time()
            time_elapsed = start_time - start_sampling_time
            logging.info(f"Time elapsed: {time_elapsed:.1f}s")
            print("+--------------------------------------+")
            print(
                f"| Sampling data for Minute {time_elapsed // 60:.0f} Sample #{(i % sampling_rate) + 1} |"
            )
            print("+--------------------------------------+")
            aqis = await sample_stations_aqi(client, stations)
            end_time = time.time()
            time_taken = end_time - start_time

            # Print the results
            for station, aqi in zip(stations, aqis):
                count_sample += 0 if aqi is None else 1
                sum_aqi += 0 if aqi is None else aqi
                print(f"Station: {station["station"]["name"]}")
                print(f"AQI (PM2.5): {aqi}\n")

            if i < total_samples - 1:
                await asyncio.sleep(max(time_gap - time_taken, 0))

    print(
        f"Average AQI (PM2.5) for {count_sample} samples across {len(stations)} stations: {sum_aqi / count_sample:.2f}"
    )


__all__ = ["run_aqi_sampling"]
