import cv2
import matplotlib.pyplot as plt

# Sample data
data = {
    "images": {"id": 0, "license": 1, "file_name": "463102759_27509703481953955_8388613840416143508_n_jpg.rf.0502018f00c4b0bbfd563af0fb934d7c.jpg", "height": 640, "width": 640, "date_captured": "2024-12-10T16:31:58+00:00"},
    "annotations": {"id": 0, "image_id": 0, "category_id": 3, "bbox": [176, 248, 174, 204], "area": 35496, "segmentation": [], "iscrowd": 0},
    "categories": {"id": 0, "name": "doll2", "supercategory": "none"}
}

# Load the image
image_path = data["images"]["file_name"]
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Extract bounding box details
bbox = data["annotations"]["bbox"]
x, y, w, h = bbox

# Draw bounding box
cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue box with thickness 2
cv2.putText(image, data["categories"]["name"], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Display image
plt.figure(figsize=(6,6))
plt.imshow(image)
plt.axis("off")
plt.show()
