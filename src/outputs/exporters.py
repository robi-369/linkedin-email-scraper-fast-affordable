thonpy
import json
import csv
from typing import List, Dict
from pathlib import Path

class Exporter:
    def export_json(self, data: List[Dict], path: str):
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)

        with open(p, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def export_csv(self, data: List[Dict], path: str):
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)

        if not data:
            return

        with open(p, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)