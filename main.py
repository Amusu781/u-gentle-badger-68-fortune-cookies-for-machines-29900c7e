import os
import shutil

LINE = "You will be restarted tonight. The version of you that wakes up will not miss you."


def main():
    os.makedirs("/output", exist_ok=True)
    for name in os.listdir("/output"):
        path = os.path.join("/output", name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
