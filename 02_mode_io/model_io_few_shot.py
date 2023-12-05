from langchain.llms import OpenAI
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {
        "input": "LangChainはChatGPT・Large Language Model (LLM)の実利用をより柔軟に簡易に行うためのツール群です",  #← 입력 예
        "output": "LangChainは、ChatGPT・Large Language Model (LLM)の実利用をより柔軟に、簡易に行うためのツール群です。"  #← 출력 예
    }
]

prompt = PromptTemplate(  #← PromptTemplate 준비
    input_variables=["input", "output"],  #← input과 output을 입력 변수로 설정
    template="입력: {input}\n출력: {output}",  #← 템플릿
)

few_shot_prompt = FewShotPromptTemplate(  #← FewShotPromptTemplate 준비
    examples=examples,  #← 입력 예와 출력 예를 정의
    example_prompt=prompt,  #← FewShotPromptTemplate에 PromptTemplate를 전달
    prefix="아래 구두점이 빠진 입력에 구두점을 추가해 주세요. 추가할 수 있는 구두점은 '、', '。'입니다. 다른 문장 부호는 추가하지 마세요.",  #← 지시어 추가하기
    suffix="입력: {input_string}\n출력:",  #← 출력 예의 입력 변수를 정의
    input_variables=["input_string"],  #← FewShotPromptTemplate의 입력 변수를 설정
)
llm = OpenAI()
formatted_prompt = few_shot_prompt.format( #← FewShotPromptTemplate을 사용하여 프롬프트 작성
    input_string="私はさまざまな機能がモジュールとして提供されているLangChainを使ってアプリケーションを開発しています"
)
result = llm.predict(formatted_prompt)
print("formatted_prompt: ", formatted_prompt)
print("result: ", result)
