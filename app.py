import streamlit as st
import pickle
import pandas as pd
import numpy as np

# ===============================
# LOAD MODEL BUNDLE
# ===============================

with open("ufc_model_bundle.pkl", "rb") as f:
    bundle = pickle.load(f)

model = bundle["model"]
label_encoders = bundle["label_encoders"]
fighter_stats_df = bundle["fighter_stats_df"]
feature_columns = bundle["feature_columns"]
median_fight_time = bundle["median_fight_time"]

# ===============================
# FIND MATCHING FIGHTER NAMES
# ===============================

def search_fighters(query):
    matches = fighter_stats_df[fighter_stats_df['fighter_name'].str.contains(query, case=False, na=False)]
    return matches['fighter_name'].tolist()

# ===============================
# PREDICTION FUNCTION
# ===============================

def predict_winner(f1_name, f2_name, weight_class="Lightweight"):

    # Get fighter stats
    f1_stats = fighter_stats_df[fighter_stats_df['fighter_name'] == f1_name]
    f2_stats = fighter_stats_df[fighter_stats_df['fighter_name'] == f2_name]

    if f1_stats.empty or f2_stats.empty:
        return None

    f1 = f1_stats.iloc[0]
    f2 = f2_stats.iloc[0]

    # STR per min
    str1 = f1['avg_STR'] / (median_fight_time / 60)
    str2 = f2['avg_STR'] / (median_fight_time / 60)

    # Encode weight class
    try:
        wc_encoded = label_encoders["Weight_Class"].transform([weight_class])[0]
    except:
        wc_encoded = 1  # fallback lightweight

    # Prepare feature vector (same order as training)
    features = pd.DataFrame([[
        f1['avg_KD'], str1, f1['avg_TD'], f1['avg_SUB'],
        f2['avg_KD'], str2, f2['avg_TD'], f2['avg_SUB'],
        wc_encoded,
        f1['reach'] - f2['reach'],
        f1['height'] - f2['height'],
        f1['stance'], f2['stance']
    ]], columns=feature_columns)

    prob = model.predict_proba(features)[0][1]

    result = {
        "fighter1": f1_name,
        "fighter2": f2_name,
        "fighter1_win_prob": float(prob * 100),
        "fighter2_win_prob": float((1 - prob) * 100),
        "winner": f1_name if prob > 0.5 else f2_name,
        "confidence": float(max(prob, 1 - prob) * 100)
    }

    return result


# ===============================
# STREAMLIT UI
# ===============================

st.title("🥊 UFC Fight Predictor")
st.write("Select two fighters and predict the winner based on historical stats.")

# Fighter 1 input
f1_input = st.text_input("Search name for Fighter 1")
f1_matches = search_fighters(f1_input) if f1_input else []

f1 = st.selectbox("Select Fighter 1", f1_matches)

# Fighter 2 input
f2_input = st.text_input("Search name for Fighter 2")
f2_matches = search_fighters(f2_input) if f2_input else []

f2 = st.selectbox("Select Fighter 2", f2_matches)

# Weight class dropdown
weight_classes = label_encoders["Weight_Class"].classes_
weight_class = st.selectbox("Weight Class", weight_classes)

# Predict button
if st.button("Predict Winner"):
    if f1 and f2:
        result = predict_winner(f1, f2, weight_class)

        if result:
            st.subheader("Prediction Result:")
            st.write(f"**Winner:** {result['winner']} ({result['confidence']}% confidence)")
            st.write(f"{result['fighter1']}: {result['fighter1_win_prob']}% chance")
            st.write(f"{result['fighter2']}: {result['fighter2_win_prob']}% chance")
        else:
            st.error("Could not generate prediction. Check fighter names.")


st.components.v1.iframe(
    "https://app.powerbi.com/view?r=eyJrIjoiNjAzYmNkOTktYzllYy00NjU3LWI3M2EtMTgyZTBiNGIzZTYwIiwidCI6IjcxMWYwNjQxLTc5ODUtNDRlNS1iMjQwLWQyZTk5MjZhNTVjMyJ9",
    height=800,
    scrolling=True
)
