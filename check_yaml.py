import yaml, sys, pathlib
for f in ("1. LLM_rules.md", "2. LLM-prompt.md"):
    p = pathlib.Path(f)
    if not p.exists():
        sys.exit(f"{f} не найден")
    parts = p.read_text(encoding="utf-8").split('---', 2)
    if len(parts) < 3:
        sys.exit(f"{f}: нет корректного YAML-блока")
    try:
        yaml.safe_load(parts[1])
        print(f"{f}: ✓")
    except yaml.YAMLError as e:
        sys.exit(f"{f}: ошибка YAML → {e}")
print("✓ YAML корректен во всех файлах")
