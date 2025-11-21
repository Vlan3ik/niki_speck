import os
import shutil

# === ФАЙЛЫ И ПАПКИ, КОТОРЫЕ НАДО ПОЛНОСТЬЮ ИГНОРИРОВАТЬ ===
IGNORED_DIRS = {'gui'}  # любые папки с именем "gui" на любом уровне
IGNORED_FILES = {'options.rpy', 'screens.rpy', "gui.rpy"}  # точные имена файлов


def remove_pycache(root_dir):
    """Удаляет все __pycache__ папки"""
    for root, dirs, files in os.walk(root_dir, topdown=True):
        if '__pycache__' in dirs:
            cache_path = os.path.join(root, '__pycache__')
            shutil.rmtree(cache_path)
            print(f"Удалено: {cache_path}")
            dirs.remove('__pycache__')  # чтобы os.walk не заходил внутрь


def should_ignore_path(path):
    """Проверяет, нужно ли пропустить файл или папку"""
    filename = os.path.basename(path)
    filename = os.path.basename(path)
    parent_dir = os.path.basename(os.path.dirname(path))

    # Игнорируем папки gui и всё внутри них
    if parent_dir in IGNORED_DIRS or filename in IGNORED_DIRS:
        return True
    # Игнорируем конкретные файлы по имени в любой папке
    if filename in IGNORED_FILES:
        return True
    return False


def save_structure(root_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        _walk_and_save(root_dir, f, "")


def _walk_and_save(current_path, file_handle, prefix):
    """Рекурсивно обходит директории с нужной фильтрацией"""
    try:
        items = os.listdir(current_path)
    except PermissionError:
        return

    # Сортируем для стабильного порядка
    items.sort()

    for item in items:
        item_path = os.path.join(current_path, item)

        # Полное игнорирование запрещённых путей
        if should_ignore_path(item_path):
            print(f"Пропущено (игнор): {item_path}")
            continue

        # Пропускаем .git
        if item == '.git':
            continue

        # Всегда пишем путь в структуру (кроме игнорируемых)
        file_handle.write(f"{item_path}\n")

        if os.path.isdir(item_path):
            _walk_and_save(item_path, file_handle, prefix + "    ")
        else:
            # Обрабатываем только нужные типы файлов
            if item.endswith(('.py', '.rpy', '.html', '.css', "md")):
                save_content(item_path, file_handle)
            elif item.endswith('.png'):
                file_handle.write(f"    └── [PNG изображение] {item} (бинарный файл, содержимое не копируется)\n")


def save_content(file_path, output_file):
    """Сохраняет содержимое текстового файла (.py, .rpy и т.д.)"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        output_file.write(f"\n{file_path} — содержимое:\n")
        output_file.write(content)
        output_file.write("\n\n" + "="*80 + "\n\n")
    except UnicodeDecodeError:
        output_file.write(f"\n{file_path} — содержимое: (не удалось прочитать как текст, возможно бинарник)\n\n")
    except Exception as e:
        output_file.write(f"\n{file_path} — ошибка чтения: {e}\n\n")


# === ЗАПУСК ===
if __name__ == "__main__":
    root_directory = r'C:\Users\user\Documents\GitHub\niki_speck'
    
    print("Удаляем __pycache__...")
    remove_pycache(root_directory)
    
    output_file_path = os.path.join(root_directory, 'project_structure.txt')
    
    print("Сканируем проект (с фильтрами)...")
    save_structure(root_directory, output_file_path)
    
    print(f"\nГотово! Структура сохранена в:\n{output_file_path}")
    print("Игнорировались: папки gui, options.rpy, screens.rpy")