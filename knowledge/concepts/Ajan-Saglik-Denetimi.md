# Ajan Sağlık Denetimi (Linter)

- **Tutarsızlık Taraması:** Ajan wiki üzerinde periyodik sağlık kontrolleri (health checks) çalıştırarak çelişen veya güncelliğini yitirmiş verileri tespit eder ve eksik veriyi tahmin/tamamlar (impute).
- **Yetim Düğüm Temizliği:** Hiçbir kavram kartı bağlantısız kalmamalıdır; denetim, `knowledge/index.md` haritasına işlenmemiş veya çift yönlü bağlantısı eksik kalan yetim düğümleri bulup graf'a entegre eder.
- **Kırık Bağlantı Onarımı:** Denetim mekanizması, hedefi olmayan referanslarını ve ilginç yeni bağlantı adaylarını belirleyerek wiki'nin bütünlüğünü artan biçimde (incrementally) iyileştirir.

[[knowledge/index]] | [[knowledge/concepts/LLM-Wiki-Derleme]]
