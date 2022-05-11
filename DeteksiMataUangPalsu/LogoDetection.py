import glob
import cv2 
import numpy as np
import imutils 
import tkinter
from tkinter import messagebox
import Main


def Logo_Detection():
    # load logo template
    logo_data = []
    logo_files = glob.glob('template/'+Main.Tamplate_lg, recursive=True)
    print("template Logo loaded:", logo_files)
    # prepare logo template
    for logo_files in logo_files:
        tmp = cv2.imread(logo_files)        
        # grayscale==========================================================
        tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Template Grayscale", tmp)                       
        # sharpening=========================================================
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])       
        tmp = cv2.filter2D(tmp, -1, kernel)
        cv2.imshow("Template Filter2D", tmp) 
        # smoothing==========================================================
        # blur===============================================================
        tmp = cv2.blur(tmp, (1, 3))  
        cv2.imshow("Template Blur", tmp)
        # Edge===============================================================        
        # with Canny=========================================================
        #tmp = cv2.Canny(tmp, 100, 220) 
        #cv2.imshow("Template Cany", tmp)       
        # with adaptiveThreshold=============================================
        tmp = cv2.adaptiveThreshold(tmp,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,5)
        cv2.imshow("Template Pembanding", tmp) 
        #===========================================================================================
        Logo = logo_files.replace('Logo\\', '').replace('.jpg', '')
        logo_data.append({"glob_logo":tmp, "Logo":Logo})

    # template matching
    for image_glob in glob.glob('test/'+Main.Image):
        for template_logo in logo_data:
            image_test_logo = cv2.imread(image_glob)
            (tmp_height, tmp_width) = template_logo['glob_logo'].shape[:2]             
            # grayscale==========================================================
            image_test_l = cv2.cvtColor(image_test_logo, cv2.COLOR_BGR2GRAY)            
            # sharpening=========================================================
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            image_test_l = cv2.filter2D(image_test_l, -1, kernel)
            # smoothing==========================================================
            # blur===============================================================
            image_test_l = cv2.blur(image_test_l, (1, 3))
            # Edge===============================================================        
            # with Canny=========================================================
            #image_test_l = cv2.Canny(image_test_l, 50, 200)
            #cv2.imshow("Step: edge with canny", image_test_l)
            # with adaptiveThreshold=============================================
            image_test_l = cv2.adaptiveThreshold(image_test_l,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,15,10)
            cv2.imshow("Image adaptiveThreshold", image_test_l)
            #===========================================================================================
            found = None
            thershold = 0.4
            for scale in np.linspace(0.2, 1.0, 20)[::-1]: 
                # scalling uang
                resized = imutils.resize(
                    image_test_l, width=int(image_test_l.shape[1] * scale))
                r = image_test_l.shape[1] / float(resized.shape[1]) 
                #cv2.imshow("Step: rescale", resized) 

                if resized.shape[0] < tmp_height or resized.shape[1] < tmp_width:
                    break

                # template matching
                result = cv2.matchTemplate(resized, template_logo['glob_logo'], cv2.TM_CCOEFF_NORMED)
                (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
                if found is None or maxVal > found[0]:
                    found = (maxVal, maxLoc, r)
                    if maxVal >= thershold: 
                        #print("money:", template['uang'], "detected")
                        root = tkinter.Tk()
                        root.withdraw()
                        messagebox.showinfo(template_logo['Logo'], "Detected") 
                                    

                if found is not None: 
                    (maxVal, maxLoc, r) = found
                    (startX, startY) = (int(maxLoc[0]*r), int(maxLoc[1] * r))
                    (endX, endY) = (
                        int((maxLoc[0] + tmp_width) * r), int((maxLoc[1] + tmp_height) * r))
                    if maxVal >= thershold:
                        cv2.rectangle(image_test_logo, (startX, startY),
                                    (endX, endY), (0, 0, 255), 2)
                        
                
                    cv2.imshow("Result", image_test_logo)

            cv2.waitKey(0)


#if __name__ == "__main__": 
#    Logo_Detection()
