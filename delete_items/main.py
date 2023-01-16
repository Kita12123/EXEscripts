"""
同作業ディレクトリ内のデータ削除（ゴミ箱へ）

Args:
    何年前より前を削除
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging
from pathlib import Path
import send2trash
import sys

log_file = Path.cwd() / "delete_log.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="[%(levelname)s]%(asctime)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p"
)


def get_ctime(path: Path, /):
    return datetime.fromtimestamp(path.stat().st_ctime)


def main(deadline, /):
    for path in Path.cwd().glob("*"):
        if path in (log_file, Path(__file__)):
            continue
        if deadline > get_ctime(path):
            send2trash.send2trash(path)
            logging.info(f"Delete -> {path}")


if __name__=="__main__":
    year_ = sys.argv[1]
    if not year_.isdigit():
        raise ValueError("引数に数値以外を指定しています。")
    deadline = datetime.now() - relativedelta(year=int(year_))
    main(deadline)
