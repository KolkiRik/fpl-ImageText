from modules.loader import load_image
from modules.reader import Reader

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
            print(f"{i}: {block.text}  (уверенность: {block.confidence:.2f})")

        print("\n")
        print("=========")
        print("\n")

if __name__ == "__main__":
    main()