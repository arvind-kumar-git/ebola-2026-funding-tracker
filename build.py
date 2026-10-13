#!/usr/bin/env python3
"""Build index.html from the CSV files in data/ and template.html.

Usage:  python3 build.py
The CSVs are the source of truth. Edit them, re-run this script, commit both.
Standard library only.
"""
import csv
import json
import os
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")


def read(name):
    with open(os.path.join(DATA, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def num(s):
    try:
        return float(s)
    except (TypeError, ValueError):
        return None


def main():
    pledges = read("pledges.csv")
    appeals = read("appeals.csv")
    evidence = read("disbursement_evidence.csv")
    timeline = read("timeline.csv")

    for r in pledges:
        r["amount_usd_m"] = num(r["amount_usd_m"])
    for r in appeals:
        for k in ("requirement_usd_m", "received_usd_m", "coverage_pct"):
            r[k] = num(r[k])
    for r in timeline:
        for k in ("pledged_usd_m", "released_usd_m"):
            r[k] = num(r[k])

    counted = [r for r in pledges if r["counts_in_total"] == "Y" and r["amount_usd_m"]]
    payload = {
        "built": date.today().isoformat(),
        "n_pledges": len(pledges),
        "n_counted": len(counted),
        "counted_total_m": round(sum(r["amount_usd_m"] for r in counted), 1),
        "pledges": pledges,
        "appeals": appeals,
        "evidence": evidence,
        "timeline": timeline,
    }
    with open(os.path.join(HERE, "template.html"), encoding="utf-8") as f:
        tpl = f.read()
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    html = tpl.replace("__DATA__", blob).replace("__BUILT__", payload["built"])
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"index.html written: {len(pledges)} pledge rows, {len(counted)} counted, "
          f"${payload['counted_total_m']:,.0f}m itemised")


if __name__ == "__main__":
    main()
