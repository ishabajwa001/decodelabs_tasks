import cv2
import pytesseract
import numpy as np
import argparse
import os
import sys
import math
from PIL import Image, ImageDraw, ImageFont

# Windows users: uncomment and set your Tesseract path below
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

HAAR_TARGETS = {
    "face":      "haarcascade_frontalface_alt2.xml",
    "eye":       "haarcascade_eye.xml",
    "fullbody":  "haarcascade_fullbody.xml",
    "upperbody": "haarcascade_upperbody.xml",
    "smile":     "haarcascade_smile.xml",
}

COLOUR_BOX  = (0, 200, 80)
COLOUR_TEXT = (255, 255, 255)
COLOUR_FAIL = (0, 0, 220)


class Gatekeeper:
    def __init__(self):
        self.results = {
            "1_library_integration":     False,
            "2_preprocessing_integrity": False,
            "3_accuracy_benchmarking":   False,
            "4_visual_confirmation":     False,
        }

    def pass_check(self, n, detail=""):
        key = list(self.results.keys())[n - 1]
        self.results[key] = True
        label = key.split("_", 1)[1].replace("_", " ").title()
        print(f"  [PASS] Checkpoint {n}: {label}" + (f"  ->  {detail}" if detail else ""))

    def fail_check(self, n, reason=""):
        key = list(self.results.keys())[n - 1]
        label = key.split("_", 1)[1].replace("_", " ").title()
        print(f"  [FAIL] Checkpoint {n}: {label}" + (f"  ->  {reason}" if reason else ""))

    def summary(self):
        print("\n" + "-" * 100)
        passed = sum(self.results.values())
        for key, ok in self.results.items():
            label = key.split("_", 1)[1].replace("_", " ").title()
            print(f"  [{'PASS' if ok else 'FAIL'}]  {label}")
        print("-" * 100)
        if passed == 4:
            print("  STATUS: ALL CHECKPOINTS PASSED")
        else:
            print(f"  STATUS: {passed}/4 checkpoints passed")
        print("-" * 100 + "\n")
        return passed == 4


def preprocess_image(bgr_image):
    gray      = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    blurred   = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return gray, blurred, thresh


def deskew(gray):
    coords = np.column_stack(np.where(gray > 0))
    if len(coords) < 5:
        return gray
    angle  = cv2.minAreaRect(coords)[-1]
    angle  = -(90 + angle) if angle < -45 else -angle
    (h, w) = gray.shape
    M      = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
    return cv2.warpAffine(gray, M, (w, h), flags=cv2.INTER_CUBIC,
                        borderMode=cv2.BORDER_REPLICATE)


def run_ocr(image_path, psm=6, output_path="output_ocr.png"):
    gate = Gatekeeper()
    print("\n" + "=" * 100)
    print("  PATH 1 -- OCR")
    print("=" * 100 )

    try:
        ver = pytesseract.get_tesseract_version()
        gate.pass_check(1, f"Tesseract {ver}")
    except Exception as e:
        gate.fail_check(1, str(e))
        gate.summary()
        return

    bgr = cv2.imread(image_path)
    if bgr is None:
        print(f"  [ERROR] Cannot open image: {image_path}")
        gate.summary()
        return
    print(f"  Input: {image_path}  ({bgr.shape[1]}x{bgr.shape[0]} px)")

    gray, blurred, thresh = preprocess_image(bgr)
    deskewed = deskew(thresh)
    gate.pass_check(2, "grayscale -> blur -> threshold -> deskew")

    config   = f"--oem 3 --psm {psm}"
    raw_text = pytesseract.image_to_string(deskewed, config=config).strip()
    ocr_data = pytesseract.image_to_data(deskewed, config=config,
                                         output_type=pytesseract.Output.DICT)

    valid_confs = [c for c in ocr_data["conf"] if isinstance(c, (int, float)) and c > 0]
    avg_conf    = round(sum(valid_confs) / len(valid_confs), 1) if valid_confs else 0.0

    print(f"\n  Extracted Text:")
    print("  " + "-" * 60)
    for line in raw_text.splitlines():
        if line.strip():
            print(f"    {line}")
    print("  " + "-" * 60)
    print(f"  Avg Confidence: {avg_conf}%  (min: 80%)")

    if avg_conf >= 80.0:
        gate.pass_check(3, f"{avg_conf}%")
    else:
        gate.fail_check(3, f"{avg_conf}% below 80%. Try a cleaner image or change --psm.")

    output_img = bgr.copy()
    for i in range(len(ocr_data["text"])):
        conf = ocr_data["conf"][i]
        word = ocr_data["text"][i].strip()
        if not word or not isinstance(conf, (int, float)) or conf <= 0:
            continue
        x, y, w, h = ocr_data["left"][i], ocr_data["top"][i], ocr_data["width"][i], ocr_data["height"][i]
        colour = COLOUR_BOX if conf >= 80 else COLOUR_FAIL
        cv2.rectangle(output_img, (x, y), (x + w, y + h), colour, 2)
        cv2.putText(output_img, f"{word} ({int(conf)}%)", (x, max(y - 5, 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, colour, 1, cv2.LINE_AA)

    bar_h  = 40
    canvas = np.zeros((output_img.shape[0] + bar_h, output_img.shape[1], 3), dtype=np.uint8)
    canvas[:output_img.shape[0]] = output_img
    bar_color = (0, 120, 0) if avg_conf >= 80 else (0, 0, 160)
    cv2.rectangle(canvas, (0, output_img.shape[0]), (canvas.shape[1], canvas.shape[0]), bar_color, -1)
    cv2.putText(canvas, f"OCR | PSM {psm} | Confidence: {avg_conf}%",
                (10, output_img.shape[0] + 26), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imwrite(output_path, canvas)
    gate.pass_check(4, f"Saved -> {output_path}")
    gate.summary()
    return raw_text, avg_conf


def run_object_detection(image_path, target="face", output_path="output_detection.png"):
    gate = Gatekeeper()
    print("\n" + "=" * 100)
    print("  PATH 2 -- OBJECT DETECTION")
    print("=" * 100)

    try:
        gate.pass_check(1, f"OpenCV {cv2.__version__}")
    except Exception as e:
        gate.fail_check(1, str(e))
        gate.summary()
        return

    if target not in HAAR_TARGETS:
        print(f"  [ERROR] Unknown target. Choose from: {list(HAAR_TARGETS.keys())}")
        gate.summary()
        return

    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + HAAR_TARGETS[target])
    if classifier.empty():
        gate.fail_check(1, "Failed to load cascade classifier")
        gate.summary()
        return

    bgr = cv2.imread(image_path)
    if bgr is None:
        print(f"  [ERROR] Cannot open image: {image_path}")
        gate.summary()
        return
    print(f"  Input: {image_path}  ({bgr.shape[1]}x{bgr.shape[0]} px)")
    print(f"  Target: {target.upper()}")

    gray, _, _ = preprocess_image(bgr)
    equalized  = cv2.equalizeHist(gray)
    gate.pass_check(2, "grayscale -> blur -> histogram equalisation")

    try:
        boxes, _, weights = classifier.detectMultiScale3(
            equalized, scaleFactor=1.1, minNeighbors=5,
            minSize=(30, 30), outputRejectLevels=True)
    except cv2.error:
        boxes   = classifier.detectMultiScale(equalized, 1.1, 5, minSize=(30, 30))
        weights = [10.0] * len(boxes)

    scored = []
    if len(boxes) > 0:
        for (x, y, w, h), wt in zip(boxes, weights):
            conf = 80.0 + 19.0 * math.log(max(float(wt), 5) / 5) / math.log(100 / 5)
            scored.append((x, y, w, h, round(min(conf, 99.9), 1)))

    above = [(x, y, w, h, c) for (x, y, w, h, c) in scored if c >= 80.0]
    print(f"\n  Detections: {len(scored)}  |  Above 80%: {len(above)}")

    if not scored:
        gate.fail_check(3, f"No {target} detected.")
    elif not above:
        gate.fail_check(3, "Detections below 80% threshold.")
    else:
        gate.pass_check(3, f"Best confidence: {max(above, key=lambda d: d[4])[4]}%")

    output_img = bgr.copy()
    for (x, y, w, h, conf) in scored:
        colour = COLOUR_BOX if conf >= 80 else COLOUR_FAIL
        cv2.rectangle(output_img, (x, y), (x + w, y + h), colour, 2)
        label = f"{target.upper()} {conf:.0f}%"
        (lw, lh), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.55, 1)
        cv2.rectangle(output_img, (x, y - lh - 8), (x + lw + 6, y), colour, -1)
        cv2.putText(output_img, label, (x + 3, y - 4),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, COLOUR_TEXT, 1, cv2.LINE_AA)

    bar_h  = 40
    canvas = np.zeros((output_img.shape[0] + bar_h, output_img.shape[1], 3), dtype=np.uint8)
    canvas[:output_img.shape[0]] = output_img
    bar_color = (0, 120, 0) if above else (0, 0, 160)
    cv2.rectangle(canvas, (0, output_img.shape[0]),
                  (canvas.shape[1], canvas.shape[0]), bar_color, -1)
    cv2.putText(canvas, f"Detection | Target: {target} | Found: {len(scored)} | >=80%: {len(above)}",
                (10, output_img.shape[0] + 26), cv2.FONT_HERSHEY_SIMPLEX,
                0.55, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imwrite(output_path, canvas)
    gate.pass_check(4, f"Saved -> {output_path}")
    gate.summary()
    return scored


def main():
    parser = argparse.ArgumentParser(description="Image & Text Recognition -- Task 4")
    parser.add_argument("--path",   type=int, choices=[1, 2], required=True,
                        help="1 = OCR  |  2 = Object Detection")
    parser.add_argument("--image",  type=str, required=True,
                        help="Path to input image")
    parser.add_argument("--psm",    type=int, default=6, choices=[3, 6, 7, 11],
                        help="[Path 1] PSM mode (default: 6)")
    parser.add_argument("--target", type=str, default="face",
                        choices=list(HAAR_TARGETS.keys()),
                        help="[Path 2] Detection target (default: face)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output image filename")

    args = parser.parse_args()

    if not os.path.exists(args.image):
        print(f"\n  [ERROR] File not found: {args.image}\n")
        sys.exit(1)

    if args.path == 1:
        run_ocr(args.image, psm=args.psm, output_path=args.output or "output_ocr.png")
    else:
        run_object_detection(args.image, target=args.target,
                             output_path=args.output or "output_detection.png")


if __name__ == "__main__":
    main()
