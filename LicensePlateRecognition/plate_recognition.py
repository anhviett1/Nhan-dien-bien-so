import cv2
import pytesseract

def detect_licence_plate(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray,11,17,17)
    edegd = cv2.Canny(gray, 30, 200)

    contours,_ = cv2.findContours(edegd.coppy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, revverse = True )[:10]

    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.018 * peri, True)
        if len(approx) == 4:
            x,y,w,h = cv2.boundingRect(contour)
            licence_plate = image[y:y+h, x:x+w]
            break
        else:
            return None
    text = pytesseract.image_to_string(licence_plate, config= '--psm 8')
    return text.strip()



