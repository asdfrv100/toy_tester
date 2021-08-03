import cv2
import datetime as dt
import h5py
import numpy as np
import os
import fnmatch

start = dt.datetime.now()

# 이미지가있는 폴더 경로

PATH = os.path.abspath(os.path.join('..', 'input'))

SOURCE_IMAGES = os.path.join(PATH, "images")

# images폴더 내에 여러폴더 조회. 폴더엔 이미지파일만 있다고 가정..

images = []
for root, dirnames, filenames in os.walk(SOURCE_IMAGES):
    for filename in fnmatch.filter(filenames, '*.*'):
        images.append(os.path.join(root, filename))

try:

    # h5파일 쓰기 시작..
    with h5py.File('data.h5', 'w') as hf:
        for i, img in enumerate(images):
            # Images

            # openCV 사용해서 이미지 읽기
            image = cv2.imread(img)

            # 이미지 읽는 와중에. 못읽는 경우가 발생해서 일단 예외로 넘김.

            # 원인은 추후에 더 파고들게되면 확인해야합니다..
            if isinstance(image, (np.ndarray, np.generic)):
                HEIGHT, WIDTH, CHANNELS = image.shape
            else:
                continue

            # 이미지 크기 설정.. 원본크기로 설정하기 떄문에 주석
            # image = cv2.resize(image, (WIDTH, HEIGHT), interpolation=cv2.INTER_CUBIC)

            Xset = hf.create_dataset(
                name='X' + str(i),
                data=image,
                shape=(HEIGHT, WIDTH, CHANNELS),
                maxshape=(HEIGHT, WIDTH, CHANNELS),
                compression="gzip",
                compression_opts=9)

            # 진행 체크

            if i % 25 == 0:
                progTime = dt.datetime.now()
                print("\n--------------------In LOOP: ", (progTime - start).seconds, "seconds")

# h5파일 읽기 시작..

f = h5py.File('static/h5/data3.h5', 'r')

keys = f.keys()

dset = ''
fIndex = -1
fName = ''

arrLen = len(keys)

# key로 이미지 데이터 불러옴. 필요한 logic은 안에 추가하면 됨

# 우선 첫번째이미지만 확인
for i, fName in enumerate(keys):
    dset = f[fName]

    break

# 이미지 데이터를 png로 인코드, b로 인코드. 후에 imgForm 값을 이미지 태그에 넣으면 웹에서 확인가능.

data = np.array(dset[:, :, :])

retval, buffer = cv2.imencode('.png', data)

png_as_text = base64.b64encode(buffer)

imgForm = "data:image/png;base64, "

imgForm += png_as_text.decode("utf-8")