# Handy — menzo fork

🇹🇷 [Türkçe](#türkçe) &nbsp;|&nbsp; 🇬🇧 [English](#english)

A fork of [cjpais/Handy](https://github.com/cjpais/Handy) with a reworked recording
overlay. [Download](#download--i̇ndirme) · [upstream docs](https://github.com/cjpais/Handy#readme)

## English

**What's different**

- **Smaller pill** — 88×24 instead of 172×40, native window resized to match. The
  record dot and cancel button are gone; they crowded the animation at this size.
- **Always black** — `#000` in both themes instead of following the app theme,
  which used to go light-on-light over bright windows.
- **Travelling waveform** — upstream binds each mark to its own FFT bucket, so
  neighbours flash independently. Here the spectrum is collapsed to its peak and
  shifted along the row, so a swell crosses the pill. Marks are dots at rest and
  stretch into bars from the centre out.
- **Slides in and out** instead of appearing on the spot.
- **Stop sound** plays once the text has been pasted, not on key release.

**Custom sounds** — drop `custom_start.wav` and `custom_stop.wav` into the app data
dir (`%APPDATA%\com.pais.handy\` on Windows) *before* launching, then pick Custom
under Sound Theme in the debug panel (`Ctrl+Shift+D`). The option stays hidden until
both files exist, and it is not in normal settings.
`scripts/gen_custom_sounds.py` generates a pair.

**Install** — [Download](#download--i̇ndirme) the Windows build, or build from source
with upstream's [BUILD.md](BUILD.md).

## Türkçe

Bu, [cjpais/Handy](https://github.com/cjpais/Handy)'nin kayıt göstergesi yeniden
tasarlanmış bir fork'u. Handy tamamen çevrimdışı çalışan bir konuşma-yazıya
uygulaması: kısayola bas, konuş, yazı imlecin olduğu yere düşsün. Ses bilgisayarından
çıkmıyor.

**Türkçe dikte için model seçimi — önemli**

Modeli **Whisper Large v3 Turbo** olarak ayarla. Handy varsayılan olarak Parakeet'i
öneriyor ama Parakeet 25 Avrupa dilini kapsıyor ve **Türkçe bunların arasında yok** —
Türkçe konuşursan anlamsız çıktı alırsın. Whisper ailesi Türkçeyi destekliyor,
Large v3 Turbo da bunların en iyi dengesi.

Ayrıca faydalı olanlar:

- **Dili Türkçe'ye sabitle.** Otomatik algılamada Türkçe-İngilizce karışık
  konuşurken model cümle ortasında dil değiştirebiliyor.
- **Özel kelimeler (Custom Words).** Sürekli kullandığın teknik terimleri ekle
  (README, commit, repo…). Transkripsiyon sonrası bulanık eşleştirmeyle düzeltiyor;
  Whisper'ın Türkçe konuşma içindeki İngilizce terimleri kaçırma sorununu büyük
  ölçüde kapatıyor.
- **Unload Model → Never.** VRAM'in müsaitse modeli bellekte tut; aradan zaman
  geçince ilk dikte yavaş başlamaz. Boşta CPU ya da güç harcamıyor.

**Bu fork'ta ne değişti**

- **Daha küçük gösterge** — 172×40 yerine 88×24. Kayıt noktası ve çarpı kaldırıldı.
- **Her temada saf siyah** — eskiden uygulama temasını takip ediyor, aydınlık
  pencerelerin üstünde beyaz kalıyordu.
- **Soldan sağa akan dalga** — upstream'de her nokta ayrı bir frekans bandına bağlı
  olduğu için komşular bağımsız zıplıyordu. Artık tek bir ses seviyesi satır boyunca
  kaydırılıyor; noktalar dinlenirken daire, konuşurken merkezden çubuğa uzuyor.
- **Süzülerek açılıp kapanıyor.**
- **Bitiş sesi** tuşu bıraktığında değil, yazı yapıştıktan sonra çalıyor.

**Özel sesler** — `custom_start.wav` ve `custom_stop.wav` dosyalarını uygulamayı
**açmadan önce** `%APPDATA%\com.pais.handy\` klasörüne koy, sonra debug panelinden
(`Ctrl+Shift+D`) Sound Theme → Custom seç. Seçenek, iki dosya da yoksa listede
görünmüyor ve normal ayarlarda değil.

## Download / İndirme

Grab the Windows installer from [Releases](https://github.com/canmenzo/Handy/releases).
It is **unsigned**, so SmartScreen warns on first run — choose *More info → Run anyway*.
Building from source: see upstream's [BUILD.md](BUILD.md).

Windows kurulum dosyası [Releases](https://github.com/canmenzo/Handy/releases)
sayfasında. **İmzasız** olduğu için Windows ilk açılışta uyarı verir; *Daha fazla
bilgi → Yine de çalıştır* de. Kaynaktan derlemek için [BUILD.md](BUILD.md).

---

Fork of [cjpais/Handy](https://github.com/cjpais/Handy) — full docs, models and
troubleshooting live there. MIT, unchanged; see [LICENSE](LICENSE).
