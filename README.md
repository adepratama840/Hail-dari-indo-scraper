# Indo Scraper v1.0.0

**Web Scraper Indonesia** - Tool scraping website yang powerful dan mudah digunakan untuk mengekstrak data dari website Indonesia dengan dukungan bahasa Indonesia yang optimal.

**Developer**: Ade Pratama  
**GitHub**: https://github.com/adepratama840  
**Email**: adepratama20071907@gmail.com  
**Version**: 1.0.0

## 🚀 Fitur Utama

- **Scraping Multi-Halaman**: Ekstrak data dari beberapa halaman sekaligus
- **Ekstraksi Komprehensif**: Dapatkan konten, link, gambar, dan informasi kontak
- **Anti-Detection**: Sistem delay dan timeout untuk menghindari pemblokiran
- **Export JSON**: Simpan hasil scraping dalam format JSON yang terstruktur
- **Optimized untuk Indonesia**: Mendukung encoding dan struktur website Indonesia

## 📋 Persyaratan Sistem

- **Python 3.7+** (Wajib)
- **Git** (untuk cloning repository)
- **pip** (Python package manager)
- **Koneksi internet** stabil
- **RAM minimum** 512MB
- **Storage** minimal 100MB free space

### Dependencies yang Diperlukan
- `requests` - HTTP library
- `beautifulsoup4` - HTML parsing
- `lxml` - XML parser
- `urllib3` - HTTP client
- `certifi` - SSL certificates

## 🔧 Instalasi Multi-Platform

### 📱 Android (Termux)
```bash
# Update packages
pkg update && pkg upgrade

# Install Python dan Git
pkg install python git

# Clone repository
git clone https://github.com/adepratama840/Hasil-dari-indo-scraper.git
cd Hasil-dari-indo-scraper

# Install dependencies
pip install -r requirements.txt

# Test installation
python indo-scraper.py
```

### 💻 Windows (CMD)
```cmd
# Pastikan Python sudah terinstall
python --version

# Clone repository
git clone https://github.com/adepratama840/Hasil-dari-indo-scraper.git
cd Hasil-dari-indo-scraper

# Install dependencies
pip install -r requirements.txt

# Test installation
python indo-scraper.py
```

### 💻 Windows (PowerShell)
```powershell
# Check Python installation
python --version

# Clone repository
git clone https://github.com/adepratama840/Hasil-dari-indo-scraper.git
Set-Location -Path "Hasil-dari-indo-scraper"

# Install dependencies
pip install -r requirements.txt

# Test installation
python indo-scraper.py
```

### 🐧 Linux (Ubuntu/Debian)
```bash
# Update system
sudo apt update && sudo apt upgrade

# Install Python dan Git
sudo apt install python3 python3-pip git

# Clone repository
git clone https://github.com/adepratama840/Hasil-dari-indo-scraper.git
cd Hasil-dari-indo-scraper

# Install dependencies
pip3 install -r requirements.txt

# Test installation
python3 indo-scraper.py
```

### 🐧 Linux (CentOS/RHEL/Fedora)
```bash
# Update system
sudo yum update  # atau sudo dnf update untuk Fedora

# Install Python dan Git
sudo yum install python3 python3-pip git  # atau sudo dnf install

# Clone repository
git clone https://github.com/adepratama840/Hasil-dari-indo-scraper.git
cd Hasil-dari-indo-scraper

# Install dependencies
pip3 install -r requirements.txt

# Test installation
python3 indo-scraper.py
```

### 🍎 macOS
```bash
# Install Homebrew (jika belum ada)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python dan Git
brew install python git

# Clone repository
git clone https://github.com/adepratama840/Hasil-dari-indo-scraper.git
cd Hasil-dari-indo-scraper

# Install dependencies
pip3 install -r requirements.txt

# Test installation
python3 indo-scraper.py
```

## 🚨 Troubleshooting Instalasi

### ❌ Error: Python tidak ditemukan

**Windows:**
```cmd
# Download Python dari python.org
# Atau install via Microsoft Store
# Pastikan centang "Add Python to PATH"
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt install python3-dev python3-venv

# CentOS/RHEL
sudo yum install python3-devel
```

**Termux:**
```bash
pkg install python-dev
```

### ❌ Error: pip tidak ditemukan

**Windows:**
```cmd
python -m ensurepip --upgrade
```

**Linux/macOS:**
```bash
sudo apt install python3-pip  # Ubuntu/Debian
sudo yum install python3-pip  # CentOS/RHEL
```

**Termux:**
```bash
pkg install python-pip
```

### ❌ Error: Git tidak ditemukan

**Windows:**
- Download Git dari https://git-scm.com/
- Install dengan default settings

**Linux:**
```bash
sudo apt install git  # Ubuntu/Debian
sudo yum install git  # CentOS/RHEL
```

**Termux:**
```bash
pkg install git
```

### ❌ Error: Permission denied

**Linux/macOS:**
```bash
# Gunakan virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# atau
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### ❌ Error: SSL Certificate

**Semua Platform:**
```bash
pip install --upgrade certifi
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt
```

### ❌ Error: Module tidak ditemukan

```bash
# Install manual satu per satu
pip install requests beautifulsoup4 lxml urllib3 certifi

# Atau force reinstall
pip install --force-reinstall -r requirements.txt
```

### ❌ Error: Encoding/Unicode (Windows)

**CMD:**
```cmd
chcp 65001
set PYTHONIOENCODING=utf-8
python indo-scraper.py
```

**PowerShell:**
```powershell
$env:PYTHONIOENCODING="utf-8"
python indo-scraper.py
```

## 💻 Cara Penggunaan

### Import Module
```python
from indo_scraper import IndoScraper
```

### Penggunaan Dasar
```python
from indo_scraper import IndoScraper

# Inisialisasi scraper
scraper = IndoScraper(delay=2.0, timeout=60)

# Scraping website
hasil = scraper.scrape(
    url="https://example.com",
    extract_links=True,
    extract_images=True,
    extract_contact=True,
    max_pages=3
)

# Simpan hasil
scraper.save_to_json(hasil, "hasil_scraping.json")
```

### Parameter Konfigurasi

| Parameter | Tipe | Default | Deskripsi |
|-----------|------|---------|-----------|
| `delay` | float | 2.0 | Waktu jeda antar request (detik) |
| `timeout` | int | 60 | Timeout untuk setiap request |
| `extract_links` | bool | True | Ekstrak semua link dari halaman |
| `extract_images` | bool | True | Ekstrak semua URL gambar |
| `extract_contact` | bool | True | Ekstrak informasi kontak |
| `max_pages` | int | 1 | Maksimal halaman yang akan di-scrape |

## 📤 Format Output

Hasil scraping akan berupa dictionary dengan struktur:

```json
{
  "url": "URL target",
  "domain": "Domain website",
  "title": "Judul halaman",
  "description": "Deskripsi meta",
  "content": "Konten teks lengkap",
  "links": ["array_link"],
  "images": ["array_gambar"],
  "contact_info": {
    "emails": ["email1", "email2"],
    "phones": ["telp1", "telp2"],
    "addresses": ["alamat1", "alamat2"]
  },
  "metadata": "metadata_lengkap",
  "status": "success",
  "scraped_pages": 3,
  "timestamp": "waktu_scraping"
}
```

## ⚡ Contoh Implementasi

### Scraping Website Sekolah
```python
scraper = IndoScraper(delay=2.0, timeout=60)

hasil = scraper.scrape(
    url="https://www.smkn5bandung.sch.id/",
    extract_links=True,
    extract_images=True,
    extract_contact=True,
    max_pages=3
)

print(f"Berhasil scrape {hasil['scraped_pages']} halaman")
print(f"Total link ditemukan: {len(hasil['links'])}")
print(f"Email kontak: {hasil['contact_info']['emails']}")
```

## ⚠️ Penting untuk Diperhatikan

### Etika Scraping
- **Hormati robots.txt** dari website target
- **Gunakan delay yang wajar** untuk tidak membebani server
- **Patuhi terms of service** website yang di-scrape
- **Jangan scraping data pribadi** tanpa izin

### Batasan Legal
- Tool ini untuk **tujuan edukasi dan riset** yang sah
- User bertanggung jawab atas **penggunaan yang legal**
- **Tidak untuk spamming** atau aktivitas merugikan
- Patuhi **undang-undang perlindungan data** yang berlaku

## 🛠️ Troubleshooting

### Error Umum dan Solusi

**1. Connection Timeout**
```python
# Tingkatkan timeout
scraper = IndoScraper(timeout=120)
```

**2. Rate Limited**
```python
# Perbesar delay
scraper = IndoScraper(delay=5.0)
```

**3. Encoding Error**
```python
# Pastikan website mendukung UTF-8
# Tool sudah dioptimasi untuk website Indonesia
```

## 📈 Kontribusi

Kami menerima kontribusi untuk pengembangan tool ini:

1. **Fork** repository ini
2. **Buat branch** fitur baru (`git checkout -b fitur-baru`)
3. **Commit** perubahan (`git commit -am 'Tambah fitur baru'`)
4. **Push** ke branch (`git push origin fitur-baru`)
5. **Buat Pull Request**

## 📞 Support

Jika mengalami kendala atau membutuhkan bantuan:

- **GitHub Issues**: https://github.com/adepratama840/Hasil-dari-indo-scraper/issues
- **Email Developer**: adepratama20071907@gmail.com
- **Documentation**: Baca dokumentasi lengkap di repository

## 📜 Lisensi

Distributed under MIT License. Lihat `LICENSE` untuk informasi lengkap.

## 🙏 Disclaimer

Tool ini dibuat untuk membantu developer Indonesia dalam melakukan web scraping yang legal dan etis. Penggunaan tool ini sepenuhnya menjadi tanggung jawab user. Developer tidak bertanggung jawab atas penyalahgunaan tool ini.

---

**Dibuat dengan oleh Ade Pratama untuk komunitas developer Indonesia**

---

## 👨‍💻 About Developer

**Ade Pratama**  
- GitHub: https://github.com/adepratama840
- Email: adepratama20071907@gmail.com
- Version: 1.0.0

*Kontribusi dan feedback sangat dihargai untuk pengembangan tool ini lebih lanjut.*
