"""
同作業ディレクトリ内のデータ削除（ゴミ箱へ）

Args:
    引数の日付より前を削除
"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging
from pathlib import Path
import send2trash
import sys
from tqdm import tqdm

log_file = Path.cwd() / "delete_log.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="[%(levelname)s]%(asctime)s - %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p"
)


def main(deadline: datetime, /):
    for path in tqdm(Path.cwd().glob("*")):
        # ログファイルは除く
        if path in log_file:
            continue
        # バッチファイルは除く
        if path.suffix == ".bat":
            continue
        timestamp = datetime.fromtimestamp(path.stat().st_ctime)
        td = timestamp - deadline
        if td.days < 0:
            print(f"Delete... -> {path}")
            send2trash.send2trash(path)
            logging.info(f"Delete -> {path}")


if __name__=="__main__":
    day_ = sys.argv[1]
    if not day_.isdigit():
        raise ValueError("引数に数値以外を指定しています。")
    deadline = datetime.now() - relativedelta(days=int(day_))
    main(deadline)
