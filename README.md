# Deployment Model Prediksi Purchases

## Isi
- `app.py` – antarmuka Streamlit
- `best_model.pkl` – model regresi terbaik
- `requirements.txt`

## Menjalankan
```bash
pip install -r requirements.txt
streamlit run app.py               # terminal 1
```
Contoh request:
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" \
 -d '{"product_views":500,"cart_additions":100,"ad_clicks":150,"discount_rate":0.25,"user_rating":3.5,"time_on_site":10,"device_type":"Mobile"}'
```
Catatan: file `.pkl` hanya andal dimuat pada versi scikit-learn yang sama saat disimpan. Jalankan `train_model.py` di komputer Anda sebelum memulai API/Streamlit (Python 3.10 pun bisa).
