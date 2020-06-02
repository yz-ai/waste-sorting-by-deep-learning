# :recycle: Derin Öğrenme ile Geri Dönüştürülebilir Atıkların Sınıflandırılması

## Waste Sorting by Deep Learning


### :octocat: Veri Kümesi

[TrashNet:](https://github.com/garythung/trashnet) Kod (yalnızca evrimsel sinir ağı için) ve kullandığımız veri kümesi ve [Mindy Yang](https://github.com/yangmindy4)'ın [Stanford Üniversitesi'nin CS 229: Makine Öğrenimi](http://cs229.stanford.edu/) dersi için dönem sonu projesi. 

---

### Veri Kümesi Kullanımı:

[Orijinal adresten](https://drive.google.com/drive/folders/0B3P9oO5A3RvSUW9qTG11Ul83TEE) `dataset-resized.zip` isimli veri kümesini indirip, `datasets/dataset-resized/` altına kopyalayınız.

Veri kümesini indirdikten sonra eğitime hazır hale getirmek için, `scripts/split-train-test-val.py` veri kümesini ayırma scriptini aşağıdaki şekilde çalıştırarak <train/test/val> olarak ayrabilirsiniz.

```
python3 split-train-test-val.py --testRatio 0.17 --valRatio 0.13 ../datasets/dataset-resized
```

Veri kümesini bölme işlemi sonucunda train/test/val sayıları aşağıdaki gibidir.

- Training set: 1770
- Test set: 429
- Validation set: 328
