# -*- coding: utf-8 -*-
"""Validate lesson data: coverage, schema, and duplicate phrases across all 300 lessons."""
import glob
import json
import os
from collections import defaultdict

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

lessons = {}
for path in sorted(glob.glob(os.path.join(DATA, "lessons-*.json"))):
    for item in json.load(open(path, encoding="utf-8")):
        if item["lesson"] in lessons:
            print("DUPLICATE lesson number:", item["lesson"], "in", path)
        lessons[item["lesson"]] = item

missing = [n for n in range(1, 301) if n not in lessons]
print("Lessons loaded:", len(lessons), "| Missing:", missing or "none")

bad = []
for n, item in lessons.items():
    if len(item.get("phrases", [])) != 5:
        bad.append((n, "phrase count != 5"))
    for ph in item.get("phrases", []):
        for key in ("en", "ipa", "vi", "example", "example_vi"):
            if not ph.get(key, "").strip():
                bad.append((n, "empty field " + key))
        if ph.get("ipa") and not ph["ipa"].startswith("/"):
            bad.append((n, "ipa not wrapped in slashes: " + ph.get("ipa", "")))
    if not item.get("hook", "").strip():
        bad.append((n, "empty hook"))
print("Schema issues:", bad or "none")

seen = defaultdict(list)
for n in sorted(lessons):
    for ph in lessons[n]["phrases"]:
        key = ph["en"].strip().lower().rstrip("?.!")
        seen[key].append(n)
dups = {k: v for k, v in seen.items() if len(v) > 1}
print("Duplicate phrases across lessons:", len(dups))
for k, v in sorted(dups.items(), key=lambda x: -len(x[1])):
    print("  %r in lessons %s" % (k, v))
