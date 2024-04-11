# 1. 라이브러리 임포트
import streamlit as st
import openai
# 2. 기능 구현 함수
def askGpt(prompt):
    messages_prompt = [{"role": "system", "content": prompt}]
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=messages_prompt)
    gptResponse = response["choices"][0]["message"]["content"]
    return gptResponse
# 3. 메인 함수
def main():
    st.set_page_config(page_title="요약 프로그램")
    # 사이드바
    with st.sidebar:
        open_apikey = st.text_input(label='OPENAI API 키', placeholder='', value='',type='password')
        # 입력받은 API 키 표시
        if open_apikey:
            openai.api_key  = open_apikey
        st.markdown('---')
    st.header("💎:green[요약프로그램]💎", divider='green')
    st.markdown('---')
    text = st.text_area(":rainbow[마 형님이 다 요약해줄게]")
    if st.button("요약🙌"):
        prompt = f'''
        **Instructions** :
        - You are an expert assistant that summarizes text into **Korean language**.
        - Your task is to summarize the **text** sentences in **Korean language**.
        - Your summaries should include the following :
            - Omit duplicate content, but increase the summary weight of duplicate content.
            - Summarize by emphasizing concepts and arguments rather than case evidence.
            - Summarize in 3 lines.
            - Use the format of a bullet point.
        -text : {text}
        '''
        st.info(askGpt(prompt))
if __name__=="__main__":
        main()