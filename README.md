http://dionysius-davis-jualjual.pbp.cs.ui.ac.id/

# TUGAS 2

1. Implementasi Checklist:

    - Membuat sebuah proyek Django baru:

        Membuat folder baru dengan file yang dibutuhkan seperti .gitignore, requirements.txt berisi library yang dibutuhkan, folder venv bernama env yang dibuat dengan command "python -m venv env", serta folder .git yang dibuat dengan command "git init" untuk keperluan git/github.
        Menjalankan command "django-admin startproject tugas1 ." pada folder baru tersebut untuk membuat proyek Django dengan nama tugas1 pada folder tersebut

    - Membuat aplikasi dengan nama main pada proyek tersebut:

        Menjalankan command "python manage.py startapp main" pada folder proyek utama untuk membuat direktori disebut main dengan struktur awal aplikasi Django. Command ini menggunakan file python manage.py pada folder untuk membuat direktori tersebut secara otomatis.

    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main:

        Menambahkan string baru 'main' pada list yang disebut INSTALLED_APPS yang berada pada file python settings.py di direktori proyek django.

    - Membuat model pada aplikasi main dengan nama Product dan memiliki beberapa atribut wajib:

        Pada models.py di direktori main, membuat class dengan nama Product dengan parameter models.Model. Class ini berisi variabel yang diinisiasi berdasarkan datatypenya masing-masing, yaitu name(CharField), seller(CharField), price(IntegerField), description(TextField).

    - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML:

        Membuat fungsi disebut show_main dengan parameter request. Fungsi ini memiliki dictionary bernama context berisi key-value pair yang akan ditampilkan melalui template HTML. Key-value pair tersebut adalah:
            'npm': '2306213836',
            'name': 'Dionysius Davis',
            'class': 'PBP C'
        Fungsi ini kemudian akan mereturn render(request, "main.html", context), yang berfungsi untuk me-render tampilan template dengan fungsi render yang diimport dari django.shortcuts

    - Membuat routing pada urls.py:

        Membuat file baru urls.py pada direktori main, yang berisi 2 variabel, yaitu app_name dan urlpatterns.
        app_name berfungsi untuk memberikan nama unik pada pola URL dalam aplikasi
        url_patterns berisi pola URL yang didefinisikan oleh fungsi path (dari django.urls), yang kemudian menggunakan fungsi show_main dari views.py sebagai tampilan ketika URL tersebut diakses.
        Kemudian melakukan routing pada tingkat proyek dengan menambahkan url baru pada urlpatterns, yang dibuat juga dengan fungsi path (dari django.urls) dengan argumen ('', include('main.urls')). include berfungsi untuk mengimpor url dari main.urls yang tadi dibuat, dan path dikosongkan ('') agar halaman aplikasi dapat diakses secara langsung

    - Melakukan deployment pada PWS:

        Membuat proyek baru pada website PWS dengan nama yang saya pilih, kemudian menambahkan variabel baru pada ALLOWED_HOSTS pada settings.py (url dari website tersebut yaitu"dionysius-davis-jualjual.pbp.cs.ui.ac.id").
        Kemudian menambahkan remote proyek pws tersebut pada proyek local. Lalu mengubah branch menjadi master dengan git branch -M master, dan melakukan push dengan git push pws master.

    - Membuat README.md yang berisi tautan dan jawaban dari pertanyaan:

        Membuat file README.md pada direktori utama, dan mengisinya melalui IDE vscode. 

2. Bagan request client ke aplikasi:
    ![Screenshot 2024-09-11 111353](https://github.com/user-attachments/assets/47b7eb8f-ca7d-4cd9-b0ce-4310035e8984)


    1. Client mengirim request HTTP melalui browser ke URL yang diinginkan.
    2. URL dicek polanya oleh urls.py, jika cocok maka requeast diteruskan ke views.py.
    3. views.py kemudian mengakses data dari models.py dan mengakses template untuk render HTML.
    4. models.py akan menerima request dari views.py, kemudian melakukan instruksi dari request tersebut.
    5. Template HTML akan menampilkan data yang diproses dari views.py dan models.py yang nantinya akan diakses client.
    6. Setelah HTML dirender, maka Django mengirimkan respon HTTP ke client, sehingga ditampilkan ke browser pengguna.

3. Fungsi git dalam pengembangan perangkat lunak:

    Git berfungsi sebagai version control, sehingga memungkinkan pelacakan perubahan kode dari waktu ke waktu. Sehingga git memungkinkan pengembalian ke versi sebelumnya jika terjadi kesalahan. 
    Git membantu dalam melakukan branching, jika ingin melakukan eksperimen terhadap proyek, sehingga pengembangan fitur atau bug fix dapat lebih terorganisir dan aman.
    Git membantu dalam kolaborasi proyek tim, yang memungkinkan menggabungkan perubahan dari berbagai cabang ke cabang utama.
    Git bisa digunakan bersamaan dengan CI/CD tools, sehingga dapat terus menjalankan integrasi dan deployment pada setiap commit.

4. Alasan penggunaan framework Django:

    Django menggunakan bahasa python, yaitu bahasa yang dikenal lebih mudah untuk dipelajari. 
    Django menggunakan pola arsitektur Model-View-Template (MVT) yang memisahkan logika bisnis, data, dan tampilan dengan jelas. Struktur ini cukup terorganisir sehingga membantu pemula untuk memahami dengan lebih baik

5. Alasan model Django disebut sebagai ORM:

    Melalui Django, database dapat dikelola (CRUD) hanya menggunakan python sederhana, tanpa perlu query SQL secara langsung.
    Pada Django, model memetakan tabel dalam database dan memungkinkan pengelolaan relasi antar tabel.

# TUGAS 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

    Hampir seluruh platform pasti berurusan dengan pertukaran data antara user, aplikasi, dan sistem, yang bisa menjadi sumber latency terhadap platform tersebut. Oleh karena itu dibutuhkan data delivery yang efisien, agar data dapat disampaikan secara cepat (atau bahkan real-time), agar platform tetap responsif terhadap penampilan dan pembaharuan data. Hal ini penting bagi pengalaman user, yang sangat bergantung pada responsivitas dari sebuah platform.
    Selain itu, data delivery yang konsisten juga diperlukan agar setiap aspek sistem pada platform mendapatkan data yang sinkron, akurat, dan up-to-date. Hal ini penting terutama bagi aplikasi seperti business inteligence platform yang memerlukan data sedetail mungkin.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    
    Menurut pendapat saya, JSON lebih baik untuk digunakan dibanding XML, dikarenakan tampilannya yang jauh lebih sederhana dan mudah dimengerti. Strukturnya yang simpel dan ringkas ini membuat JSON lebih populer dibandingkan XML, karena ukurannya cenderung lebih kecil (krusial untuk handling data dalam jumlah banyak), serta lebih mudah untuk diparsing dan dimanipulasi.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    
    Secara singkat, method is_valid() berfungsi untuk memastikan bahwa data yang disubmit user pada form tersebut valid. Validasi ini meliputi beberapa hal seperti:
    - Tipe data yang sesuai yang didefinisikan
    - Panjang data sesuai dengan aturan yang didefinisikan
    - Tidak ada input field yang kosong
    - Memenuhi aturan-aturan spesifik lain seperti username yang harus unik

    Jika data tersebut tidak valid, maka aplikasi dapat mengirimkan feedback berupa pesan kesalahan yang sesuai pada user. Method is_valid() juga membantu dalam mencegah serangan cyber seperti injection attacks, sehingga menjaga agar data yang disimpan aman.

4.  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

    csrf_token berfungsi untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). CSRF adalah serangan dimana penyerang mengirimkan permintaan tidak sah melalui seorang pengguna yang sah/diautentikasi. 
    
    Tanpa csrf_token, aplikasi menjadi rentan terhadap serangan csrf tersebut. Permintaan tidak sah tersebut akan dijalankan tanpa ada konfirmasi lebih lanjut, sehingga dapat membahayakan sistem ataupun data pengguna. Penyerangan ini dapat melibatkan pengguna tanpa sepengetahuannya, yang mungkin tertipu oleh situs atau link yang berbahaya.

    Penyerang menyiapkan perangkap bagi pengguna yang dapat berupa situs atau link yang berbahaya. Pengguna yang tertipu akan hal itu, akan diarahkan menuju sebuah aplikasi, dimana mereka harus memasukkan kredensial mereka. Setelah pengguna login, situs/link tersebut akan mengirimkan kode permintaan POST ke aplikasi target, misalnya untuk memodifikasi data. Karena tidak ada csrf_token, dan permintaan datang dari pengguna yang sah, maka permintaan dieksekusi tanpa disadari. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    - ### Membuat input form untuk menambahkan objek model pada app sebelumnya.

    Pertama, membuat file forms.py pada direktori main. Class ProductForm diberi parameter ModelForm untuk mendefinisikannya sebagai form. Class ini memiliki model Product (dari models.py) dengan field yang berisi atribut dari product tersebut. Berikut kode langsung dari forms.py:

    ```bash
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "seller", "description", "price"]
    ```

    Kemudian, terdapat beberapa perubahan yang harus dilakukan pada views.py. 
        - Mengimport redirect dari django.shortcuts
        - Pada context di fungsi show_main, menambahkan key-value pair untuk product.
        - Menambahkan fungsi create_mood_entry yang berfungsi untuk menambahkan objek Product secara otomatis ketika data disubmit dari form. Fungsi ini juga menghandle validasi input dari form tersebut.
    Berikut adalah kode yang ditambahkan pada views.py:

    ```bash
    from django.shortcuts import render, redirect
    ...

    def show_main(request):
        ...
        context = {
            ...
            'products': products
        }

    ...

    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "create_product.html", context)
    ```


    - ### Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

    Karena ingin show by id, maka perlu ditambahkan variabel id pada class Product di file models.py, agar tiap objek memiliki id yang unik untuk mencegah celah keamanan pada id. Id tersebut dibuat secara unik menggunakan uuid. Berikut kode yang ditambahkan pada file models.py:

    ```bash
    ...
    import uuid
    
    class ...
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        ...
    ```

    Pertama, mengimport HttpResponse dan serializers dari django.http dan django.core. Kemudian menambahkan 4 fungsi tersebut, yaitu show_xml, show_json, show_xml_by_id, dan show_json_by_id. Masing-masing fungsi menerima parameter request, memiliki variabel data yang menyimpan seluruh objek product, serta me-return HttpResponse yang berisi 2 parameter, yaitu data hasil query yang diserialisasi menjadi json/xml dan content_type="application/...". (... adalah "xml"/"json", mengikuti jenis fungsi yang dibuat).
    Untuk fungsi yang show by id, maka fungsi memiliki parameter tambahan id, dan data yang disimpan pun difilter terlebih dahulu menggunakan id. Untuk lebih jelas, maka berikut adalah kode yang ditambahkan pada views.py:

    ```bash
    ...
    from django.http import HttpResponse
    from django.core import serializers

    ...
    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    ```

    - ### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2. 

    Mengimport kelima function baru dari views.py ke urls.py, dan menambahkan setiap path URL untuk setiap metode pengaksesan data pada urlpatterns. Berikut adalah kode yang perlu ditambahkan pada urls.py:

    ```bash
    ...
    urlpatterns = [
        ...
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```

    ## POSTMAN Screenshot

    1. XML
        ![Screenshot 2024-09-16 185355](https://github.com/user-attachments/assets/dadf51c6-f2ea-4388-8e09-ff95d646e69b)
    2. XML by ID
        ![Screenshot 2024-09-16 185423](https://github.com/user-attachments/assets/bd8b2bdc-7622-4e9e-9ad9-3cc874371da9)
    3. JSON
        ![Screenshot 2024-09-16 185442](https://github.com/user-attachments/assets/15887604-005e-4975-b45a-e7b9c62e254a)
    4. JSON by ID
        ![Screenshot 2024-09-16 185458](https://github.com/user-attachments/assets/5252e298-24d4-453b-8edb-3d4125c3f8d7)

# TUGAS 4

### 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()

HttpResponseRedirect() harus menerima URL lengkap, atau menggunakan reverse untuk mencari URL tersebut. Sedangkan redirect() dapat menerima nama view atau objek model yang kemudian digunakan mencari URL yang sesuai. Selain itu redirect() juga memungkinkan penerimaan argumen seperti **args** dan **kwargs**.

Dapat dikatakan bahwa redirect() adalah versi *shortcut* dari HttpResponseRedirect().


### 2. Jelaskan cara kerja penghubungan model Product dengan User!

Menambahkan atribut user pada model Product yang berisi models.ForeignKey(User, on_delete=models.CASCADE). Foreign key ini bertujuan sebagai referensi antara product dengan user yang sedang logged in, sehingga product tersebut hanya menjadi milik user tersebut. Product tersebut pun hanya akan ditampilkan jika user yang sedang logged in adalah user yang direferensikan melalui foreign key tersebut.

### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

- *Authentication*:
    Authentication adalah proses verifikasi pengguna yang mencoba untuk log in
- *Authorization*:
    Authorization dilakukan setelah user telah diautentikasi, untuk menentukan hak/akses yang akan dimiliki oleh pengguna.

Django mengimplementasikan *authentication* pada django.contrib.auth, melalui proses seperti *login*, *logout*, dan *register*. Sedangkan authorization diimplementasikan melalui *permissions* dan *groups*.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

- Melalui *session*:
    Django membuat *session* baru unik setiap pengguna baru log in.
    *Session* ini menjadi pengingat bagi aplikasi untuk selalu memverifikasi pengguna tersebut di setiap *request* mereka.

- *Cookies*:
    *Cookies* berfungsi untuk menyimpan informasi penting seperti **session key**, **settings/preferensi user**, dan informasi dari pengguna lainnya.
    - Tidak semua *cookies* aman digunakan, karena ada yang tidak terenkripsi sehingga rentan terhadap serangan. Ada juga *cookies* yang menyimpan informasi sensitif seperti password dan lain-lain.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

#### - Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

####     a. registrasi:
- Membuat fungsi register menggunakan **UserCreationForm()** yang diimport dari **django.contrib.auth.forms** pada **views.py** di **main**.
![Screenshot 2024-09-24 204036](https://github.com/user-attachments/assets/1c8fb30e-b5de-4fe7-9ea0-edcf9cb208d0)

- Membuat file baru **register.html** pada direktori **templates** sebagai halaman register yang berisi form ini:
![Screenshot 2024-09-24 204309](https://github.com/user-attachments/assets/0d6eef6a-697e-47f8-9c4d-37298c375994)

Menambahkan juga url dari **register.html** pada **urls.py** di **main**

####     b. login:
- Membuat fungsi login dengan mengimplementasikan **AuthenticationForm** yang diimport dari **django.contrib.auth.forms** dan method **authenticate** serta **login** dari **django.contrib.auth** pada **views.py** di **main**.
![Screenshot 2024-09-24 204659](https://github.com/user-attachments/assets/6f0037a6-df16-4002-bbc1-3b09f672f391)
- Membuat file baru **login.html** pada direktori **templates** sebagai halaman login yang berisi form ini:
![Screenshot 2024-09-24 204852](https://github.com/user-attachments/assets/c1bf81a1-1865-4100-a298-b6cd5ad68384)

Menambahkan juga url dari **login.html** pada **urls.py** di **main**, serta menambahkan restriksi akses untuk pengguna yang belum login dengan menambahkan **@login_required(login_url='/login')** di atas fungsi **show_main()** **views.py**.


####     c. logout:
- Membuat fungsi logout dengan menggunakan **logout** yang diimport dari django.contrib.auth, kemudian di redirect ke halaman login. Fungsi ini dibuat pada views.py di main.
![Screenshot 2024-09-24 205214](https://github.com/user-attachments/assets/6af39c6c-6294-4c5a-9596-056120491357)

#### - Membuat dua akun pengguna dengan masing-masing tiga *dummy* data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

- Memanfaatkan halaman yang sudah dibuat pada step sebelumnya untuk registrasi 2 user, dan login menggunakan user-user tersebut.
- Kemudian mendaftarkan 3 *product* untuk masing-masing user menggunakan form yang sudah dibuat pada tugas sebelumnya.

#### - Menghubungkan model Product dengan User.
        
- Pada class Product di models.py, menambahkan atribut baru yaitu user yang berisi models.ForeignKey(User, on_delete=models.CASCADE). (Perlu mengimport **User*** dari **django.contrib.auth.models** terlebih dahulu)
- Mengubah isi fungsi **create_product** pada **views.py** di **main** menjadi:
![Screenshot 2024-09-24 210622](https://github.com/user-attachments/assets/774941dc-0b89-4e2b-a4f2-3f6e4afacf1d)
- Mengubah value dari **product** pada **show_main** di **views.py** menjadi **MoodEntry.objects.filter(user=request.user)**

#### - Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan **cookies** seperti **last login** pada halaman utama aplikasi.

- Pada fungsi **login_user** di **views.py**, selalu menambahkan *cookie* baru dengan fungsi **set_cookie** dari **HttpResponseRedirect**. *Cookie* ini menyimpan *datetime* saat user tersebut login.
- *Cookie* ditampilkan pada *main page* aplikasi, dan dihapus ketika user logout.

# TUGAS 5

### 1.  Jika terdapat beberapa *CSS selector* untuk suatu elemen `HTML`, jelaskan urutan prioritas pengambilan *CSS selector* tersebut!

Urutan prioritas pengambilan CSS selector:
1. *inline style* : style="..." (Langsung pada elemen di html)
2. *IDs* : #myId {...}
3. *Classes* : .myClass {...}
4. *Element(div, p, h1)* dan *Pseudo-Element(::before, ::after) selectors* : p {...}
5. *Universal* : * {...}

*CSS selector* akan memprioritaskan sesuai urutan tersebut. Sebuah *styling* pada suatu selector hanya akan diterapkan jika tidak terdapat *styling* dari *selector* (prioritas) sebelumnya.

### 2. Mengapa *responsive design* menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan *responsive design*!

- Aplikasi yang menerapkan *responsive design*:
- - https://www.youtube.com/
- - https://www.facebook.com/
- - dll

- Aplikasi yang belum menerapkan *responsive design*:
- - https://dequeuniversity.com/library/responsive/1-non-responsive

### 3. Jelaskan perbedaan antara *margin*, *border*, dan *padding*, serta cara untuk mengimplementasikan ketiga hal tersebut!

#### - *Margin*
- - *Margin* adalah batas antara suatu elemen dengan elemen lainnya.
.example {
    Margin: 20px;
}

Pada contoh ini, *elemen* dengan *class* `example` akan memiliki jarak sebesar `20px` dari *elemen* lain pada semua sisinya.

#### - *Border*
- - *Border* adalah garis yang mengelilingi suatu elemen. 
.example {
    border: 2px solid black;
}

Pada contoh ini, *elemen* dengan *class* `example` akan dikelilingi suatu *border* selebar `2px` yang berupa garis *solid* berwarna hitam.

#### - *Padding*
- - *Padding* adalah jarak antara suatu elemen dengan *bordernya*.
.example {
    padding: 10px;
}

Pada contoh ini, *elemen* dengan *class* `example` akan memiliki jarak `10px` antara isi *elemen* dengan *bordernya*.

### 4. Jelaskan konsep *flex box* dan *grid layout* beserta kegunaannya!
- *Flex box* adalah sebutan untuk jenis container elemen, yang dapat mengatur ukuran dan posisi dari elemen di dalamnya secara satu dimensi (horizontal atau vertikal). *Flex box* berperan sebagai sebuah container dari *elemen-elemen* yang ingin diatur. *Flex box* memungkinkan *elemen-elemen* ini untuk diselaraskan dengan mudah satu dengan yang lain, baik untuk posisinya ataupun ukurannya, sehingga dapat membantu dalam pembuatan *web responsif*.

- - Walaupun sama-sama berperan sebagai container, berbeda dengan *flex box*, *grid layout* digunakan untuk mengatur elemen dalam dua dimensi, yaitu horizontal dan vertikal secara bersamaan. Setiap ruang elemen dapat diatur secara presisi, sehingga memungkinkan kombinasi ukuran dan posisi dengan lebih mudah. *Grid layout* juga sangant membantu dalam pembuatan *web responsif*, dan dapat lebih mudah menangani design website yang kompleks dikarenakan kemampuannya dalam mengatur ruang 2 dimensi.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Implementasikan fungsi untuk menghapus dan mengedit product.
- - Menambahkan fungsi baru create_product dan edit_product pada views.py, menambahkan path yang sesuai pada urls.py, lalu membuat halaman baru (create_product.html dan edit_product.html) untuk membuat/mengedit produk tersebut.

- - - modifikasi pada views.py
![Screenshot 2024-10-02 091215](https://github.com/user-attachments/assets/16bca58b-3a91-43b4-90f1-6f5cfa395bb1)

- Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS Tailwind
- - Menggunakan *CSS Tailwind* untuk mengcustom desain dari `login.html`, `register.html`, dan `create_product.html`. Menggunakan *CSS* untuk membuat halaman menjadi *responsive* dan lebih menarik dengan membuat *button*, memberi warna, *positioning*, dll.
- - Menggunakan CSS Tailwind untuk membuat halaman lebih menarik, dan menggunakan flex box sebagai container untuk menjaga web agar tetap responsif.
- - - Menambahkan *if statement* pada `main.html` untuk mengecek jika produk memiliki value atau tidak. Jika tidak maka menampilkan gambar yang sudah dipilih.
- - - Membuat file baru `card_product.html` yang sudah diedit dengan *CSS Tailwind* untuk menampilkan setiap produk dengan menarik. File ini akan dipanggil untuk setiap produk yang ada dengan field yang diisi oleh info produk tersebut.
- - Membuat 2 *button* tersebut yang berfungsi untuk menjalankan salah satu dari 2 fungsi baru (*edit* dan *delete*) pada `views.py` ketika di *click*.
- - Membuat file baru `navbar.html` dengan opening dan *closing tag nav*. *Navbar* ini diisi dengan beberapa *shortcut button*, *logout button*, info pengguna, dll. Kemudian menginclude *navbar* ini pada halaman lain seperti `main.html`, `create_product.html`, dan `edit_product.html`. Mengimplementasikan 2 mode, yaitu untuk desktop dan mobile, sehingga navbar tetap responsif.