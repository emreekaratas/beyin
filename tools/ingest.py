import sys
import shutil
from pathlib import Path
from datetime import datetime

def ingest(source_path: str):
    src = Path(source_path)
    if not src.exists():
        print(f"[HATA]: Kaynak dosya bulunamadi: {src}")
        sys.exit(1)

    # Dizinleri hazirla
    vault_root = Path(__file__).resolve().parent.parent
    raw_dir = vault_root / "raw"
    log_file = vault_root / "knowledge" / "log.md"
    raw_dir.mkdir(exist_ok=True)

    # Hedef dosya adi: YYYYMMDD_HHMMSS_dosyaadi.uzanti
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_name = f"{timestamp}_{src.name}"
    dest_path = raw_dir / dest_name

    # Kopyala (Ham veri guvenligi)
    shutil.copy2(src, dest_path)

    # knowledge/log.md kutugune isle
    log_entry = f"| {datetime.now().strftime('%Y-%m-%d %H:%M')} | Ingest | `{dest_name}` | `raw/` altina alindi. |\n"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)

    print(f"[TAMAM]: Kaynak guvenle raw/ altina alindi -> {dest_name}")
    print(f"[TAMAM]: knowledge/log.md guncellendi.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanim: python tools/ingest.py <dosya_yolu>")
        sys.exit(1)
    ingest(sys.argv[1])