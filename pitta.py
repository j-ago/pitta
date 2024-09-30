import streamlit as st

# Title of the app
st.title('Pittaアンバランス度診断アプリ')

# Instructions
st.write('以下の質問にお答えください。各質問に最も当てはまる答えを選んでください。')

# Questions from the Excel file
questions = [
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
    # Add additional questions here
]

# Mapping response options to their corresponding scores
options = {
    "当てはまる": 4,
    "まあまあ当てはまる": 3,
    "どちらともいえない": 2,
    "あまり当てはまらない": 1,
    "当てはまらない": 0,
}

# Initialize the total score
total_score = 0

# Display questions and collect responses
for idx, question in enumerate(questions):
    question_text = f"質問{idx + 1}　{question}"
    response = st.radio(question_text, list(options.keys()), key=question_text)
    total_score += options[response]

# Button to view the diagnosis
if st.button('診断結果を見る'):
    # Calculate the score as a percentage of the maximum score (40)
    percentage_score = (total_score / 40) * 100

    # Display the result based on the percentage
    st.write("## 診断結果")

    if percentage_score <= 20:
        st.success("安定している状態です。この状態を維持するように心がけてください。")
    elif percentage_score <= 40:
        st.info("比較的安定している状態です。乱れが多く出ないように心がけてください。")
    elif percentage_score <= 60:
        st.warning("乱れが少し出ている状態です。安定化に向けて心がけてください。")
    elif percentage_score <= 80:
        st.warning("乱れが多く出ている状態です。安定化に向けて積極的に対応してください。")
    else:
        st.error("とても乱れている状態です。改善に向けて迅速に対応してください。")

    st.write(f"あなたのスコアは: {total_score} / 40 ({percentage_score:.2f}%)")