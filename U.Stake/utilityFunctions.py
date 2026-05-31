from random import randint
import numpy as np
import json

# image1 = './U.Stake/images/screenshot1.png'
# image2 = './U.Stake/images/screenshot2.png'
slotFile = 'slotdata.json'

def SaveFile(location,list):
    
    with open(location,'w',encoding= 'utf-8') as f:
         json.dump(list, f, indent=4)

def LoadFile(location):
    with open(location, "r", encoding="utf-8") as f:
        return json.load(f)

def Sleep(sb, number = False):
    num = 0
    if number:
        num = number
    else:
        num = randint(1,1)
    print(f'Sleeping: {num}')
    sb.sleep(num)

def GetRandomNumber(max):
    randNum = randint(0,max)
    print(f'randNum: {randNum}')
    return randNum

def MarkTheDom(sb,xVal, yVal):
    sb.execute_script(f"""
        const marker = document.createElement('div');
        marker.style.position = 'fixed';
        marker.style.left = '{xVal}px';
        marker.style.top = '{yVal}px';
        marker.style.width = '20px';
        marker.style.height = '20px';
        marker.style.background = 'lime';
        marker.style.border = '2px solid black';
        marker.style.borderRadius = '50%';
        marker.style.zIndex = '999999';

        document.body.appendChild(marker);
    """)

def ClickTheDom(sb,xVal,yVal):
    sb.driver.execute_cdp_cmd(
        'Input.dispatchMouseEvent',
        {
            'type': 'mouseMoved',
            'x': xVal,
            'y': yVal,
            'button': 'none'
        }
    )
    sb.driver.execute_cdp_cmd(
        'Input.dispatchMouseEvent',
        {
            'type': 'mousePressed',
            'x': xVal,
            'y': yVal,
            'button': 'left',
            'clickCount': 1
        }
    )
    sb.driver.execute_cdp_cmd(
        'Input.dispatchMouseEvent',
        {
            'type': 'mouseReleased',
            'x': xVal,
            'y': yVal,
            'button': 'left',
            'clickCount': 1
        }
    )

# def LoadMore(sb):
#     # Click the "load more" button to load more slots
#     isThere = True
#     count = 0
#     loadMoreElement = '.load-more-container button'
    
#     while isThere:
#         # make sure button loads
#         Sleep(sb)
#         # see if "load more" button is still at the bottom of the list
#         if sb.is_element_present(loadMoreElement):
#             print('found load more button')
#             sb.click(loadMoreElement)
#             count += 1
#         else:
#             print('load more btn not found')
#             isThere = False
        
#         print(count)


# def CycleProvidersList(sb):
#     fullSlotList = []
#     providersBtnStr = '//div[contains(@class, "main-content")]//button[.//span[normalize-space()="Publishers"]]'
#     providerString = '.provider-list > div > label > span:nth-of-type(2) > p > div > span'
    
#     Sleep(sb)
#     # click providers
#     sb.click(providersBtnStr)
#     # get count of elements to use index to loop over
#     count = len(sb.find_elements(providerString)) -1
#     manualPopularCount = 14
#     print(f'count of providers: {count}')

#     for i in range(count):
#         # target only slots after popular ones
#         if i < manualPopularCount:
#             continue
#         # refind elements (needed)
#         providers = checkRefresh(sb,providerString)
#         print(providers[i].text)
#         # click provider
#         providers[i].click()
#         # unselect provider bar
#         sb.click(providersBtnStr)
#         # get provider slot list
#         providerSlotList = GetSlotList(sb)
#         fullSlotList.append(providerSlotList)
#         # reopen provider bar
#         sb.click(providersBtnStr)
#         # refind elements (needed)
#         providers = sb.find_elements(providerString)
#         # unclick added provider
#         checkBuggedProviders(sb,providers)
#         providers[i].click()
#     # add indexes
#     returnSlotList = addIndexes(fullSlotList)
#     SaveFile(returnSlotList)

# def checkBuggedProviders(sb,providers):
#     pass
#     captchaString = '#main-wrapper > #content > #verifying'
#     # while len(providers == 0):
#     # refresh page and 
#     # if captcha, solve
#     # if redirect, close
#     # find providers again

# def GetSlotList(sb):
#     slotObjList = []
#     LoadMore(sb)
#     # select the icons
#     availableIdList = checkAvailable(sb)
#     # break out if no slots available
#     if availableIdList == None:
#         return
#     # slotElements = sb.find_elements('.game-card-wrap > .link > .img-wrap > img')
#     for id in availableIdList:
#         splitNames = splitSlotNames(id)
#         slotElementObj = {
#             'name': splitNames[1], 
#             'creator': splitNames[0],
#             'full': id
#         }
#         slotObjList.append(slotElementObj)
#     print('finished provider')    
#     return slotObjList

# def checkAvailable(sb):
#     idList = []
#     parentElement = sb.find_elements('.game-card-wrap > .link > .img-wrap')
#     #slotElements = sb.find_elements('.game-card-wrap > .link > .img-wrap > img')
#     #notAvailable = sb.find_elements('.game-card-wrap > .link > .img-wrap > .overlay-text > span:nth-of-type(2)')
#     # loop over parent element
#     for element in parentElement:
#         try:
#             if element.children[3].children[4].text == 'Not available in your region':
#                 continue
#         except:
#             idList.append(element.children[0].id)
#         # random empty comments might mess up this 
#     if len(idList) > 0:
#         return idList
#     else:
#         return

# def checkRefresh(sb,providerString):
#     providers = sb.find_elements(providerString)
#     while len(providers) < 3:
#         providers = sb.find_elements(providerString)
#         # refresh page
#         sb.refresh_page()
#     return providers

# def splitSlotNames(string):
#     arr = string.split('-')
#     publisher = ''
#     slot = ''
#     for i in range(len(arr)):
#         match i:
#             case 0:
#                 publisher += arr[i]
#             case 1:
#                 slot += arr[i]
#             case _:
#                 slot += f' {arr[i]}'

#     return (publisher, slot)

# def addIndexes(slotsList):
#     for i in range(len(slotsList)):
#         for j in range(len(slotsList[i])):
#             slotsList[i][j]['index1'] = i
#             slotsList[i][j]['index2'] = j
#     return slotsList

# def compareImages(image1,image2):
#     # Load images
#     img1 = cv2.imread(image1)
#     img2 = cv2.imread(image2)
#     # Convert to grayscale
#     gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#     gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
#     # Compare
#     score = ssim(gray1, gray2, full=True)[0]
#     print("Similarity:", score)
#     if score > .8:
#         # same image
#         print('same Image, screen has not changed')
#         return True
#     else:
#         # different image
#         return False
    
# def splashScreen(WebInstance,Capture):
#     # screenshot
#     WebInstance.takePicture()
#     # find words
#     Capture.extractText()
#     # print(Capture.textBlocks) # return a list?
#     allFoundWords = Capture.textBlocks
#     for obj in range(len(allFoundWords)):
#         Capture.selectClickTarget()
#         # try clicking on words
#         WebInstance.tryClickAt(Capture.clickTarget)
#         # take screenshot 2
#         WebInstance.takePicture(2)
#         # compare both screenshots with scikit-image opencv-python
#         sameImage = compareImages()
#         if sameImage == True:
#             # remove that click option and try again

#             continue
#         else:
#             break

def keepAlive():
    input("Press ENTER to close...")