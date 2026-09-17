import os
import re
from pathlib import Path

vault = Path(__file__).resolve().parent.parent
concepts_dir = vault / "knowledge" / "concepts"
index_file = vault / "knowledge" / "index.md"

def run_lint():
    print("=== BILGI TABANI SAGLIK VE GRAF DENETIMI ===")
    if not concepts_dir.exists():
        print("[HATA]: knowledge/concepts/ dizini bulunamadi.")
        return

    concept_files = list(concepts_dir.glob("*.md"))
    concept_names = [f.stem for f in concept_files]
    index_content = index_file.read_text(encoding="utf-8") if index_file.exists() else ""

    broken_links = []
    orphans = []

    for f in concept_files:
        content = f.read_text(encoding="utf-8")
        links = re.findall(r"\[\[(.*?)\]\]", content)
        
        has_internal_link = False
        for l in links:
            target = l.split("|")[0].split("/")[-1].strip()
            if target and target != "index":
                has_internal_link = True
                if target not in concept_names:
                    broken_links.append((f.name, target))
        
        if f.stem not in index_content and not has_internal_link:
            orphans.append(f.name)

    print(f"Toplam Kavram Karti : {len(concept_files)}")
    print(f"Kirik Baglantilar    : {broken_links if broken_links else '0 (Temiz)'}")
    print(f"Yetim (Orphan) Dugum: {orphans if orphans else '0 (Temiz)'}")

if __name__ == "__main__":
    run_lint()