---
title: Kurallar
updated: 2026-09-16
---
# Kurallar

- **kural:** Bir dosyayı değiştirmeden önce mevcut durumunu oku. **neden:** Varsayımlarla içerik ezilmesini önlemek.
- **kural:** `raw/` dizinindeki kaynak dosyalara yazma/silme yapma. **neden:** Kaynak veri bütünlüğünü korumak.
- **kural:** Her kavram sayfasına en az bir çift yönlü bağlantı (`[[bağlantı]]`) ekle. **neden:** Graftsız yetim dosya oluşumunu engellemek.
- **kural:** Çözüm için uzun kod blokları yığma, sistem tasarımını ve çalıştırma komutunu ver. **neden:** Operatör zihniyeti.
- **kural:** Terminal komutları verilirken doğrudan Windows CMD veya Python script formatında verilmeli, tırnak ve yönlendirme kaçışları Windows standartlarına uygun olmalıdır. **neden:** Windows ortamında Bash sözdiziminin yol ve karakter hatalarına yol açması.
- **kural:** Terminal ve dosya işlemlerinde boru (`|`) veya yönlendirme (`>`) içeren ham shell blokları yerine dosya sistemi API'lerini veya Python araçlarını kullan. **neden:** Windows CMD ortamında boru karakterlerinin ayrıştırıcıyı bozması.