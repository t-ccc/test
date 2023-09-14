from llama_cpp import Llama
from zhconv import convert

llm = Llama(model_path="D:/Downloads/chinese-llama-2-7b-16k/ggml-model-f16.gguf")
# output = llm("什麽是LlaMa？", max_tokens=1024, stop=["Q:", "\n"], echo=True)
while True:
    human = convert(input("Enter: "), 'zh-hans')
    print("waiting for response...")
    output = llm(human, max_tokens=0)
    print(output)
    print(output["choices"][0]["text"])
