import csv


def load_csv(file_path):
    # 1.打开文件
    with open(file_path, encoding='utf-8') as f:
        # 2.生成csv读取器
        reader = csv.reader(f)
        next(reader)
        return list(reader)
