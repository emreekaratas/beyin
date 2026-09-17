# LLM Wiki Derleme Protokolü

- **İndeksleme:** Kaynak dokümanlar `raw/` dizinine değiştirilmeden indekslenir; LLM bu ham veriyi okuyup artan (incremental) şekilde bir wiki'ye — birbirine bağlı `.md` dosyalarından oluşan bir dizin yapısına — dönüştürür.
- **Atomik Kartlaştırma:** Ajan `raw/` içeriğinin özetlerini çıkarır, veriyi kavramlara ayırır, her kavram için ayrı bir makale yazar ve bunları backlink'lerle birbirine bağlar; sonuç tek tek atomik kavram kartlarından oluşan bir graf olur.
- **İnsan Dokunmazlığı:** Wiki'nin tüm verisini LLM yazar ve bakımını yapar; insan (Obsidian üzerinden) yalnızca izler/okur, wiki'ye elle nadiren veya hiç dokunmaz — düzenleme yetkisi ajanda kalır.

[[knowledge/index]] | [[knowledge/concepts/Sistem-Mimarisi]] | [[knowledge/concepts/Ajan-Hafizasi]]
