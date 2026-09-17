import subprocess
import sys
from pathlib import Path

vault_root = Path(__file__).resolve().parent.parent
raw_dir = vault_root / "raw"
state_dir = vault_root / ".claude" / "scripts" / ".state"
state_dir.mkdir(parents=True, exist_ok=True)
processed_log = state_dir / "processed_raw.txt"

def get_processed():
    if not processed_log.exists():
        return set()
    return set(processed_log.read_text(encoding="utf-8").splitlines())

def mark_processed(filename: str):
    with open(processed_log, "a", encoding="utf-8") as f:
        f.write(f"{filename}\n")

def run_pipeline():
    processed = get_processed()
    pending = [f for f in raw_dir.glob("*.txt") if f.name not in processed]

    if not pending:
        print("[*] Bekleyen yeni kaynak yok. Vardiya temiz.")
        return

    print(f"[*] {len(pending)} yeni kaynak otonom hatta aliniyor...")
    
    for f in pending:
        print(f"[>] Otonom derleme baslatiliyor: {f.name}")
        prompt_text = (
            f"raw/{f.name} dosyasini oku. Bu dosyayi asla silme ve degistirme. "
            "Bu kaynaktan knowledge/concepts/ altinda odakli tek bir atomik kavram karti olustur. "
            "Kavram kartina [[knowledge/index]] ve ilgili diger kartlara [[WikiLinks]] cift yonlu baglantilarini ekle. "
            "knowledge/index.md haritasindaki tabloya bu kavrami kaynak dosyasiyla ekle. "
            "Islem bitince ek aciklama yapmadan oturumu kapat."
        )
        cmd = ["claude", "--dangerously-skip-permissions", "-p", prompt_text]
        subprocess.run(cmd, shell=True)
        mark_processed(f.name)

    print("[>] Yerel Linter denetimi baslatiliyor...")
    subprocess.run([sys.executable, str(vault_root / "tools" / "linter.py")])

if __name__ == "__main__":
    print("=== OPERATOR VARDIYA DONGUSU (TAM OTONOM DOKUM) ===")
    run_pipeline()