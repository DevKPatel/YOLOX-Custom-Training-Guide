import os

def get_file_name(im_ann):
    return im_ann.get("file_name", None) or os.path.basename(im_ann.get("coco_url", ""))

# Test cases
test_cases = [
    {"file_name": "image1.jpg", "coco_url": 'http://images.cocodataset.org/val2017/000000397133.jpg'},  # Should return "image1.jpg"
    {"coco_url": 'http://images.cocodataset.org/val2017/000000397133.jpg'},  # Should return "image2.jpg"
    {"file_name": "image3.png"},  # Should return "image3.png"
    {},  # Should return an empty string
]

# Run tests
for i, test in enumerate(test_cases):
    print(f"Test {i+1}: {get_file_name(test)}")
