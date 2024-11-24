Mühendislil Fakültesi 
Bilgisayar Mühendisliği Bölümü 
1. Diyorjon Ochilov (22040101139) 
2. Yesset Yelebayev (22040101123) 
Soyut 
Derin Öğrenme (DL), sağlık, endüstri ve akademi gibi birçok alanda karmaşık zorlukların 
üstesinden gelmek için son derece etkili olduğunu kanıtlamış olup tiroid teşhisi, akciğer nodülü 
tespiti, bilgisayarlı görü, büyük veri analitiği ve insan seviyesinde karar alma gibi çeşitli 
alanlarda kullanıma sahiptir. Bununla birlikte, dijital teknolojideki gelişmeler, demokrasiyi, 
ulusal güvenliği ve gizliliği tehdit edebilecek yazılımların geliştirilmesine de yol açmıştır. Son 
zamanlarda ortaya çıkan bu DL tabanlı uygulamalardan biri de deepfake teknolojisidir. 
Deepfake sistemleri, sahneleri veya öğeleri değiştirerek insanların gerçeğinden ayırt 
edemeyeceği sahte görüntüler, videolar ve sesler oluşturabilir. Çeşitli teknolojiler sayesinde 
artık bireyler sentetik konuşma, görüntü veya video üretme yeteneğine sahiptir ve bu manipüle 
edilmiş görsellerin kalitesi o kadar yüksektir ki çıplak gözle gerçek içerikten neredeyse ayırt 
edilemez hale gelmiştir. Bu durum, kamuoyunu yanıltmaktan mahkemede sahte deliller 
kullanılmasına kadar çeşitli sorunlara yol açabilir. Bu riskler göz önünde bulundurulduğunda, 
gerçeği manipülasyondan ayırt etmemize yardımcı olacak teknolojiye duyulan ihtiyaç 
kaçınılmaz hale gelmiştir. 
Bu çalışma, DL tabanlı algoritmalar kullanarak deepfake tespit yöntemlerine ilişkin mevcut 
literatürün kapsamlı bir değerlendirmesini sunmaktadır. Deepfake tespit yaklaşımlarını video 
tespiti, görüntü tespiti, ses tespiti ve hibrit multimedya tespiti gibi uygulama alanlarına göre 
sınıflandırıyoruz. Bu makalenin amacı, okuyuculara (1) deepfake'lerin nasıl üretildiği ve tespit 
edildiği, (2) bu alandaki son gelişmeler ve yenilikler, (3) mevcut güvenlik yöntemlerinin zayıf 
yönleri ve (4) daha fazla araştırma ve odaklanma gerektiren alanlar hakkında daha iyi bir 
anlayış kazandırmaktır. Bulgular, Derin Sinir Ağları (CNN) yönteminin bu alanda en yaygın 
kullanılan DL tekniği olduğunu göstermektedir. Araştırmalar, yayınların çoğunluğunun video 
tabanlı deepfake tespiti üzerine odaklandığını ortaya koymaktadır. Çalışmaların çoğu, 
doğruluk parametresi en fazla öne çıkarılan metrik olmak üzere, yalnızca bir metrikte 
iyileştirme yapmayı amaçlamaktadır. 
Bu makale şu başlıklar altında sınıflandırılmıştır: Teknolojiler > Makine Öğrenimi 
Algoritmik 
Gelişim 
Uygulama Alanları > Bilim ve Teknoloji 
Sahte içerik oluşturma 
> 
Multimedya 
Görsel materyalleri manipüle etmek ve farklı hedefleri takip etmek için çeşitli teknikler 
bulunmaktadır . Aşağıdaki bölümde, bunlar arasında en yaygın ve umut verici olanlardan 
bazılarına hızlı bir bakış sunulacaktır. Nesne ekleme, çoğaltma ve silme gibi işlemler oldukça 
sık yapılan manipülasyonlardır . Yeni bir nesne, başka bir resimden (birleştirme) veya aynı 
resimden (kopyala-yapıştır) alınarak eklenebilir. Mevcut bir nesne, arka plan genişletilerek 
örtülmek suretiyle kaldırılabilir (doldurma), örneğin örnek tabanlı doldurma tekniğinde olduğu 
gibi . Tüm bu işlemler, yaygın olarak kullanılan resim düzenleme yazılımları ile kolayca 
gerçekleştirilebilir. Ayrıca, öğeyi sahneye daha iyi uydurmak, görsel çekiciliği artırmak ve 
tutarlı bir perspektif ve ölçek sağlamak için ölçekleme, döndürme veya renk düzeltme gibi 
uygun bir son işlem de yapılabilir . Bu arada, gelişmiş bilgisayar grafikleri teknikleri, DL ve 
çok katmanlı ağlar benzer sonuçlar üretmiştir. 
TANITIM 
Yapay Zeka (YZ) yaklaşımlarının derin sahte (deepfake) algılama alanındaki uygulamalarının, 
görüntü, video ve multimedya içerikleri gibi tüm kategorileri kapsayan ayrıntılı ve kapsamlı 
bir değerlendirmesi bulunmamaktadır. Bu çalışma, sahtekarlık, damgalama, dolandırıcılık, 
aldatma gibi konularla mücadele amacıyla derin sahte içeriklerin YZ yaklaşımlarıyla tespit 
edilmesindeki başarıları ve bu teknolojileri kullanan modern sistemlerin tam bir incelemesini 
sunmaya odaklanmıştır. Son zamanlarda yapılan derin sahte tespit teknikleri üzerine çeşitli YZ 
uygulamalarına dair incelemeler göz önüne alındığında, bu çalışma en ilgi çekici araştırma 
alanına değinerek önemli bir katkı sağlamaktadır. Bu çalışma, ilgili çalışmalardan bulguları 
bulmak, analiz etmek ve birleştirmek amacıyla sistematik bir literatür incelemesi (SLR) 
(Doewes ve ark., 2023; Zadeh ve ark., 2023) yöntemi kullanmaktadır. Derin sahte algılamada 
kullanılan dört ana YZ stratejisi; görüntü derin sahte algılama, video derin sahte algılama, ses 
derin sahte algılama ve hibrit multimedya derin sahte algılamadır. Bu alanda YZ yöntemleri 
kullanan her kategori ve yaklaşım için avantajlar, engeller, veri setleri, kullanım alanları, 
simülasyon ortamları, güvenlik ve aktarım öğrenmesi (TL) gibi çeşitli özellikler 
değerlendirilmiştir. Bu makale, derin sahte algılama alanında YZ yaklaşımlarının kullanımını 
tartışmakta ve çeşitli sorunlara değinmektedir. Ayrıca, gelecekte yapılacak çalışmalara detaylı 
bir şekilde değinilerek çözümlenmesi gereken tüm konular vurgulanmıştır. Özetle, bu 
makalenin katkıları şunlardır: 
Derin sahte algılama alanında YZ konusuna geniş bir bakış sunmak; 
YZ-derin sahte algılama için mevcut yöntemlerin tam bir incelemesini sağlamak; 
Derin sahte algılama ile YZ’yi içeren temel yöntemlerin bir özetini sağlamak; 
YZ-derin sahte algılamada her stratejiyi kritik özelliklerle birlikte incelemek; 
Belirtilen tekniklerin geliştirilebileceği önemli alanları vurgulamak. 
Deepfake Detection 
Bu, sahte içerik tespitinin bir alt alanıdır ve belirli bir kişinin yüzünü veya sesini içeren 
video, ses veya görüntülerin doğruluğunu incelemek için kullanılan yöntemleri kapsar. 
Deepfake tespit algoritmaları, genellikle yapay zeka destekli sinir ağları (CNN, RNN 
gibi) ve derin öğrenme (DL) tabanlı teknikler kullanarak bir videonun veya görüntünün 
orijinalliğini analiz eder. Deepfake'ler sıklıkla belirli özelliklerde (örneğin göz kırpma 
sıklığı, yüz doku detayları) kusur gösterir, ancak bu detaylar çıplak gözle tespit 
edilemeyecek kadar karmaşık olabilir. 
Fake Image Detection (Sahte Görüntü Tespiti) 
Bu yöntemler, tekil görüntülerin sahte veya gerçek olup olmadığını belirlemeye 
odaklanır. Görüntü manipülasyonu genellikle kopyala-yapıştır (copy-move), 
birleştirme (splicing) veya doldurma (inpainting) gibi işlemlerle yapılır. Bu tür tespit 
teknikleri, hatalı pikseller, ışık ve gölge uyumsuzlukları veya aşırı yumuşatılmış 
kenarlar gibi kusurları analiz eder. Çoğu sahte görüntü, Geleneksel Sinir Ağları (CNN), 
Destek Vektör Makineleri (SVM) veya Görsel İmza Analizi gibi algoritmalarla tespit 
edilir. 
Fake Video Detection (Sahte Video Tespiti) 
Sahte video tespiti, bir dizi ardışık görüntüyü analiz ederek videonun gerçek veya sahte 
olup olmadığını belirler. Bu teknik, videolardaki kronolojik tutarsızlıkları, mekansal ve 
zamansal detayları dikkate alır. RCNN (Bölgesel Geleneksel Sinir Ağları) ve RNN gibi 
sinir ağı modelleri, sahte video tespiti için yaygın olarak kullanılır. Ayrıca, yüz ifadesi, 
dudak senkronizasyonu ve göz kırpma gibi davranışsal özelliklerin analiz edilmesi de 
sahte video tespitinde yaygın bir yöntemdir.Geleneksel teknikler ve derin öğrenme 
(DL) yaklaşımları en sık kullanılan yöntemlerdir. Yüz tanıma ve multimedya adli 
bilişiminde canlılık algılama da çözümler sunabilir. Günümüzde DL, gerçeğe yakın 
sahte yüzler oluşturabilir, görünmez sahtecilik izlerini bulabilir ve sahte videoları 
tanıyabilir. DL yaklaşımları, geleneksel görüntü adli bilişim tekniklerinin aksine, 
özellik çıkarma ve özellik sınıflandırmayı bir ağ yapısında birleştirerek baştan sona 
otomatik bir özellik öğrenme ve sınıflandırma yöntemi sağlar (Zheng, Liu, Ni, ve 
diğerleri, 2021). Öte yandan, geleneksel görüntü adli bilişim yöntemleri video için 
genellikle uygun değildir, çünkü sıkıştırma veri kalitesini önemli ölçüde düşürür. DL, 
dijital 
adli 
bilimlerde ilerledikçe, geleneksel görüntü adli yöntemlerini 
değiştirmektedir. Bu nedenle, derin sahte videoları tespit etmek için otomatik 
yaklaşımlar, bu videoların barış ve güvenliği ne kadar etkileyebileceği göz önünde 
bulundurularak son derece önemli hale gelmiştir. 
Bu bölümde, DL yaklaşımlarıyla sahte videoları nasıl tespit edebileceğimizi ele 
alacağız. Güera ve Delp (2018), derin sahte filmleri otomatik olarak tespit eden bir 
zaman farkındalığına sahip bir yöntem sunmuştur. Bu yöntem, ardışık kareleri işlemek 
için bir konvolüsyonel LSTM yapısı kullanmaktadır. Konvolüsyonel LSTM iki önemli 
bileşene sahiptir: (1) Kare özelliklerini çıkarmak için CNN; (2) Zaman dizisi analizini 
yapmak için LSTM. Test edilen bir video dizisinde, her kare için CNN tarafından 
üretilen özellikler çıkarılmıştır. Ardışık karelerin özellikleri birleştirilmiş ve analiz için 
LSTM'ye gönderilmiştir. Son olarak, dizinin derin sahte mi yoksa sahte olmayan bir 
video mu olduğunu belirleme olasılığı hesaplanmıştır. Bu yöntem, farklı video 
sitelerinden toplanmış geniş bir derin sahte video koleksiyonunda test edilmiştir. 
Yapılarının basit olmasına rağmen, sistemin bu görevde rekabetçi sonuçlar elde 
edebildiği görülmüştür. 
Sahte hibrit multimedya tespiti 
Derin sahte içerikler (algoritmalarla değiştirilmiş video, fotoğraf, ses ve görüntüler), sosyal 
medyanın yayılma hızıyla birleştiğinde büyük toplumsal karmaşaya yol açabilir. Dijital 
içeriğin doğruluğunu doğrulamak için derin sahte tespit algoritmaları veya değiştirilemez meta 
veriler gibi anti-dezenformasyon teknolojilerine ihtiyaç vardır. Derin sahte dijital içeriği tespit 
etmek, analiz etmek ve engellemek için doğru şekilde geliştirilmiş araçlara sahip olmak, 
multimedya teknolojisiyle etkileşimde kritik önem taşır. Multimedya içeriği; video, sanat eseri, 
fotoğraf ve ses kayıtları gibi birçok formda olabilir. Dijital içeriğin geçmişini takip etmek için 
güvenilir ve sağlam bir mekanizma olsa bile, bu amaca ulaşmak zorlayıcı olabilir. 
Bu bölümde, hibrit multimedya içeriğini tanımlamak için DL (derin öğrenme) tekniklerini nasıl 
kullanabileceğimizi ele alacağız. Khalil ve arkadaşları (2021), sınıflandırma doğruluğunu 
artırmak için bir kapsül ağı (CapsNet) eğitmek amacıyla doku özelliklerini çıkarma ve Yüksek 
Çözünürlüklü Ağ (HRNet) tabanlı bir strateji kullanan bir derin sahte tespit yöntemi sundu. 
HRNet’in temel fikri, herhangi bir mekansal bilgiyi kaybetmeyi önlemektir; bu durum, kapsül 
ağının temel fikriyle oldukça iyi örtüşmektedir—yalnız, orijinal HRNet’in sonunda bir 
havuzlama katmanı (pooling layer) bulunmaktadır. HRNet'teki havuzlama katmanı çıkarılmış 
ve HRNet’in ürettiği ham özellik vektörü, bu iki fikri en iyi şekilde uyumlu hale getirmiştir. 
Bir kapsül ağı (CapsNet), iyileştirilmiş bir yönlendirme yöntemiyle (Xiao ve ark., 2020; Xiao 
ve ark., 2021) birleştirildiğinde, çok fazla veri veya parametre gerektirmeden daha iyi özellik 
soyutlama ve temsil yetenekleri sunar. "You Only Look Once" (YOLO-v3) yüz tanıma sistemi 
olarak kullanıldığında yanlış pozitif tahminlerde önemli bir azalma sağlanmış ve ek ön işleme 
adımlarına gerek kalmamıştır. İki farklı özellik çıkarma tekniğinin birleşimiyle model daha 
güçlü ve geliştirilmiş hale gelmiştir. Dokulara dayalı yöntem, sahte yüz ve çevresindeki arka 
planın dokuları arasındaki farklılıklara dayanarak modele özgün bir katkı sağlamıştır. CNN 
tabanlı HRNet, kapsül ağına detaylı bilgiler sağlayarak mekansal bilgiyi kaybetmeden en ince 
ayrıntılardan faydalanmayı mümkün kılmıştır. 
HRNet'in sonuçları, girilen görüntülere yapılan bir artırma–normalizasyon adımı ile 
geliştirilmiştir. Üstün özellik soyutlama ve sınıflandırma performansıyla CapsNet, sunulan 
görüntünün gerçek mi yoksa sahte mi olduğunu belirlemiştir. 
