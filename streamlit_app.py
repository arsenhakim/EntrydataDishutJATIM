import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
import time
import pickle
from pathlib import Path
import os
import json
from datetime import date
import calendar
from datetime import datetime


#Menu Horizontal 
selected = option_menu(
    menu_title="Main menu",
    options=["Home", "Produksi Kayu", "Produksi Non-Kayu"],
    icons=["house-fill", "tree-fill", "globe-asia-australia" ],
    default_index= 0,
    orientation="horizontal",
)

#Page HOME
if selected == "Home":
    bg_image_home = """
    <style>
    [data-testid="stMain"] {
    background-image: url("https://i.im.ge/2025/01/09/zJvIwW.WhatsApp-Image-2025-01-09-at-10-07-49-AM.jpeg");
    background-size: 1400px 800px
    }

    [data-testid="stHeadingWithActionElements"] {
    [id="entry-data-produksi-hutan-rakyat"]{
        [id="selamat-datang-di-webapp-dishut-jatim"] {
            color: white;
        }
        color: rgba(255,255,255, 0.9);
        }
    }

    [data-testid="stElementContainer"] {
        color: white;
    }

    [data-testid="stWidgetLabel"] {
    data-testid="stMarkdownContainer"{
        color: white;
        }
    color: white);
    }

    [data-testid="stMarkdown"] {
    color: rgba(255,255,255, 0.9);
    }

    [data-testid="stHeader"] {
    background-image: url("https://i.im.ge/2025/01/09/zJv1iq.WhatsApp-Image-2025-01-09-at-10-03-29-AM.jpeg");
    background-size: 1500px 60px;
    }

    [data-testid="stForm"] {
    background-color: grey;
    }

    </style>
    """
    st.markdown(bg_image_home, unsafe_allow_html=True)
    st.title("Selamat datang di Web Entry Data Dishut JATIM")
        


#Page Produksi Non-Kayu
if selected == "Produksi Non-Kayu":
    bg_image_nonkayu = """
    <style>
    [data-testid="stMain"] {
    background-image: url("https://i.im.ge/2025/01/09/zJvIwW.WhatsApp-Image-2025-01-09-at-10-07-49-AM.jpeg");
    background-size: 1400px 800px
    }

    [data-testid="stElementContainer"] {
        color: white;
    }

    [data-testid="stHeadingWithActionElements"] {
    [id="entry-data-produksi-hutan-rakyat"]{
        color: rgba(255,255,255, 0.9);
        }
    }

    [data-testid="stMarkdownContainer"] {
        [class="st-emotion-cache-89jlt8 e121c1cl0"] {
            color: white;
        }    
    }
    

    [data-testid="stWidgetLabel"] {
    data-testid="stMarkdownContainer"{
        color: black;
        }
    color: white);
    }

    [data-testid="stMarkdown"] {
    color: rgba(255,255,255, 0.9);
    }

    [data-testid="stHeader"] {
    background-image: url("https://i.im.ge/2025/01/09/zJv1iq.WhatsApp-Image-2025-01-09-at-10-03-29-AM.jpeg");
    background-size: 1500px 60px;
    }

    [data-testid="stForm"] {
    background-color: grey;
    }

    [data-testid="stFormSubmitButton"] {
        color: black;
    }

    [id="app"] {
        color: grey;
    }

    </style>
    """
    st.markdown(bg_image_nonkayu, unsafe_allow_html=True)
    
    st.title("Entry Data Produksi Non-Kayu Hutan Rakyat")
    st.markdown("Tolong isi form berikut dengan benar")
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    creds = Credentials.from_service_account_info(
        st.secrets["google_cloud"],  # Load secrets
        scopes=scope
    )

    client = gspread.authorize(creds)

    # Open the Google Sheet
    spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1R_eDvmifnpFQU6i-G-m1nKTjstEN6WoPep_zf2_pGJ0")

    # Open the worksheet
    worksheet_nonkayu = spreadsheet.worksheet("Dataproduksinonkayuhutanrakyat")

        # Read the data from the worksheet
    data_nonkayu = pd.DataFrame(worksheet_nonkayu.get_all_records(head = 2))
    

    #list CDK
    cdk_list = [
        ('1', 'BANYUWANGI'),
        ('2', 'BOJONEGORO'),
        ('3', 'JEMBER'),
        ('4', 'LUMAJANG'),
        ('5', 'MADIUN'),
        ('6', 'MALANG'),
        ('7', 'NGANJUK'),
        ('8', 'PACITAN'),
        ('9', 'SUMENEP'),
        ('10', 'TRENGGALEK'),
    ]

    #list kabupaten
    Kabupaten_list = [
        ('3501', '8', 'KAB. PACITAN'),
        ('3502', '8', 'KAB. PONOROGO'),
        ('3503', '10', 'KAB. TRENGGALEK'),
        ('3504', '10', 'KAB. TULUNGAGUNG'),
        ('3505', '6', 'KAB. BLITAR'),
        ('3506', '10', 'KAB. KEDIRI'),
        ('3507', '6', 'KAB. MALANG'),
        ('3508', '4', 'KAB. LUMAJANG'),
        ('3509', '3', 'KAB. JEMBER'),
        ('3510', '1', 'KAB. BANYUWANGI'),
        ('3511', '3', 'KAB. BONDOWOSO'),
        ('3512', '1', 'KAB. SITUBONDO'),
        ('3513', '4', 'KAB. PROBOLINGGO'),
        ('3514', '4', 'KAB. PASURUAN'),
        ('3515', '2', 'KAB. SIDOARJO'),
        ('3516', '7', 'KAB. MOJOKERTO'),
        ('3517', '7', 'KAB. JOMBANG'),
        ('3518', '7', 'KAB. NGANJUK'),
        ('3519', '5', 'KAB. MADIUN'),
        ('3520', '5', 'KAB. MAGETAN'),
        ('3521', '5', 'KAB. NGAWI'),
        ('3522', '2', 'KAB. BOJONEGORO'),
        ('3523', '2', 'KAB. TUBAN'),
        ('3524', '2', 'KAB. LAMONGAN'),
        ('3525', '2', 'KAB. GRESIK'),
        ('3526', '9', 'KAB. BANGKALAN'),
        ('3527', '9', 'KAB. SAMPANG'),
        ('3528', '9', 'KAB. PAMEKASAN'),
        ('3529', '9', 'KAB. SUMENEP'),
        ('3571', '10', 'KOTA KEDIRI'),
        ('3572', '6', 'KOTA BLITAR'),
        ('3573', '6', 'KOTA MALANG'),
        ('3574', '4', 'KOTA PROBOLINGGO'),
        ('3575', '4', 'KOTA PASURUAN'),
        ('3576', '7', 'KOTA MOJOKERTO'),
        ('3577', '5', 'KOTA MADIUN'),
        ('3578', '2', 'KOTA SURABAYA'),
        ('3579', '6', 'KOTA BATU')
    ]

    #list kecamatan
    Kecamatan_list = [
        ('350101', '3501', 'Donorojo'),
        ('350102', '3501', 'Pringkuku'),
        ('350103', '3501', 'Punung'),
        ('350104', '3501', 'Pacitan'),
        ('350105', '3501', 'Kebonagung'),
        ('350106', '3501', 'Arjosari'),
        ('350107', '3501', 'Nawangan'),
        ('350108', '3501', 'Bandar'),
        ('350109', '3501', 'Tegalombo'),
        ('350110', '3501', 'Tulakan'),
        ('350111', '3501', 'Ngadirojo'),
        ('350112', '3501', 'Sudimoro'),
        ('350201', '3502', 'Slahung'),
        ('350202', '3502', 'Ngrayun'),
        ('350203', '3502', 'Bungkal'),
        ('350204', '3502', 'Sambit'),
        ('350205', '3502', 'Sawoo'),
        ('350206', '3502', 'Sooko'),
        ('350207', '3502', 'Pulung'),
        ('350208', '3502', 'Mlarak'),
        ('350209', '3502', 'Jetis'),
        ('350210', '3502', 'Siman'),
        ('350211', '3502', 'Balong'),
        ('350212', '3502', 'Kauman'),
        ('350213', '3502', 'Badegan'),
        ('350214', '3502', 'Sampung'),
        ('350215', '3502', 'Sukorejo'),
        ('350216', '3502', 'Babadan'),
        ('350217', '3502', 'Ponorogo'),
        ('350218', '3502', 'Jenangan'),
        ('350219', '3502', 'Ngebel'),
        ('350220', '3502', 'Jambon'),
        ('350221', '3502', 'Pudak'),
        ('350301', '3503', 'Panggul'),
        ('350302', '3503', 'Munjungan'),
        ('350303', '3503', 'Pule'),
        ('350304', '3503', 'Dongko'),
        ('350305', '3503', 'Tugu'),
        ('350306', '3503', 'Karangan'),
        ('350307', '3503', 'Kampak'),
        ('350308', '3503', 'Watulimo'),
        ('350309', '3503', 'Bendungan'),
        ('350310', '3503', 'Gandusari'),
        ('350311', '3503', 'Trenggalek'),
        ('350312', '3503', 'Pogalan'),
        ('350313', '3503', 'Durenan'),
        ('350314', '3503', 'Suruh'),
        ('350401', '3504', 'Tulungagung'),
        ('350402', '3504', 'Boyolangu'),
        ('350403', '3504', 'Kedungwaru'),
        ('350404', '3504', 'Ngantru'),
        ('350405', '3504', 'Kauman'),
        ('350406', '3504', 'Pagerwojo'),
        ('350407', '3504', 'Sendang'),
        ('350408', '3504', 'Karangrejo'),
        ('350409', '3504', 'Gondang'),
        ('350410', '3504', 'Sumbergempol'),
        ('350411', '3504', 'Ngunut'),
        ('350412', '3504', 'Pucanglaban'),
        ('350413', '3504', 'Rejotangan'),
        ('350414', '3504', 'Kalidawir'),
        ('350415', '3504', 'Besuki'),
        ('350416', '3504', 'Campurdarat'),
        ('350417', '3504', 'Bandung'),
        ('350418', '3504', 'Pakel'),
        ('350419', '3504', 'Tanggunggunung'),
        ('350501', '3505', 'Wonodadi'),
        ('350502', '3505', 'Udanawu'),
        ('350503', '3505', 'Srengat'),
        ('350504', '3505', 'Kademangan'),
        ('350505', '3505', 'Bakung'),
        ('350506', '3505', 'Ponggok'),
        ('350507', '3505', 'Sanankulon'),
        ('350508', '3505', 'Wonotirto'),
        ('350509', '3505', 'Nglegok'),
        ('350510', '3505', 'Kanigoro'),
        ('350511', '3505', 'Garum'),
        ('350512', '3505', 'Sutojayan'),
        ('350513', '3505', 'Panggungrejo'),
        ('350514', '3505', 'Talun'),
        ('350515', '3505', 'Gandusari'),
        ('350516', '3505', 'Binangun'),
        ('350517', '3505', 'Wlingi'),
        ('350518', '3505', 'Doko'),
        ('350519', '3505', 'Kesamben'),
        ('350520', '3505', 'Wates'),
        ('350521', '3505', 'Selorejo'),
        ('350522', '3505', 'Selopuro'),
        ('350601', '3506', 'Semen'),
        ('350602', '3506', 'Mojo'),
        ('350603', '3506', 'Kras'),
        ('350604', '3506', 'Ngadiluwih'),
        ('350605', '3506', 'Kandat'),
        ('350606', '3506', 'Wates'),
        ('350607', '3506', 'Ngancar'),
        ('350608', '3506', 'Puncu'),
        ('350609', '3506', 'Plosoklaten'),
        ('350610', '3506', 'Gurah'),
        ('350611', '3506', 'Pagu'),
        ('350612', '3506', 'Gampengrejo'),
        ('350613', '3506', 'Grogol'),
        ('350614', '3506', 'Papar'),
        ('350615', '3506', 'Purwoasri'),
        ('350616', '3506', 'Plemahan'),
        ('350617', '3506', 'Pare'),
        ('350618', '3506', 'Kepung'),
        ('350619', '3506', 'Kandangan'),
        ('350620', '3506', 'Tarokan'),
        ('350621', '3506', 'Kunjang'),
        ('350622', '3506', 'Banyakan'),
        ('350623', '3506', 'Ringinrejo'),
        ('350624', '3506', 'Kayen Kidul'),
        ('350625', '3506', 'Ngasem'),
        ('350626', '3506', 'Badas'),
        ('350701', '3507', 'Donomulyo'),
        ('350702', '3507', 'Pagak'),
        ('350703', '3507', 'Bantur'),
        ('350704', '3507', 'Sumbermanjing Wetan'),
        ('350705', '3507', 'Dampit'),
        ('350706', '3507', 'Ampelgading'),
        ('350707', '3507', 'Poncokusumo'),
        ('350708', '3507', 'Wajak'),
        ('350709', '3507', 'Turen'),
        ('350710', '3507', 'Gondanglegi'),
        ('350711', '3507', 'Kalipare'),
        ('350712', '3507', 'Sumberpucung'),
        ('350713', '3507', 'Kepanjen'),
        ('350714', '3507', 'Bululawang'),
        ('350715', '3507', 'Tajinan'),
        ('350716', '3507', 'Tumpang'),
        ('350717', '3507', 'Jabung'),
        ('350718', '3507', 'Pakis'),
        ('350719', '3507', 'Pakisaji'),
        ('350720', '3507', 'Ngajum'),
        ('350721', '3507', 'Wagir'),
        ('350722', '3507', 'Dau'),
        ('350723', '3507', 'Karang Ploso'),
        ('350724', '3507', 'Singosari'),
        ('350725', '3507', 'Lawang'),
        ('350726', '3507', 'Pujon'),
        ('350727', '3507', 'Ngantang'),
        ('350728', '3507', 'Kasembon'),
        ('350729', '3507', 'Gedangan'),
        ('350730', '3507', 'Tirtoyudo'),
        ('350731', '3507', 'Kromengan'),
        ('350732', '3507', 'Wonosari'),
        ('350733', '3507', 'Pagelaran'),
        ('350801', '3508', 'Tempursari'),
        ('350802', '3508', 'Pronojiwo'),
        ('350803', '3508', 'Candipuro'),
        ('350804', '3508', 'Pasirian'),
        ('350805', '3508', 'Tempeh'),
        ('350806', '3508', 'Kunir'),
        ('350807', '3508', 'Yosowilangun'),
        ('350808', '3508', 'Rowokangkung'),
        ('350809', '3508', 'Tekung'),
        ('350810', '3508', 'Lumajang'),
        ('350811', '3508', 'Pasrujambe'),
        ('350812', '3508', 'Senduro'),
        ('350813', '3508', 'Gucialit'),
        ('350814', '3508', 'Padang'),
        ('350815', '3508', 'Sukodono'),
        ('350816', '3508', 'Kedungjajang'),
        ('350817', '3508', 'Jatiroto'),
        ('350818', '3508', 'Randuagung'),
        ('350819', '3508', 'Klakah'),
        ('350820', '3508', 'Ranuyoso'),
        ('350821', '3508', 'Sumbersuko'),
        ('350901', '3509', 'Jombang'),
        ('350902', '3509', 'Kencong'),
        ('350903', '3509', 'Sumberbaru'),
        ('350904', '3509', 'Gumukmas'),
        ('350905', '3509', 'Umbulsari'),
        ('350906', '3509', 'Tanggul'),
        ('350907', '3509', 'Semboro'),
        ('350908', '3509', 'Puger'),
        ('350909', '3509', 'Bangsalsari'),
        ('350910', '3509', 'Balung'),
        ('350911', '3509', 'Wuluhan'),
        ('350912', '3509', 'Ambulu'),
        ('350913', '3509', 'Rambipuji'),
        ('350914', '3509', 'Panti'),
        ('350915', '3509', 'Sukorambi'),
        ('350916', '3509', 'Jenggawah'),
        ('350917', '3509', 'Ajung'),
        ('350918', '3509', 'Tempurejo'),
        ('350919', '3509', 'Kaliwates'),
        ('350920', '3509', 'Patrang'),
        ('350921', '3509', 'Sumbersari'),
        ('350922', '3509', 'Arjasa'),
        ('350923', '3509', 'Mumbulsari'),
        ('350924', '3509', 'Pakusari'),
        ('350925', '3509', 'Jelbuk'),
        ('350926', '3509', 'Mayang'),
        ('350927', '3509', 'Kalisat'),
        ('350928', '3509', 'Ledokombo'),
        ('350929', '3509', 'Sukowono'),
        ('350930', '3509', 'Silo'),
        ('350931', '3509', 'Sumberjambe'),
        ('351001', '3510', 'Pesanggaran'),
        ('351002', '3510', 'Bangorejo'),
        ('351003', '3510', 'Purwoharjo'),
        ('351004', '3510', 'Tegaldlimo'),
        ('351005', '3510', 'Muncar'),
        ('351006', '3510', 'Cluring'),
        ('351007', '3510', 'Gambiran'),
        ('351008', '3510', 'Srono'),
        ('351009', '3510', 'Genteng'),
        ('351010', '3510', 'Glenmore'),
        ('351011', '3510', 'Kalibaru'),
        ('351012', '3510', 'Singojuruh'),
        ('351013', '3510', 'Rogojampi'),
        ('351014', '3510', 'Kabat'),
        ('351015', '3510', 'Glagah'),
        ('351016', '3510', 'Banyuwangi'),
        ('351017', '3510', 'Giri'),
        ('351018', '3510', 'Wongsorejo'),
        ('351019', '3510', 'Songgon'),
        ('351020', '3510', 'Sempu'),
        ('351021', '3510', 'Kalipuro'),
        ('351022', '3510', 'Siliragung'),
        ('351023', '3510', 'Tegalsari'),
        ('351024', '3510', 'Licin'),
        ('351025', '3510', 'Blimbingsari'),
        ('351101', '3511', 'Maesan'),
        ('351102', '3511', 'Tamanan'),
        ('351103', '3511', 'Tlogosari'),
        ('351104', '3511', 'Sukosari'),
        ('351105', '3511', 'Pujer'),
        ('351106', '3511', 'Grujugan'),
        ('351107', '3511', 'Curahdami'),
        ('351108', '3511', 'Tenggarang'),
        ('351109', '3511', 'Wonosari'),
        ('351110', '3511', 'Tapen'),
        ('351111', '3511', 'Bondowoso'),
        ('351112', '3511', 'Wringin'),
        ('351113', '3511', 'Tegalampel'),
        ('351114', '3511', 'Klabang'),
        ('351115', '3511', 'Cermee'),
        ('351116', '3511', 'Prajekan'),
        ('351117', '3511', 'Pakem'),
        ('351118', '3511', 'Sumberwringin'),
        ('351119', '3511', 'Sempol'),
        ('351120', '3511', 'Binakal'),
        ('351121', '3511', 'Taman Krocok'),
        ('351122', '3511', 'Botolinggo'),
        ('351123', '3511', 'Jambesari Darus Sholah'),
        ('351201', '3512', 'Jatibanteng'),
        ('351202', '3512', 'Besuki'),
        ('351203', '3512', 'Suboh'),
        ('351204', '3512', 'Mlandingan'),
        ('351205', '3512', 'Kendit'),
        ('351206', '3512', 'Panarukan'),
        ('351207', '3512', 'Situbondo'),
        ('351208', '3512', 'Panji'),
        ('351209', '3512', 'Mangaran'),
        ('351210', '3512', 'Kapongan'),
        ('351211', '3512', 'Arjasa'),
        ('351212', '3512', 'Jangkar'),
        ('351213', '3512', 'Asembagus'),
        ('351214', '3512', 'Banyuputih'),
        ('351215', '3512', 'Sumbermalang'),
        ('351216', '3512', 'Banyuglugur'),
        ('351217', '3512', 'Bungatan'),
        ('351301', '3513', 'Sukapura'),
        ('351302', '3513', 'Sumber'),
        ('351303', '3513', 'Kuripan'),
        ('351304', '3513', 'Bantaran'),
        ('351305', '3513', 'Leces'),
        ('351306', '3513', 'Banyuanyar'),
        ('351307', '3513', 'Tiris'),
        ('351308', '3513', 'Krucil'),
        ('351309', '3513', 'Gading'),
        ('351310', '3513', 'Pakuniran'),
        ('351311', '3513', 'Kotaanyar'),
        ('351312', '3513', 'Paiton'),
        ('351313', '3513', 'Besuk'),
        ('351314', '3513', 'Kraksaan'),
        ('351315', '3513', 'Krejengan'),
        ('351316', '3513', 'Pejarakan'),
        ('351317', '3513', 'Maron'),
        ('351318', '3513', 'Gending'),
        ('351319', '3513', 'Dringu'),
        ('351320', '3513', 'Tegalsiwalan'),
        ('351321', '3513', 'Sumberasih'),
        ('351322', '3513', 'Wonomerto'),
        ('351323', '3513', 'Tongas'),
        ('351324', '3513', 'Lumbang'),
        ('351401', '3514', 'Purwodadi'),
        ('351402', '3514', 'Tutur'),
        ('351403', '3514', 'Puspo'),
        ('351404', '3514', 'Lumbang'),
        ('351405', '3514', 'Pasrepan'),
        ('351406', '3514', 'Kejayan'),
        ('351407', '3514', 'Wonorejo'),
        ('351408', '3514', 'Purwosari'),
        ('351409', '3514', 'Sukorejo'),
        ('351410', '3514', 'Prigen'),
        ('351411', '3514', 'Pandaan'),
        ('351412', '3514', 'Gempol'),
        ('351413', '3514', 'Beji'),
        ('351414', '3514', 'Bangil'),
        ('351415', '3514', 'Rembang'),
        ('351416', '3514', 'Kraton'),
        ('351417', '3514', 'Pohjentrek'),
        ('351418', '3514', 'Gondangwetan'),
        ('351419', '3514', 'Winongan'),
        ('351420', '3514', 'Grati'),
        ('351421', '3514', 'Nguling'),
        ('351422', '3514', 'Lekok'),
        ('351423', '3514', 'Rejoso'),
        ('351424', '3514', 'Tosari'),
        ('351501', '3515', 'Tarik'),
        ('351502', '3515', 'Prambon'),
        ('351503', '3515', 'Krembung'),
        ('351504', '3515', 'Porong'),
        ('351505', '3515', 'Jabon'),
        ('351506', '3515', 'Tanggulangin'),
        ('351507', '3515', 'Candi'),
        ('351508', '3515', 'Sidoarjo'),
        ('351509', '3515', 'Tulangan'),
        ('351510', '3515', 'Wonoayu'),
        ('351511', '3515', 'Krian'),
        ('351512', '3515', 'Balongbendo'),
        ('351513', '3515', 'Taman'),
        ('351514', '3515', 'Sukodono'),
        ('351515', '3515', 'Buduran'),
        ('351516', '3515', 'Gedangan'),
        ('351517', '3515', 'Sedati'),
        ('351518', '3515', 'Waru'),
        ('351601', '3516', 'Jatirejo'),
        ('351602', '3516', 'Gondang'),
        ('351603', '3516', 'Pacet'),
        ('351604', '3516', 'Trawas'),
        ('351605', '3516', 'Ngoro'),
        ('351606', '3516', 'Pungging'),
        ('351607', '3516', 'Kutorejo'),
        ('351608', '3516', 'Mojosari'),
        ('351609', '3516', 'Dlanggu'),
        ('351610', '3516', 'Bangsal'),
        ('351611', '3516', 'Puri'),
        ('351612', '3516', 'Trowulan'),
        ('351613', '3516', 'Sooko'),
        ('351614', '3516', 'Gedeg'),
        ('351615', '3516', 'Kemlagi'),
        ('351616', '3516', 'Jetis'),
        ('351617', '3516', 'Dawarblandong'),
        ('351618', '3516', 'Mojoanyar'),
        ('351701', '3517', 'Perak'),
        ('351702', '3517', 'Gudo'),
        ('351703', '3517', 'Ngoro'),
        ('351704', '3517', 'Bareng'),
        ('351705', '3517', 'Wonosalam'),
        ('351706', '3517', 'Mojoagung'),
        ('351707', '3517', 'Mojowarno'),
        ('351708', '3517', 'Diwek'),
        ('351709', '3517', 'Jombang'),
        ('351710', '3517', 'Peterongan'),
        ('351711', '3517', 'Sumobito'),
        ('351712', '3517', 'Kesamben'),
        ('351713', '3517', 'Tembelang'),
        ('351714', '3517', 'Ploso'),
        ('351715', '3517', 'Plandaan'),
        ('351716', '3517', 'Kabuh'),
        ('351717', '3517', 'Kudu'),
        ('351718', '3517', 'Bandarkedungmulyo'),
        ('351719', '3517', 'Jogoroto'),
        ('351720', '3517', 'Megaluh'),
        ('351721', '3517', 'Ngusikan'),
        ('351801', '3518', 'Sawahan'),
        ('351802', '3518', 'Ngetos'),
        ('351803', '3518', 'Berbek'),
        ('351804', '3518', 'Loceret'),
        ('351805', '3518', 'Pace'),
        ('351806', '3518', 'Prambon'),
        ('351807', '3518', 'Ngronggot'),
        ('351808', '3518', 'Kertosono'),
        ('351809', '3518', 'Patianrowo'),
        ('351810', '3518', 'Baron'),
        ('351811', '3518', 'Tanjunganom'),
        ('351812', '3518', 'Sukomoro'),
        ('351813', '3518', 'Nganjuk'),
        ('351814', '3518', 'Bagor'),
        ('351815', '3518', 'Wilangan'),
        ('351816', '3518', 'Rejoso'),
        ('351817', '3518', 'Gondang'),
        ('351818', '3518', 'Ngluyu'),
        ('351819', '3518', 'Lengkong'),
        ('351820', '3518', 'Jatikalen'),
        ('351901', '3519', 'Kebonsari'),
        ('351902', '3519', 'Dolopo'),
        ('351903', '3519', 'Geger'),
        ('351904', '3519', 'Dagangan'),
        ('351905', '3519', 'Kare'),
        ('351906', '3519', 'Gemarang'),
        ('351907', '3519', 'Wungu'),
        ('351908', '3519', 'Madiun'),
        ('351909', '3519', 'Jiwan'),
        ('351910', '3519', 'Balerejo'),
        ('351911', '3519', 'Mejayan'),
        ('351912', '3519', 'Saradan'),
        ('351913', '3519', 'Pilangkenceng'),
        ('351914', '3519', 'Sawahan'),
        ('351915', '3519', 'Wonoasri'),
        ('352001', '3520', 'Poncol'),
        ('352002', '3520', 'Parang'),
        ('352003', '3520', 'Lembeyan'),
        ('352004', '3520', 'Takeran'),
        ('352005', '3520', 'Kawedanan'),
        ('352006', '3520', 'Magetan'),
        ('352007', '3520', 'Plaosan'),
        ('352008', '3520', 'Panekan'),
        ('352009', '3520', 'Sukomoro'),
        ('352010', '3520', 'Bendo'),
        ('352011', '3520', 'Maospati'),
        ('352012', '3520', 'Barat'),
        ('352013', '3520', 'Karangrejo'),
        ('352014', '3520', 'Karas'),
        ('352015', '3520', 'Kartoharjo'),
        ('352016', '3520', 'Ngariboyo'),
        ('352017', '3520', 'Nguntoronadi'),
        ('352018', '3520', 'Sidorejo'),
        ('352101', '3521', 'Sine'),
        ('352102', '3521', 'Ngrambe'),
        ('352103', '3521', 'Jogorogo'),
        ('352104', '3521', 'Kendal'),
        ('352105', '3521', 'Geneng'),
        ('352106', '3521', 'Kwadungan'),
        ('352107', '3521', 'Karangjati'),
        ('352108', '3521', 'Padas'),
        ('352109', '3521', 'Ngawi'),
        ('352110', '3521', 'Paron'),
        ('352111', '3521', 'Kedunggalar'),
        ('352112', '3521', 'Widodaren'),
        ('352113', '3521', 'Mantingan'),
        ('352114', '3521', 'Pangkur'),
        ('352115', '3521', 'Bringin'),
        ('352116', '3521', 'Pitu'),
        ('352117', '3521', 'Karanganyar'),
        ('352118', '3521', 'Gerih'),
        ('352119', '3521', 'Kasreman'),
        ('352201', '3522', 'Ngraho'),
        ('352202', '3522', 'Tambakrejo'),
        ('352203', '3522', 'Ngambon'),
        ('352204', '3522', 'Ngasem'),
        ('352205', '3522', 'Bubulan'),
        ('352206', '3522', 'Dander'),
        ('352207', '3522', 'Sugihwaras'),
        ('352208', '3522', 'Kedungadem'),
        ('352209', '3522', 'Kepohbaru'),
        ('352210', '3522', 'Baureno'),
        ('352211', '3522', 'Kanor'),
        ('352212', '3522', 'Sumberejo'),
        ('352213', '3522', 'Balen'),
        ('352214', '3522', 'Kapas'),
        ('352215', '3522', 'Bojonegoro'),
        ('352216', '3522', 'Kalitidu'),
        ('352217', '3522', 'Malo'),
        ('352218', '3522', 'Purwosari'),
        ('352219', '3522', 'Padangan'),
        ('352220', '3522', 'Kasiman'),
        ('352221', '3522', 'Temayang'),
        ('352222', '3522', 'Margomulyo'),
        ('352223', '3522', 'Trucuk'),
        ('352224', '3522', 'Sukosewu'),
        ('352225', '3522', 'Kedewan'),
        ('352226', '3522', 'Gondang'),
        ('352227', '3522', 'Sekar'),
        ('352228', '3522', 'Gayam'),
        ('352301', '3523', 'Kenduruan'),
        ('352302', '3523', 'Jatirogo'),
        ('352303', '3523', 'Bangilan'),
        ('352304', '3523', 'Bancar'),
        ('352305', '3523', 'Senori'),
        ('352306', '3523', 'Tambakboyo'),
        ('352307', '3523', 'Singgahan'),
        ('352308', '3523', 'Kerek'),
        ('352309', '3523', 'Parengan'),
        ('352310', '3523', 'Montong'),
        ('352311', '3523', 'Soko'),
        ('352312', '3523', 'Jenu'),
        ('352313', '3523', 'Merakurak'),
        ('352314', '3523', 'Rengel'),
        ('352315', '3523', 'Semanding'),
        ('352316', '3523', 'Tuban'),
        ('352317', '3523', 'Plumpang'),
        ('352318', '3523', 'Palang'),
        ('352319', '3523', 'Widang'),
        ('352320', '3523', 'Grabagan'),
        ('352401', '3524', 'Sukorame'),
        ('352402', '3524', 'Bluluk'),
        ('352403', '3524', 'Modo'),
        ('352404', '3524', 'Ngimbang'),
        ('352405', '3524', 'Babat'),
        ('352406', '3524', 'Kedungpring'),
        ('352407', '3524', 'Brondong'),
        ('352408', '3524', 'Laren'),
        ('352409', '3524', 'Sekaran'),
        ('352410', '3524', 'Maduran'),
        ('352411', '3524', 'Sambeng'),
        ('352412', '3524', 'Sugio'),
        ('352413', '3524', 'Pucuk'),
        ('352414', '3524', 'Paciran'),
        ('352415', '3524', 'Solokuro'),
        ('352416', '3524', 'Mantup'),
        ('352417', '3524', 'Sukodadi'),
        ('352418', '3524', 'Karanggeneng'),
        ('352419', '3524', 'Kembangbahu'),
        ('352420', '3524', 'Kalitengah'),
        ('352421', '3524', 'Turi'),
        ('352422', '3524', 'Lamongan'),
        ('352423', '3524', 'Tikung'),
        ('352424', '3524', 'Karangbinangun'),
        ('352425', '3524', 'Deket'),
        ('352426', '3524', 'Glagah'),
        ('352427', '3524', 'Sarirejo'),
        ('352501', '3525', 'Dukun'),
        ('352502', '3525', 'Balongpanggang'),
        ('352503', '3525', 'Panceng'),
        ('352504', '3525', 'Benjeng'),
        ('352505', '3525', 'Duduksampeyan'),
        ('352506', '3525', 'Wringinanom'),
        ('352507', '3525', 'Ujungpangkah'),
        ('352508', '3525', 'Kedamean'),
        ('352509', '3525', 'Sidayu'),
        ('352510', '3525', 'Manyar'),
        ('352511', '3525', 'Cerme'),
        ('352512', '3525', 'Bungah'),
        ('352513', '3525', 'Menganti'),
        ('352514', '3525', 'Kebomas'),
        ('352515', '3525', 'Driyorejo'),
        ('352516', '3525', 'Gresik'),
        ('352517', '3525', 'Sangkapura'),
        ('352518', '3525', 'Tambak'),
        ('352601', '3526', 'Bangkalan'),
        ('352602', '3526', 'Socah'),
        ('352603', '3526', 'Burneh'),
        ('352604', '3526', 'Kamal'),
        ('352605', '3526', 'Arosbaya'),
        ('352606', '3526', 'Geger'),
        ('352607', '3526', 'Klampis'),
        ('352608', '3526', 'Sepulu'),
        ('352609', '3526', 'Tanjung Bumi'),
        ('352610', '3526', 'Kokop'),
        ('352611', '3526', 'Kwanyar'),
        ('352612', '3526', 'Labang'),
        ('352613', '3526', 'Tanah Merah'),
        ('352614', '3526', 'Tragah'),
        ('352615', '3526', 'Blega'),
        ('352616', '3526', 'Modung'),
        ('352617', '3526', 'Konang'),
        ('352618', '3526', 'Galis'),
        ('352701', '3527', 'Sreseh'),
        ('352702', '3527', 'Torjun'),
        ('352703', '3527', 'Sampang'),
        ('352704', '3527', 'Camplong'),
        ('352705', '3527', 'Omben'),
        ('352706', '3527', 'Kedungdung'),
        ('352707', '3527', 'Jrengik'),
        ('352708', '3527', 'Tambelangan'),
        ('352709', '3527', 'Banyuates'),
        ('352710', '3527', 'Robatal'),
        ('352711', '3527', 'Sokobanah'),
        ('352712', '3527', 'Ketapang'),
        ('352713', '3527', 'Pangarengan'),
        ('352714', '3527', 'Karangpenang'),
        ('352801', '3528', 'Tlanakan'),
        ('352802', '3528', 'Pademawu'),
        ('352803', '3528', 'Galis'),
        ('352804', '3528', 'Pamekasan'),
        ('352805', '3528', 'Proppo'),
        ('352806', '3528', 'Palenggaan'),
        ('352807', '3528', 'Pegantenan'),
        ('352808', '3528', 'Larangan'),
        ('352809', '3528', 'Pakong'),
        ('352810', '3528', 'Waru'),
        ('352811', '3528', 'Batumarmar'),
        ('352812', '3528', 'Kadur'),
        ('352813', '3528', 'Pasean'),
        ('352901', '3529', 'Kota Sumenep'),
        ('352902', '3529', 'Kalianget'),
        ('352903', '3529', 'Manding'),
        ('352904', '3529', 'Talango'),
        ('352905', '3529', 'Bluto'),
        ('352906', '3529', 'Saronggi'),
        ('352907', '3529', 'Lenteng'),
        ('352908', '3529', 'Giliginting'),
        ('352909', '3529', 'Guluk-Guluk'),
        ('352910', '3529', 'Ganding'),
        ('352911', '3529', 'Pragaan'),
        ('352912', '3529', 'Ambunten'),
        ('352913', '3529', 'Pasongsongan'),
        ('352914', '3529', 'Dasuk'),
        ('352915', '3529', 'Rubaru'),
        ('352916', '3529', 'Batang Batang'),
        ('352917', '3529', 'Batuputih'),
        ('352918', '3529', 'Dungkek'),
        ('352919', '3529', 'Gapura'),
        ('352920', '3529', 'Gayam'),
        ('352921', '3529', 'Nonggunong'),
        ('352922', '3529', 'Raas'),
        ('352923', '3529', 'Masalembu'),
        ('352924', '3529', 'Arjasa'),
        ('352925', '3529', 'Sapeken'),
        ('352926', '3529', 'Batuan'),
        ('352927', '3529', 'Kangayan'),
        ('357101', '3571', 'Mojoroto'),
        ('357102', '3571', 'Kota'),
        ('357103', '3571', 'Pesantren'),
        ('357201', '3572', 'Kepanjenkidul'),
        ('357202', '3572', 'Sukorejo'),
        ('357203', '3572', 'Sananwetan'),
        ('357301', '3573', 'Blimbing'),
        ('357302', '3573', 'Klojen'),
        ('357303', '3573', 'Kedungkandang'),
        ('357304', '3573', 'Sukun'),
        ('357305', '3573', 'Lowokwaru'),
        ('357401', '3574', 'Kademangan'),
        ('357402', '3574', 'Wonoasih'),
        ('357403', '3574', 'Mayangan'),
        ('357404', '3574', 'Kanigaran'),
        ('357405', '3574', 'Kedopok'),
        ('357501', '3575', 'Gadingrejo'),
        ('357502', '3575', 'Purworejo'),
        ('357503', '3575', 'Bugul Kidul'),
        ('357504', '3575', 'Panggungrejo'),
        ('357601', '3576', 'Prajuritkulon'),
        ('357602', '3576', 'Magersari'),
        ('357603', '3576', 'Kranggan'),
        ('357701', '3577', 'Kartoharjo'),
        ('357702', '3577', 'Manguharjo'),
        ('357703', '3577', 'Taman'),
        ('357801', '3578', 'Karang Pilang'),
        ('357802', '3578', 'Wonocolo'),
        ('357803', '3578', 'Rungkut'),
        ('357804', '3578', 'Wonokromo'),
        ('357805', '3578', 'Tegalsari'),
        ('357806', '3578', 'Sawahan'),
        ('357807', '3578', 'Genteng'),
        ('357808', '3578', 'Gubeng'),
        ('357809', '3578', 'Sukolilo'),
        ('357810', '3578', 'Tambaksari'),
        ('357811', '3578', 'Simokerto'),
        ('357812', '3578', 'Pabean Cantian'),
        ('357813', '3578', 'Bubutan'),
        ('357814', '3578', 'Tandes'),
        ('357815', '3578', 'Krembangan'),
        ('357816', '3578', 'Semampir'),
        ('357817', '3578', 'Kenjeran'),
        ('357818', '3578', 'Lakarsantri'),
        ('357819', '3578', 'Benowo'),
        ('357820', '3578', 'Wiyung'),
        ('357821', '3578', 'Dukuh Pakis'),
        ('357822', '3578', 'Gayungan'),
        ('357823', '3578', 'Jambangan'),
        ('357824', '3578', 'Tenggilis Mejoyo'),
        ('357825', '3578', 'Gunung Anyar'),
        ('357826', '3578', 'Mulyorejo'),
        ('357827', '3578', 'Sukomanunggal'),
        ('357828', '3578', 'Asem Rowo'),
        ('357829', '3578', 'Bulak'),
        ('357830', '3578', 'Pakal'),
        ('357831', '3578', 'Sambikerep'),
        ('357901', '3579', 'Batu'),
        ('357902', '3579', 'Bumiaji'),
        ('357903', '3579', 'Junrejo')
    ]

    bulan_nama = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus", 
    9: "September", 10: "Oktober", 11: "November", 12: "Desember"
    }

    cdk_df = pd.DataFrame(cdk_list, columns=['cdk_id', 'cdk_name'])
    kabupaten_df = pd.DataFrame(Kabupaten_list, columns=['kabupaten_id', 'cdk_id', 'kabupaten_name'])
    kecamatan_df = pd.DataFrame(Kecamatan_list, columns=['kecamatan_id', 'kabupaten_id', 'kecamatan_name'])

    # Mapping Kabupaten per CDK
    cdk_kabupaten_map = (
    kabupaten_df
    .groupby("cdk_id")["kabupaten_name"]
    .apply(list)
    .to_dict()
    )

    # Mapping Kecamatan per Kabupaten
    kabupaten_kecamatan_map = (
        kecamatan_df
        .merge(kabupaten_df, on="kabupaten_id")
        .groupby("kabupaten_id")["kecamatan_name"]
        .apply(list)
        .to_dict()
    )

    # Streamlit app
    if "selected_cdk" not in st.session_state:
        st.session_state.selected_cdk = ""
        st.session_state.kabupaten_options = []
        st.session_state.selected_kabupaten = ""
        st.session_state.kecamatan_options = []
    
    def periksa_kabupaten(cdk):
        if cdk:
            st.session_state.selected_cdk = cdk
            cdk_id = cdk_df[cdk_df["cdk_name"] == cdk]["cdk_id"].values[0]
            st.session_state.kabupaten_options = cdk_kabupaten_map.get(cdk_id, [])
        else:
            st.session_state.kabupaten_options = []
        
        # Reset semua state terkait form

        st.session_state.kabupaten_name = ""
        st.session_state.kecamatan_select = ""
        st.session_state.kecamatan_options = []
        st.session_state.desa = ""
        st.session_state.kth = ""
        st.session_state.penyuluh = ""
        st.session_state.laporanprodkayu = 0.0
        st.session_state.datante = 0.0
        st.session_state.bambu = 0.0
        st.session_state.getah_pinus = 0.0
        st.session_state.daun_kayuputih = 0.0
        st.session_state.porang = 0.0
        st.session_state.kopi = 0.0
        st.session_state.madu = 0.0
        st.session_state.durian = 0.0
        st.session_state.alpukat = 0.0
        st.session_state.jahe = 0.0
        st.session_state.kunyit = 0.0
        st.session_state.hhbk = 0.0
        st.session_state.ntebtg = 0.0
        st.session_state.ntekg = 0.0
        st.session_state.rp = 0.0

    with st.form(key="Form_Dataproduksinonkayuhutanrakyat"):
        
        st.subheader("Pilih Bulan dan Tahun")
        bulan = st.selectbox("Bulan Laporan Produksi", options=list(bulan_nama.keys()), format_func=lambda x : bulan_nama[x], key="bulan_name")
        tahun = st.number_input("Tahun Laporan Produksi", value=datetime.now().year, min_value=2000, max_value=2100, step=1, key="tahun_nm")
        
        month_name = bulan_nama[bulan]

        cdk = st.selectbox(
            label="CDK",
            options=[""] + cdk_df["cdk_name"].tolist(),
            key="cdk_name"
        )
        if st.form_submit_button("Periksa Kabupaten"):
            periksa_kabupaten(cdk)


        Kabupaten = st.selectbox(
            label="Kabupaten/Kota",
            options=[""] + st.session_state.kabupaten_options,
            key="kabupaten_name",
        )

        if st.form_submit_button("Periksa Kecamatan"):
            if Kabupaten:
                st.session_state.selected_kabupaten = Kabupaten
                Kabupaten_id = kabupaten_df[kabupaten_df["kabupaten_name"] == Kabupaten]["kabupaten_id"].values[0]
                st.session_state.kecamatan_options = kabupaten_kecamatan_map.get(Kabupaten_id, [])
            else:
                st.session_state.kecamatan_options = []

        Kecamatan = st.selectbox(
            label="Kecamatan",
            options=[""] + st.session_state.kecamatan_options,
            key="kecamatan_select",
        )
        # Input lainnya
        Desa = st.text_input(label="Desa", key="desa")
        kth = st.text_input(label="KTH", key="kth")
        Penyuluh = st.text_input(label="Penyuluh pendamping", key="penyuluh")
        Bambu = st.number_input(label="Bambu (Btg)", key="bambu")
        Getah_pinus = st.number_input(label="Getah Pinus (Kg)", key="getah_pinus", min_value=0.0)
        Daun_kayuputih = st.number_input(label="Daun Kayu Putih (Kg)", key="daun_kayuputih", min_value=0.0)
        Porang = st.number_input(label="Porang (Kg)", key="porang", min_value=0.0)
        Kopi = st.number_input(label="Kopi (Kg)", key="kopi", min_value=0.0)
        Madu = st.number_input(label="Madu (Kg)", key="madu", min_value=0.0)
        Durian = st.number_input(label="Durian (Kg)", key="durian", min_value=0.0)
        Alpukat = st.number_input(label="Alpukat (Kg)", key="alpukat", min_value=0.0)
        Jahe = st.number_input(label="Jahe (Kg)", key="jahe", min_value=0.0)
        Kunyit = st.number_input(label="Kunyit (Kg)", key="kunyit", min_value=0.0)
        hhbk = st.number_input(label="HHBK Lainnya (Kg)", key="hhbk", min_value=0.0)
        nte_btg = st.number_input(label="Nilai NTE (Btg)", key="ntebtg", min_value=0.0)
        nte_kg = st.number_input(label="Nilai NTE (Kg)", key="ntekg", min_value=0.0)
        jumlah_rupiah = st.number_input(label="Nilai Rupiah", key="rp", min_value=0.0)
        Jumlah_Btg = int(Bambu)
        Jumlah_Kg = int(Getah_pinus) + int(Daun_kayuputih) + int(Porang) + int(Kopi) + int(Madu) + int(Durian) + int(Alpukat) + int(Jahe) + int(Kunyit) + int(hhbk)

        if st.form_submit_button(label="Konfirmasi laporan"):
            if not Kabupaten or not Kecamatan or not Desa or not kth or not Penyuluh:
                st.warning("Tolong isi form dengan lengkap")
            else:
                # Membuat DataFrame untuk data input
                dataprodhutanrakyatnonkayu = pd.DataFrame(
                    [
                        {
                            "CDK": cdk,
                            "Kabupaten/Kota": Kabupaten,
                            "Kecamatan": Kecamatan,
                            "Desa": Desa,
                            "KTH": kth,
                            "Penyuluh Pendamping": Penyuluh,
                            "Bambu (Btg)": Bambu,
                            "Getah Pinus (Kg)": Getah_pinus,
                            "Daun Kayu Putih (Kg)": Daun_kayuputih,
                            "Porang (Kg)": Porang,
                            "Kopi (Kg)": Kopi,
                            "Madu (Kg)": Madu,
                            "Durian (Kg)": Durian,
                            "Alpukat (Kg)": Alpukat,
                            "Jahe (Kg)": Jahe,
                            "Kunyit (Kg)": Kunyit,
                            "HHBK Lainnya (Kg)": hhbk,
                            "Btg": Jumlah_Btg,
                            "Kg": Jumlah_Kg,
                            "Btg_NTE": nte_btg,
                            "Kg_NTE": nte_kg,
                            "Rp": jumlah_rupiah,
                            "Bulan": bulan,
                            "Tahun": tahun,
                        }
                    ]
                )
                # Update existing data
                df_update = pd.concat([data_nonkayu, dataprodhutanrakyatnonkayu])

                # data_to_append = [[""] + row for row in dataprodhutanrakyatnonkayu[header_row.tolist()].values.tolist()]
                data_to_append = [[""] + row for row in dataprodhutanrakyatnonkayu.values.tolist()]
                
                last_row = len(worksheet_nonkayu.get_all_values())
                                
                # Append rows to worksheet
                worksheet_nonkayu.insert_rows(data_to_append, last_row + 1)
                
                new_row_start_index = last_row + 1
                new_row_end_index = new_row_start_index + len(dataprodhutanrakyatnonkayu) - 1

                for row_index in range(new_row_start_index, new_row_end_index + 1):
                    timestamp_formula = f"=IF(NOT(ISBLANK(B{row_index}));NOW();\"\")"
                    worksheet_nonkayu.update_cell(row_index, 1, timestamp_formula)

                                
                st.success("Data berhasil diinput")
                for key in [
                    "cdk_name",
                    "kabupaten_name",
                    "kecamatan_select",
                    "desa",
                    "kth",
                    "penyuluh",
                    "bambu",
                    "getah_pinus",
                    "daun_kayuputih",
                    "porang",
                    "kopi",
                    "madu",
                    "durian",
                    "alpukat",
                    "jahe",
                    "kunyit",
                    "hhbk",
                    "ntebtg",
                    "ntekg",
                    "rp"
                ]:
                    if key in st.session_state:
                        del st.session_state[key]

                # Rerun untuk mereset form
                periksa_kabupaten(cdk)
                st.session_state.cdk_name = ""
                st.rerun()
                #Page Produksi Kayu
if selected == "Produksi Kayu":
    # Display judul web
    bg_image = """
    <style>
    [data-testid="stMain"] {
    background-image: url("https://i.im.ge/2025/01/09/zJvIwW.WhatsApp-Image-2025-01-09-at-10-07-49-AM.jpeg");
    background-size: 1400px 800px
    }

    [data-testid="stElementContainer"] {
        color: white;
    }

    [data-testid="stHeadingWithActionElements"] {
    [id="entry-data-produksi-hutan-rakyat"]{
        color: rgba(255,255,255, 0.9);
        }
    }

    [data-testid="stMarkdownContainer"] {
        [class="st-emotion-cache-89jlt8 e121c1cl0"] {
            color: white;
        }    
    }
    

    [data-testid="stWidgetLabel"] {
    data-testid="stMarkdownContainer"{
        color: black;
        }
    color: white);
    }

    [data-testid="stMarkdown"] {
    color: rgba(255,255,255, 0.9);
    }

    [data-testid="stHeader"] {
    background-image: url("https://i.im.ge/2025/01/09/zJv1iq.WhatsApp-Image-2025-01-09-at-10-03-29-AM.jpeg");
    background-size: 1500px 60px;
    }

    [data-testid="stForm"] {
    background-color: grey;
    }

    [data-testid="stFormSubmitButton"] {
        color: black;
    }

    [id="app"] {
        color: grey;
    }

    </style>
    """

    st.markdown(bg_image, unsafe_allow_html=True)
    st.title("Entry Data Produksi Kayu Hutan Rakyat")
    st.markdown("Tolong isi form berikut dengan benar")

    # Google Sheets connection setup
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    creds = Credentials.from_service_account_info(
        st.secrets["google_cloud"],  # Load secrets
        scopes=scope
    )

    client = gspread.authorize(creds)

    # Open the Google Sheet
    spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1R_eDvmifnpFQU6i-G-m1nKTjstEN6WoPep_zf2_pGJ0")

    # Open the worksheet
    worksheet = spreadsheet.worksheet("Dataproduksikayuhutanrakyat")

    # Read the data from the worksheet
    existing_data = pd.DataFrame(worksheet.get_all_records(head = 2))

    #list CDK
    cdk_list = [
        ('1', 'BANYUWANGI'),
        ('2', 'BOJONEGORO'),
        ('3', 'JEMBER'),
        ('4', 'LUMAJANG'),
        ('5', 'MADIUN'),
        ('6', 'MALANG'),
        ('7', 'NGANJUK'),
        ('8', 'PACITAN'),
        ('9', 'SUMENEP'),
        ('10', 'TRENGGALEK'),
    ]

    #list kabupaten
    Kabupaten_list = [
        ('3501', '8', 'KAB. PACITAN'),
        ('3502', '8', 'KAB. PONOROGO'),
        ('3503', '10', 'KAB. TRENGGALEK'),
        ('3504', '10', 'KAB. TULUNGAGUNG'),
        ('3505', '6', 'KAB. BLITAR'),
        ('3506', '10', 'KAB. KEDIRI'),
        ('3507', '6', 'KAB. MALANG'),
        ('3508', '4', 'KAB. LUMAJANG'),
        ('3509', '3', 'KAB. JEMBER'),
        ('3510', '1', 'KAB. BANYUWANGI'),
        ('3511', '3', 'KAB. BONDOWOSO'),
        ('3512', '1', 'KAB. SITUBONDO'),
        ('3513', '4', 'KAB. PROBOLINGGO'),
        ('3514', '4', 'KAB. PASURUAN'),
        ('3515', '2', 'KAB. SIDOARJO'),
        ('3516', '7', 'KAB. MOJOKERTO'),
        ('3517', '7', 'KAB. JOMBANG'),
        ('3518', '7', 'KAB. NGANJUK'),
        ('3519', '5', 'KAB. MADIUN'),
        ('3520', '5', 'KAB. MAGETAN'),
        ('3521', '5', 'KAB. NGAWI'),
        ('3522', '2', 'KAB. BOJONEGORO'),
        ('3523', '2', 'KAB. TUBAN'),
        ('3524', '2', 'KAB. LAMONGAN'),
        ('3525', '2', 'KAB. GRESIK'),
        ('3526', '9', 'KAB. BANGKALAN'),
        ('3527', '9', 'KAB. SAMPANG'),
        ('3528', '9', 'KAB. PAMEKASAN'),
        ('3529', '9', 'KAB. SUMENEP'),
        ('3571', '10', 'KOTA KEDIRI'),
        ('3572', '6', 'KOTA BLITAR'),
        ('3573', '6', 'KOTA MALANG'),
        ('3574', '4', 'KOTA PROBOLINGGO'),
        ('3575', '4', 'KOTA PASURUAN'),
        ('3576', '7', 'KOTA MOJOKERTO'),
        ('3577', '5', 'KOTA MADIUN'),
        ('3578', '2', 'KOTA SURABAYA'),
        ('3579', '6', 'KOTA BATU')
    ]

    #list kecamatan
    Kecamatan_list = [
        ('350101', '3501', 'Donorojo'),
        ('350102', '3501', 'Pringkuku'),
        ('350103', '3501', 'Punung'),
        ('350104', '3501', 'Pacitan'),
        ('350105', '3501', 'Kebonagung'),
        ('350106', '3501', 'Arjosari'),
        ('350107', '3501', 'Nawangan'),
        ('350108', '3501', 'Bandar'),
        ('350109', '3501', 'Tegalombo'),
        ('350110', '3501', 'Tulakan'),
        ('350111', '3501', 'Ngadirojo'),
        ('350112', '3501', 'Sudimoro'),
        ('350201', '3502', 'Slahung'),
        ('350202', '3502', 'Ngrayun'),
        ('350203', '3502', 'Bungkal'),
        ('350204', '3502', 'Sambit'),
        ('350205', '3502', 'Sawoo'),
        ('350206', '3502', 'Sooko'),
        ('350207', '3502', 'Pulung'),
        ('350208', '3502', 'Mlarak'),
        ('350209', '3502', 'Jetis'),
        ('350210', '3502', 'Siman'),
        ('350211', '3502', 'Balong'),
        ('350212', '3502', 'Kauman'),
        ('350213', '3502', 'Badegan'),
        ('350214', '3502', 'Sampung'),
        ('350215', '3502', 'Sukorejo'),
        ('350216', '3502', 'Babadan'),
        ('350217', '3502', 'Ponorogo'),
        ('350218', '3502', 'Jenangan'),
        ('350219', '3502', 'Ngebel'),
        ('350220', '3502', 'Jambon'),
        ('350221', '3502', 'Pudak'),
        ('350301', '3503', 'Panggul'),
        ('350302', '3503', 'Munjungan'),
        ('350303', '3503', 'Pule'),
        ('350304', '3503', 'Dongko'),
        ('350305', '3503', 'Tugu'),
        ('350306', '3503', 'Karangan'),
        ('350307', '3503', 'Kampak'),
        ('350308', '3503', 'Watulimo'),
        ('350309', '3503', 'Bendungan'),
        ('350310', '3503', 'Gandusari'),
        ('350311', '3503', 'Trenggalek'),
        ('350312', '3503', 'Pogalan'),
        ('350313', '3503', 'Durenan'),
        ('350314', '3503', 'Suruh'),
        ('350401', '3504', 'Tulungagung'),
        ('350402', '3504', 'Boyolangu'),
        ('350403', '3504', 'Kedungwaru'),
        ('350404', '3504', 'Ngantru'),
        ('350405', '3504', 'Kauman'),
        ('350406', '3504', 'Pagerwojo'),
        ('350407', '3504', 'Sendang'),
        ('350408', '3504', 'Karangrejo'),
        ('350409', '3504', 'Gondang'),
        ('350410', '3504', 'Sumbergempol'),
        ('350411', '3504', 'Ngunut'),
        ('350412', '3504', 'Pucanglaban'),
        ('350413', '3504', 'Rejotangan'),
        ('350414', '3504', 'Kalidawir'),
        ('350415', '3504', 'Besuki'),
        ('350416', '3504', 'Campurdarat'),
        ('350417', '3504', 'Bandung'),
        ('350418', '3504', 'Pakel'),
        ('350419', '3504', 'Tanggunggunung'),
        ('350501', '3505', 'Wonodadi'),
        ('350502', '3505', 'Udanawu'),
        ('350503', '3505', 'Srengat'),
        ('350504', '3505', 'Kademangan'),
        ('350505', '3505', 'Bakung'),
        ('350506', '3505', 'Ponggok'),
        ('350507', '3505', 'Sanankulon'),
        ('350508', '3505', 'Wonotirto'),
        ('350509', '3505', 'Nglegok'),
        ('350510', '3505', 'Kanigoro'),
        ('350511', '3505', 'Garum'),
        ('350512', '3505', 'Sutojayan'),
        ('350513', '3505', 'Panggungrejo'),
        ('350514', '3505', 'Talun'),
        ('350515', '3505', 'Gandusari'),
        ('350516', '3505', 'Binangun'),
        ('350517', '3505', 'Wlingi'),
        ('350518', '3505', 'Doko'),
        ('350519', '3505', 'Kesamben'),
        ('350520', '3505', 'Wates'),
        ('350521', '3505', 'Selorejo'),
        ('350522', '3505', 'Selopuro'),
        ('350601', '3506', 'Semen'),
        ('350602', '3506', 'Mojo'),
        ('350603', '3506', 'Kras'),
        ('350604', '3506', 'Ngadiluwih'),
        ('350605', '3506', 'Kandat'),
        ('350606', '3506', 'Wates'),
        ('350607', '3506', 'Ngancar'),
        ('350608', '3506', 'Puncu'),
        ('350609', '3506', 'Plosoklaten'),
        ('350610', '3506', 'Gurah'),
        ('350611', '3506', 'Pagu'),
        ('350612', '3506', 'Gampengrejo'),
        ('350613', '3506', 'Grogol'),
        ('350614', '3506', 'Papar'),
        ('350615', '3506', 'Purwoasri'),
        ('350616', '3506', 'Plemahan'),
        ('350617', '3506', 'Pare'),
        ('350618', '3506', 'Kepung'),
        ('350619', '3506', 'Kandangan'),
        ('350620', '3506', 'Tarokan'),
        ('350621', '3506', 'Kunjang'),
        ('350622', '3506', 'Banyakan'),
        ('350623', '3506', 'Ringinrejo'),
        ('350624', '3506', 'Kayen Kidul'),
        ('350625', '3506', 'Ngasem'),
        ('350626', '3506', 'Badas'),
        ('350701', '3507', 'Donomulyo'),
        ('350702', '3507', 'Pagak'),
        ('350703', '3507', 'Bantur'),
        ('350704', '3507', 'Sumbermanjing Wetan'),
        ('350705', '3507', 'Dampit'),
        ('350706', '3507', 'Ampelgading'),
        ('350707', '3507', 'Poncokusumo'),
        ('350708', '3507', 'Wajak'),
        ('350709', '3507', 'Turen'),
        ('350710', '3507', 'Gondanglegi'),
        ('350711', '3507', 'Kalipare'),
        ('350712', '3507', 'Sumberpucung'),
        ('350713', '3507', 'Kepanjen'),
        ('350714', '3507', 'Bululawang'),
        ('350715', '3507', 'Tajinan'),
        ('350716', '3507', 'Tumpang'),
        ('350717', '3507', 'Jabung'),
        ('350718', '3507', 'Pakis'),
        ('350719', '3507', 'Pakisaji'),
        ('350720', '3507', 'Ngajum'),
        ('350721', '3507', 'Wagir'),
        ('350722', '3507', 'Dau'),
        ('350723', '3507', 'Karang Ploso'),
        ('350724', '3507', 'Singosari'),
        ('350725', '3507', 'Lawang'),
        ('350726', '3507', 'Pujon'),
        ('350727', '3507', 'Ngantang'),
        ('350728', '3507', 'Kasembon'),
        ('350729', '3507', 'Gedangan'),
        ('350730', '3507', 'Tirtoyudo'),
        ('350731', '3507', 'Kromengan'),
        ('350732', '3507', 'Wonosari'),
        ('350733', '3507', 'Pagelaran'),
        ('350801', '3508', 'Tempursari'),
        ('350802', '3508', 'Pronojiwo'),
        ('350803', '3508', 'Candipuro'),
        ('350804', '3508', 'Pasirian'),
        ('350805', '3508', 'Tempeh'),
        ('350806', '3508', 'Kunir'),
        ('350807', '3508', 'Yosowilangun'),
        ('350808', '3508', 'Rowokangkung'),
        ('350809', '3508', 'Tekung'),
        ('350810', '3508', 'Lumajang'),
        ('350811', '3508', 'Pasrujambe'),
        ('350812', '3508', 'Senduro'),
        ('350813', '3508', 'Gucialit'),
        ('350814', '3508', 'Padang'),
        ('350815', '3508', 'Sukodono'),
        ('350816', '3508', 'Kedungjajang'),
        ('350817', '3508', 'Jatiroto'),
        ('350818', '3508', 'Randuagung'),
        ('350819', '3508', 'Klakah'),
        ('350820', '3508', 'Ranuyoso'),
        ('350821', '3508', 'Sumbersuko'),
        ('350901', '3509', 'Jombang'),
        ('350902', '3509', 'Kencong'),
        ('350903', '3509', 'Sumberbaru'),
        ('350904', '3509', 'Gumukmas'),
        ('350905', '3509', 'Umbulsari'),
        ('350906', '3509', 'Tanggul'),
        ('350907', '3509', 'Semboro'),
        ('350908', '3509', 'Puger'),
        ('350909', '3509', 'Bangsalsari'),
        ('350910', '3509', 'Balung'),
        ('350911', '3509', 'Wuluhan'),
        ('350912', '3509', 'Ambulu'),
        ('350913', '3509', 'Rambipuji'),
        ('350914', '3509', 'Panti'),
        ('350915', '3509', 'Sukorambi'),
        ('350916', '3509', 'Jenggawah'),
        ('350917', '3509', 'Ajung'),
        ('350918', '3509', 'Tempurejo'),
        ('350919', '3509', 'Kaliwates'),
        ('350920', '3509', 'Patrang'),
        ('350921', '3509', 'Sumbersari'),
        ('350922', '3509', 'Arjasa'),
        ('350923', '3509', 'Mumbulsari'),
        ('350924', '3509', 'Pakusari'),
        ('350925', '3509', 'Jelbuk'),
        ('350926', '3509', 'Mayang'),
        ('350927', '3509', 'Kalisat'),
        ('350928', '3509', 'Ledokombo'),
        ('350929', '3509', 'Sukowono'),
        ('350930', '3509', 'Silo'),
        ('350931', '3509', 'Sumberjambe'),
        ('351001', '3510', 'Pesanggaran'),
        ('351002', '3510', 'Bangorejo'),
        ('351003', '3510', 'Purwoharjo'),
        ('351004', '3510', 'Tegaldlimo'),
        ('351005', '3510', 'Muncar'),
        ('351006', '3510', 'Cluring'),
        ('351007', '3510', 'Gambiran'),
        ('351008', '3510', 'Srono'),
        ('351009', '3510', 'Genteng'),
        ('351010', '3510', 'Glenmore'),
        ('351011', '3510', 'Kalibaru'),
        ('351012', '3510', 'Singojuruh'),
        ('351013', '3510', 'Rogojampi'),
        ('351014', '3510', 'Kabat'),
        ('351015', '3510', 'Glagah'),
        ('351016', '3510', 'Banyuwangi'),
        ('351017', '3510', 'Giri'),
        ('351018', '3510', 'Wongsorejo'),
        ('351019', '3510', 'Songgon'),
        ('351020', '3510', 'Sempu'),
        ('351021', '3510', 'Kalipuro'),
        ('351022', '3510', 'Siliragung'),
        ('351023', '3510', 'Tegalsari'),
        ('351024', '3510', 'Licin'),
        ('351025', '3510', 'Blimbingsari'),
        ('351101', '3511', 'Maesan'),
        ('351102', '3511', 'Tamanan'),
        ('351103', '3511', 'Tlogosari'),
        ('351104', '3511', 'Sukosari'),
        ('351105', '3511', 'Pujer'),
        ('351106', '3511', 'Grujugan'),
        ('351107', '3511', 'Curahdami'),
        ('351108', '3511', 'Tenggarang'),
        ('351109', '3511', 'Wonosari'),
        ('351110', '3511', 'Tapen'),
        ('351111', '3511', 'Bondowoso'),
        ('351112', '3511', 'Wringin'),
        ('351113', '3511', 'Tegalampel'),
        ('351114', '3511', 'Klabang'),
        ('351115', '3511', 'Cermee'),
        ('351116', '3511', 'Prajekan'),
        ('351117', '3511', 'Pakem'),
        ('351118', '3511', 'Sumberwringin'),
        ('351119', '3511', 'Sempol'),
        ('351120', '3511', 'Binakal'),
        ('351121', '3511', 'Taman Krocok'),
        ('351122', '3511', 'Botolinggo'),
        ('351123', '3511', 'Jambesari Darus Sholah'),
        ('351201', '3512', 'Jatibanteng'),
        ('351202', '3512', 'Besuki'),
        ('351203', '3512', 'Suboh'),
        ('351204', '3512', 'Mlandingan'),
        ('351205', '3512', 'Kendit'),
        ('351206', '3512', 'Panarukan'),
        ('351207', '3512', 'Situbondo'),
        ('351208', '3512', 'Panji'),
        ('351209', '3512', 'Mangaran'),
        ('351210', '3512', 'Kapongan'),
        ('351211', '3512', 'Arjasa'),
        ('351212', '3512', 'Jangkar'),
        ('351213', '3512', 'Asembagus'),
        ('351214', '3512', 'Banyuputih'),
        ('351215', '3512', 'Sumbermalang'),
        ('351216', '3512', 'Banyuglugur'),
        ('351217', '3512', 'Bungatan'),
        ('351301', '3513', 'Sukapura'),
        ('351302', '3513', 'Sumber'),
        ('351303', '3513', 'Kuripan'),
        ('351304', '3513', 'Bantaran'),
        ('351305', '3513', 'Leces'),
        ('351306', '3513', 'Banyuanyar'),
        ('351307', '3513', 'Tiris'),
        ('351308', '3513', 'Krucil'),
        ('351309', '3513', 'Gading'),
        ('351310', '3513', 'Pakuniran'),
        ('351311', '3513', 'Kotaanyar'),
        ('351312', '3513', 'Paiton'),
        ('351313', '3513', 'Besuk'),
        ('351314', '3513', 'Kraksaan'),
        ('351315', '3513', 'Krejengan'),
        ('351316', '3513', 'Pejarakan'),
        ('351317', '3513', 'Maron'),
        ('351318', '3513', 'Gending'),
        ('351319', '3513', 'Dringu'),
        ('351320', '3513', 'Tegalsiwalan'),
        ('351321', '3513', 'Sumberasih'),
        ('351322', '3513', 'Wonomerto'),
        ('351323', '3513', 'Tongas'),
        ('351324', '3513', 'Lumbang'),
        ('351401', '3514', 'Purwodadi'),
        ('351402', '3514', 'Tutur'),
        ('351403', '3514', 'Puspo'),
        ('351404', '3514', 'Lumbang'),
        ('351405', '3514', 'Pasrepan'),
        ('351406', '3514', 'Kejayan'),
        ('351407', '3514', 'Wonorejo'),
        ('351408', '3514', 'Purwosari'),
        ('351409', '3514', 'Sukorejo'),
        ('351410', '3514', 'Prigen'),
        ('351411', '3514', 'Pandaan'),
        ('351412', '3514', 'Gempol'),
        ('351413', '3514', 'Beji'),
        ('351414', '3514', 'Bangil'),
        ('351415', '3514', 'Rembang'),
        ('351416', '3514', 'Kraton'),
        ('351417', '3514', 'Pohjentrek'),
        ('351418', '3514', 'Gondangwetan'),
        ('351419', '3514', 'Winongan'),
        ('351420', '3514', 'Grati'),
        ('351421', '3514', 'Nguling'),
        ('351422', '3514', 'Lekok'),
        ('351423', '3514', 'Rejoso'),
        ('351424', '3514', 'Tosari'),
        ('351501', '3515', 'Tarik'),
        ('351502', '3515', 'Prambon'),
        ('351503', '3515', 'Krembung'),
        ('351504', '3515', 'Porong'),
        ('351505', '3515', 'Jabon'),
        ('351506', '3515', 'Tanggulangin'),
        ('351507', '3515', 'Candi'),
        ('351508', '3515', 'Sidoarjo'),
        ('351509', '3515', 'Tulangan'),
        ('351510', '3515', 'Wonoayu'),
        ('351511', '3515', 'Krian'),
        ('351512', '3515', 'Balongbendo'),
        ('351513', '3515', 'Taman'),
        ('351514', '3515', 'Sukodono'),
        ('351515', '3515', 'Buduran'),
        ('351516', '3515', 'Gedangan'),
        ('351517', '3515', 'Sedati'),
        ('351518', '3515', 'Waru'),
        ('351601', '3516', 'Jatirejo'),
        ('351602', '3516', 'Gondang'),
        ('351603', '3516', 'Pacet'),
        ('351604', '3516', 'Trawas'),
        ('351605', '3516', 'Ngoro'),
        ('351606', '3516', 'Pungging'),
        ('351607', '3516', 'Kutorejo'),
        ('351608', '3516', 'Mojosari'),
        ('351609', '3516', 'Dlanggu'),
        ('351610', '3516', 'Bangsal'),
        ('351611', '3516', 'Puri'),
        ('351612', '3516', 'Trowulan'),
        ('351613', '3516', 'Sooko'),
        ('351614', '3516', 'Gedeg'),
        ('351615', '3516', 'Kemlagi'),
        ('351616', '3516', 'Jetis'),
        ('351617', '3516', 'Dawarblandong'),
        ('351618', '3516', 'Mojoanyar'),
        ('351701', '3517', 'Perak'),
        ('351702', '3517', 'Gudo'),
        ('351703', '3517', 'Ngoro'),
        ('351704', '3517', 'Bareng'),
        ('351705', '3517', 'Wonosalam'),
        ('351706', '3517', 'Mojoagung'),
        ('351707', '3517', 'Mojowarno'),
        ('351708', '3517', 'Diwek'),
        ('351709', '3517', 'Jombang'),
        ('351710', '3517', 'Peterongan'),
        ('351711', '3517', 'Sumobito'),
        ('351712', '3517', 'Kesamben'),
        ('351713', '3517', 'Tembelang'),
        ('351714', '3517', 'Ploso'),
        ('351715', '3517', 'Plandaan'),
        ('351716', '3517', 'Kabuh'),
        ('351717', '3517', 'Kudu'),
        ('351718', '3517', 'Bandarkedungmulyo'),
        ('351719', '3517', 'Jogoroto'),
        ('351720', '3517', 'Megaluh'),
        ('351721', '3517', 'Ngusikan'),
        ('351801', '3518', 'Sawahan'),
        ('351802', '3518', 'Ngetos'),
        ('351803', '3518', 'Berbek'),
        ('351804', '3518', 'Loceret'),
        ('351805', '3518', 'Pace'),
        ('351806', '3518', 'Prambon'),
        ('351807', '3518', 'Ngronggot'),
        ('351808', '3518', 'Kertosono'),
        ('351809', '3518', 'Patianrowo'),
        ('351810', '3518', 'Baron'),
        ('351811', '3518', 'Tanjunganom'),
        ('351812', '3518', 'Sukomoro'),
        ('351813', '3518', 'Nganjuk'),
        ('351814', '3518', 'Bagor'),
        ('351815', '3518', 'Wilangan'),
        ('351816', '3518', 'Rejoso'),
        ('351817', '3518', 'Gondang'),
        ('351818', '3518', 'Ngluyu'),
        ('351819', '3518', 'Lengkong'),
        ('351820', '3518', 'Jatikalen'),
        ('351901', '3519', 'Kebonsari'),
        ('351902', '3519', 'Dolopo'),
        ('351903', '3519', 'Geger'),
        ('351904', '3519', 'Dagangan'),
        ('351905', '3519', 'Kare'),
        ('351906', '3519', 'Gemarang'),
        ('351907', '3519', 'Wungu'),
        ('351908', '3519', 'Madiun'),
        ('351909', '3519', 'Jiwan'),
        ('351910', '3519', 'Balerejo'),
        ('351911', '3519', 'Mejayan'),
        ('351912', '3519', 'Saradan'),
        ('351913', '3519', 'Pilangkenceng'),
        ('351914', '3519', 'Sawahan'),
        ('351915', '3519', 'Wonoasri'),
        ('352001', '3520', 'Poncol'),
        ('352002', '3520', 'Parang'),
        ('352003', '3520', 'Lembeyan'),
        ('352004', '3520', 'Takeran'),
        ('352005', '3520', 'Kawedanan'),
        ('352006', '3520', 'Magetan'),
        ('352007', '3520', 'Plaosan'),
        ('352008', '3520', 'Panekan'),
        ('352009', '3520', 'Sukomoro'),
        ('352010', '3520', 'Bendo'),
        ('352011', '3520', 'Maospati'),
        ('352012', '3520', 'Barat'),
        ('352013', '3520', 'Karangrejo'),
        ('352014', '3520', 'Karas'),
        ('352015', '3520', 'Kartoharjo'),
        ('352016', '3520', 'Ngariboyo'),
        ('352017', '3520', 'Nguntoronadi'),
        ('352018', '3520', 'Sidorejo'),
        ('352101', '3521', 'Sine'),
        ('352102', '3521', 'Ngrambe'),
        ('352103', '3521', 'Jogorogo'),
        ('352104', '3521', 'Kendal'),
        ('352105', '3521', 'Geneng'),
        ('352106', '3521', 'Kwadungan'),
        ('352107', '3521', 'Karangjati'),
        ('352108', '3521', 'Padas'),
        ('352109', '3521', 'Ngawi'),
        ('352110', '3521', 'Paron'),
        ('352111', '3521', 'Kedunggalar'),
        ('352112', '3521', 'Widodaren'),
        ('352113', '3521', 'Mantingan'),
        ('352114', '3521', 'Pangkur'),
        ('352115', '3521', 'Bringin'),
        ('352116', '3521', 'Pitu'),
        ('352117', '3521', 'Karanganyar'),
        ('352118', '3521', 'Gerih'),
        ('352119', '3521', 'Kasreman'),
        ('352201', '3522', 'Ngraho'),
        ('352202', '3522', 'Tambakrejo'),
        ('352203', '3522', 'Ngambon'),
        ('352204', '3522', 'Ngasem'),
        ('352205', '3522', 'Bubulan'),
        ('352206', '3522', 'Dander'),
        ('352207', '3522', 'Sugihwaras'),
        ('352208', '3522', 'Kedungadem'),
        ('352209', '3522', 'Kepohbaru'),
        ('352210', '3522', 'Baureno'),
        ('352211', '3522', 'Kanor'),
        ('352212', '3522', 'Sumberejo'),
        ('352213', '3522', 'Balen'),
        ('352214', '3522', 'Kapas'),
        ('352215', '3522', 'Bojonegoro'),
        ('352216', '3522', 'Kalitidu'),
        ('352217', '3522', 'Malo'),
        ('352218', '3522', 'Purwosari'),
        ('352219', '3522', 'Padangan'),
        ('352220', '3522', 'Kasiman'),
        ('352221', '3522', 'Temayang'),
        ('352222', '3522', 'Margomulyo'),
        ('352223', '3522', 'Trucuk'),
        ('352224', '3522', 'Sukosewu'),
        ('352225', '3522', 'Kedewan'),
        ('352226', '3522', 'Gondang'),
        ('352227', '3522', 'Sekar'),
        ('352228', '3522', 'Gayam'),
        ('352301', '3523', 'Kenduruan'),
        ('352302', '3523', 'Jatirogo'),
        ('352303', '3523', 'Bangilan'),
        ('352304', '3523', 'Bancar'),
        ('352305', '3523', 'Senori'),
        ('352306', '3523', 'Tambakboyo'),
        ('352307', '3523', 'Singgahan'),
        ('352308', '3523', 'Kerek'),
        ('352309', '3523', 'Parengan'),
        ('352310', '3523', 'Montong'),
        ('352311', '3523', 'Soko'),
        ('352312', '3523', 'Jenu'),
        ('352313', '3523', 'Merakurak'),
        ('352314', '3523', 'Rengel'),
        ('352315', '3523', 'Semanding'),
        ('352316', '3523', 'Tuban'),
        ('352317', '3523', 'Plumpang'),
        ('352318', '3523', 'Palang'),
        ('352319', '3523', 'Widang'),
        ('352320', '3523', 'Grabagan'),
        ('352401', '3524', 'Sukorame'),
        ('352402', '3524', 'Bluluk'),
        ('352403', '3524', 'Modo'),
        ('352404', '3524', 'Ngimbang'),
        ('352405', '3524', 'Babat'),
        ('352406', '3524', 'Kedungpring'),
        ('352407', '3524', 'Brondong'),
        ('352408', '3524', 'Laren'),
        ('352409', '3524', 'Sekaran'),
        ('352410', '3524', 'Maduran'),
        ('352411', '3524', 'Sambeng'),
        ('352412', '3524', 'Sugio'),
        ('352413', '3524', 'Pucuk'),
        ('352414', '3524', 'Paciran'),
        ('352415', '3524', 'Solokuro'),
        ('352416', '3524', 'Mantup'),
        ('352417', '3524', 'Sukodadi'),
        ('352418', '3524', 'Karanggeneng'),
        ('352419', '3524', 'Kembangbahu'),
        ('352420', '3524', 'Kalitengah'),
        ('352421', '3524', 'Turi'),
        ('352422', '3524', 'Lamongan'),
        ('352423', '3524', 'Tikung'),
        ('352424', '3524', 'Karangbinangun'),
        ('352425', '3524', 'Deket'),
        ('352426', '3524', 'Glagah'),
        ('352427', '3524', 'Sarirejo'),
        ('352501', '3525', 'Dukun'),
        ('352502', '3525', 'Balongpanggang'),
        ('352503', '3525', 'Panceng'),
        ('352504', '3525', 'Benjeng'),
        ('352505', '3525', 'Duduksampeyan'),
        ('352506', '3525', 'Wringinanom'),
        ('352507', '3525', 'Ujungpangkah'),
        ('352508', '3525', 'Kedamean'),
        ('352509', '3525', 'Sidayu'),
        ('352510', '3525', 'Manyar'),
        ('352511', '3525', 'Cerme'),
        ('352512', '3525', 'Bungah'),
        ('352513', '3525', 'Menganti'),
        ('352514', '3525', 'Kebomas'),
        ('352515', '3525', 'Driyorejo'),
        ('352516', '3525', 'Gresik'),
        ('352517', '3525', 'Sangkapura'),
        ('352518', '3525', 'Tambak'),
        ('352601', '3526', 'Bangkalan'),
        ('352602', '3526', 'Socah'),
        ('352603', '3526', 'Burneh'),
        ('352604', '3526', 'Kamal'),
        ('352605', '3526', 'Arosbaya'),
        ('352606', '3526', 'Geger'),
        ('352607', '3526', 'Klampis'),
        ('352608', '3526', 'Sepulu'),
        ('352609', '3526', 'Tanjung Bumi'),
        ('352610', '3526', 'Kokop'),
        ('352611', '3526', 'Kwanyar'),
        ('352612', '3526', 'Labang'),
        ('352613', '3526', 'Tanah Merah'),
        ('352614', '3526', 'Tragah'),
        ('352615', '3526', 'Blega'),
        ('352616', '3526', 'Modung'),
        ('352617', '3526', 'Konang'),
        ('352618', '3526', 'Galis'),
        ('352701', '3527', 'Sreseh'),
        ('352702', '3527', 'Torjun'),
        ('352703', '3527', 'Sampang'),
        ('352704', '3527', 'Camplong'),
        ('352705', '3527', 'Omben'),
        ('352706', '3527', 'Kedungdung'),
        ('352707', '3527', 'Jrengik'),
        ('352708', '3527', 'Tambelangan'),
        ('352709', '3527', 'Banyuates'),
        ('352710', '3527', 'Robatal'),
        ('352711', '3527', 'Sokobanah'),
        ('352712', '3527', 'Ketapang'),
        ('352713', '3527', 'Pangarengan'),
        ('352714', '3527', 'Karangpenang'),
        ('352801', '3528', 'Tlanakan'),
        ('352802', '3528', 'Pademawu'),
        ('352803', '3528', 'Galis'),
        ('352804', '3528', 'Pamekasan'),
        ('352805', '3528', 'Proppo'),
        ('352806', '3528', 'Palenggaan'),
        ('352807', '3528', 'Pegantenan'),
        ('352808', '3528', 'Larangan'),
        ('352809', '3528', 'Pakong'),
        ('352810', '3528', 'Waru'),
        ('352811', '3528', 'Batumarmar'),
        ('352812', '3528', 'Kadur'),
        ('352813', '3528', 'Pasean'),
        ('352901', '3529', 'Kota Sumenep'),
        ('352902', '3529', 'Kalianget'),
        ('352903', '3529', 'Manding'),
        ('352904', '3529', 'Talango'),
        ('352905', '3529', 'Bluto'),
        ('352906', '3529', 'Saronggi'),
        ('352907', '3529', 'Lenteng'),
        ('352908', '3529', 'Giliginting'),
        ('352909', '3529', 'Guluk-Guluk'),
        ('352910', '3529', 'Ganding'),
        ('352911', '3529', 'Pragaan'),
        ('352912', '3529', 'Ambunten'),
        ('352913', '3529', 'Pasongsongan'),
        ('352914', '3529', 'Dasuk'),
        ('352915', '3529', 'Rubaru'),
        ('352916', '3529', 'Batang Batang'),
        ('352917', '3529', 'Batuputih'),
        ('352918', '3529', 'Dungkek'),
        ('352919', '3529', 'Gapura'),
        ('352920', '3529', 'Gayam'),
        ('352921', '3529', 'Nonggunong'),
        ('352922', '3529', 'Raas'),
        ('352923', '3529', 'Masalembu'),
        ('352924', '3529', 'Arjasa'),
        ('352925', '3529', 'Sapeken'),
        ('352926', '3529', 'Batuan'),
        ('352927', '3529', 'Kangayan'),
        ('357101', '3571', 'Mojoroto'),
        ('357102', '3571', 'Kota'),
        ('357103', '3571', 'Pesantren'),
        ('357201', '3572', 'Kepanjenkidul'),
        ('357202', '3572', 'Sukorejo'),
        ('357203', '3572', 'Sananwetan'),
        ('357301', '3573', 'Blimbing'),
        ('357302', '3573', 'Klojen'),
        ('357303', '3573', 'Kedungkandang'),
        ('357304', '3573', 'Sukun'),
        ('357305', '3573', 'Lowokwaru'),
        ('357401', '3574', 'Kademangan'),
        ('357402', '3574', 'Wonoasih'),
        ('357403', '3574', 'Mayangan'),
        ('357404', '3574', 'Kanigaran'),
        ('357405', '3574', 'Kedopok'),
        ('357501', '3575', 'Gadingrejo'),
        ('357502', '3575', 'Purworejo'),
        ('357503', '3575', 'Bugul Kidul'),
        ('357504', '3575', 'Panggungrejo'),
        ('357601', '3576', 'Prajuritkulon'),
        ('357602', '3576', 'Magersari'),
        ('357603', '3576', 'Kranggan'),
        ('357701', '3577', 'Kartoharjo'),
        ('357702', '3577', 'Manguharjo'),
        ('357703', '3577', 'Taman'),
        ('357801', '3578', 'Karang Pilang'),
        ('357802', '3578', 'Wonocolo'),
        ('357803', '3578', 'Rungkut'),
        ('357804', '3578', 'Wonokromo'),
        ('357805', '3578', 'Tegalsari'),
        ('357806', '3578', 'Sawahan'),
        ('357807', '3578', 'Genteng'),
        ('357808', '3578', 'Gubeng'),
        ('357809', '3578', 'Sukolilo'),
        ('357810', '3578', 'Tambaksari'),
        ('357811', '3578', 'Simokerto'),
        ('357812', '3578', 'Pabean Cantian'),
        ('357813', '3578', 'Bubutan'),
        ('357814', '3578', 'Tandes'),
        ('357815', '3578', 'Krembangan'),
        ('357816', '3578', 'Semampir'),
        ('357817', '3578', 'Kenjeran'),
        ('357818', '3578', 'Lakarsantri'),
        ('357819', '3578', 'Benowo'),
        ('357820', '3578', 'Wiyung'),
        ('357821', '3578', 'Dukuh Pakis'),
        ('357822', '3578', 'Gayungan'),
        ('357823', '3578', 'Jambangan'),
        ('357824', '3578', 'Tenggilis Mejoyo'),
        ('357825', '3578', 'Gunung Anyar'),
        ('357826', '3578', 'Mulyorejo'),
        ('357827', '3578', 'Sukomanunggal'),
        ('357828', '3578', 'Asem Rowo'),
        ('357829', '3578', 'Bulak'),
        ('357830', '3578', 'Pakal'),
        ('357831', '3578', 'Sambikerep'),
        ('357901', '3579', 'Batu'),
        ('357902', '3579', 'Bumiaji'),
        ('357903', '3579', 'Junrejo')
    ]
   
    bulan_nama = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus", 
    9: "September", 10: "Oktober", 11: "November", 12: "Desember"
    }


    cdk_df = pd.DataFrame(cdk_list, columns=['cdk_id', 'cdk_name'])
    kabupaten_df = pd.DataFrame(Kabupaten_list, columns=['kabupaten_id', 'cdk_id', 'kabupaten_name'])
    kecamatan_df = pd.DataFrame(Kecamatan_list, columns=['kecamatan_id', 'kabupaten_id', 'kecamatan_name'])

    # Mapping Kabupaten per CDK
    cdk_kabupaten_map = (
    kabupaten_df
    .groupby("cdk_id")["kabupaten_name"]
    .apply(list)
    .to_dict()
    )

    # Mapping Kecamatan per Kabupaten
    kabupaten_kecamatan_map = (
        kecamatan_df
        .merge(kabupaten_df, on="kabupaten_id")
        .groupby("kabupaten_id")["kecamatan_name"]
        .apply(list)
        .to_dict()
    )

    # Streamlit app
    if "selected_cdk" not in st.session_state:
        st.session_state.selected_cdk = ""
        st.session_state.kabupaten_options = []
        st.session_state.selected_kabupaten = ""
        st.session_state.kecamatan_options = []
    
    def periksa_kabupaten(cdk):
        if cdk:
            st.session_state.selected_cdk = cdk
            cdk_id = cdk_df[cdk_df["cdk_name"] == cdk]["cdk_id"].values[0]
            st.session_state.kabupaten_options = cdk_kabupaten_map.get(cdk_id, [])
        else:
            st.session_state.kabupaten_options = []
        
        # Reset semua state terkait form

        st.session_state.kabupaten_name = ""
        st.session_state.kecamatan_select = ""
        st.session_state.kecamatan_options = []
        st.session_state.desa = ""
        st.session_state.kth = ""
        st.session_state.penyuluh = ""
        st.session_state.laporanprodkayu = 0.0
        st.session_state.datante = 0.0
        st.session_state.keterangan = ""
        st.session_state.jati = 0.0
        st.session_state.sengon = 0.0
        st.session_state.mahoni = 0.0
        st.session_state.gmelina = 0.0
        st.session_state.sonokeling = 0.0
        st.session_state.pinus = 0.0
        st.session_state.akasia = 0.0
        st.session_state.mindi = 0.0
        st.session_state.balsa = 0.0
        st.session_state.jabon = 0.0
        st.session_state.jeniskayulain = 0.0

    # Form untuk input
    with st.form(key="Form_Dataproduksikayuhutanrakyat"):
        
        st.subheader("Pilih Bulan dan Tahun")
        bulan = st.selectbox("Bulan", options=list(bulan_nama.keys()), format_func=lambda x : bulan_nama[x], key="bulan_name")
        tahun = st.number_input("Tahun", value=datetime.now().year, min_value=2000, max_value=2100, step=1, key="tahun_nm")
        
        month_name = bulan_nama[bulan]

        cdk = st.selectbox(
            label="CDK",
            options=[""] + cdk_df["cdk_name"].tolist(),
            key="cdk_name"
        )
        if st.form_submit_button("Periksa Kabupaten"):
            periksa_kabupaten(cdk)


        Kabupaten = st.selectbox(
            label="Kabupaten/Kota",
            options=[""] + st.session_state.kabupaten_options,
            key="kabupaten_name",
        )

        if st.form_submit_button("Periksa Kecamatan"):
            if Kabupaten:
                st.session_state.selected_kabupaten = Kabupaten
                Kabupaten_id = kabupaten_df[kabupaten_df["kabupaten_name"] == Kabupaten]["kabupaten_id"].values[0]
                st.session_state.kecamatan_options = kabupaten_kecamatan_map.get(Kabupaten_id, [])
            else:
                st.session_state.kecamatan_options = []

        Kecamatan = st.selectbox(
            label="Kecamatan",
            options=[""] + st.session_state.kecamatan_options,
            key="kecamatan_select",
        )

        # Input lainnya
        Desa = st.text_input(label="Desa", key="desa")
        kth = st.text_input(label="KTH", key="kth")
        Penyuluh = st.text_input(label="Penyuluh pendamping", key="penyuluh")
        Jati = st.number_input(label="Jati", key="jati", min_value=0.0)
        Sengon = st.number_input(label="Sengon", key="sengon", min_value=0.0)
        Mahoni = st.number_input(label="Mahoni", key="mahoni", min_value=0.0)
        Gmelina = st.number_input(label="Gmelina", key="gmelina", min_value=0.0)
        Sonokeling = st.number_input(label="Sonokeling", key="sonokeling", min_value=0.0)
        Pinus = st.number_input(label="Pinus", key="pinus", min_value=0.0)
        Akasia = st.number_input(label="Akasia", key="akasia", min_value=0.0)
        Mindi = st.number_input(label="Mindi", key="mindi", min_value=0.0)
        Balsa = st.number_input(label="Balsa", key="balsa", min_value=0.0)
        Jabon = st.number_input(label="Jabon", key="jabon", min_value=0.0)
        Jenis_lainnya = st.number_input(label="Jenis Kayu Lainnya", key="jeniskayulain", min_value=0.0)
        Jumlah_kayu = int(Jati) + int(Sengon) + int(Mahoni) + int(Gmelina) + int(Sonokeling) + int(Pinus) + int(Akasia) + int(Mindi) + int(Balsa) + int(Jabon) + int(Jenis_lainnya)
        data_NTE = st.number_input(label="Data NTE", min_value=0.0, key="datante")
        selisih = float(data_NTE) - float(Jumlah_kayu)
        Keterangan = st.text_input(label="Keterangan lainnya", key="keterangan")

        if st.form_submit_button(label="Konfirmasi laporan"):
            if not Kabupaten or not Kecamatan or not Desa or not kth or not Penyuluh:
                st.warning("Tolong isi form dengan lengkap")
            else:
                # Membuat DataFrame untuk data input
                dataprodhutanrakyat = pd.DataFrame(
                    [
                        {
                            "CDK": cdk,
                            "Kabupaten/Kota": Kabupaten,
                            "Kecamatan": Kecamatan,
                            "Desa": Desa,
                            "KTH": kth,
                            "Penyuluh Pendamping": Penyuluh,
                            "Jati": Jati,
                            "Sengon": Sengon,
                            "Mahoni": Mahoni,
                            "Gmelina": Gmelina,
                            "Sonokeling": Sonokeling,
                            "Pinus": Pinus,
                            "Akasia": Akasia,
                            "Mindi": Mindi,
                            "Balsa": Balsa,
                            "Jabon": Jabon,
                            "Jenis Lainnya": Jenis_lainnya,
                            "Jumlah": Jumlah_kayu,
                            "Data NTE (m3)": data_NTE,
                            "Selisih (m3)": selisih,
                            "Keterangan Lainnya": Keterangan,
                            "Bulan": bulan,
                            "Tahun": tahun,
                        }
                    ]
                )
                # Update existing data
                df_update = pd.concat([existing_data, dataprodhutanrakyat])

                data_to_append = [[""] + row for row in dataprodhutanrakyat.values.tolist()]

                # Append rows to worksheet

                last_row_kayu = len(worksheet.get_all_values())
                worksheet.insert_rows(data_to_append, last_row_kayu + 1)
                
                new_row_start_index_kayu = last_row_kayu + 1
                new_row_end_index_kayu = new_row_start_index_kayu + len(dataprodhutanrakyat) - 1

                for row_index_kayu in range(new_row_start_index_kayu, new_row_end_index_kayu + 1):
                    timestamp_formula = f"=IF(NOT(ISBLANK(B{row_index_kayu}));NOW();\"\")"
                    worksheet.update_cell(row_index_kayu, 1, timestamp_formula)
                
                st.success("Data berhasil diinput")
                for key in [
                    "cdk_name",
                    "kabupaten_name",
                    "kecamatan_select",
                    "desa",
                    "kth",
                    "penyuluh",
                    "jati",
                    "sengon",
                    "mahoni",
                    "gmelina",
                    "sonokeling",
                    "pinus",
                    "akasia",
                    "mindi",
                    "balsa",
                    "jabon",
                    "jeniskayulain",
                    "datante",
                    "keterangan",
                ]:
                    if key in st.session_state:
                        del st.session_state[key]

                # Rerun untuk mereset form
                periksa_kabupaten(cdk)
                st.session_state.cdk_name = ""
                st.rerun()
