import time
import schedule

from stock_notifier import StockNotifier


def main():
    stock_notifier = StockNotifier()
    stock_notifier.check()


def scheduler():
    schedule.every(60).seconds.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
    scheduler()


