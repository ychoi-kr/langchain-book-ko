# LangChain Book
이 리포지토리는 서적 "[LangChain 완전 입문 생성 AI 응용 프로그램 개발이 도모하는 대규모 언어 모델의 조작 방법](https://book.impress.co.jp/books/1123101047)"에서 작성하는 소스 코드입니다.


## 04_memory 샘플 코드가 제대로 작동하지 않는 문제에 대해
4장에서 사용하는 채팅 화면을 만드는 라이브러리인 chainlit의 파괴적인 업데이트의 영향으로 샘플 코드가 제대로 작동하지 않는 문제가 발생했습니다.

다음 명령을 실행하면 작성 시점의 버전으로 낮추어 정상적으로 동작할 수 있습니다.

```
python3 -m pip install chainlit==0.5.1
```
