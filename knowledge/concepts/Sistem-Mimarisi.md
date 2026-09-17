# Sistem Mimarisi

- **Operatörün Masası (Vault):** Tüm sistem tek bir Obsidian vault'u üzerinde çalışır; dizin yapısı hem insan hem ajan için ortak gezinme haritasıdır.
- **İş Tarifi (CLAUDE.md):** Kimlik, yükleme sırası, veri akışı kuralları ve düzeltme protokolünü tanımlayan tek otorite kaynağıdır; tüm ajan davranışı buna bağlıdır.
- **Veri Ayrımı (raw → knowledge → outputs):** `raw/` salt okunur ham veri havuzudur; ajan bunu derleyip `knowledge/` altında çift yönlü bağlantılı kavram kartlarına dönüştürür; nihai sentezler `outputs/` altında teslim edilir.
- **Hafıza Kancaları:** `🔮 850-Companion/` katmanı (Core, Kurallar, Last-Session, Threads) oturum başında yüklenir ve oturum kapanışında/düzeltmelerde güncellenerek kalıcı bağlamı taşır.

[[knowledge/index]] | [[knowledge/concepts/Ajan-Hafizasi]] | [[knowledge/concepts/LLM-Wiki-Derleme]] | [[knowledge/concepts/Prompt-Engineering]]
