
"""Aplikasi Streamlit prediksi purchases.
Jalankan: streamlit run app.py
"""

from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

FEATURES = [
    "product_views",
    "cart_additions",
    "ad_clicks",
    "discount_rate",
    "user_rating",
    "time_on_site",
    "device_type"
]

st.set_page_config(
    page_title="Prediksi Purchases",
    page_icon="🛒",
    layout="centered"
)


# Memuat model lokal
@st.cache_resource
def load_model():
    model_path = Path(__file__).with_name("best_model (1).pkl")
    return joblib.load(model_path)


# Fungsi prediksi
def predict_df(df: pd.DataFrame):
    model = load_model()
    return model.predict(df[FEATURES]).round(2).tolist()


st.title("🛒 Prediksi Jumlah Pembelian")
st.caption(
    "Sistem Prediksi jumlah pembelian (purchases) berdasarkan data perilaku pengguna "
    "pada data e-commerce."
)


# Tab aplikasi
tab1, tab2 = st.tabs([
    "Prediksi tunggal",
    "Prediksi batch (CSV)"
])


# =================================
# PREDIKSI TUNGGAL
# =================================
with tab1:

    c1, c2 = st.columns(2)

    with c1:
        views = st.number_input(
            "product_views", 0, 5000, 500
        )

        carts = st.number_input(
            "cart_additions", 0, 1000, 100
        )

        clicks = st.number_input(
            "ad_clicks", 0, 2000, 150
        )

        device = st.selectbox(
            "device_type",
            ["Mobile", "Desktop", "Tablet"]
        )

    with c2:
        disc = st.slider(
            "discount_rate", 0.0, 0.5, 0.25, 0.01
        )

        rating = st.slider(
            "user_rating", 1.0, 5.0, 3.5, 0.1
        )

        tsite = st.number_input(
            "time_on_site (menit)",
            0.0, 120.0, 10.0
        )

    if st.button("Prediksi", type="primary"):

        row = pd.DataFrame([{
            "product_views": views,
            "cart_additions": carts,
            "ad_clicks": clicks,
            "discount_rate": disc,
            "user_rating": rating,
            "time_on_site": tsite,
            "device_type": device
        }])

        try:
            prediction = predict_df(row)[0]

            st.metric(
                "Prediksi purchases",
                f"{prediction:.1f}"
            )

        except Exception as e:
            st.error(f"Gagal memprediksi: {e}")


# =================================
# PREDIKSI BATCH
# =================================
with tab2:

    st.write(
        "Unggah CSV dengan kolom: "
        + ", ".join(FEATURES)
    )

    up = st.file_uploader(
        "File CSV",
        type="csv"
    )

    if up is not None:

        data = pd.read_csv(up)

        missing = [
            c for c in FEATURES
            if c not in data.columns
        ]

        if missing:
            st.error(f"Kolom kurang: {missing}")

        else:
            try:
                data["predicted_purchases"] = predict_df(data)

                st.dataframe(data)

                st.download_button(
                    "Unduh hasil",
                    data.to_csv(index=False),
                    "hasil_prediksi.csv",
                    "text/csv"
                )

            except Exception as e:
                st.error(f"Gagal memprediksi: {e}")
