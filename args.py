import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="aqi_cli",
        description="calculate average of air pollutant PM2.5 over n minutes, of all the stations map bound by two pairs of latitudes and longitudes",
        epilog="Have fun!",
    )
    parser.add_argument(
        "-lat1",
        "--latitude-1",
        type=float,
        action="store",
        help="latitude of the first point",
        required=True,
    )
    parser.add_argument(
        "-lng1",
        "--longitude-1",
        type=float,
        action="store",
        help="longitude of the first point",
        required=True,
    )
    parser.add_argument(
        "-lat2",
        "--latitude-2",
        type=float,
        action="store",
        help="latitude of the second point",
        required=True,
    )
    parser.add_argument(
        "-lng2",
        "--longitude-2",
        type=float,
        action="store",
        help="longitude of the second point",
        required=True,
    )
    parser.add_argument(
        "-sp",
        "--sampling-period",
        type=int,
        nargs="?",
        default=5,
        action="store",
        help="sampling period in minutes",
    )
    parser.add_argument(
        "-sr",
        "--sampling-rate",
        type=int,
        nargs="?",
        default=1,
        action="store",
        help="sampling rate in sample(s) / minute",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        action="store_true",
        help="verbose mode",
    )
    return parser.parse_args()
