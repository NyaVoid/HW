def custom_write(file_name, strings):
    with open(file_name, 'w+', encoding='utf-8') as f:
        score = 0
        string_pos = {}
        for el in strings:
            score += 1
            f.write(el + '\n')
            string_pos.update({(score, f.tell()): el})
        return string_pos
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']
result = custom_write('nya.txt', info)
for elem in result.items():
  print(elem)