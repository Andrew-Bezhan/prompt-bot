# build_cases_index.py  v2
import pathlib, datetime, urllib.parse, yaml

rows = []
for md in pathlib.Path("cases").rglob("*.md"):
    front = ""
    with md.open(encoding="utf-8") as fp:
        if fp.readline().strip() == "---":
            for line in fp:
                if line.strip() == "---":
                    break
                front += line
    meta = yaml.safe_load(front) if front else {}

    title   = meta.get("title", md.stem)
    domain  = md.parent.name
    updated = meta.get("last_updated",
                       datetime.date.fromtimestamp(md.stat().st_mtime).isoformat())

    rel        = md.as_posix()                       # ./cases/real/…
    url_target = urllib.parse.quote(rel)             # пробелы → %20
    link       = f"[{rel}](./{url_target})"          # кликабельный Path

    rows.append((link, title, domain, updated))

rows.sort()

with open("cases/index.md", "w", encoding="utf-8") as out:
    out.write("| Path | Title | Domain | Last Updated |\n")
    out.write("| --- | --- | --- | --- |\n")
    for p, t, d, u in rows:
        out.write(f"| {p} | {t} | {d} | {u} |\n")

print("✓ cases/index.md обновлён – все ссылки кликабельны")
