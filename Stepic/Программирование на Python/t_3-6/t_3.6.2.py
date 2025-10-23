import requests

with open('dataset_3378_3.txt', 'r') as f:
    first_url = f.readline().strip()

base_url = "https://stepik.org/media/attachments/course67/3.6.3/"

current_url = first_url

while True:
    content = requests.get(current_url).text.strip()

    if content.startswith("We"):
        print("Найден последний файл!")
        print("Содержимое:")
        print(content)
        break
    else:
        next_filename = content
        current_url = base_url + next_filename
        print(f"Переходим к файлу: {next_filename}")

with open('result.txt', 'w') as f:
    f.write(content)