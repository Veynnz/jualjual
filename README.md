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