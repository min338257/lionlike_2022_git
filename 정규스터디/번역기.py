from googletrans inport Translator

translator = Translator()

sentence = input("번역을 원하는 문장을 입력해주세요 : ")
dest = input("어떤 언어로 번역을 원하시나요? : ")

result = translator.translate(sentence, dest)
detected = translator.detect(sentence)

print("===========출 력 결 과===========")
print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)
print("===============================")