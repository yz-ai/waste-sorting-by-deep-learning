# :recycle: Derin Öğrenme ile Geri Dönüştürülebilir Atıkların Sınıflandırılması

## Waste Sorting by Deep Learning

İklim değişikliği ve küresel ısınmanın sonuçlarından biri aşırı kaynak tüketiminden kaynaklanmaktadır. Küresel ısınmayı yavaşlatmak ve enerji tasarrufunu arttırmak için atık yönetimi çerçevesinde geri dönüşümün yaygın olarak uygulanması gerekmektedir. Atık yönetimi ve geri dönüşüm yalnızca çevresel açıdan avantajlı olmakla kalmaz, aynı zamanda sürdürülebilir bir ekonomi için de büyük önem taşır. İnsan çalışanlar yerine akıllı sistemleri tercih etmek, insanların refahı yüksek ortamlarında çalışmasını sağlamak sosyal açıdan önemli bir adımdır. Akıllı atık yönetimi yaklaşımları önemli bir araştırma alanıdır.


---

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yz-ai/waste-sorting-by-deep-learning/blob/master/notebooks/waste-sorting-by-dl-training.ipynb) **Google Colab Eğitim Not Defterinde Aç**

---

### [PyIstanbul #111 Python Saati Online Etkinliği](https://www.meetup.com/tr-TR/python-istanbul/events/270976079/)

:apple: Demo ve tüm detaylar için [tıklayınız](https://github.com/yz-ai/waste-sorting-by-deep-learning)

:movie_camera: Sunumun tamamını [buradan](https://www.youtube.com/watch?v=5kTNnXin6r8&feature=youtu.be) izleyebilirsiniz.

:bar_chart: Sunum dosyasına [buradan](https://github.com/yz-ai/waste-sorting-by-deep-learning/) erişebilirsiniz.

Bu çalışma *[M. Ayyüce Kızrak](http://www.ayyucekizrak.com/) T.C. CB Dijital Dönüşüm Ofisi / Bahçeşehir Üniversitesi, [Yavuz Kömeçoğlu](http://blog.yavuzkomecoglu.com/) (Kodiks Bilişim)* tarafından gerçekleştirilmiştir.

---
:octocat: **Veri Kümesi**

[TrashNet:](https://github.com/garythung/trashnet) Kod (yalnızca evrimsel sinir ağı için) ve kullandığımız veri kümesi ve [Mindy Yang](https://github.com/yangmindy4)'ın [Stanford Üniversitesi'nin CS 229: Makine Öğrenimi](http://cs229.stanford.edu/) dersi için dönem sonu projesi. 

---

### Kullanım:

[Orijinal adresten](https://drive.google.com/drive/folders/0B3P9oO5A3RvSUW9qTG11Ul83TEE) veri kümesini indirip, bu repodaki <datasets/dataset-resized> dosyası içine kopyalamak <dataset-resized.zip> kullanabilirsiniz.

Veri kümesini indirdikten sonra ilgili klasöre yükleme işlemeini (örneğin; <datasets/dataset-resized/cardboard> olacak şekilde) tamamladıktan sonra <scripts/split-train-test-val.py> çalıştırılarak <train/test/val> olarak ayrabilirsiniz.

+ Test ratio: '0.17'.
+ Val ratio: '0.13'.
+ Number of Classes: '6'.
allImgsM len 2527
testIdx 429
valIdx 328
trainIdx 1770
+ Training set size: '1770'.
+ Test set size: '429'.
+ Validation set size: '328'

---

:bookmark_tabs: **Makaleler**

**[RecycleNet: Intelligent Waste Sorting Using Deep Neural Networks](https://ieeexplore.ieee.org/document/8466276)**

**Classification of Recyclable Materials Using Efficient Deep Learning Models and Benchmarking of GPU Performance** (Kabul Edildi)

---

:warning: Yapay zekaya dayalı akıllıca tasarlanmış bir atık yönetimi tesisi ile [Birleşmiş Milletler'in sürdürülebilir kalkınma hedeflerinin](https://ec.europa.eu/international-partnerships/sustainable-development-goals_en) gerçekleştirilmesine katkıda bulunarak sürdürülebilir şehirler tasarlamaya ihtiyaç vardır. Akıllı atık yönetimi, küresel ısınmayı durdurmak için en önemli araçlardan biri harcama ve enerji tasarrufudur. Bu sürdürülebilir bir ekonomi için büyük önem taşıyor. Daha sofistike yaklaşımlarla günlük hayatta kullanılacak atık tesisleri tasarlamak önemli hedefler arasında olmalıdır. Atık malzeme sınıflandırması için son teknoloji cihaz uygulamaları hakkında daha fazla araştırma yapılması gerekmektedir. İnsanlar, dünya çapında yapay zekayı kullanılarak elde edilebilecek faydaları ölçülebilir.

---

**Kaynaklar:**

1.	Williams, P. T., Waste Treatment and Disposal, John Wiley & Sons, (2005).
2.	Palmer, J. A., Environmental Thinking in the Early Years: Understanding and Misunderstanding of Concepts Related to Waste Management, Environmental Education Research, Vol. 1, no. 1, (1995), 35–45.
3.	Amick, D. S., Reflection on the Origins of Recycling: a Paleolithic Perspective, Lithic Technology, Vol. 39, no. 1, (2014), 64–69.
4.	Davidson Cummings L., Voluntary Strategies in the Environmental Improvement: Recycling as Cooptation, Journal of Voluntary Action Research, Vol. 6, no. 3-4, (1977), 153–160.
5.	Alvarez-Ch ́avez, C. R., Edwards, S., Moure-Eraso, R., and Geiser, K., Sustainability of Bio-Based Plastics: General Comparative Analysis and Recommendations for Improvement, Journal of Cleaner Production, Vol. 23, no. 1, (2012), 47–56.
6.	Liu, C., Sharan, L., Adelson, E. H., and Rosenholtz, R., Exploring Features in a Bayesian Framework for Material Recognition, in Computer Vision and Pattern Recognition (CVPR), Conference on.IEEE, (2010), 239–246.
7.	Yang, M., and Thung, G., Classification of Trash for Recyclability Status, arXiv preprint, (2016).
8.	Thung, G., Trashnet, GitHub repository, (2016).
9.	Özkaya, U., and Seyfi, L., Fine-Tuning Models Comparisons on Garbage Classification for Recyclability, 2nd International Symposium on Innovative Approaches in Scientific Studies, (2019)
10.	Seredkin, A. V., Tokarev, M. P., Plohih, A., Gobyzov, O. A., and Markovich, D. M., Development of a Method of Detection and Classification of Waste Objects on a Conveyor for a Robotic Sorting System, Journal of Physics: Conference Series, Vol. 1359, (2019).
11.	Vo, A. H., Son, L., H., Vo, M. T., Le, T., A Novel Framework for Trash Classification Using Deep Transfer Learning, IEEE Access, Vol. 7, (2019).
