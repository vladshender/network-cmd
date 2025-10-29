import os

# 🧭 Файл для запису
sidebar_path = '_sidebar.md'

def generate_sidebar():
    with open(sidebar_path, 'w', encoding='utf-8') as f:
        f.write('* [🏠 Головна](README.md)\n')
        for folder in sorted(os.listdir('.')):
            if os.path.isdir(folder) and not folder.startswith('.') and folder not in ['.git', '__pycache__']:
                f.write(f'* {folder}\n')
                for file in sorted(os.listdir(folder)):
                    if file.endswith('.md'):
                        name = os.path.splitext(file)[0]
                        f.write(f'  * [{name}]({folder}/{file})\n')

if __name__ == '__main__':
    generate_sidebar()
    print(f'✅ Сайдбар згенеровано в {sidebar_path}')
