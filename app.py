import streamlit as st
import json
from results import get_result  # 結果出力関数（後ほど提供）
import random

# タイトルと説明
st.set_page_config(page_title="まめこ式 発信ズレ診断", layout="centered")
st.title("📘 まめこ式・発信ズレ診断")
st.write("noteが書けない・読まれない… その原因、あなたの『発信のズレ』かもしれません。")

# 質問を読み込む
with open("questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

# 質問の順序をシャッフル
random.shuffle(questions)

st.markdown("#### 👉 20問の質問に「はい」または「いいえ」で答えてください。")

# 回答用変数
responses = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

with st.form("diagnosis_form"):
    for idx, q in enumerate(questions):
        answer = st.radio(f"{idx+1}. {q['text']}", ["はい", "いいえ"], key=f"q{idx}")
        if answer == "はい":
            responses[q["type"]] += 1
    submitted = st.form_submit_button("診断する")

if submitted:
    st.markdown("---")
    st.header("📊 診断結果")

    main_type = max(responses, key=responses.get)
    sub_type = sorted(responses.items(), key=lambda x: x[1], reverse=True)[1][0]

    st.write(f"あなたの主タイプ：**Type {main_type}**")
    st.write(f"補助タイプ：**Type {sub_type}**")

    # 結果表示
    result_text = get_result(main_type)
    st.markdown(result_text, unsafe_allow_html=True)

    st.markdown("---")
    st.info("この結果に基づいて、あなたに合ったnoteの章・プロンプトをご提案します。")
