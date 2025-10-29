import os

def generate_sidebar(base_dir='.'):
    sidebar_lines = ["* [🏠 Головна](/README.md)\n"]

    for root, dirs, files in os.walk(base_dir):
        # Пропускаємо приховані папки та службові директорії
        if root.startswith('./.') or root.startswith('.git'):
            continue

        if root == '.':
            continue

        level = root.count(os.sep)
        folder_name = os.path.basename(root)
        indent = '  ' * (level - 1)
        sidebar_lines.append(f"{indent}* **{folder_name}**\n")

        for file in sorted(files):
            if file.endswith('.md'):
                file_path = os.path.join(root, file).replace('\\', '/')
                file_path = file_path.replace('./', '')  # 🔥 ось ключова зміна
                display_name = os.path.splitext(file)[0]
                sidebar_lines.append(f"{indent}  * [{display_name}]({file_path})\n")

    with open('_sidebar.md', 'w', encoding='utf-8') as f:
        f.writelines(sidebar_lines)


if __name__ == '__main__':
    generate_sidebar()
