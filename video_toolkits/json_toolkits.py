import json


def load_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data


def dump_json(obj, file_path):
    with open(file_path, "w") as wf:
        json.dump(obj, wf, ensure_ascii=False)


__all__ = ["load_json", "dump_json"]
