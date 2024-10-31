import streamlit as st

# Language selection dropdown
language = st.selectbox("言語 - Language", options=["日本語", "English"], index=0)

# Title of the app based on selected language
st.title('Pittaアンバランス度診断アプリ' if language == "日本語" else "Pitta Imbalance Diagnosis App")

# Instructions
st.write('以下の質問にお答えください。各質問に最も当てはまる答えを選んでください。' if language == "日本語" else "Please answer the following questions by selecting the most applicable answer.")

# Questions in Japanese and English for Pitta
questions_japanese = [
    "やたらに汗が出る",
    "肌に赤いブツブツ（発疹）ができる",
    "顔面や鼻が赤い",
    "白目部分が赤く充血する",
    "お腹がいっぱいになるまで大食する",
    "冷たい飲み物や食べ物を食べずにおれない",
    "口内炎ができている。あるいは口臭が強い",
    "口の渇きが強い。あるいは口内が塩からい味がする",
    "胸やけがしたり、肛門の灼熱感がある",
    "大便が軟便ぎみで下痢しやすい",
]

questions_english = [
    "I sweat profusely",
    "Red bumps (rash) appear on the skin",
    "Red face and nose",
    "The whites of the eyes are red and bloodshot",
    "Eat until you're full",
    "Frequently needs cold drinks or food",
    "Prone to mouth ulcers or bad breath",
    "Severe thirst or a salty taste in the mouth",
    "Heartburn or burning sensation in the anus",
    "Loose stools or prone to diarrhea",
]

# Select questions based on language
questions = questions_japanese if language == "日本語" else questions_english

# Mapping response options to their corresponding scores
options = {
    "当てはまる" if language == "日本語" else "Applies to me": 4,
    "まあまあ当てはまる" if language == "日本語" else "Somewhat applies to me": 3,
    "どちらともいえない" if language == "日本語" else "Neither does it apply to me": 2,
    "あまり当てはまらない" if language == "日本語" else "Not very applicable": 1,
    "当てはまらない" if language == "日本語" else "Does not apply to me": 0,
}

# Initialize the total score
total_score = 0

# Display questions and collect responses
for idx, question in enumerate(questions):
    question_text = f"質問{idx + 1}　{question}" if language == "日本語" else f"Question {idx + 1}: {question}"
    st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>{question_text}</p>", unsafe_allow_html=True)
    response = st.radio("", list(options.keys()), key=question_text)
    total_score += options[response]

# Button to view the diagnosis
if st.button('診断結果を見る' if language == "日本語" else "View Diagnosis"):
    # Calculate the score as a percentage of the maximum score (40)
    percentage_score = (total_score / 40) * 100

    # Display the result based on the percentage
    st.write("## 診断結果" if language == "日本語" else "## Diagnosis Result")

    if percentage_score <= 20:
        st.success("安定している状態です。この状態を維持するように心がけてください。" if language == "日本語" else "You are in a stable state. Please continue to maintain this condition.")
    elif percentage_score <= 40:
        st.info("比較的安定している状態です。乱れが多く出ないように心がけてください。" if language == "日本語" else "You are relatively stable. Try to avoid disruptions.")
    elif percentage_score <= 60:
        st.warning("乱れが少し出ている状態です。安定化に向けて心がけてください。" if language == "日本語" else "Some instability is present. Please aim for stabilization.")
    elif percentage_score <= 80:
        st.warning("乱れが多く出ている状態です。安定化に向けて積極的に対応してください。" if language == "日本語" else "There is significant instability. Take proactive measures to stabilize.")
    else:
        st.error("とても乱れている状態です。改善に向けて迅速に対応してください。" if language == "日本語" else "Your state is highly unstable. Please take immediate steps for improvement.")

    st.write(f"あなたのスコアは: {total_score} / 40 ({percentage_score:.2f}%)" if language == "日本語" else f"Your score is: {total_score} / 40 ({percentage_score:.2f}%)")
