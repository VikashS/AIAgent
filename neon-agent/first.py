import ollama
llm = "qwen2.5"


def start_agent():
    stream = ollama.generate(model=llm, prompt='''who is Donald Obama?''', stream=True)
    for chunk in stream:
        print(chunk['response'], end='', flush=True)


if __name__=="__main__":
    start_agent()