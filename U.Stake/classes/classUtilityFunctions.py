import json
import cv2
import time
from skimage.metrics import structural_similarity as ssim
from utilityFunctions import Sleep
from classes.Capture import Capture

slotFile = 'slotdata.json'
ssDir = './U.Stake/images/screenshots/'

def pullScrapedSlots():
    slotList = []
    with open(slotFile,'r') as file:
        slotdata = json.load(file)
        for i in range(len(slotdata)):
            for j in range(len(slotdata[i])):
                slotObj = slotdata[i][j]
                print(slotObj)
                slotList.append(slotObj)
        return slotList

def getInfoFromScrapedSlots(slotInput):
    # loop over slotData
    with open(slotFile, 'r') as file:
        slotdata = json.load(file)
        for i in range(len(slotdata)):
            for j in range(len(slotdata[i])):
                if slotdata[i][j]['full'] == slotInput:
                        print(f'Done! Found: {slotdata[i][j]["full"]}')
                        return slotdata[i][j]
                else:
                        print(f'looping to find slot: {slotdata[i][j]["full"]}')
        return False

def takePicture(sb,action=False, increment=0, fileName=False, eleStr=False):
        destination = ''
        match action:
            case 'custom':
                destination = f'{ssDir}{fileName}.png'
            case 'fin':
                destination = f'{ssDir}fin.png'
            case 'tmp':
                destination = f'{ssDir}tmp.png'
            case 'increment':
                destination = f'{ssDir}screenshot{increment}.png'
            case _:
                print('no matching action for takePicture')

        if eleStr:
            elem = sb.find_element(eleStr)
            elem.screenshot(destination)
            scaleImg(sb,eleStr,destination)
        else:
            sb.save_screenshot(destination)
        return destination

def findEmbeddedCoords(sb,checkWordList):
        # click bonus
        destination = takePicture(sb=sb,action='tmp')
        # find the word "Get Bonus"'s box
        cap = Capture(imageLocation=destination,action='check end words',closingWordsList=checkWordList)
        wordBlock = cap.targetBlock['box']

        dpr = sb.execute_script('return window.devicePixelRatio')
        centerX = int(((wordBlock[0][0] + wordBlock[2][0]) / 2) / dpr)
        centerY = int(((wordBlock[0][1] + wordBlock[2][1]) / 2) / dpr)

        return (centerX,centerY)

def scaleImg(sb,eleStr,destination):
        rect = sb.execute_script(f"""
            const rect =
                document.querySelector('{eleStr}')
                .getBoundingClientRect();
            return rect;
        """)
        img = cv2.imread(destination)

        w = int(rect['width'])
        h = int(rect['height'])

        scaled = cv2.resize(img,(w, h),interpolation=cv2.INTER_AREA)
        cv2.imwrite(destination, scaled)

def compareImages(image1,image2,similarity=False):
    # Load images
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)
    # Convert to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # Compare
    score = ssim(gray1, gray2, full=True)[0]
    print('Similarity:', score)
    if similarity == False:
         similarity = .9
    if score > similarity:
        # same image
        print('same Image, screen has not changed')
        return True
    else:
        # different image
        return False
    
def checkCaptcha(sb):
        Sleep(sb,5)
        captchaTag = '//h2[contains(., "Performing security verification")]'
        while True:
            if sb.is_element_present(captchaTag):
                sb.solve_captcha()
            else:
                print('captcha tag not found')
                break

def checkRegionChange(sb):
        Sleep(sb, 3)
        target = '[data-testid="modal-close"]'
        while True:
            if sb.is_element_present(target):
                sb.click(target)
            else:
                print('close btn not found')
                break

def clickDomElement(sb,selector):
    info = sb.execute_script(f"""
        const canvas = document.querySelector('{selector}');
        const rect = canvas.getBoundingClientRect();
        info = {{
            x: rect.x,
            y: rect.y,
            width: rect.width,
            height: rect.height,
            internalWidth: canvas.width,
            internalHeight: canvas.height
        }};
        const xVal = info.width * .5 + info.x
        const yVal = info.height * .65 + info.y
        // hover
        canvas.dispatchEvent(new PointerEvent('pointermove', {{
            clientX: xVal,
            clientY: yVal,
            bubbles: true
        }}));

        // click sequence
        canvas.dispatchEvent(new PointerEvent('pointerdown', {{
            clientX: xVal,
            clientY: yVal,
            bubbles: true
        }}));

        canvas.dispatchEvent(new PointerEvent('pointerup', {{
            clientX: xVal,
            clientY: yVal,
            bubbles: true
        }}));
        return info
    """)
    return info

def clickXY(sb,selector,x,y):
    sb.execute_script(f"""
        const element = document.querySelector('{selector}');
        console.log(element)
        // hover
        element.dispatchEvent(new PointerEvent('pointermove', {{
            clientX: {x},
            clientY: {y},
            bubbles: true
        }}));
        // click sequence
        element.dispatchEvent(new PointerEvent('pointerdown', {{
            clientX: {x},
            clientY: {y},
            bubbles: true
        }}));
        element.dispatchEvent(new PointerEvent('pointerup', {{
            clientX: {x},
            clientY: {y},
            bubbles: true
        }}));
    """)

def cleanNumber(numString):
    try:
        return float(
            numString\
            .replace(' ', '')\
            .replace('-','')\
            .replace('$', '')\
            .replace(',', '')\
            .replace('USD', '')\
            .replace('WIN:','')
        )
    except:
         print(f'not able to properly parse to float: {numString}')
         
def splitSlotNames(string):
        arr = string.split('-')
        publisher = ''
        slot = ''
        for i in range(len(arr)):
            match i:
                case 0:
                    publisher += arr[i]
                case 1:
                    slot += arr[i]
                case _:
                    slot += f' {arr[i]}'
        return (publisher, slot)

