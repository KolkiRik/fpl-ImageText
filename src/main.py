from modules.loader import load_image
from modules.reader import Reader
from modules.printer import render_text
from modules.cropper import get_image_text_fragment
from modules.comparator import glyph_similarity

def main():
    """
    Тест прототипа проекта по считыванию текста с изображения
    """

    test_paths = ["data/test_four_lines.jpg", "data/test_hello.png",
                  "data/test_hello_eng.png", "data/test_three_lines_eng.png"]

    print("Загрузка модели (EasyOCR)")
    reader = Reader()

    for image_path in test_paths:

        print(f"Загружаем тестовое изображение: {image_path}")
        image = load_image(image_path)
        print(f"Размер тестового изображения: {image.shape}")

        print("Распознание текста")
        blocks = reader.recognize(image=image)

        print(f"Найдено текстовых блоков: {len(blocks)}")
        for i, block in enumerate(blocks, start=1):
            width = block.box_coords[1][0] - block.box_coords[0][0]
            height = block.box_coords[2][1] - block.box_coords[1][1]
            font_print = render_text(block.text, "arial.ttf", 15, int(width), int(height))
            img_frag = get_image_text_fragment(image, block.box_coords)
            print(f"{i}: {block.text}  (уверенность: {block.confidence:.2f}) (сходство по шрифту: {glyph_similarity(img_frag, font_print)})")

        print("\n")
        print("=========")
        print("\n")

if __name__ == "__main__":
    main()
