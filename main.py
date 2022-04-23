import argparse
import asyncio

from yeelightvrc.simple import YeelightVrcService


async def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", help="The ip of yeelight")
    args = parser.parse_args()

    loop = asyncio.get_event_loop()
    service = YeelightVrcService(args.ip, "127.0.0.1", 9000)
    loop.create_task(service.run())


if __name__ == "__main__":
    asyncio.run(main())
    input("press to continue...")
