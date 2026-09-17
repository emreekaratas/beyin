# Prompt Engineering

Bağlantılar: [[knowledge/index]], [[knowledge/concepts/Vibe-Coding]], [[knowledge/concepts/Sistem-Mimarisi]]

- **Tanım:** Üretken yapay zeka modellerinden istenen çıktıyı almak için doğal dil girdilerini ("prompt") yapılandırma sürecidir; ilişkili disiplin olan "context engineering" ise sistem talimatları, araçlar ve token bütçesi gibi prompt-dışı bağlamın yönetimine odaklanır.
- **Temel Teknikler:** Few-shot/multi-shot örnekleme, chain-of-thought (adım adım akıl yürütme) ve türevi self-consistency, tree-of-thought (paralel dallanan akıl yürütme), rol atama ve retrieval-augmented generation (RAG) ile otomatik prompt üretimi/optimizasyonu (ör. DSPy, GEPA). Modellerin prompt formatına ve sıralamasına aşırı duyarlı olması (bazı çalışmalarda %40'ı aşan doğruluk farkı) tekniğin kırılganlığının temel nedenidir.
- **Operatör Mimarisindeki Rolü:** `beyin` sisteminde CLAUDE.md, Kurallar.md ve oturum talimatları birer prompt/context engineering ürünüdür — Emre'nin niyetini ajan davranışına çeviren katman budur; [[knowledge/concepts/Vibe-Coding]]'in kurumsal disiplin haline gelmiş biçimi olarak, ajanın ham veriyi derleyip [[knowledge/concepts/Sistem-Mimarisi]] sınırları içinde çalışmasını sağlar.
