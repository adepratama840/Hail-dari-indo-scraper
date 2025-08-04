from indo_scraper import IndoScraper

scraper = IndoScraper(delay=2.0, timeout=60)

hasil = scraper.scrape(
    url="https://www.smkn5bandung.sch.id/",
    extract_links=True,      # Ekstrak semua link
    extract_images=True,     # Ekstrak semua gambar
    extract_contact=True,    # Ekstrak informasi kontak
    max_pages=3             # Scraping maksimal 3 halaman
)

# Simpan hasil ke JSON
scraper.save_to_json(hasil, "hasil_scraping.json")