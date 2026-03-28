# 📁 File Arranger App (Streamlit)

A simple and interactive **Streamlit web app** that allows you to upload `.jpg` images and automatically organize them into a folder with renamed filenames.

---

## 🚀 Features

* 📤 Upload multiple `.jpg` images
* 📂 Automatically creates an `images/` folder
* 🔄 Renames files in sequence (`photo-1.jpg`, `photo-2.jpg`, ...)
* 🎯 One-click arrangement using a button
* 📋 Displays arranged file names

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit 🎈
* OS Module (file handling)

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/file-arranger-app.git
cd file-arranger-app
```

2. Install dependencies:

```bash
pip install streamlit
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Upload multiple `.jpg` files using the UI
2. Files are saved locally in the current directory
3. Click on **"Arrange Files"**
4. The app:

   * Filters `.jpg` files
   * Creates an `images/` folder (if not exists)
   * Moves and renames files into that folder

---

## 📁 Output Example

```
images/
 ├── photo-1.jpg
 ├── photo-2.jpg
 ├── photo-3.jpg
```

---

## ⚠️ Notes

* Only `.jpg` files are supported currently
* Files are renamed sequentially (existing files may be overwritten)
* Runs locally on your system

---

## 🔮 Future Improvements

* Support for multiple file types (`.png`, `.jpeg`)
* Image preview before arranging
* Custom naming option
* Download arranged files as ZIP

---

## 🙌 Contributing

Feel free to fork this repo and improve it. Pull requests are welcome!

---

## 📄 License

This project is open-source and free to use.

---

⭐ If you like this project, consider giving it a star!
