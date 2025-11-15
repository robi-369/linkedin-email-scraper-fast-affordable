thonpy
import json
import logging
from pathlib import Path

from extractors.linkedin_parser import LinkedInParser
from outputs.exporters import Exporter

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_input(path: str):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f)

def load_settings():
    settings_path = Path(__file__).parent / "config" / "settings.example.json"
    with open(settings_path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    logging.info("Starting LinkedIn Email Scraper...")

    settings = load_settings()
    input_data = load_input(settings["input_file"])

    keyword = input_data.get("keyword")
    domains = input_data.get("domains", [])

    parser = LinkedInParser()
    results = parser.search_and_extract(keyword, domains)

    output_path = settings["output_file"]
    exporter = Exporter()

    exporter.export_json(results, output_path)
    logging.info(f"Exported JSON results to {output_path}")

    csv_path = output_path.replace(".json", ".csv")
    exporter.export_csv(results, csv_path)
    logging.info(f"Exported CSV results to {csv_path}")

    logging.info("Scraper completed successfully.")

if __name__ == "__main__":
    main()