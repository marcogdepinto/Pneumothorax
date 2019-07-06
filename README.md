# Pneumothorax

This repository contains a pipeline built for the [Kaggle SIIM-ACR Pneumothorax Detection competition](https://www.kaggle.com/c/siim-acr-pneumothorax-segmentation/).

The goal of the competition is to develop a model to classify (and if present, segment) pneumothorax from a set of chest radiographic images in DICOM format.

A pneumothorax is an abnormal collection of air in the pleural space between the lung and the chest wall: it can result in death if not treated.

Pneumothorax is usually diagnosed by a radiologist on a chest x-ray, and can sometimes be very difficult to confirm. 

An accurate AI algorithm to detect pneumothorax would be useful in a lot of clinical scenarios. #AI could be used to triage chest radiographs for priority interpretation, or to provide a more confident diagnosis for non-radiologists.

![Radiography](https://github.com/marcogdepinto/Pneumothorax/blob/master/exampleimage/radiography.jpg)

# About the dataset

Instructions to download the data are included in the competition information.

The data is comprised of images in DICOM format (radiographies) and annotations in the form of image IDs and run-length-encoded (RLE) masks. 

Some of the images contain instances of pneumothorax (collapsed lung), which are indicated by encoded binary masks in the annotations. Some images have multiple annotations.

``1.2.276.0.7230010.3.1.4.8323329.14508.1517875252.443873,387620 23 996 33 986 43 977 51 968 58 962 65 956 70 952 74 949 76 946 79``
Images without pneumothorax have a mask value of -1.

`1.2.276.0.7230010.3.1.4.8323329.1034.1517875166.8504,-1`

# How to run the scripts

Running `examplefile.py`` it will be possible to review the example of a file structure we are working on.

The output will be the following (using the same file I used):

`(0008, 0005) Specific Character Set              CS: 'ISO_IR 100'
(0008, 0016) SOP Class UID                       UI: Secondary Capture Image Storage
(0008, 0018) SOP Instance UID                    UI: 1.2.276.0.7230010.3.1.4.8323329.300.1517875162.258081
(0008, 0020) Study Date                          DA: '19010101'
(0008, 0030) Study Time                          TM: '000000.00'
(0008, 0050) Accession Number                    SH: ''
(0008, 0060) Modality                            CS: 'CR'
(0008, 0064) Conversion Type                     CS: 'WSD'
(0008, 0090) Referring Physician's Name          PN: ''
(0008, 103e) Series Description                  LO: 'view: AP'
(0010, 0010) Patient's Name                      PN: '88c14312-3265-4a3f-b7bb-41818107d607'
(0010, 0020) Patient ID                          LO: '88c14312-3265-4a3f-b7bb-41818107d607'
(0010, 0030) Patient's Birth Date                DA: ''
(0010, 0040) Patient's Sex                       CS: 'F'
(0010, 1010) Patient's Age                       AS: '58'
(0018, 0015) Body Part Examined                  CS: 'CHEST'
(0018, 5101) View Position                       CS: 'AP'
(0020, 000d) Study Instance UID                  UI: 1.2.276.0.7230010.3.1.2.8323329.300.1517875162.258080
(0020, 000e) Series Instance UID                 UI: 1.2.276.0.7230010.3.1.3.8323329.300.1517875162.258079
(0020, 0010) Study ID                            SH: ''
(0020, 0011) Series Number                       IS: "1"
(0020, 0013) Instance Number                     IS: "1"
(0020, 0020) Patient Orientation                 CS: ''
(0028, 0002) Samples per Pixel                   US: 1
(0028, 0004) Photometric Interpretation          CS: 'MONOCHROME2'
(0028, 0010) Rows                                US: 1024
(0028, 0011) Columns                             US: 1024
(0028, 0030) Pixel Spacing                       DS: ['0.139', '0.139']
(0028, 0100) Bits Allocated                      US: 8
(0028, 0101) Bits Stored                         US: 8
(0028, 0102) High Bit                            US: 7
(0028, 0103) Pixel Representation                US: 0
(0028, 2110) Lossy Image Compression             CS: '01'
(0028, 2114) Lossy Image Compression Method      CS: 'ISO_10918_1'
(7fe0, 0010) Pixel Data                          OB: Array of 154050 bytes`
`

To build your full dataframe, you should run ``createdataframe.py``.

In the `` dataframe `` folder you will find two pickles with the train and test dataframes I have already prepared as output examples for the script.


