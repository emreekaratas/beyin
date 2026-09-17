# beyin

Emre'nin ikinci beyni ve operatör karargahı. Karpathy'nin LLM OS modelinden ilham alan, ham veriyi otonom biçimde bilgi grafiğine derleyen bir kişisel sistem.

## Mimari

| Dizin | Rol | Erişim Kuralı |
| --- | --- | --- |
| `raw/` | Ham veri havuzu | SALT OKUNUR — silme/üzerine yazma yasak |
| `knowledge/` | LLM Wiki (bilgi grafiği) | Ajan derler, tüm kavramlar `[[WikiLinks]]` ile bağlanır |
| `🔮 850-Companion/` | Kalıcı hafıza katmanı | Oturum kapanışında ve düzeltmelerde güncellenir |
| `🧠 500-Knowledge/` | İnsan notları | Yalnızca Emre yazar/düzenler |
| `outputs/` | Teslim alanı | Nihai sentezler ve raporlar |
| `tools/` | CLI araçları | Tekrarlayan veri işleri için Python/Bash betikleri |
| `daily/` | Günlük operatör kayıtları | Vardiya döngüsü çıktıları |

Tüm davranış kuralları ve yükleme sırası `CLAUDE.md` içinde tanımlıdır.

## Akış

1. **Ingest** — kaynak veri `raw/` altına düşer (`tools/fetch_source.py`, `tools/ingest.py`)
2. **Derle** — ajan ham veriyi okuyup `knowledge/concepts/` altında atomik, çift yönlü bağlı kavram kartlarına dönüştürür, `knowledge/index.md` haritasını günceller
3. **Sağlık Denetimi** — `tools/lint.py` / `tools/linter.py` yetim düğüm ve kırık bağlantı taraması yapar
4. **Sentez** — birden fazla kavram birleştirilerek `outputs/` altına operatör raporu teslim edilir

Otonom vardiya döngüsü `tools/watcher.py` ve `tools/run_vardiya.bat` ile çalışır.

## Kurallar

Düzeltme protokolü: bir uyarı/düzeltme geldiğinde bu, gerekçesiyle birlikte `🔮 850-Companion/Kurallar.md` dosyasına kaydedilir. Güncel kural listesi ve nedenleri o dosyada tutulur.
