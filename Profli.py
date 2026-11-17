<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <!-- Mengatur tampilan agar responsif di berbagai perangkat -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Judul halaman yang akan muncul di tab browser -->
    <title>[Reynhard Joshua Setiawan]</title>
    <!-- Memuat kerangka kerja CSS Tailwind dari CDN untuk styling yang cepat -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Memuat library ikon Lucide dari CDN -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <!-- Memuat font Inter dari Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Memuat library Chart.js untuk membuat diagram radar -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        /* Gaya dasar untuk seluruh body */
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6; /* Latar belakang terang */
            color: #1f2937; /* Warna teks gelap */
            overflow-x: hidden; /* Mencegah gulir horizontal */
        }
        /* Gaya untuk bagian hero dengan gradasi animasi */
        .container-hero {
            background: linear-gradient(to bottom, #3b82f6, #f3f4f6);
            color: #1f2937;
            background-size: 200% 200%;
            animation: gradient-animation 10s ease infinite;
        }
        /* Definisi animasi gradasi */
        @keyframes gradient-animation {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        /* Gaya untuk gambar profil */
        .profile-pic {
            width: 150px;
            height: 150px;
            border-radius: 50%; /* Membuat gambar bulat */
            object-fit: cover;
            border: 4px solid white;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }
        /* Gaya dasar untuk semua kartu (section) */
        .section-card {
            background-color: white;
            border-radius: 1.5rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            padding: 2.5rem;
        }
        /* Gaya untuk bilah sisi (sidebar) */
        .sidebar {
            transition: transform 0.3s ease-in-out; /* Animasi geser */
        }
        /* Gaya untuk overlay gelap yang muncul saat sidebar terbuka */
        .overlay {
            background-color: rgba(0, 0, 0, 0.5);
            transition: opacity 0.3s ease-in-out; /* Animasi pudar */
        }


        /* Gaya baru untuk tautan navigasi agar terlihat lebih minimalis dan modern */
        .nav-link {
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 0.75rem 1rem;
            border-radius: 0.75rem;
            font-weight: 500;
            transition: background-color 0.2s ease-in-out, transform 0.2s ease-in-out;
            color: white; /* Warna teks putih */
        }
        /* Efek hover untuk tautan navigasi */
        .nav-link:hover {
            background-color: rgba(255, 255, 255, 0.1); /* Latar belakang semi-transparan saat hover */
            transform: translateX(5px); /* Sedikit bergeser ke kanan */
        }


        .sidebar_abc{
            left: 200;
        }
    </style>
</head>
<body class="bg-gray-100 text-gray-800">


    <!-- Sidebar Menu (Tersembunyi secara default) -->
    <div id="sidebar-menu" class="fixed top-0 left-0 h-full w-64 z-50 transform -translate-x-full shadow-lg sidebar bg-gray-800 text-white">
        <div class="p-6">
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-2xl font-bold">Navigasi</h2>
            </div>
            <!-- Daftar tautan navigasi yang diperbarui -->
            <nav class="flex flex-col space-y-2">
                <a href="#about" class="nav-link">
                    <span data-lucide="user" class="w-5 h-5"></span>
                    <span>About Me</span>
                </a>
                <a href="#profile-and-stats" class="nav-link">
                    <span data-lucide="bar-chart-2" class="w-5 h-5"></span>
                    <span>Profil & Statistik</span>
                </a>
                <a href="#education" class="nav-link">
                    <span data-lucide="book-open" class="w-5 h-5"></span>
                    <span>Pendidikan</span>
                </a>
                <a href="#vision" class="nav-link">
                    <span data-lucide="target" class="w-5 h-5"></span>
                    <span>Visi & Misi</span>
                </a>
                <a href="#hobbies" class="nav-link">
                    <span data-lucide="heart" class="w-5 h-5"></span>
                    <span>My Hobbies</span>
                </a>
                <a href="#rewards" class="nav-link">
                    <span data-lucide="award" class="w-5 h-5"></span>
                    <span>Reward</span>
                </a>
                <a href="#projects" class="nav-link">
                    <span data-lucide="code" class="w-5 h-5"></span>
                    <span>Gallery</span>
                </a>
                <a href="#contact" class="nav-link">
                    <span data-lucide="mail" class="w-5 h-5"></span>
                    <span>Social Media</span>
                </a>
            </nav>
        </div>
    </div>


    <!-- Overlay (Tersembunyi secara default) yang muncul di atas konten saat sidebar terbuka -->
    <div id="overlay" class="fixed inset-0 z-40 opacity-0 transition-opacity pointer-events-none overlay"></div>


    <!-- Bagian Header & Hero -->
    <header class="container-hero min-h-[30vh] md:min-h-[40vh] flex flex-col justify-center items-center p-8 relative z-30">
        <!-- Tombol untuk membuka menu sidebar -->
        <button id="menu-btn" class="fixed top-6 left-6 text-gray-700 hover:text-gray-900 focus:outline-none z-50">
            <span data-lucide="menu" class="w-8 h-8"></span>
        </button>
        <!-- Gambar profil -->
        <img class="profile-pic mb-4 transform transition-transform duration-300 hover:scale-105" src="https://lh3.google.com/mail-doc-preview/1ZhqCF56Ftmy6fJ-XVcvWw57oVEXhYkqK=w2880-h1282?authuser=0&auditContext=forDisplay" alt="Menampilkan REINHARD.JPG">
        <!-- logo kalam kudus -->
        <!-- Judul utama dan subjudul -->
        <h1 class="text-3xl md:text-5xl font-bold tracking-tight mb-2 text-center">Reynhard Joshua Setiawan</h1>
        <p class="text-lg md:text-xl font-medium opacity-90 text-center">[-Live For Christ, Die For Christ-]</p>
    </header>


    <!-- Konten utama halaman -->
    <main class="container mx-auto p-4 sm:p-6 md:p-8 lg:p-12">
        <!-- Bagian About Me -->
        <section id="about" class="section-card mb-8 max-w-4xl mx-auto">
            <div class="flex items-center justify-center mb-6">
                <span data-lucide="user" class="text-blue-600 mr-2"></span>
                <h2 class="text-2xl font-bold text-gray-800">About Me</h2>
            </div>
            <p class="text-gray-600 max-w-2xl mx-auto text-justify">
                [A mankind created In God^s image]
            </p>
        </section>
       
        <!-- Bagian Profil & Statistik -->
        <div id="profile-and-stats" class="flex flex-col md:flex-row justify-center items-stretch gap-8 mb-8 max-w-4xl mx-auto">
            <!-- Kartu Profil -->
            <section class="section-card w-full md:w-1/2">
                <div class="flex items-center justify-center mb-6">
                    <span data-lucide="user-circle" class="text-blue-600 mr-2"></span>
                    <h2 class="text-2xl font-bold text-gray-800">Profile</h2>
                </div>
                <!-- Detail profil dalam format list -->
                <div class="space-y-4">
                    <div class="flex items-center space-x-2">
                        <p class="font-semibold text-gray-700 w-36">Nama:</p>
                        <p class="text-gray-600">[Reynhard Joshua Setiawan]</p>
                    </div>
                    <div class="flex items-center space-x-2">
                        <p class="font-semibold text-gray-700 w-36">NISN:</p>
                        <p class="text-gray-600">[NISN]</p>
                    </div>
                    <div class="flex items-center space-x-2">
                        <p class="font-semibold text-gray-700 w-36">Tanggal Lahir:</p>
                        <p class="text-gray-600">[1-Maret-2009]</p>
                    </div>
                    <div class="flex items-center space-x-2">
                        <p class="font-semibold text-gray-700 w-36">Kelas:</p>
                        <p class="text-gray-600">[XI F1]</p>
                    </div>
                    <div class="flex items-center space-x-2">
                        <p class="font-semibold text-gray-700 w-36">Mata Pelajaran Favorit:</p>
                        <p class="text-gray-600">[Matematika TL, Kimia, Biologi]</p>
                    </div>
                </div>
            </section>
           
            <!-- Kartu Statistik dengan Diagram Radar -->
            <section class="section-card w-full md:w-1/2">
                <div class="flex items-center justify-center mb-6">
                    <span data-lucide="bar-chart-2" class="text-blue-600 mr-2"></span>
                    <h2 class="text-2xl font-bold text-gray-800">Statistik</h2>
                </div>
                <!-- Kanvas (canvas) untuk menampilkan diagram -->
                <div class="flex justify-center">
                    <canvas id="radarChart" class="w-full h-auto"></canvas>
                </div>
            </section>
        </div>


        <!-- Bagian Pendidikan -->
        <section id="education" class="section-card mb-8 max-w-4xl mx-auto">
            <div class="flex items-center justify-center mb-6">
                <span data-lucide="book-open" class="text-blue-600 mr-2"></span>
                <h2 class="text-2xl font-bold text-gray-800">Pendidikan</h2>
            </div>
            <!-- Daftar riwayat pendidikan -->
            <div class="space-y-6">
                <div>
                    <h3 class="font-semibold text-gray-800 text-lg">Sekolah Menengah Atas</h3>
                    <p class="text-gray-600 text-sm">[nama sekolah]</p>
                    <p class="text-gray-500 text-xs">[tahun pendidikan]</p>
                    <p class="text-gray-500 text-xs mt-1">[jurusan jika, jika tidak hapus saya command ini]</p>
                </div>
                <div>
                    <h3 class="font-semibold text-gray-800 text-lg">Sekolah Menengah Pertama</h3>
                    <p class="text-gray-600 text-sm">[nama sekolah]</p>
                    <p class="text-gray-500 text-xs">[tahun pendidikan]</p>
                    <p class="text-gray-500 text-xs mt-1">[jurusan jika, jika tidak hapus saya command ini]</p>
                </div>
                <div>
                    <h3 class="font-semibold text-gray-800 text-lg">Sekolah Dasar</h3>
                    <p class="text-gray-600 text-sm">[SD PIUS Payakumbuh]</p>
                    <p class="text-gray-500 text-xs">[2015]</p>
                </div>
            </div>
        </section>


        <!-- Bagian Visi & Misi -->
        <section id="vision" class="section-card mb-8 max-w-4xl mx-auto">
            <div class="flex items-center justify-center mb-6">
                <span data-lucide="target" class="text-blue-600 mr-2"></span>
                <h2 class="text-2xl font-bold text-gray-800">Visi & Misi</h2>
            </div>
            <div class="space-y-4">
                <div class="text-gray-600">
                    <h3 class="text-xl font-semibold text-gray-800 mb-2">Visi:</h3>
                    <p>[visi]</p>
                </div>
                <div class="text-gray-600">
                    <h3 class="text-xl font-semibold text-gray-800 mb-2">Misi:</h3>
                    <ul class="list-disc list-inside space-y-1">
                        <li>[misi]</li>
                        <li>[misi]</li>
                        <li>[misi]</li>
                    </ul>
                </div>
            </div>
        </section>


        <!-- Bagian Hobi -->
        <section id="hobbies" class="section-card mb-8 max-w-4xl mx-auto">
            <div class="flex items-center justify-center mb-6">
                <span data-lucide="heart" class="text-blue-600 mr-2"></span>
                <h2 class="text-2xl font-bold text-gray-800">My Hobbies</h2>
            </div>
            <ul class="list-disc list-inside space-y-2 text-gray-600 max-w-2xl mx-auto">
                <li>[hobby]</li>
                <li>[hobby]</li>
                <li>[hobby]</li>
                <li>[hobby]</li>
            </ul>
        </section>
       
        <!-- Bagian Penghargaan (Reward) -->
        <section id="rewards" class="section-card mb-8 max-w-4xl mx-auto">
            <div class="flex items-center justify-center mb-6">
                <span data-lucide="award" class="text-blue-600 mr-2"></span>
                <h2 class="text-2xl font-bold text-gray-800">Reward</h2>
            </div>
            <ul class="list-disc list-inside space-y-2 text-gray-600 max-w-2xl mx-auto">
                <li>[Prestasi]</li>
                <li>[jika tidak ada prestasi tulis"untuk saat ini saya belum mempunyai prestas, tetapi saya akan terus berusaha untuk kedepannya"]</li>
            </ul>
        </section>


        <!-- Bagian My Project -->
        <section id="projects" class="section-card mb-8 max-w-4xl mx-auto">
            <div class="flex items-center justify-center mb-6">
                <span data-lucide="code" class="text-blue-600 mr-2"></span>
                <h2 class="text-2xl font-bold text-gray-800">Gallery</h2>
            </div>
            <!-- Tampilan galeri dengan grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                <!-- Proyek 1 -->
                <div class="bg-gray-200 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300">
                    <img class="w-full h-64 object-cover rounded-t-xl" src="foto gallery" alt="Web Portofolio Interaktif">
                    <div class="p-4">
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">[judul foto]</h3>
                        <p class="text-sm text-gray-600">[deskripsi foto]</p>
                    </div>
                </div>
                <!-- Proyek 2 -->
                <div class="bg-gray-200 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300">
                    <img class="w-full h-64 object-cover rounded-t-xl" src="foto gallery" alt="Aplikasi Kalkulator Berbasis Python">
                    <div class="p-4">
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">[judul foto]</h3>
                        <p class="text-sm text-gray-600">[deskripsi foto]</p>
                    </div>
                </div>
                <!-- Proyek 3 -->
                <div class="bg-gray-200 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300">
                    <img class="w-full h-64 object-cover rounded-t-xl" src="foto gallery" alt="Desain Logo untuk Komunitas Sekolah">
                    <div class="p-4">
                        <h3 class="text-lg font-semibold text-gray-800 mb-2">[Judul foto]</h3>
                        <p class="text-sm text-gray-600">[deskripsi foto]</p>
                    </div>
                </div>
            </div>
        </section>


        <!-- Bagian Sosial & Kontak -->
        <section id="contact" class="section-card mb-8 max-w-2xl mx-auto">
            <div class="flex items-center justify-center mb-6">
                <span data-lucide="mail" class="text-blue-600 mr-2"></span>
                <h2 class="text-2xl font-bold text-gray-800">Social Media</h2>
            </div>
            <!-- Ikon media sosial -->
            <div class="flex justify-center space-x-6">
                <a href="link akun instagram" class="text-gray-600 hover:text-blue-600 transition" target="_blank">
                    <span data-lucide="instagram" class="w-8 h-8"></span>
                </a>
                <a href="https://wa.me/nomor telepon" class="text-gray-600 hover:text-blue-600 transition" target="_blank">
                    <span data-lucide="message-circle" class="w-8 h-8"></span>
                </a>
                <a href="mailto: ninop940@gmail.com" class="text-gray-600 hover:text-blue-600 transition">
                    <span data-lucide="mail" class="w-8 h-8"></span>
                </a>
            </div>
        </section>


    </main>


    <!-- Bagian footer (kaki halaman) -->
    <footer class="text-center p-6 text-gray-500 text-sm">
        <p>[quotes]</p>
    </footer>


    <script>
        // Menginisialisasi ikon dari library Lucide
        lucide.createIcons();


        // Mendapatkan elemen-elemen dari HTML dengan ID mereka
        const menuBtn = document.getElementById('menu-btn');
        const sidebar = document.getElementById('sidebar-menu');
        const overlay = document.getElementById('overlay');
        const navLinks = document.querySelectorAll('#sidebar-menu a');


        // Fungsi untuk membuka sidebar
        function openSidebar() {
            sidebar.classList.remove('-translate-x-full'); // Geser sidebar ke tampilan
            sidebar.classList.add('translate-x-0');
            overlay.classList.remove('opacity-0', 'pointer-events-none'); // Tampilkan overlay
            overlay.classList.add('opacity-100', 'pointer-events-auto');
        }


        // Fungsi untuk menutup sidebar
        function closeSidebar() {
            sidebar.classList.remove('translate-x-0'); // Geser sidebar keluar tampilan
            sidebar.classList.add('-translate-x-full');
            overlay.classList.remove('opacity-100', 'pointer-events-auto'); // Sembunyikan overlay
            overlay.classList.add('opacity-0', 'pointer-events-none');
        }


        // Menambahkan event listener ke tombol menu
        menuBtn.addEventListener('click', openSidebar);


        // Menutup sidebar saat overlay diklik
        overlay.addEventListener('click', closeSidebar);


        // Menutup sidebar dan melakukan gulir mulus saat link navigasi diklik
        navLinks.forEach(link => {
            link.addEventListener('click', (event) => {
                event.preventDefault(); // Mencegah perilaku default (melompat ke bagian)
               
                // Mendapatkan ID target dari atribut href (misal: dari "#about" menjadi "about")
                const targetId = link.getAttribute('href').substring(1);
                const targetElement = document.getElementById(targetId);


                // Jika elemen target ditemukan, lakukan gulir mulus
                if (targetElement) {
                    targetElement.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
               
                closeSidebar(); // Tutup sidebar setelah mengklik
            });
        });


        // ==========================================================
        // Logika untuk Diagram Radar (Chart.js)
        // ==========================================================
        // Mendapatkan konteks kanvas untuk menggambar diagram
        const ctx = document.getElementById('radarChart').getContext('2d');
        // Data yang akan ditampilkan di diagram
        const radarData = {
            labels: [
                'Kerja Sama Tim',
                'Kreativitas',
                'Kemampuan Beradaptasi',
                'Inisiatif',
                'Logika'
            ],
            datasets: [{
                label: 'Kemampuan Pribadi',
                data: [7, 8, 10, 8, 9], // Nilai untuk setiap label (skala 1-10)
                fill: true,
                backgroundColor: 'rgba(59, 130, 246, 0.2)', // Warna area
                borderColor: 'rgb(59, 130, 246)', // Warna garis
                pointBackgroundColor: 'rgb(59, 130, 246)', // Warna titik
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgb(59, 130, 246)'
            }]
        };


        // Konfigurasi untuk diagram
        const radarConfig = {
            type: 'radar', // Jenis diagram
            data: radarData, // Data yang digunakan
            options: {
                responsive: true, // Diagram akan responsif terhadap ukuran layar
                maintainAspectRatio: false, // Memungkinkan perubahan rasio aspek
                elements: {
                    line: { borderWidth: 3 }
                },
                scales: {
                    r: { // Konfigurasi sumbu radar
                        angleLines: { color: 'rgba(0, 0, 0, 0.1)' },
                        grid: { color: 'rgba(0, 0, 0, 0.1)' },
                        pointLabels: {
                            font: { size: 14, weight: 'bold', family: 'Inter' },
                            color: '#4b5563'
                        },
                        ticks: {
                            display: false, // Sembunyikan angka di sumbu
                            max: 10, min: 0, stepSize: 1
                        }
                    }
                },
                plugins: {
                    legend: { // Konfigurasi legenda (label di atas diagram)
                        display: true,
                        position: 'top',
                        labels: {
                            font: { family: 'Inter', weight: '500' },
                            color: '#1f2937'
                        }
                    }
                }
            },
        };


        // Membuat objek diagram baru
        new Chart(ctx, radarConfig);
    </script>
</body>
</html>



