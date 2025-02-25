import os
import requests

# 設定總的圖片存放資料夾名稱
base_folder = 'images'
if not os.path.exists(base_folder):
    os.makedirs(base_folder)

# 定義多個圖片網址模板，每個 {} 代表圖片編號
urls = [
    "https://ncueeclass.ncu.edu.tw/sysdata/doc/e/e3a6de88a14b638f/images/{}.jpg",
    "https://ncueeclass.ncu.edu.tw/sysdata/doc/8/857bb04345ab3a09/images/{}.jpg",
    "https://ncueeclass.ncu.edu.tw/sysdata/doc/2/23fb0755fc2b7639/images/{}.jpg",
    "https://ncueeclass.ncu.edu.tw/sysdata/doc/1/12d25e809fff992b/images/{}.jpg",
    "https://ncueeclass.ncu.edu.tw/sysdata/doc/d/d24c977fa39e2386/images/{}.jpg",
    "https://ncueeclass.ncu.edu.tw/sysdata/doc/8/8252060b3b3cac7e/images/{}.jpg"
]

# 對每個 URL 模板進行爬取，每個模板在 images 下建立一個子資料夾 (例如：group1, group2, ...)
for group_index, base_url in enumerate(urls, start=1):
    # 為每個 group 建立子資料夾
    group_folder = os.path.join(base_folder, f"group{group_index}")
    if not os.path.exists(group_folder):
        os.makedirs(group_folder)
        
    # 下載 1 ~ 80 的圖片，存放在該 group 資料夾中
    for i in range(1, 81):
        url = base_url.format(i)
        try:
            response = requests.get(url)
            response.raise_for_status()  # 若回應狀態非 200，會拋出例外
            image_path = os.path.join(group_folder, f"{i}.jpg")
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f"成功下載：group{group_index}/{i}.jpg")
        except requests.HTTPError as http_err:
            print(f"HTTP error 發生於 group{group_index}/{i}.jpg: {http_err}")
        except Exception as err:
            print(f"其他錯誤發生於 group{group_index}/{i}.jpg: {err}")
