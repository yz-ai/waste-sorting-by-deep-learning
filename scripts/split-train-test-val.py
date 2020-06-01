import argparse
import errno
import os
import random
import shutil


def createFolder(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def getImgs(imageDir):
    exts = ["jpg", "png"]

    allImgsM = []
    classes = set()
    for subdir, dirs, files in os.walk(imageDir):
        for fName in files:
            (imageClass, imageName) = (os.path.basename(subdir), fName)
            if any(imageName.lower().endswith("." + ext) for ext in exts):
                if imageClass not in classes:
                    classes.add(imageClass)

                allImgsM.append((imageClass, imageName))
    print("+ Number of Classes: '{}'.".format(len(classes)))
    return (allImgsM)


def moveImages(imageDir, arrImgs, typeName):
    for lbl, img in arrImgs:
        origPath = os.path.join(imageDir, lbl, img)
        newDir = os.path.join(imageDir, typeName, lbl)
        newPath = os.path.join(imageDir, typeName, lbl, img)
        createFolder(newDir)
        shutil.move(origPath, newPath)

def removeFolder(imageDir, arrImgs):
    for lbl, img in arrImgs:
        d = os.path.join(imageDir, lbl)
        if os.path.isdir(d):
            os.rmdir(d)

def createTrainValSplit(imageDir, testRatio, valRatio):
    print("+ Test ratio: '{}'.".format(testRatio))
    print("+ Val ratio: '{}'.".format(valRatio))

    testImgs = []
    valImgs = []

    allImgsM = getImgs(imageDir)
    print("allImgsM len", len(allImgsM))


    testIdx = int(len(allImgsM) * testRatio)
    valIdx = int(len(allImgsM) * valRatio)
    trainIdx = len(allImgsM) - testIdx - valIdx
    
    print("testIdx",testIdx)
    print("valIdx",valIdx)
    print("trainIdx",trainIdx)

    random.shuffle(allImgsM)
    testImgs = allImgsM[0:testIdx]
    valImgs = allImgsM[testIdx:(testIdx+valIdx)]
    trainImgs = allImgsM[(testIdx+valIdx):]

    print("+ Training set size: '{}'.".format(len(trainImgs)))
    print("+ Test set size: '{}'.".format(len(testImgs)))
    print("+ Validation set size: '{}'.".format(len(valImgs)))

    moveImages(imageDir, trainImgs, 'train')
    moveImages(imageDir, valImgs, 'val')
    moveImages(imageDir, testImgs, 'test')

    removeFolder(imageDir, valImgs)
    removeFolder(imageDir, testImgs)
     

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('imageDir', type=str, 
                        help="Directory of images to partition in-place to 'train' and 'val' directories.")
    parser.add_argument('--testRatio', type=float, default=0.10,
                        help="Test to training ratio.")
    parser.add_argument('--valRatio', type=float, default=0.10,
                        help="Validation to training ratio.")                        
    args = parser.parse_args()

    createTrainValSplit(args.imageDir, args.testRatio, args.valRatio)

