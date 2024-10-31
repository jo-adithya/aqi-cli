import asyncio

from args import parse_args
from helpers import get_stations, run_aqi_sampling
from logger import setup_logger


async def main():
    args = parse_args()
    setup_logger(args.verbose)
    stations = get_stations(
        args.latitude_1, args.longitude_1, args.latitude_2, args.longitude_2
    )
    await run_aqi_sampling(stations, args.sampling_period, args.sampling_rate)


if __name__ == "__main__":
    asyncio.run(main())
