-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 19, 2021 at 12:48 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sppd`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_customer`
--

CREATE TABLE `accounts_customer` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `date_created` datetime(6) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'admin'),
(2, 'customer');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add anggaran', 7, 'add_anggaran'),
(26, 'Can change anggaran', 7, 'change_anggaran'),
(27, 'Can delete anggaran', 7, 'delete_anggaran'),
(28, 'Can view anggaran', 7, 'view_anggaran'),
(29, 'Can add instansi', 8, 'add_instansi'),
(30, 'Can change instansi', 8, 'change_instansi'),
(31, 'Can delete instansi', 8, 'delete_instansi'),
(32, 'Can view instansi', 8, 'view_instansi'),
(33, 'Can add pegawai', 9, 'add_pegawai'),
(34, 'Can change pegawai', 9, 'change_pegawai'),
(35, 'Can delete pegawai', 9, 'delete_pegawai'),
(36, 'Can view pegawai', 9, 'view_pegawai'),
(37, 'Can add rincian', 10, 'add_rincian'),
(38, 'Can change rincian', 10, 'change_rincian'),
(39, 'Can delete rincian', 10, 'delete_rincian'),
(40, 'Can view rincian', 10, 'view_rincian'),
(41, 'Can add surat_perintah', 11, 'add_surat_perintah'),
(42, 'Can change surat_perintah', 11, 'change_surat_perintah'),
(43, 'Can delete surat_perintah', 11, 'delete_surat_perintah'),
(44, 'Can view surat_perintah', 11, 'view_surat_perintah'),
(45, 'Can add sppd', 12, 'add_sppd'),
(46, 'Can change sppd', 12, 'change_sppd'),
(47, 'Can delete sppd', 12, 'delete_sppd'),
(48, 'Can view sppd', 12, 'view_sppd'),
(49, 'Can add pengeluaran', 13, 'add_pengeluaran'),
(50, 'Can change pengeluaran', 13, 'change_pengeluaran'),
(51, 'Can delete pengeluaran', 13, 'delete_pengeluaran'),
(52, 'Can view pengeluaran', 13, 'view_pengeluaran'),
(53, 'Can add customer', 14, 'add_customer'),
(54, 'Can change customer', 14, 'change_customer'),
(55, 'Can delete customer', 14, 'delete_customer'),
(56, 'Can view customer', 14, 'view_customer');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$nD1xcwblKKLfOIGkqt9zh3$GjjW/GJLwUDwIV6r7fxtUF4oWTDJVX7RW9L7xI+9mHU=', '2021-06-18 22:31:08.000000', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2021-06-18 22:29:37.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-06-18 22:31:26.603663', '1', 'admin', 1, '[{\"added\": {}}]', 3, 1),
(2, '2021-06-18 22:31:40.339370', '2', 'customer', 1, '[{\"added\": {}}]', 3, 1),
(3, '2021-06-18 22:31:52.910224', '1', 'admin', 2, '[{\"changed\": {\"fields\": [\"Groups\"]}}]', 4, 1),
(4, '2021-06-18 22:35:16.607860', '1', 'DINAS KOMUNIKASI, INFORMATIKA, PERSANDIAN DAN STATISTIK', 1, '[{\"added\": {}}]', 8, 1),
(5, '2021-06-18 22:37:49.871464', '1', 'FRANS PIETER ISTIA, S.SOS, MM', 1, '[{\"added\": {}}]', 9, 1),
(6, '2021-06-18 22:38:48.334180', '2', 'YETI HATTI RUMPUMBO', 1, '[{\"added\": {}}]', 9, 1),
(7, '2021-06-18 22:39:55.826072', '3', 'STEVANUS INDOUW, SH', 1, '[{\"added\": {}}]', 9, 1),
(8, '2021-06-18 22:40:50.299190', '4', 'DEBORA KARUBUY, SE', 1, '[{\"added\": {}}]', 9, 1),
(9, '2021-06-18 22:41:37.945714', '5', 'MEISARI, SE', 1, '[{\"added\": {}}]', 9, 1),
(10, '2021-06-18 22:43:24.160761', '1', 'FRANS PIETER ISTIA, S.SOS, MM', 2, '[{\"changed\": {\"fields\": [\"Jabatan\"]}}]', 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(14, 'accounts', 'customer'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'myapp', 'anggaran'),
(8, 'myapp', 'instansi'),
(9, 'myapp', 'pegawai'),
(13, 'myapp', 'pengeluaran'),
(10, 'myapp', 'rincian'),
(12, 'myapp', 'sppd'),
(11, 'myapp', 'surat_perintah'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-06-18 22:25:02.568594'),
(2, 'auth', '0001_initial', '2021-06-18 22:25:39.248146'),
(3, 'accounts', '0001_initial', '2021-06-18 22:25:47.290085'),
(4, 'admin', '0001_initial', '2021-06-18 22:26:02.806565'),
(5, 'admin', '0002_logentry_remove_auto_add', '2021-06-18 22:26:02.946236'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2021-06-18 22:26:03.205235'),
(7, 'contenttypes', '0002_remove_content_type_name', '2021-06-18 22:26:08.589111'),
(8, 'auth', '0002_alter_permission_name_max_length', '2021-06-18 22:26:15.096844'),
(9, 'auth', '0003_alter_user_email_max_length', '2021-06-18 22:26:16.192372'),
(10, 'auth', '0004_alter_user_username_opts', '2021-06-18 22:26:16.461651'),
(11, 'auth', '0005_alter_user_last_login_null', '2021-06-18 22:26:20.012372'),
(12, 'auth', '0006_require_contenttypes_0002', '2021-06-18 22:26:20.160586'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2021-06-18 22:26:20.490601'),
(14, 'auth', '0008_alter_user_username_max_length', '2021-06-18 22:26:21.014194'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2021-06-18 22:26:21.401556'),
(16, 'auth', '0010_alter_group_name_max_length', '2021-06-18 22:26:21.754653'),
(17, 'auth', '0011_update_proxy_permissions', '2021-06-18 22:26:21.863530'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2021-06-18 22:26:22.213570'),
(19, 'myapp', '0001_initial', '2021-06-18 22:27:05.298701'),
(20, 'myapp', '0002_remove_sppd_maksud_perjalanan', '2021-06-18 22:27:05.902440'),
(21, 'sessions', '0001_initial', '2021-06-18 22:27:10.907660');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('cy2pwrw9q688vfup8dj185xkw1w1d5go', '.eJxVjMEOwiAQRP-FsyHQhVI8eu83kN0FpGpoUtqT8d9tkx40mdO8N_MWAbe1hK2lJUxRXIUWl9-OkJ-pHiA-sN5nyXNdl4nkociTNjnOMb1up_t3ULCVfZ2MtU7D4CnniGAJsiKtOrCO2RMZp9kg7SHVD5g5gWfmzmoPvXYoPl_vEzhN:1luN12:qW_p2EcVE_q2KbMWAxkMfui23MI-4nnT8h5xx_-Y6o4', '2021-07-02 22:31:08.624678');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_anggaran`
--

CREATE TABLE `myapp_anggaran` (
  `id` bigint(20) NOT NULL,
  `tahun` varchar(200) DEFAULT NULL,
  `dana` varchar(200) DEFAULT NULL,
  `periode` varchar(200) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_instansi`
--

CREATE TABLE `myapp_instansi` (
  `id` bigint(20) NOT NULL,
  `nama` varchar(200) DEFAULT NULL,
  `alamat` varchar(200) DEFAULT NULL,
  `telepon` varchar(200) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `situs` varchar(200) DEFAULT NULL,
  `logo` varchar(100) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_instansi`
--

INSERT INTO `myapp_instansi` (`id`, `nama`, `alamat`, `telepon`, `email`, `situs`, `logo`, `created_at`, `updated_at`) VALUES
(1, 'DINAS KOMUNIKASI, INFORMATIKA, PERSANDIAN DAN STATISTIK', 'Manokwari', '082335233512', 'manokwari@gmail.com', 'dodiman.pythonanywhere.com', 'Coat_of_arms_of_West_Papua.svg_fB9kTiM_W2NIslE.png', '2021-06-18 22:35:16.604857', '2021-06-18 22:35:16.604857');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_pegawai`
--

CREATE TABLE `myapp_pegawai` (
  `id` bigint(20) NOT NULL,
  `nip` varchar(200) DEFAULT NULL,
  `nama` varchar(200) DEFAULT NULL,
  `pangkat` varchar(200) DEFAULT NULL,
  `golongan` varchar(200) DEFAULT NULL,
  `jabatan` varchar(200) DEFAULT NULL,
  `status_pegawai` varchar(200) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_pegawai`
--

INSERT INTO `myapp_pegawai` (`id`, `nip`, `nama`, `pangkat`, `golongan`, `jabatan`, `status_pegawai`, `created_at`, `updated_at`) VALUES
(1, '196903101991031017', 'FRANS PIETER ISTIA, S.SOS, MM', 'Kepala Dinas Kominfo', 'IVB', 'Kepala Dinas Kominfo Persandian dan Statistik', 'PNS', '2021-06-18 22:37:49.740470', '2021-06-18 22:43:23.862278'),
(2, '198405072010012012', 'YETI HATTI RUMPUMBO', 'Pengatur Muda Tk. 1', 'IIB', 'Bendahara Pengeluaran', 'PNS', '2021-06-18 22:38:48.315222', '2021-06-18 22:38:48.315222'),
(3, '197601312006051002', 'STEVANUS INDOUW, SH', 'Pembina', 'IVA', 'Kepala Bidang Informasi Dan Komunikasi Publik', 'PNS', '2021-06-18 22:39:55.698679', '2021-06-18 22:39:55.698679'),
(4, '197905182010042001', 'DEBORA KARUBUY, SE', 'Penata', 'IIIC', 'Kasabbag. Program dan Keuangan', 'PNS', '2021-06-18 22:40:50.208734', '2021-06-18 22:40:50.208734'),
(5, '19840507201001201', 'MEISARI, SE', 'Pembina', 'IIIB', 'Sekretaris', 'PNS', '2021-06-18 22:41:37.852620', '2021-06-18 22:41:37.852620');

-- --------------------------------------------------------

--
-- Table structure for table `myapp_pengeluaran`
--

CREATE TABLE `myapp_pengeluaran` (
  `id` bigint(20) NOT NULL,
  `nomor_bukti_pengeluaran` varchar(200) DEFAULT NULL,
  `sumber_dana` varchar(200) DEFAULT NULL,
  `keperluan` varchar(200) DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  `keterangan` varchar(200) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `pegawai_id` bigint(20) NOT NULL,
  `sppd_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_pengeluaran_rincian`
--

CREATE TABLE `myapp_pengeluaran_rincian` (
  `id` bigint(20) NOT NULL,
  `pengeluaran_id` bigint(20) NOT NULL,
  `rincian_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_rincian`
--

CREATE TABLE `myapp_rincian` (
  `id` bigint(20) NOT NULL,
  `uraian` varchar(200) DEFAULT NULL,
  `kuantitas` int(10) UNSIGNED NOT NULL CHECK (`kuantitas` >= 0),
  `satuan` varchar(200) DEFAULT NULL,
  `harga` int(11) NOT NULL,
  `jumlahnya` int(11) NOT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `myapp_sppd`
--

CREATE TABLE `myapp_sppd` (
  `id` bigint(20) NOT NULL,
  `nomor` varchar(200) DEFAULT NULL,
  `tempat_berangkat` varchar(200) DEFAULT NULL,
  `tempat_tujuan` varchar(200) DEFAULT NULL,
  `tanggal_berangkat` date DEFAULT NULL,
  `tanggal_kembali` date DEFAULT NULL,
  `keterangan` varchar(200) DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `surat_perintah_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_sppd`
--

INSERT INTO `myapp_sppd` (`id`, `nomor`, `tempat_berangkat`, `tempat_tujuan`, `tanggal_berangkat`, `tanggal_kembali`, `keterangan`, `created_at`, `updated_at`, `surat_perintah_id`) VALUES
(1, '001/2021', 'manokwari', 'jakarta', '2021-06-19', '2021-06-20', 'fds coba yang bagus', '2021-06-18 22:44:47.402621', '2021-06-18 22:45:51.199240', 1);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_surat_perintah`
--

CREATE TABLE `myapp_surat_perintah` (
  `id` bigint(20) NOT NULL,
  `nomor` varchar(200) DEFAULT NULL,
  `uraian` varchar(200) DEFAULT NULL,
  `tanggal` date DEFAULT NULL,
  `created_at` datetime(6) DEFAULT NULL,
  `updated_at` datetime(6) DEFAULT NULL,
  `koordinator_id` bigint(20) NOT NULL,
  `penanggung_jawab_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_surat_perintah`
--

INSERT INTO `myapp_surat_perintah` (`id`, `nomor`, `uraian`, `tanggal`, `created_at`, `updated_at`, `koordinator_id`, `penanggung_jawab_id`) VALUES
(1, '001/2021', 'perjalanan dinas selama 3 hari', '2021-06-19', '2021-06-18 22:44:47.187617', '2021-06-18 22:44:47.187617', 3, 1);

-- --------------------------------------------------------

--
-- Table structure for table `myapp_surat_perintah_pengikut`
--

CREATE TABLE `myapp_surat_perintah_pengikut` (
  `id` bigint(20) NOT NULL,
  `surat_perintah_id` bigint(20) NOT NULL,
  `pegawai_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `myapp_surat_perintah_pengikut`
--

INSERT INTO `myapp_surat_perintah_pengikut` (`id`, `surat_perintah_id`, `pegawai_id`) VALUES
(1, 1, 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_customer`
--
ALTER TABLE `accounts_customer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `myapp_anggaran`
--
ALTER TABLE `myapp_anggaran`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_instansi`
--
ALTER TABLE `myapp_instansi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_pegawai`
--
ALTER TABLE `myapp_pegawai`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_pengeluaran`
--
ALTER TABLE `myapp_pengeluaran`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myapp_pengeluaran_pegawai_id_589e3362_fk_myapp_pegawai_id` (`pegawai_id`),
  ADD KEY `myapp_pengeluaran_sppd_id_4069c834_fk_myapp_sppd_id` (`sppd_id`);

--
-- Indexes for table `myapp_pengeluaran_rincian`
--
ALTER TABLE `myapp_pengeluaran_rincian`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `myapp_pengeluaran_rincia_pengeluaran_id_rincian_i_d6b178c4_uniq` (`pengeluaran_id`,`rincian_id`),
  ADD KEY `myapp_pengeluaran_ri_rincian_id_b43581f8_fk_myapp_rin` (`rincian_id`);

--
-- Indexes for table `myapp_rincian`
--
ALTER TABLE `myapp_rincian`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `myapp_sppd`
--
ALTER TABLE `myapp_sppd`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `surat_perintah_id` (`surat_perintah_id`);

--
-- Indexes for table `myapp_surat_perintah`
--
ALTER TABLE `myapp_surat_perintah`
  ADD PRIMARY KEY (`id`),
  ADD KEY `myapp_surat_perintah_koordinator_id_e12e32a7_fk_myapp_pegawai_id` (`koordinator_id`),
  ADD KEY `myapp_surat_perintah_penanggung_jawab_id_6d60057a_fk_myapp_peg` (`penanggung_jawab_id`);

--
-- Indexes for table `myapp_surat_perintah_pengikut`
--
ALTER TABLE `myapp_surat_perintah_pengikut`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `myapp_surat_perintah_pen_surat_perintah_id_pegawa_951a4818_uniq` (`surat_perintah_id`,`pegawai_id`),
  ADD KEY `myapp_surat_perintah_pegawai_id_d8df86d7_fk_myapp_peg` (`pegawai_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_customer`
--
ALTER TABLE `accounts_customer`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `myapp_anggaran`
--
ALTER TABLE `myapp_anggaran`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `myapp_instansi`
--
ALTER TABLE `myapp_instansi`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `myapp_pegawai`
--
ALTER TABLE `myapp_pegawai`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `myapp_pengeluaran`
--
ALTER TABLE `myapp_pengeluaran`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `myapp_pengeluaran_rincian`
--
ALTER TABLE `myapp_pengeluaran_rincian`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `myapp_rincian`
--
ALTER TABLE `myapp_rincian`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `myapp_sppd`
--
ALTER TABLE `myapp_sppd`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `myapp_surat_perintah`
--
ALTER TABLE `myapp_surat_perintah`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `myapp_surat_perintah_pengikut`
--
ALTER TABLE `myapp_surat_perintah_pengikut`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_customer`
--
ALTER TABLE `accounts_customer`
  ADD CONSTRAINT `accounts_customer_user_id_11606857_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `myapp_pengeluaran`
--
ALTER TABLE `myapp_pengeluaran`
  ADD CONSTRAINT `myapp_pengeluaran_pegawai_id_589e3362_fk_myapp_pegawai_id` FOREIGN KEY (`pegawai_id`) REFERENCES `myapp_pegawai` (`id`),
  ADD CONSTRAINT `myapp_pengeluaran_sppd_id_4069c834_fk_myapp_sppd_id` FOREIGN KEY (`sppd_id`) REFERENCES `myapp_sppd` (`id`);

--
-- Constraints for table `myapp_pengeluaran_rincian`
--
ALTER TABLE `myapp_pengeluaran_rincian`
  ADD CONSTRAINT `myapp_pengeluaran_ri_pengeluaran_id_6971c78e_fk_myapp_pen` FOREIGN KEY (`pengeluaran_id`) REFERENCES `myapp_pengeluaran` (`id`),
  ADD CONSTRAINT `myapp_pengeluaran_ri_rincian_id_b43581f8_fk_myapp_rin` FOREIGN KEY (`rincian_id`) REFERENCES `myapp_rincian` (`id`);

--
-- Constraints for table `myapp_sppd`
--
ALTER TABLE `myapp_sppd`
  ADD CONSTRAINT `myapp_sppd_surat_perintah_id_89e87372_fk_myapp_surat_perintah_id` FOREIGN KEY (`surat_perintah_id`) REFERENCES `myapp_surat_perintah` (`id`);

--
-- Constraints for table `myapp_surat_perintah`
--
ALTER TABLE `myapp_surat_perintah`
  ADD CONSTRAINT `myapp_surat_perintah_koordinator_id_e12e32a7_fk_myapp_pegawai_id` FOREIGN KEY (`koordinator_id`) REFERENCES `myapp_pegawai` (`id`),
  ADD CONSTRAINT `myapp_surat_perintah_penanggung_jawab_id_6d60057a_fk_myapp_peg` FOREIGN KEY (`penanggung_jawab_id`) REFERENCES `myapp_pegawai` (`id`);

--
-- Constraints for table `myapp_surat_perintah_pengikut`
--
ALTER TABLE `myapp_surat_perintah_pengikut`
  ADD CONSTRAINT `myapp_surat_perintah_pegawai_id_d8df86d7_fk_myapp_peg` FOREIGN KEY (`pegawai_id`) REFERENCES `myapp_pegawai` (`id`),
  ADD CONSTRAINT `myapp_surat_perintah_surat_perintah_id_da3b202c_fk_myapp_sur` FOREIGN KEY (`surat_perintah_id`) REFERENCES `myapp_surat_perintah` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
