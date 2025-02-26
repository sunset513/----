**README.md**

```markdown
# 圖片爬蟲與 PDF 產生工具

此專案包含兩個主要功能：
1. **圖片爬蟲**：依據多個 URL 模板，自動爬取指定範圍內的圖片，並依不同 URL 模板建立獨立的子資料夾儲存圖片。
2. **PDF 產生**：讀取各子資料夾中的圖片，將每組圖片依照數字排序合併成一份 PDF，並依序命名為 `ch1.pdf`, `ch2.pdf`, … 等，存放於 `pdf` 資料夾中。

## 專案架構

```
.
├── images/               # 下載圖片的資料夾，每個 URL 模板對應一個子資料夾 (group1, group2, …)
├── pdf/                  # 產生的 PDF 檔案儲存資料夾
├── crawler.py            # 圖片爬蟲程式，負責依 URL 模板下載圖片 (1~80)
├── pdf_generator.py      # PDF 產生程式，負責將各子資料夾內的圖片合併成 PDF
├── README.md             # 專案說明文件
└── requirements.txt      # 所需 Python 套件
```

## 使用方式
建立虛擬環境
在專案目錄下執行以下命令（此處範例虛擬環境名稱為 venv）：

```bash
python -m venv venv
```

啟動虛擬環境
Windows:
```bash
venv\Scripts\activate
```

macOS / Linux:
```bash
source venv/bin/activate
```

安裝相依套件  
虛擬環境啟動後，執行以下命令安裝 requirements.txt 中的套件：

```bash
pip install -r requirements.txt
```
   安裝所需套件：
   ```bash
   pip install -r requirements.txt
   ```

2. **下載圖片**  
   執行 `crawler.py`，爬取各個 URL 模板的圖片，圖片將依序存放於 `images` 資料夾下的各個子資料夾中。
   ```bash
   python crawler.py
   ```

3. **產生 PDF**  
   執行 `pdf_generator.py`，程式將讀取 `images` 中的子資料夾圖片，並依序合併成 PDF，存放於 `pdf` 資料夾中。
   ```bash
   python pdf_generator.py
   ```

## 注意事項
- 請確認網路連線正常，否則下載圖片可能會失敗。
- 如需更改圖片來源或下載範圍，可修改程式中的 URL 模板或迴圈數值。

## 作者
sunset513 
by gpt-o3-mini