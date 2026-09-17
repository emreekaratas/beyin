import sys
import urllib.request
import re
from pathlib import Path
from datetime import datetime

vault_root = Path(__file__).resolve().parent.parent
raw_dir = vault_root / "raw"
log_file = vault_root / "knowledge" / "log.md"

def clean_html(raw_html: str) -> str:
    # Basit HTML etiket temizleme (Harici kütüphane bağımlılığı olmadan)
    text = re.sub(r'<script.*?</script>', '', raw_html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<[^>]+>', ' ', text)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return '\n\n'.join(lines)

def fetch(url: str, slug: str):
    raw_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{timestamp}_{slug}.txt"
    dest_path = raw_dir / filename

    print(f"[*] Kaynak indiriliyor: {url}")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (AI-Operator-Agent)'})
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read().decode('utf-8', errors='ignore')
            text_content = clean_html(content)
            
            dest_path.write_text(text_content, encoding='utf-8')
            print(f"[TAMAM] Ham veri diske yazildi -> raw/{filename}")

            # knowledge/log.md dosyasina isle
            log_entry = f"| {datetime.now().strftime('%Y-%m-%d %H:%M')} | WebFetch | `{filename}` | {url} kaynağından ham veri çekildi. |\n"
            with open(log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
            print(f"[TAMAM] Kütük güncellendi -> knowledge/log.md")

    except Exception as e:
        print(f"[HATA] Kaynak çekilemedi: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Kullanim: python tools/fetch_source.py <URL> <dosya_kisa_adi>")
        sys.exit(1)
    fetch(sys.argv[1], sys.argv[2])