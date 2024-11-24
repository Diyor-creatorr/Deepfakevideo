# Gerekli kütüphaneleri import etme
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import models, transforms
import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk


#  (ResNet50)
class DeepfakeDetector(nn.Module):
    def __init__(self):
        super(DeepfakeDetector, self).__init__()
        # ResNet50 kullanımı
        self.base_model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
        self.base_model.fc = nn.Linear(self.base_model.fc.in_features, 2)  # 2 class: gerçek vs sahte

    def forward(self, x):
        return self.base_model(x)


def extract_frames(self, video_path):
    # Dosya yolunun geçerli olup olmadığını kontrol etme
    if not os.path.exists(video_path):
        raise ValueError(f"Geçersiz dosya yolu: {video_path}")

    # Video açma
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError(f"Video dosyası açılamadı: {video_path}")

    frames = []
    frame_interval = 10  # Her 10. çerçeveyi alıyoruz.

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if len(frames) % frame_interval == 0:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (224, 224))
            frames.append(frame)

    cap.release()
    return frames

# Veri seti sınıfı (DeepfakeVideoDataset)
class DeepfakeVideoDataset(Dataset):
    def __init__(self, video_paths, labels, transform=None):
        self.video_paths = video_paths
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.video_paths)

    def __getitem__(self, idx):
        video_path = self.video_paths[idx]
        label = self.labels[idx]

        frames = self.extract_frames(video_path)  # Videoyu karelere ayırma
        if self.transform:
            frames = [self.transform(frame) for frame in frames]
            frames = torch.stack(frames, dim=0)

        return frames, label

    def extract_frames(self, video_path):
        cap = cv2.VideoCapture(video_path)
        frames = []
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (224, 224))
            frames.append(frame)
        cap.release()
        return frames


# Video dosyasını işleme ve analiz etme fonksiyonu
def analyze_video_with_accuracy(video_path, model, device):
    # Dosya yolunun geçerli olup olmadığını kontrol etme
    if not os.path.exists(video_path):
        raise ValueError(f"Geçersiz dosya yolu: {video_path}")

    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_interval = 10  # Her 10. çerçeveyi alıyoruz.

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if len(frames) % frame_interval == 0:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (224, 224))
            frames.append(frame)

    cap.release()

    frames = np.array(frames)
    frames = [transform(frame) for frame in frames]
    frames = torch.stack(frames, dim=0)

    frames = frames.to(device)

    with torch.no_grad():  # Tahmin sırasında grad hesaplamasını devre dışı bırakıyoruz.
        outputs = model(frames)
    _, predicted = torch.max(outputs, 1)

    # Accuracy hesaplama (örnek etiketlerle)
    true_labels = [1 if i % 2 == 0 else 0 for i in range(len(frames))]  # Örnek: Çiftler gerçek, tekler sahte.
    true_labels = torch.tensor(true_labels, device=device)
    accuracy = (predicted == true_labels).float().mean().item()

    # Sonuç formatı
    result = "Real" if predicted[0].item() == 1 else "Fake"
    return result, accuracy


# Tkinter GUI oluşturma
class DeepfakeApp:
    def __init__(self, root, model, device):
        self.root = root
        self.root.title("Deepfake Detection")
        self.model = model
        self.device = device

        self.upload_button = tk.Button(root, text="Video Yükle", command=self.upload_video)
        self.upload_button.pack(pady=20)

        self.detect_button = tk.Button(root, text="Tıkla ve Tespit Et", command=self.detect_video, state=tk.DISABLED)
        self.detect_button.pack(pady=20)

        self.train_button = tk.Button(root, text="Modeli Eğit", command=self.train_model)
        self.train_button.pack(pady=20)

        self.video_label = tk.Label(root)
        self.video_label.pack()

        self.result_label = tk.Label(root, text="Sonuç: ", font=('Helvetica', 14))
        self.result_label.pack(pady=20)

        self.video_path = None

    def upload_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
        if self.video_path:
            self.detect_button.config(state=tk.NORMAL)
            self.show_video_frame(self.video_path)

    def show_video_frame(self, video_path):
        cap = cv2.VideoCapture(video_path)
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (224, 224))
            image = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image)
            self.video_label.config(image=photo)
            self.video_label.image = photo
        cap.release()

    def detect_video(self):
        if not self.video_path:
            messagebox.showerror("Hata", "Lütfen bir video yükleyin.")
            return

        result, accuracy = analyze_video_with_accuracy(self.video_path, self.model, self.device)

        if result == "Real":
            self.result_label.config(text=f"Sonuç: {result}\nAccuracy: {accuracy:.2f}", fg="green")
        else:
            self.result_label.config(text=f"Sonuç: {result}\nAccuracy: {accuracy:.2f}", fg="red")

    def train_model(self):
        # Eğitim için video yolları ve etiketler
        video_paths = ['Видео WhatsApp 2024-11-10 в 18.19.22_5e53642f.mp4', 'dc1b9097.mp4', ...]  # Gerçek ve sahte videoların yolları
        labels = [0, 1, 0, ...]  # 0: Gerçek, 1: Sahte etiketler

        # Eğitim için veri seti
        transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        train_dataset = DeepfakeVideoDataset(video_paths, labels, transform=transform)
        train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)

        # Modeli, loss fonksiyonunu ve optimizer'ı başlatma
        model = DeepfakeDetector().to(self.device)
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=0.0001)

        # Eğitim döngüsü
        for epoch in range(10):  # 10 epoch örnek
            model.train()
            running_loss = 0.0
            for inputs, targets in train_loader:
                inputs, targets = inputs.to(self.device), targets.to(self.device)

                optimizer.zero_grad()

                outputs = model(inputs)
                loss = criterion(outputs, targets)
                loss.backward()
                optimizer.step()

                running_loss += loss.item()

            print(f"Epoch [{epoch + 1}/10], Loss: {running_loss / len(train_loader)}")

        # Modeli kaydetme
        torch.save(model.state_dict(), 'deepfake_detector.pth')
        messagebox.showinfo("Eğitim Tamamlandı", "Model başarıyla eğitildi ve kaydedildi.")


# Modeli ve cihazı hazırlama
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = DeepfakeDetector().to(device)

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # ResNet için normalize
])

# Tkinter Arayüzü
root = tk.Tk()
app = DeepfakeApp(root, model, device)
root.mainloop()
