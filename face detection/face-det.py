{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8f7ff7b8",
   "metadata": {},
   "source": [
    "تشخیص چهره"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ee2abbe5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "\n",
    "# خواندن تصویر و تبدیل آن به تصویر خاکستری\n",
    "image = cv2.imread('12.jpg')\n",
    "gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "# ساخت یک شیء CascadeClassifier برای تشخیص چهره\n",
    "face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')\n",
    "\n",
    "# تشخیص چهره‌ها در تصویر\n",
    "faces = face_cascade.detectMultiScale(gray_image, scaleFactor= 1.3, minNeighbors=5, minSize=(30, 30))\n",
    "\n",
    "# نمایش مربع‌های تشخیص داده شده بر روی تصویر اصلی\n",
    "for (x, y, w, h) in faces:\n",
    "    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)\n",
    "\n",
    "# نمایش تصویر با مربع‌های تشخیص داده شده\n",
    "cv2.imshow('Detected Faces', image)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2f2c4b2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "\n",
    "# خواندن تصویر و تبدیل آن به تصویر خاکستری\n",
    "image = cv2.imread('11.jpg')\n",
    "gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "# ساخت یک شیء CascadeClassifier برای تشخیص چهره\n",
    "face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')\n",
    "\n",
    "# تنظیمات تشخیص\n",
    "scale_factor = 1.3  # فاصله بین مقادیر 1 تا 2 - مقدار بزرگتر تعداد کمتری از چهره‌ها را تشخیص می‌دهد.\n",
    "min_neighbors = 5  # تعداد حداقل همسایه‌ها برای تشخیص چهره‌ها\n",
    "min_face_size = (30, 30)  # حداقل اندازه چهره‌ها\n",
    "\n",
    "# تشخیص چهره‌ها در تصویر\n",
    "faces = face_cascade.detectMultiScale(gray_image, scaleFactor=scale_factor, minNeighbors=min_neighbors, minSize=min_face_size)\n",
    "\n",
    "# نمایش مربع‌های تشخیص داده شده بر روی تصویر اصلی\n",
    "for (x, y, w, h) in faces:\n",
    "    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)\n",
    "\n",
    "# نمایش تصویر با مربع‌های تشخیص داده شده\n",
    "cv2.imshow('Detected Faces', image)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46a4f4be",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8d226ee2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
