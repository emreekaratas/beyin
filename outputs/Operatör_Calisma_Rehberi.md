# Operatör Çalışma Rehberi

## Günlük Veri Akışı: Ingest → Derle → Sağlık Kontrolü

**1. Ingest (Ham Veri Girişi)**
Kaynak dokümanlar `raw/` dizinine indekslenir ve bir daha değiştirilmez ([[knowledge/concepts/Sistem-Mimarisi]] — Veri Ayrımı ilkesi). Bu katman salt okunurdur; silme veya üzerine yazma yasaktır.

**2. Derle (Wiki Derleme)**
Ajan `raw/` içeriğini okuyup [[knowledge/concepts/LLM-Wiki-Derleme]] protokolüne göre atomik kavram kartlarına dönüştürür: her kavram ayrı bir `.md` dosyası olur, `knowledge/index.md` haritasına işlenir ve ilgili düğümlere çift yönlü `[[WikiLink]]` ile bağlanır. Bu süreç, ham kaynağı bozmadan bilgiyi grafa dahil eden tekrarlanabilir bir damıtma akışıdır ([[knowledge/concepts/Ajan-Hafizasi]]). İnsan bu katmana elle dokunmaz; düzenleme yetkisi ajanda kalır.

**3. Sağlık Kontrolü (Linting)**
Ajan periyodik olarak [[knowledge/concepts/Ajan-Saglik-Denetimi]] işletir: tutarsız/güncelliğini yitirmiş veriyi tarar, yetim (bağlantısız) düğümleri `knowledge/index.md`'ye işleyip grafa entegre eder, kırık `[[WikiLink]]` referanslarını onarır. Bu adım wiki'nin bütünlüğünü artan biçimde korur.

## Katmanlar ve Sınırlar

| Dizin | Rol | Erişim |
| --- | --- | --- |
| `raw/` | Ham veri havuzu | Salt okunur |
| `knowledge/` | LLM Wiki | Ajan derler, insan izler |
| `🔮 850-Companion/` | Kalıcı hafıza | Oturum kapanışında güncellenir |
| `outputs/` | Teslim alanı | Nihai sentezler burada |

Mimari temel: [[knowledge/concepts/Sistem-Mimarisi]]. Bağlam taşıyıcı: [[knowledge/concepts/Ajan-Hafizasi]].

## Operatör Kuralı
Her yeni kavram kartı üretildiğinde `knowledge/index.md`'ye satır olarak eklenmeli ve en az bir çift yönlü bağlantı almalıdır — yetim düğüm bırakılmaz.
