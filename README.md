# SOLDATEN SMS BOMBER — Python Edition

```
███████╗ ██████╗ ██╗      ██████╗  █████╗ ████████╗███████╗███╗   ██╗
██╔════╝██╔═══██╗██║     ██╔══██╗██╔══██╗╚══██╔══╝██╔════╝████╗  ██║
███████╗██║   ██║██║     ██║  ██║███████║   ██║   █████╗  ██╔██╗ ██║
╚════██║██║   ██║██║     ██║  ██║██╔══██║   ██║   ██╔══╝  ██║╚██╗██║
███████║╚██████╔╝███████╗██████╔╝██║  ██║   ██║   ███████╗██║ ╚████║
╚══════╝ ╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═══╝
```

> ⚠️ **Yalnızca eğitim / araştırma amaçlıdır. İzinsiz kullanım yasaktır.**

---

## Kurulum

### Kali Linux / Debian / Ubuntu

```bash
# Python 3.8+ gerekli
python3 --version

# Pip ile bağımlılıkları yükle
pip3 install -r requirements.txt

# Çalıştır
python3 main.py
```

### Windows

```powershell
# Python 3.8+ kurulu olmalı
python --version

# Bağımlılıkları yükle
pip install -r requirements.txt

# Çalıştır
python main.py
```

---

## Proje Yapısı

```
Soldaten Sms Tool/
├── main.py               ← Ana giriş noktası
├── requirements.txt      ← Python bağımlılıkları
├── README.md
└── modules/
    ├── __init__.py
    ├── ascii_art.py      ← SOLDATEN banner + terminal görselleri
    ├── animations.py     ← Spinner, typewriter, matrix rain
    └── sms.py            ← 50+ Türk API hedefi (async/aiohttp)
```

---

## Özellikler

- **50+ servis** eş zamanlı (asyncio + aiohttp) olarak çalışır
- **Renkli terminal** çıktısı (colorama)
- **SOLDATEN ASCII** banner
- **Spinner & countdown** animasyonları
- **Hit / Miss** log sistemi
- **Kali Linux** ile tam uyumlu

---

## Bağımlılıklar

| Paket      | Versiyon | Açıklama                    |
|------------|----------|-----------------------------|
| aiohttp    | 3.9.5    | Async HTTP istekleri         |
| colorama   | 0.4.6    | Renkli terminal çıktısı      |
