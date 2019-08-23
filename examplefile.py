from pydicom.filereader import dcmread

dcm_file_path = '/Users/marcogdepinto/PycharmProjects/Pneumothorax/dataset/dicom-images-train/1.2.276.0.7230010.3.1.2.8323329.300.1517875162.258080/1.2.276.0.7230010.3.1.3.8323329.300.1517875162.258079/1.2.276.0.7230010.3.1.4.8323329.300.1517875162.258081.dcm'
dcm_data = dcmread(dcm_file_path)

print(dcm_data)
