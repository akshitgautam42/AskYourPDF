import openai
import json
import re

def extract_question_answer_pairs(text):
    pairs = []
    data = json.loads(text)
    for item in data:
        question = item['question']
        answer = item['answer']
        pairs.append((question, answer))
    return pairs


openai.api_key = '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'

text = "Deep in the heart of an enchanted forest, where sunlight danced through the canopies of ancient trees, a mystical creature known as the Forest Guardian resided. With emerald-green eyes and shimmering wings, the Guardian possessed the power to protect the delicate balance of nature. Each day, it would soar above the treetops, overseeing the thriving flora and fauna below.One fateful morning, as the Forest Guardian was perched upon a moss-covered branch, it noticed a disturbance in the otherwise tranquil forest. A group of lumberjacks had encroached upon its domain, axes poised to fell the majestic trees. Filled with sadness and determination, the Guardian vowed to defend its home.With a wave of its wings, the Forest Guardian summoned a gust of wind, toppling the lumberjacks' tools and forcing them to retreat. But the threat remained, for the desire for timber lingered in the hearts of others. The Guardian knew it must find a way to educate and inspire harmony between humans and nature.Thus, it embarked on a quest to spread its message far and wide. Through whispered secrets to the wind, the Guardian communicated with animals, who in turn shared its wisdom with humans. Tales of the Forest Guardian's magic and compassion began to circulate, kindling a newfound respect and reverence for the natural world.As seasons passed, the forest flourished, protected by the watchful eyes and tireless efforts of the Forest Guardian. It became a sanctuary where creatures big and small, humans and animals, lived in harmony, recognizing the interconnectedness of all life. And the legend of the Forest Guardian lived on, a symbol of hope and unity in a world that learned to treasure and preserve the gifts of nature."

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content":  """You are a smart assistant designed to help teachers come up with reading comprehension questions.
Given a piece of text, you must come up with 10 question and answer pairs that can be used to test a student's reading comprehension abilities.
When coming up with this question/answer pair, you must respond in the following format:
```
{
    "question": "$YOUR_QUESTION_HERE",
    "answer": "$THE_ANSWER_HERE"
}
```

Everything between the ``` must be valid json.
"""
         },
        {"role": "user", "content": f"""Please come up with 10 question/answer pairs, in the specified JSON format, for the following text:
----------------
{text}"""},
        
    ]
)

message_content = response["choices"][0]["message"]["content"]
print(message_content)
def extract_json_objects(text):
    json_objects = []
    start_index = 0
    while True:
        start_index = text.find('{', start_index)
        if start_index == -1:
            break
        end_index = text.find('}', start_index) + 1
        if end_index == 0:
            break
        json_str = text[start_index:end_index]
        try:
            json_obj = json.loads(json_str)
            json_objects.append(json_obj)
        except json.JSONDecodeError:
            pass
        start_index = end_index
    return json_objects

json_objects = extract_json_objects(message_content)
print(json_objects[0]['question'])
print(json_objects[0]['answer'])

# pairs = extract_question_answer_pairs(message_content)
# for i, pair in enumerate(pairs, 1):
#     print(f"Question {i}: {pair[0]}")
#     print(f"Answer {i}: {pair[1]}")
#     print()

