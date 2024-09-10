http://dionysius-davis-jualjual.pbp.cs.ui.ac.id/

Implementasi Checklist:
1. Membuat sebuah proyek Django baru:
    Membuat folder baru dengan file yang dibutuhkan seperti .gitignore, requirements.txt berisi library yang dibutuhkan, folder venv bernama env yang dibuat dengan command "python -m venv env", serta folder .git yang dibuat dengan command "git init" untuk keperluan git/github.
    Menjalankan command "django-admin startproject tugas1 ." pada folder baru tersebut untuk membuat proyek Django dengan nama tugas1 pada folder tersebut

2. Membuat aplikasi dengan nama main pada proyek tersebut:
    Menjalankan command "python manage.py startapp main" pada folder proyek utama untuk membuat direktori disebut main dengan struktur awal aplikasi Django. Command ini menggunakan file python manage.py pada folder untuk membuat direktori tersebut secara otomatis.

3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main:
    Menambahkan string baru 'main' pada list yang disebut INSTALLED_APPS yang berada pada file python settings.py di direktori proyek django.

4. Membuat model pada aplikasi main dengan nama Product dan memiliki beberapa atribut wajib:
Pada models.py di direktori main, membuat class dengan nama Product dengan argumen models.Model. Class ini berisi variabel yang diinisiasi berdasarkan datatypenya masing-masing, yaitu name(CharField), seller(CharField), price(IntegerField), description(TextField).

5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML:
    Membuat fungsi disebut show_main dengan argumen request. Fungsi ini memiliki dictionary bernama context berisi key-value pair yang akan ditampilkan melalui template HTML. Key-value pair tersebut adalah:
        'app': 'JualJual',
        'npm': '2306213836',
        'name': 'Dionysius Davis',
        'class': 'PBP C'
    Fungsi ini kemudian akan mereturn render(request, "main.html", context), yang berfungsi untuk me-render tampilan template dengan fungsi render yang diimport dari django.shortcuts

6. Membuat file baru urls.py pada direktori main, yang berisi 2 variabel, yaitu app_name dan urlpatterns.
app_name berfungsi untuk memberikan nama unik pada pola URL dalam aplikasi
url_patterns berisi pola URL yang didefinisikan oleh fungsi path (dari django.urls), yang kemudian menggunakan fungsi show_main dari views.py sebagai tampilan ketika URL tersebut diakses.

    Kemudian melakukan routing pada tingkat proyek dengan menambahkan url baru pada urlpatterns, yang dibuat juga dengan fungsi path (dari django.urls) dengan argumen ('', include('main.urls')). include berfungsi untuk mengimpor url dari main.urls yang tadi dibuat, dan path dikosongkan ('') agar halaman aplikasi dapat diakses secara langsung

7. Melakukan deployment pada PWS:
    Membuat proyek baru pada website PWS dengan nama yang saya pilih, kemudian menambahkan variabel baru pada ALLOWED_HOSTS pada settings.py (url dari website tersebut yaitu"dionysius-davis-jualjual.pbp.cs.ui.ac.id").
    Kemudian menambahkan remote proyek pws tersebut pada proyek local. Lalu mengubah branch menjadi master dengan git branch -M master, dan melakukan push dengan git push pws master.

8. Membuat README.md yang berisi tautan dan jawaban dari pertanyaan:
    Membuat file README.md pada direktori utama, dan mengisinya melalui IDE vscode. 

Bagan request client ke aplikasi:
    +-------------+             +------------+           +------------+           +------------+          +-------------+
    |  Client     | ----------> |  urls.py   | --------> |  views.py  | --------> | models.py  |  ------> |  HTML       |
    | (Request)   |  Request    | (Routing)  | Mapping   | (Logic)    | Query     | (Database) |  Fetch   | (Rendering) |
    +-------------+             +------------+           +------------+           +------------+          +-------------+
                                                                                                              |       
                                                                                                    Response  |          
                                                                                                              v          
                                                                                                          +-------------+
                                                                                                          |  Client     |
                                                                                                          | (Response)  |
                                                                                                          +-------------+

    1. Client mengirim request HTTP melalui browser ke URL yang diinginkan.
    2. URL dicek polanya oleh urls.py, jika cocok maka requeast diteruskan ke views.py.
    3. views.py kemudian mengakses data dari models.py dan mengakses template untuk render HTML.
    4. models.py akan menerima request dari views.py, kemudian melakukan instruksi dari request tersebut.
    5. Template HTML akan menampilkan data yang diproses dari views.py dan models.py yang nantinya akan diakses client.
    6. Setelah HTML dirender, maka Django mengirimkan respon HTTP ke client, sehingga ditampilkan ke browser pengguna.

Fungsi git dalam pengembangan perangkat lunak:

    Git berfungsi sebagai version control, sehingga memungkinkan pelacakan perubahan kode dari waktu ke waktu. Sehingga git memungkinkan pengembalian ke versi sebelumnya jika terjadi kesalahan. 
    Git membantu dalam melakukan branching, jika ingin melakukan eksperimen terhadap proyek, sehingga pengembangan fitur atau bug fix dapat lebih terorganisir dan aman.
    Git membantu dalam kolaborasi proyek tim, yang memungkinkan menggabungkan perubahan dari berbagai cabang ke cabang utama.
    Git bisa digunakan bersamaan dengan CI/CD tools, sehingga dapat terus menjalankan integrasi dan deployment pada setiap commit.

Alasan penggunaan framework Django:

    Django menggunakan bahasa python, yaitu bahasa yang dikenal lebih mudah untuk dipelajari. 
    Django menggunakan pola arsitektur Model-View-Template (MVT) yang memisahkan logika bisnis, data, dan tampilan dengan jelas. Struktur ini cukup terorganisir sehingga membantu pemula untuk memahami dengan lebih baik

Alasan model Django disebut sebagai ORM:

    Melalui Django, database dapat dikelola (CRUD) hanya menggunakan python sederhana, tanpa perlu query SQL secara langsung.
    Pada Django, model memetakan tabel dalam database dan memungkinkan pengelolaan relasi antar tabel.