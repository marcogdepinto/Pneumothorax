import os
import time
import pickle
import numpy as np
import pandas as pd
from pydicom.filereader import dcmread


class CreateDataframe:

    def preptraindata(path):
        '''
        This method is used to load the training data.
        '''
        count = 0
        for root, dirs, file in os.walk(path):
            if not dirs:
                continue
            else:
                # print(root, dirs, file) # Taking first level with path in root and second level with dirs. File is empty
                for nroot, ndirs, nfile in os.walk(root):
                    if not nfile:
                        continue
                    else:
                        start_time = time.time()
                        dcm_file_path_str = nroot + '/' + nfile[0]
                        if not dcm_file_path_str.endswith('.dcm'):
                            continue
                        dcm_data = dcmread(dcm_file_path_str)

                        # Structuring metadata

                        metadata_dict = {"file_path": dcm_file_path_str}
                        metadata_dict["storage_type"] = dcm_data.SOPClassUID
                        metadata_dict["patient_name"] = dcm_data.PatientName.family_name + " " + dcm_data.PatientName.given_name
                        metadata_dict["patient_id"] = dcm_data.PatientID
                        metadata_dict["patient_age"] = dcm_data.PatientAge
                        metadata_dict["patient_sex"] = dcm_data.PatientSex
                        metadata_dict["modality"] = dcm_data.Modality
                        metadata_dict["body_part_examined"] = dcm_data.BodyPartExamined
                        metadata_dict["view_position"] = dcm_data.ViewPosition

                        if "PixelData" in dcm_data:
                            rows = int(dcm_data.Rows)
                            cols = int(dcm_data.Columns)
                            metadata_dict["image_height"] = rows
                            metadata_dict["image_width"] = cols
                            metadata_dict["image_size"] = len(dcm_data.PixelData)
                        else:
                            metadata_dict["image_height"] = np.nan
                            metadata_dict["image_width"] = np.nan
                            metadata_dict["image_size"] = np.nan

                        if "PixelSpacing" in dcm_data:
                            metadata_dict["pixel_spacing_x"] = dcm_data.PixelSpacing[0]
                            metadata_dict["pixel_spacing_y"] = dcm_data.PixelSpacing[1]
                        else:
                            metadata_dict["pixel_spacing_x"] = np.nan
                            metadata_dict["pixel_spacing_y"] = np.nan

                        # Insert a count. If first iteration create new dataframe.
                        # Else append data on dataframe already created

                        print("--- Iteration loaded. Loading time: %s seconds ---" % (time.time() - start_time))
                        count += 1
                        print(count)

                        if count == 1:
                            metadata_df = pd.DataFrame.from_records([metadata_dict])
                        else:
                            metadata_df = metadata_df.append([metadata_dict])

        # Resetting index
        metadata_df = metadata_df.reset_index()

        # Dropping useless index column (all values to zero)
        metadata_df = metadata_df.drop(columns=['index'])

        # Saving dataframe to local pickle to be loaded from another module
        with open('./dataframe/sample_images.pickle', 'wb') as f:
            pickle.dump(metadata_df, f)

        return metadata_df

createdf = CreateDataframe.preptraindata(path='dataset/dicom-images-test') # Switch between training or test

