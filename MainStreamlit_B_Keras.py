import streamlit as st
import pickle
import os

#model_path = r'D:\UAJY Kuliah Andra 220711902\Matkul\Semester 5\Pembelajaran Mesin dan Pembelajaran Mendalam B\99 UTS\proj\BestModel_CLF_GBC_Keras.pkl'
#model_path = r'C:\Users\tab3v\OneDrive\Dokumen\PMPM_Regresi\Lasso_price_model.pkl'

#model=os.path.join(model_path,'BestModel_CLF_GBC_Keras.pkl')

#with open(model_path, 'rb') as f:
    #loaded_model = pickle.load(f)

#scaler = loaded_model[0]
#feature_selector = loaded_model[1]
#CS_model = loaded_model

from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu('UTS ML Kelas B Kelompok Keras',
                           ['Klasifikasi',
                            'Regresi', 'Catatan'],
                            default_index=0)
    
if selected == 'Klasifikasi':
    
    model='BestModel_CLF_GBC_Keras.pkl'
    
    with open(model, 'rb') as f:
        loaded_model = pickle.load(f)
        
    CS_model = loaded_model
    
    st.title('Klasifikasi')

    file = st.file_uploader("Masukkan File", type=["csv", "txt"])

    st.write('Masukkan luas dalam meter persegi')
    squaremeters = st.number_input("Masukkan luas", 0)

    st.write('Masukkan jumlah kamar')
    numberofrooms = st.slider("Jumlah kamar",0,100)

    st.write('Mempunyai halaman ?')
    hasyard = st.radio("Halaman", ["Ya","Tidak"])

    st.write('Mempunyai kolam renang ?')
    haspool = st.radio("Kolam renang", ["Ya","Tidak"])

    st.write('Masukkan jumlah lantai')
    floors = st.slider("Jumlah lantai",0,100)

    st.write('Masukkan kode lokasi')
    citycode = st.number_input("kode lokasi", 0)

    st.write('Masukkan eksklusivitas kawasan')
    citypartrange = st.slider("citypartrange",0,10)

    st.write('Masukkan jumlah pemilik sebelumnya')
    numprevowners = st.slider("prevOwner",0,10)

    st.write('Masukkan tahun pembuatan')
    made = st.number_input("Tahun", 0)

    st.write('Merupakan Gedung baru atau tidak ?')
    isnewbuilt = st.radio("gedung baru", ["Ya","Tidak"])

    st.write('Mempunyai Perlindungan badai ?')
    hasstormprotector = st.radio("perlindungan badai", ["Ya","Tidak"])

    st.write('Masukkan luas basement')
    basement = st.number_input("luas basement", 0)

    st.write('Masukkan luas loteng')
    attic = st.number_input("luas loteng", 0)

    st.write('Masukkan luas garasi')
    garage = st.number_input("luas garasi", 0)

    st.write('Mempunyai Gudang ?')
    hasstorageroom = st.radio("gudang", ["Ya","Tidak"])

    st.write('Masukkan jumlah ruang tamu')
    hasguestroom = st.slider("ruangTamu",0,10)

    if hasyard == "Ya":
        input_hasyardYes = 1
        input_hasyardNo = 0
    else:
        input_hasyardYes = 0
        input_hasyardNo = 1

    if haspool == "Ya":
        input_haspoolYes = 1
        input_haspoolNo = 0
    else:
        input_haspoolYes = 0
        input_haspoolNo = 1

    if isnewbuilt == "Ya":
        input_isnewbuiltYes = 1
        input_isnewbuiltNo = 0
    else:
        input_isnewbuiltYes = 0
        input_isnewbuiltNo = 1

    if hasstormprotector == "Ya":
        input_hasstormprotectorYes = 1
        input_hasstormprotectorNo = 0
    else:
        input_hasstormprotectorYes = 0
        input_hasstormprotectorNo = 1

    if hasstorageroom == "Ya":
        input_hasstorageroomYes = 1
        input_hasstorageroomNo = 0
    else:
        input_hasstorageroomYes = 0
        input_hasstorageroomNo = 1


    input_data = [ input_hasyardNo,input_hasyardYes,input_haspoolNo,input_haspoolYes,input_isnewbuiltYes, input_isnewbuiltNo, input_hasstormprotectorNo, input_hasstormprotectorYes, input_hasstorageroomNo,input_hasstorageroomYes,  squaremeters, numberofrooms, floors, citycode, citypartrange,
              numprevowners, made , basement, attic, garage, hasguestroom]

                 
    st.write("Data property yang akan diinput ke model")
    st.write(input_data)

    if st.button("Prediksi Kategori"):
        CS_model_prediction = CS_model.predict([input_data])
        outcome = {0: 'Basic', 2: 'Luxury', 1: 'Middle'}
        st.write(f"Property tersebut diprediksi **{outcome[CS_model_prediction[0]]}**")

if selected == 'Regresi':

    model='SVR_price_model.pkl'
    
    with open(model, 'rb') as f:
        loaded_model = pickle.load(f)

    
    st.title('Regresi')

    st.write('Masukkan File')
    file = st.file_uploader("Masukkan File", type=["csv", "txt"])
    st.write('Masukkan Luas dalam Meter Persegi')
    squaremeters = st.number_input("Masukkan luas", 0)

    st.write('Masukkan Jumlah Kamar')
    numberofrooms = st.slider("Jumlah kamar", 0, 100)

    st.write('Mempunyai Halaman?')
    hasyard = st.radio("Halaman", ["Ya", "Tidak"])

    st.write('Mempunyai Kolam Renang?')
    haspool = st.radio("Kolam renang", ["Ya", "Tidak"])

    st.write('Masukkan Jumlah Lantai')
    floors = st.slider("Jumlah lantai", 0, 100)

    st.write('Masukkan Kode Lokasi')
    citycode = st.number_input("Kode lokasi", 0)

    st.write('Masukkan Eksklusivitas Kawasan')
    citypartrange = st.slider("Citypartrange", 0, 10)

    st.write('Masukkan Jumlah Pemilik Sebelumnya')
    numprevowners = st.slider("Prev Owner", 0, 10)

    st.write('Masukkan Tahun Pembuatan')
    made = st.number_input("Tahun", 0)

    st.write('Merupakan Gedung Baru atau Tidak?')
    isnewbuilt = st.radio("Gedung baru", ["Ya", "Tidak"])

    st.write('Mempunyai Perlindungan Badai?')
    hasstormprotector = st.radio("Perlindungan badai", ["Ya", "Tidak"])

    st.write('Masukkan Luas Basement')
    basement = st.number_input("Luas basement", 0)

    st.write('Masukkan Luas Loteng')
    attic = st.number_input("Luas loteng", 0)

    st.write('Masukkan Luas Garasi')
    garage = st.number_input("Luas garasi", 0)

    st.write('Mempunyai Gudang?')
    hasstorageroom = st.radio("Gudang", ["Ya", "Tidak"])

    st.write('Masukkan Jumlah Ruang Tamu')
    hasguestroom = st.slider("Ruang Tamu", 0, 10)

    if hasyard == "Ya":
        input_hasyardYes = 1
        input_hasyardNo = 0
    else:
        input_hasyardYes = 0
        input_hasyardNo = 1

    if haspool == "Ya":
        input_haspoolYes = 1
        input_haspoolNo = 0
    else:
        input_haspoolYes = 0
        input_haspoolNo = 1

    if isnewbuilt == "Ya":
        input_isnewbuiltYes = 1
        input_isnewbuiltNo = 0
    else:
        input_isnewbuiltYes = 0
        input_isnewbuiltNo = 1

    if hasstormprotector == "Ya":
        input_hasstormprotectorYes = 1
        input_hasstormprotectorNo = 0
    else:
        input_hasstormprotectorYes = 0
        input_hasstormprotectorNo = 1

    if hasstorageroom == "Ya":
        input_hasstorageroomYes = 1
        input_hasstorageroomNo = 0
    else:
        input_hasstorageroomYes = 0
        input_hasstorageroomNo = 1

    input_data = [ input_hasyardNo,input_hasyardYes,input_haspoolNo,input_haspoolYes,input_isnewbuiltYes, input_isnewbuiltNo, input_hasstormprotectorNo, input_hasstormprotectorYes, input_hasstorageroomNo,input_hasstorageroomYes,  squaremeters, numberofrooms, floors, citycode, citypartrange,
              numprevowners, made , basement, attic, garage, hasguestroom]

    st.write("Data property yang akan diinput ke model")
    st.write(input_data)

    if st.button("Prediksi Harga"):
        with open(model, 'rb') as f:
            regression_model = pickle.load(f)

        predicted_price = regression_model.predict([input_data])
        st.write(f"Harga properti yang diprediksi adalah **{predicted_price[0]:,.2f}**")
    
    

if selected == 'Catatan':
    st.title('Catatan')
    st.write('Kelompok Keras')
    st.write('')
    st.write('1) Aldo 220711837')
    st.write('2) Rian 220711842')
    st.write('3) Yosua Vito 220711893')
    st.write('4) Vinciant Andra Kaisarea 220711902')
    





