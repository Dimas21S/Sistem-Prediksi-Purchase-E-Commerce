# Deployment Model Prediksi Purchases

## Isi
- `api.py` – REST API (FastAPI): `/health`, `/predict`, `/predict/batch`
- `app.py` – antarmuka Streamlit (mode model lokal atau memanggil REST API)
- `train_model.py` – melatih ulang model dari `ecommerce_clean.csv` dan menyimpan `best_model.pkl`
- `ecommerce_clean.csv` – data bersih hasil notebook
- `best_model.pkl` – model Linear Regression
- `requirements.txt`

## Menjalankan
```bash
pip install -r requirements.txt
python train_model.py             # latih ulang model agar cocok dengan versi library Anda
uvicorn api:app --port 8000        # terminal 1 (docs otomatis: http://localhost:8000/docs)
streamlit run app.py               # terminal 2
```
Contoh request:
```bash
curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" \
 -d '{"product_views":500,"cart_additions":100,"ad_clicks":150,"discount_rate":0.25,"user_rating":3.5,"time_on_site":10,"device_type":"Mobile"}'
```
Catatan: file `.pkl` hanya andal dimuat pada versi scikit-learn yang sama saat disimpan. Jalankan `train_model.py` di komputer Anda sebelum memulai API/Streamlit (Python 3.10 pun bisa).
