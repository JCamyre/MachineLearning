import numpy as np
from PIL import ImageGrab
import cv2
import ctypes
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D 
import pyautogui # To ensure window size same as game window size

def roi(img, vertices):
	mask = np.zeros_like(img)
	cv2.fillPoly(mask, vertices, 255)
	masked = cv2.bitwise_and(img, mask)
	return masked


def process_img(original_image):
	processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
	processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300) # Canny Edge detection
	vertices = np.array([[460, 180], [820, 180], [820, 540], [460, 540]])
	processed_img = roi(processed_img, [vertices]) # [vertices] very important, raises error
	return processed_img

def main():
	last_time = time.time()
	while(True):
		screen = np.array(ImageGrab.grab(bbox=(0, 40, 1275, 750)))
		new_screen = process_img(screen)
		# print('down')
		# PressKey(W)
		# time.sleep(3)
		# print('up')
		# ReleaseKey(W)
		print(f'Loop at {1/(time.time() - last_time):.1f} fps') 
		last_time = time.time()
		cv2.imshow('window', new_screen)
		# cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
		if cv2.waitKey(25) & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			break

if __name__ == '__main__':
	main()

