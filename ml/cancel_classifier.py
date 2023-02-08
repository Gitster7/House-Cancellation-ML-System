import joblib
import numpy as np
import pandas as pd

class Classifier:
    def __init__(self):
        path_to_artifacts = './ml/artifacts/'
        self.encoder = joblib.load(path_to_artifacts + "encoder.joblib")
        self.model = joblib.load(path_to_artifacts + "rf.joblib")

    def preprocessing(self, input_data):
        #JSON to pandas DataFrame
        input_data = pd.DataFrame(input_data, index=[0])
        # convert categorical
        cat_columns = input_data.select_dtypes(object).columns[1:]
        input_data_cat = input_data[cat_columns]
        input_data_cat = self.encoder.transform(input_data_cat)
        input_data_cat = pd.DataFrame(input_data_cat.toarray(), columns=self.encoder.get_feature_names_out())
        # numerical data
        input_data_num = input_data.select_dtypes(exclude='object')
        input_data_num.index = np.arange(0, len(input_data_num))
        # complete data
        input_data = pd.concat([input_data_cat, input_data_num], axis=1)
        return input_data

    def predict(self, input_data):
        return self.model.predict_proba(input_data)

    def postprocessing(self, input_data):
        label = 'Not Cancel'
        if input_data[1] >= 0.5:
            label = 'Cancel'
        return {"probability":input_data[1], "label":label, "status":"OK"}

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0]  # only one sample
            prediction = self.postprocessing(prediction)

        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction




################################
        # SCRIPT TEST
################################

# input_data = {
#     'Booking_ID':'INN00001',
#     'no_of_adults':2,
#     'no_of_children':0,
#     'no_of_weekend_nights':1,
#     'no_of_week_nights':2,
#     'type_of_meal_plan':'Meal Plan 1',
#     'required_car_parking_space':0,
#     'room_type_reserved':'Room_Type 1',
#     'lead_time':224,
#     'arrival_year':2017,
#     'arrival_month':10,
#     'arrival_date':2,
#     'market_segment_type':'Offline',
#     'repeated_guest':0,
#     'no_of_previous_cancellations':0,
#     'no_of_previous_bookings_not_canceled':0,
#     'avg_price_per_room':65.0,
#     'no_of_special_requests':0,
# }
#
# cls = Classifier()
# res = cls.compute_prediction(input_data)
# print(res)
