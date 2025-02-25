import os
from PIL import Image

# 設定總的圖片資料夾與 PDF 輸出資料夾名稱
images_base_folder = 'images'
pdf_folder = 'pdf'
if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)

# 取得 images 資料夾中所有子資料夾（假設名稱為 group1, group2, ...）
group_folders = [d for d in os.listdir(images_base_folder) if os.path.isdir(os.path.join(images_base_folder, d))]
group_folders.sort()  # 預設 group1, group2, ... 順序正確

# 對每一個子資料夾產生一份 PDF
for idx, group in enumerate(group_folders, start=1):
    group_path = os.path.join(images_base_folder, group)
    # 取得該子資料夾中所有 jpg 檔案，並依檔名數字排序
    image_files = [f for f in os.listdir(group_path) if f.lower().endswith('.jpg')]
    image_files.sort(key=lambda x: int(os.path.splitext(x)[0]))
    
    images = []
    for filename in image_files:
        img_path = os.path.join(group_path, filename)
        try:
            img = Image.open(img_path).convert('RGB')
            images.append(img)
        except Exception as e:
            print(f"讀取 {img_path} 時發生錯誤: {e}")

    # 若有圖片則產生 PDF
    if images:
        pdf_path = os.path.join(pdf_folder, f"ch{idx}.pdf")
        images[0].save(pdf_path, save_all=True, append_images=images[1:])
        print(f"成功產生 PDF：{pdf_path}")
    else:
        print(f"子資料夾 {group_path} 中找不到圖片")
